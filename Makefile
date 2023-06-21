all:
	python P0_collect_docket_IDs.py

lint:
	black *.py --line-length 80
	flake8 *.py --ignore=E501
