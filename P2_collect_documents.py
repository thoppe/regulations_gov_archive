from datetime import datetime, timedelta
import pandas as pd
from dspipe import Pipe
import utils
import json
import bs4
import time

date_key = "attributes.commentEndDate"

df = pd.read_csv(
    "artifacts/LISTING_rules_and_posted_rules.csv",
    nrows=None,
)
df[date_key] = pd.to_datetime(df[date_key]).dt.date

# Filter out withdrawn documents
df = df[df["attributes.withdrawn"] == False]

# Shuffle to get a good sampling
df = df.sample(frac=1, random_state=102)

buffer_days = 30
check_time = datetime.now().date() - timedelta(days=buffer_days)

# Make sure we skip items where there commentEndDate is later than the buffer
idx = df[date_key] > check_time
if idx.sum():
    print(f"Filtering {idx.sum()} documents for buffer date")

df = df[~idx]


def compute(docID, f1):
    session = utils.get_session()
    headers = utils.get_API_KEY()

    url = f"https://api.regulations.gov/v4/documents/{docID}"
    params = {"include": "attachments"}

    r = session.get(url, headers=headers, params=params)
    js = r.json()

    if not r.ok:
        if r.status_code == 429:
            print("Sleeping for one hour")
            time.sleep(60 * 60)
            return compute(docID, f1)

        if r.status_code == 404:
            print(f"404 {docID} skipping")
            return

        raise ValueError(docID, r.status_code, r.content)

    attrs = js["data"]["attributes"]
    title = attrs["title"]

    # Debugging statement
    # print(json.dumps(attrs, indent=2))

    # Error checking
    if "fileFormats" not in attrs:
        print(attrs)
        raise KeyError("Missing fileFormat")

    # IF the key exists but is null use an empty list
    if attrs["fileFormats"] is None:
        attrs["fileFormats"] = []

    # Try to download the HTM, we need to find out which one
    target_download = None

    for row in attrs["fileFormats"]:
        if row["format"] == "htm":
            target_download = row

    # Raise an Error if not found
    # assert target_download

    if target_download is not None:
        r2 = session.get(target_download["fileUrl"])
        if not r2.ok:
            raise ValueError(r2.status_code, r2.content)

        soup = bs4.BeautifulSoup(r2.text, "html.parser")
        text = soup.text.strip()
        js["data"]["content"] = {"text": text}

    else:
        print("Missing htm fileFormat", attrs["fileFormats"])
        text = ""

    with open(f1, "w") as FOUT:
        json.dump(js, FOUT)

    print(f"Saved {f1} {title} ({len(text)})")


Pipe(df["id"], "data/documents", output_suffix=".json")(compute, 1)
