import json
from datetime import datetime, timedelta
from dspipe import Pipe
import utils


days_back = 5_000  # Number of days we will go backwards
buffer_days = 30  # Number of days before we start collecting data

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
    session = utils.get_session()
    headers = utils.get_API_KEY()

    target_date = datetime.now() - timedelta(days=days_back)
    y0 = target_date.year
    m0 = target_date.month
    d0 = target_date.day

    f_save = f1.parent / f"{y0:04d}_{int(m0):02d}_{int(d0):02d}.json"

    if f_save.exists():
        return f_save

    # print(f"Starting {f_save}")

    params = {
        "filter[documentType]": list(selected_documentType),
        "filter[postedDate]": f"{y0:04d}-{m0:02d}-{d0:02d}",
        "page[size]": 250,
    }

    url = "https://api.regulations.gov/v4/documents"

    total_pages = None
    data = []
    page_n = 1

    while True:
        r = session.get(url, headers=headers, params=params)

        if not r.ok:
            raise ValueError(r.status_code, r.content)

        js = r.json()
        total_pages = js["meta"]["totalPages"]
        total_elements = js["meta"]["totalElements"]

        # Check if true. If so, this method won't work anymore and break.
        assert js["meta"]["totalElements"] < 5000

        data.append(r.json())

        if total_pages == 0:
            break

        # Break if we've completed the expected number of pages
        if page_n >= total_pages:
            break

        page_n += 1

    jsx = json.dumps(data, indent=2)

    with open(f_save, "w") as FOUT:
        FOUT.write(jsx)

    print(f"Saved {f_save} {len(data)} {total_pages} ({total_elements})")


Pipe(range(buffer_days, days_back), "data/daily_search_results")(compute, 1)
