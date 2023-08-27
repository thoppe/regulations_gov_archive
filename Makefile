all:
	python P0_collect_docket_IDs.py

lint:
	black *.py --line-length 80
	flake8 *.py --ignore=E501

add_data:
	git add data/daily_search_results
