import pandas as pd
import json
from dspipe import Pipe


def compute(f0):
    with open(f0) as FIN:
        js = json.load(FIN)

    # Assume we only have one page and flatten the JSON
    assert len(js) == 1
    js = js[0]

    # Get the date from the search filter
    meta = js["meta"]
    date = meta["filters"]["postedDate"]["fromDate"]

    for item in js["data"]:
        # As a data quality check, we assume there is exactly one link
        # and that link is a "self" link
        assert "links" in item
        assert len(item["links"]) == 1
        assert "self" in item["links"]

    dx = pd.json_normalize(js["data"])
    dx["postedDate"] = date

    return dx


load_src = "data/daily_search_results/"
df = pd.concat(Pipe(load_src)(compute, -1))

# Convert the date so we can sort by it
df["postedDate"] = pd.to_datetime(df["postedDate"])

# Sort by date then docketID
df = df.sort_values(["postedDate", "attributes.docketId"], ascending=False)

df.to_csv("artifacts/LISTING_rules_and_posted_rules.csv", index=False)

print(f"{len(df)} items")

# Print the top 10 counts
g = df.value_counts("attributes.agencyId")
print(g[:10])
