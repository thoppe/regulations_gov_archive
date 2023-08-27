all:
	python P0_collect_document_IDs.py

lint:
	black *.py --line-length 80
	flake8 *.py --ignore=E501

add_data:
	python src/B0_build_README.py
	git add data/daily_search_results
