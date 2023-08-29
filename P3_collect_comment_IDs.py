import pandas as pd
import json
from datetime import datetime, timedelta
from dspipe import Pipe
import utils
import time

# url = https://api.regulations.gov/v4/comments?filter[commentOnId]=0900006483a6cba3&api_key=DEMO_KEY

date_key = "attributes.commentEndDate"

df = pd.read_csv(
    "artifacts/LISTING_rules_and_posted_rules.csv",
    nrows=None,
)
df[date_key] = pd.to_datetime(df[date_key]).dt.date

# Filter out withdrawn documents
df = df[df["attributes.withdrawn"] == False]

# Drop any items where we've already pulled the comments
if "total_comments" in df:
    df = df[df["total_comments"].isnull()]

# Shuffle to get a good sampling
df = df.sample(frac=1, random_state=102)

buffer_days = 30
check_time = datetime.now().date() - timedelta(days=buffer_days)

# Make sure we skip items where there commentEndDate is later than the buffer
idx = df[date_key] > check_time
if idx.sum():
    print(f"Filtering {idx.sum()} documents before buffer date {check_time}")

df = df[~idx]


def compute(objectId, f1):
    session = utils.get_session()
    headers = utils.get_API_KEY()

    params = {
        "filter[commentOnId]": objectId,
        "page[size]": 5,
    }

    url = "https://api.regulations.gov/v4/comments"
    r = session.get(url, headers=headers, params=params)

    if not r.ok:
        if r.status_code == 429:
            # Sleep as long as the API tells us
            sleep_time = int(r.headers["Retry-After"])
            print(f"Sleeping for {sleep_time} seconds")
            time.sleep(sleep_time + 4)
            return compute(objectId, f1)

        raise ValueError(r.status_code, r.content)

    js = r.json()
    meta = js["meta"]

    total_elements = meta["totalElements"]

    """
        # Check if true. If so, this method won't work anymore and break.
        # assert js["meta"]["totalElements"] < 5000

        data.append(r.json())
        total_pages = meta["totalPages"]

        if total_pages == 0:
            break

        # Break if we've completed the expected number of pages
        if page_n >= total_pages:
            break

        page_n += 1
    """

    jsx = json.dumps(meta, indent=2)

    # Output if we got over 1K comments to view
    if total_elements > 1_000:
        print(jsx)

    with open(f1, "w") as FOUT:
        FOUT.write(jsx)

    print(f"Saved {f1} ({total_elements})")


Pipe(df["attributes.objectId"], "data/comments_meta", output_suffix=".json")(
    compute, 4
)
