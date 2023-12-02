install-all:
	poetry install

upgrade-deps:
	poetry update
	poetry export --without-hashes -f requirements.txt --output requirements.txt
	poetry export --without-hashes --with dev -f requirements.txt --output requirements_all.txt

format-all:
	isort . --skip setup.py
	black --exclude setup.py .

pytest:
	pytest -vv --cov=requisites --cov-report=term-missing --cov-report=xml tests/
