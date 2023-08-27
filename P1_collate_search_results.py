import pandas as pd
import json
from dspipe import Pipe


def compute(f0):
    with open(f0) as FIN:
        js = json.load(FIN)

    # Assume we only have one page and flatten the JSON
    assert len(js) == 1
    js = js[0]

    # meta = js["meta"]

    for item in js["data"]:
        # As a data quality check, we assume there is exactly one link
        # and that link is a "self" link
        assert "links" in item
        assert len(item["links"]) == 1
        assert "self" in item["links"]

        # Flatten this single dictionary
        item["links.self"] = item["links"]["self"]
        del item["links"]

        print(item)


load_src = "data/daily_search_results/"
Pipe(load_src)(compute, 1)
