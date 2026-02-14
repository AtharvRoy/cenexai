PYTHON ?= python
VENV ?= .venv

.PHONY: venv install test run check

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	. $(VENV)/bin/activate && $(PYTHON) -m pip install --upgrade pip
	. $(VENV)/bin/activate && $(PYTHON) -m pip install -r requirements.txt

test:
	. $(VENV)/bin/activate && $(PYTHON) -m unittest discover -s tests -p 'test_*.py'

run:
	. $(VENV)/bin/activate && uvicorn app.main:app --reload

check:
	$(PYTHON) -m compileall app tests
