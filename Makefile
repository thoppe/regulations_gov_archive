all:
	python P0_collect_document_IDs.py

lint:
	black *.py src --line-length 80
	flake8 *.py src --ignore=E501,E712

add_data:
	python src/C0_collate_search_results.py
	python src/B0_build_README.py
	git add data/daily_search_results
