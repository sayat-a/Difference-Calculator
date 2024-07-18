lint:
	poetry run flake8 gendiff


test:
	poetry run pytest


test-coverage:
	poetry run pytest --cov


lint:
	poetry run flake8 hexlet_python_package


selfcheck:
	poetry check


check: selfcheck test lint