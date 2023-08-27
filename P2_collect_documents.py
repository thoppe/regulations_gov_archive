from datetime import datetime, timedelta
import pandas as pd
from dspipe import Pipe
import utils
import json
import bs4

date_key = "attributes.commentEndDate"

df = pd.read_csv(
    "artifacts/LISTING_rules_and_posted_rules.csv",
    nrows=None,
)
df[date_key] = pd.to_datetime(df[date_key]).dt.date

# Shuffle to get a good sampling
df = df.sample(frac=1, random_state=23)

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
        raise ValueError(r.status_code, r.content)

    title = js["data"]["attributes"]["title"]

    # Try to download the HTM, we need to find out which one
    target_download = None
    for row in js["data"]["attributes"]["fileFormats"]:
        if row["format"] == "htm":
            target_download = row

    # Raise an Error if not found
    assert target_download

    r2 = session.get(target_download["fileUrl"])
    if not r2.ok:
        raise ValueError(r2.status_code, r2.content)

    soup = bs4.BeautifulSoup(r2.text, "html.parser")
    text = soup.text.strip()
    js["data"]["content"] = {"text": text}

    with open(f1, "w") as FOUT:
        json.dump(js, FOUT)

    print(f"Saved {f1} {title} ({len(text)})")


Pipe(df["id"], "data/documents", output_suffix=".json")(compute, 1)
