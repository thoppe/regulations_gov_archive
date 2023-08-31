import pandas as pd
import seaborn as sns
import pylab as plt

nrows = None
df = pd.read_csv(
    "artifacts/LISTING_rules_and_posted_rules.csv",
    dtype={"total_comments": "Int64"},
    nrows=nrows,
)

date_key = "attributes.postedDate"
df["year"] = pd.to_datetime(df[date_key]).dt.year

df = df.dropna(subset=["total_comments"])

# Apply a year filter
df = df[df["year"] >= 1990]
g = df.groupby("year")
print(g.size())

plt.figure(figsize=(16 / 2, 8 / 2))

g0 = g["total_comments"].sum().reset_index()
sns.lineplot(
    data=g0, x="year", y="total_comments", marker="o", label="Total comments"
)

g1 = g.size().reset_index()
sns.lineplot(data=g1, x="year", y=0, marker="o", label="Total documents")

g2 = g["attributes.frDocNum"].apply(lambda x: x.nunique()).reset_index()
sns.lineplot(
    data=g2,
    x="year",
    y="attributes.frDocNum",
    marker="x",
    label="Unique Federal registers (FR)",
)

g3 = g["attributes.docketId"].apply(lambda x: x.nunique()).reset_index()
sns.lineplot(
    data=g3,
    x="year",
    y="attributes.docketId",
    marker="o",
    label="Unique Docket IDs",
)

plt.title("regulations.gov document statistics")
sns.despine()
plt.yscale("log")
plt.xlabel("Year")
plt.ylabel("Counts")
plt.tight_layout()
plt.savefig(
    "artifacts/figures/document_statistics.jpg", bbox_inches="tight", dpi=100
)
plt.show()
