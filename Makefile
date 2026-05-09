.PHONY: test test-cov lint type-check format clean

install-dev:
	pip install -e ".[dev]"

test:
	pytest

test-cov:
	pytest --cov=avx --cov-report=html --cov-report=term

test-watch:
	ptw -- --testmon

lint:
	flake8 avx tests
	black --check avx tests

format:
	black avx tests
	isort avx tests

type-check:
	mypy avx

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +

all-checks: lint type-check test
	echo "All checks passed!"