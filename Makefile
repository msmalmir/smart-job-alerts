install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black *.py app/*.py

lint:
	pylint --disable=R,C *.py app/*.py

all: install lint test