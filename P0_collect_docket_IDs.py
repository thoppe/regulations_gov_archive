import json
from datetime import datetime, timedelta
from dspipe import Pipe
import utils


days_back = 5_000  # Number of days we will go backwards
buffer_days = 10  # Number of days before we start collecting data
target_date = datetime.now() - timedelta(days=buffer_days)

selected_documentType = set(
    [
        "Proposed Rule",
        "Rule",
        # "Notice",
        # "Other",
        # "Supporting & Related Material",
    ]
)


def compute(days_back, f1):
    target_date = datetime.now() - timedelta(days=days_back)
    y0 = target_date.year
    m0 = target_date.month
    d0 = target_date.day

    params = {
        "filter[documentType]": list(selected_documentType),
        "filter[postedDate]": f"{y0:04d}-{m0:02d}-{d0:02d}",
        "page[size]": 250,
    }

    url = "https://api.regulations.gov/v4/documents"
    f_save = f1.parent / f"{y0}_{int(m0):02d}_{int(d0):02d}.json"

    if f_save.exists():
        return f_save

    total_pages = None
    data = []
    page_n = 0

    while True:
        page_n += 1
        r = session.get(url, headers=headers, params=params)

        if not r.ok:
            raise ValueError(r.status_code, r.content)

        js = r.json()
        total_pages = js["meta"]["totalPages"]

        # Break if we've completed the expected number of pages
        if page_n == total_pages:
            break

        # If this is true we are in trouble, this method won't work anymore.
        assert js["meta"]["totalElements"] < 5000

        data.append(r.json())

    jsx = json.dumps(data, indent=2)

    with open(f_save, "w") as FOUT:
        FOUT.write(jsx)

    print(f"Saved {f_save}")

session = utils.get_session()
headers = utils.get_API_KEY()

Pipe(range(days_back), "data/daily_search_results")(compute, 1)
