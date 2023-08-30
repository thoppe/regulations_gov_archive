from pathlib import Path
import json
from datetime import datetime, timedelta
from dspipe import Pipe
import utils

full_collect_year = 1996
first_collection_year = 1960

# Date we begin collecting data from API
stop_date = datetime(full_collect_year, 1, 1)
buffer_days = 14  # Number of days before we start collecting data

today = datetime.today()
days_back = (today - stop_date).days + 10

selected_documentType = set(
    [
        "Proposed Rule",
        "Rule",
        # "Notice",
        # "Other",
        # "Supporting & Related Material",
    ]
)


def compute(days_back, f1, entire_year=None):
    session = utils.get_session()
    headers = utils.get_API_KEY()

    params = {
        "filter[documentType]": list(selected_documentType),
        "page[size]": 250,
    }

    # If this is non-zero, grab the entire year
    if entire_year is not None:
        y0 = entire_year
        params["filter[postedDate][ge]"] = f"{y0:04d}-{1:02d}-{1:02d}"
        params["filter[postedDate][le]"] = f"{y0:04d}-{12:02d}-{31:02d}"
        save_dest = Path("data/daily_search_results/")
        f_save = save_dest / f"{year}_complete.json"

    else:
        target_date = datetime.now() - timedelta(days=days_back)

        if target_date < stop_date:
            return

        y0 = target_date.year
        m0 = target_date.month
        d0 = target_date.day

        params["filter[postedDate]"] = f"{y0:04d}-{m0:02d}-{d0:02d}"
        f_save = f1.parent / f"{y0:04d}_{int(m0):02d}_{int(d0):02d}.json"

    if f_save.exists():
        return f_save

    url = "https://api.regulations.gov/v4/documents"

    total_pages = None
    data = []
    page_n = 1

    while True:
        r = session.get(url, headers=headers, params=params)

        if not r.ok:
            if r.status_code == 429:
                utils.sleep_if_needed(r)
                return compute(days_back, f1)

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

    # Since we are pulling small chunks, assume we only have one page
    assert len(data) == 1

    jsx = json.dumps(data, indent=2)

    API_left = r.headers["X-Ratelimit-Remaining"]

    with open(f_save, "w") as FOUT:
        FOUT.write(jsx)

    print(
        f"Saved {f_save} {len(data)} {total_pages} ({total_elements}) "
        f"[{API_left}]"
    )


Pipe(range(buffer_days, days_back), "data/daily_search_results")(compute, 1)

# From 1995 and prior, it is safe to grab entire years
for year in range(first_collection_year, full_collect_year)[::-1]:
    compute(None, None, year)
