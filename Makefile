#!/bin/bash
VENVBIN=./venv/bin
NODEBIN=./node_modules/.bin
PYTHON=$(VENVBIN)/python
PIP=$(VENVBIN)/pip
PYLINT=$(VENVBIN)/pylint

all: env

env:
	cp ./etc/git-hooks/pre-commit ./.git/hooks/pre-commit
	virtualenv -p python3 venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

dev:
	source venv/bin/activate

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf venv
	rm -rf vendored
