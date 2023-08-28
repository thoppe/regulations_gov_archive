import pandas as pd

content = ""

df = pd.read_csv(
    "artifacts/LISTING_rules_and_posted_rules.csv",
    parse_dates=["postedDate"],
    nrows=None,
)

last_date = df["postedDate"].max().strftime("%Y-%m-%d")
first_date = df["postedDate"].min().strftime("%Y-%m-%d")
n_agency = len(df["attributes.agencyId"].unique())
n_dockets = len(df["attributes.docketId"].unique())
n_FRID = len(df["attributes.frDocNum"].unique())

content = ["## Data Statistics"]
content.append(f"+ {len(df):,d} total documents")
content.append(f"+ Unique agencies: {n_agency:,}")
content.append(f"+ Unique dockets : {n_dockets:,}")
content.append(f"+ Unique FR IDs  : {n_FRID:,}")
content.append(f"+ Latest date    : {last_date}")
content.append(f"+ Earliest date  : {first_date}")


content = "\n".join(content)

f_header = "src/assets/README_header.md"
f_footer = "src/assets/README_footer.md"
header = open(f_header).read()
footer = open(f_footer).read()

readme_text = "\n\n".join([header, content, footer])
print(content)

with open("README.md", "w") as FOUT:
    FOUT.write(readme_text)
