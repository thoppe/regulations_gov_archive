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
n_comments = int(df["total_comments"].sum())
frac_known_comments = 1 - df["total_comments"].isnull().sum() / len(df)

content = ["## Data Statistics"]

content.append("|     |     |")
content.append("|---- |---- |")
content.append(f"| Total documents | {len(df):,d}    |")
content.append(f"| Unique agencies | {n_agency:,}    |")
content.append(f"| Unique dockets  | {n_dockets:,}   |")
content.append(f"| Unique FR IDs   | {n_FRID:,}      |")
content.append(f"| Total comments  | {n_comments:,}  |")
content.append("")

content.append("## Data ingestion progress")
content.append("|     |     |")
content.append("|---- |---- |")
content.append(f"| Latest date   | {last_date} |")
content.append(f"| Earliest date | {first_date}    |")
content.append(
    f"| Fraction of documents scanned for comments  | {frac_known_comments:0.4f} |"
)
content.append("")

content.append("## Documents with top comments")
df = pd.read_csv(
    "artifacts/LISTING_rules_and_posted_rules.csv",
    dtype={"total_comments": "Int64"},
)
df = df.dropna(subset=["total_comments"]).sort_values(
    "total_comments", ascending=False
)
# df = df.rename(
#    columns={"attributes.title": "title", "attributes.agencyId": "agency"}
# )
content.append("| docId | comments | Title |")
content.append("|------|---------:|-------|")
for _, row in df[:20].iterrows():
    docID = row["id"]
    title = row["attributes.title"].replace("|", r"\|")
    title = " ".join(title.split())
    url = f"https://www.regulations.gov/document/{docID}"
    content.append(f"| [{docID}]({url}) | {row.total_comments:,} | {title} |")

content = "\n".join(content)

f_header = "src/assets/README_header.md"
f_footer = "src/assets/README_footer.md"
header = open(f_header).read()
footer = open(f_footer).read()

readme_text = "\n\n".join([header, content, footer])
print(content)

with open("README.md", "w") as FOUT:
    FOUT.write(readme_text)
