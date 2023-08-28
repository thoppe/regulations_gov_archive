import pandas as pd
import json
from dspipe import Pipe


def compute(f0):
    with open(f0) as FIN:
        js = json.load(FIN)
    js["objectId"] = f0.stem

    for key in ["aggregations", "filters"]:
        if key in js:
            del js[key]
    return js


load_src = "data/comments_meta/"
key = "objectId"

comments = pd.DataFrame(Pipe(load_src)(compute, -1)).set_index(key)

f_save = "artifacts/LISTING_rules_and_posted_rules.csv"
df = pd.read_csv(f_save)
df = df.set_index("attributes.objectId")

# Use Pandas new Int64 dtype to represent NaNs
df["total_comments"] = comments["totalElements"].astype("Int64")
df = df.reset_index()

# Save the dataframe back to disk
df.to_csv(f_save, index=False)

# Print the top comments
dx = df.dropna(subset=["total_comments"]).sort_values(
    "total_comments", ascending=False
)
dx = dx.rename(
    columns={"attributes.title": "title", "attributes.agencyId": "agency"}
)
print(dx[["agency", "total_comments", "title"]][:15])
