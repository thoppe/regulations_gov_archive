collect:
	python src/P0_collect_document_IDs.py
	python src/P1_collect_comment_meta.py
#	python P1_download_text.py
#	python P2_collect_documents.py
#	python P1_collect_documents.py

add_data:
	python src/C0_collate_search_results.py
	python src/C1_collate_comments_meta.py
	python src/B0_build_README.py
	git add data/daily_search_results
	python src/A0_analyze_comments_per_year.py

lint:
	black *.py src --line-length 80
	flake8 *.py src --ignore=E501,E712
