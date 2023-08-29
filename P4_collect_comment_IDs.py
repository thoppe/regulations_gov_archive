from datetime import timedelta, datetime
import pandas as pd
from dspipe import Pipe
import utils
import pytz

# Helps when breaking things up
import diskcache as dc

cache = dc.Cache("tmp_working_cache")
# cache = {}

date_key = "attributes.commentEndDate"

df = pd.read_csv(
    "artifacts/LISTING_rules_and_posted_rules.csv",
    nrows=None,
    dtype={"total_comments": "Int64"},
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
    print(f"Filtering {idx.sum()} documents before buffer date {check_time}")

df = df[~idx]

# For now, don't download objects without commentEndDate
df = df.dropna(subset=[date_key])

# Drop any documents without comments
df = df.dropna(subset=["total_comments"])

# Drop any with < 1K comments or > 10K comments for now
df = df[df.total_comments >= 1_000]
df = df[df.total_comments <= 10_000]


def cache_download(url, session, headers, params):
    key = (url, headers, params)

    if key not in cache:
        print(params)
        r = session.get(url, headers=headers, params=params)

        if r.status_code == 429:
            utils.sleep_if_needed(r)
            return cache_download(url, session, headers, params)

        assert r.ok
        cache[key] = r

    return cache[key]


def compute(objectId, f1):
    session = utils.get_session()
    headers = utils.get_API_KEY()

    url = "https://api.regulations.gov/v4/comments"

    params = {
        "filter[commentOnId]": objectId,
        "sort": "lastModifiedDate,documentId",
        "page[size]": 250,
        "page[number]": 1,
    }

    cutoff_date = None
    total_elements = None
    data = []

    while True:
        # Do not add this on the first search
        if cutoff_date is not None:
            params["filter[lastModifiedDate][ge]"] = cutoff_date

        # Download page #1
        params["page[number]"] = 1
        js = cache_download(url, session, headers=headers, params=params).json()
        data.extend(js["data"])

        # total_elements is only correct on the first search
        if total_elements is None:
            total_elements = js["meta"]["totalElements"]

        # This is correct every first page search
        total_pages = js["meta"]["totalPages"]

        for page_n in range(2, total_pages + 1):
            params["page[number]"] = page_n
            r = cache_download(url, session, headers=headers, params=params)
            js = r.json()
            data.extend(js["data"])

        # Gather the data and find the latest known date
        # Don't trust the API to do the order correctly
        dx = pd.json_normalize(data)
        date_key = "attributes.lastModifiedDate"
        dx[date_key] = pd.to_datetime(dx[date_key])

        # Why does the API need to convert to EST timezone??
        EST_tz = pytz.timezone("US/Eastern")
        cutoff_date = dx[date_key].max()
        cutoff_date = cutoff_date.tz_convert(EST_tz)
        cutoff_date = cutoff_date.strftime("%Y-%m-%d %H:%M:%S")

        # We don't need to do another round here
        if total_pages < 20:
            break

        current_search_elements = js["meta"]["totalElements"]
        if current_search_elements in [0, 1]:
            break

    df = pd.json_normalize(data)

    key = "id"
    df = df.drop_duplicates(subset=[key])
    df = df.sort_values(key).set_index(key)

    if not len(df) == total_elements:
        print(f"Missing {total_elements - len(df)}, not saving")
        return None

    print(f"Saving {f1}")
    df.to_csv(f1)


# For testing
# objectId = "09000064851c6f17"
# compute(objectId, None)

Pipe(
    df["attributes.objectId"], "data/comments_objectIDs", output_suffix=".csv"
)(compute, 1)
