import json
import pandas as pd
from dspipe import Pipe
import utils

# Helps when breaking things up
import diskcache as dc

cache = dc.Cache("tmp_working_cache")


def cache_download(url, session, headers, params):
    key = (url, headers, params)

    if key not in cache:
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

    url = f"https://api.regulations.gov/v4/comments/{objectId}"

    params = {
        "include": "attachments",
    }

    r = cache_download(url, session, headers, params)
    js = r.json()
    output_json = json.dumps(js, indent=2)

    with open(f1, "w") as FOUT:
        FOUT.write(output_json)


def process(f0):
    df = pd.read_csv(f0)

    df = df.sample(n=100, random_state=222)

    Pipe(df["id"], "data/comments_detail", output_suffix=".json")(compute, 4)


Pipe("data/comments_objectIDs/", limit=5)(process, 1)
