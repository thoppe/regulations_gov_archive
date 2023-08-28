from pathlib import Path
import pandas as pd
from dspipe import Pipe
import requests
import bs4
import time

df = pd.read_csv(
    "artifacts/LISTING_rules_and_posted_rules.csv",
    nrows=1200,
)

# If we get this response from the server, log it then continue
skippable_status_codes = [404, 403]

# Filter out withdrawn documents
df = df[df["attributes.withdrawn"] == False]

# Shuffle to get a good sampling
df = df.sample(frac=1, random_state=102)

# Load up any previous errors for reference
f_errors = Path("data/errors_FR_doc_text.csv")
if f_errors.exists():
    err_df = pd.read_csv(f_errors)
else:
    err_df = pd.DataFrame()

bad_doc_IDS = set(err_df["docID"].values.tolist())
idx = df["id"].isin(bad_doc_IDS)
df = df[~idx]
print(
    f"Filtering {idx.sum()} previously scanned docIDs with {skippable_status_codes} errors"
)


def compute(docID, f1):
    base_url = "https://downloads.regulations.gov"
    url = f"{base_url}/{docID}/content.htm"

    r = requests.get(url)

    if not r.ok:
        if r.status_code == 429:
            print("Sleeping for one hour")
            time.sleep(60 * 60)
            return compute(docID, f1)

        if r.status_code in skippable_status_codes:
            print(f"{r.status_code} {docID} skipping, missing")
            return {"docID": docID, "status_code": r.status_code}

        raise ValueError(docID, r.status_code, r.content)

    soup = bs4.BeautifulSoup(r.text, "html.parser")
    text = soup.text.strip()
    title = soup.title.text.strip()

    with open(f1, "w") as FOUT:
        FOUT.write(text)

    print(f"Saved {f1} {title} ({len(text)})")
    time.sleep(0.5)
    return None


P = Pipe(df["id"], "data/FR_doc_text", output_suffix=".txt")

new_errors = []
for error in P(compute, 5):
    if error is not None:
        new_errors.append(error)
new_errors = pd.DataFrame(new_errors)
err_df = pd.concat([err_df, new_errors])
err_df.to_csv(f_errors, index=False)
print(err_df)
