#!/bin/bash

chmod 644 .gitignore .travis.yml
chmod 644 LICENSE MANIFEST.in README.md requirements.txt setup.cfg tox.ini
chmod 644 setup.py unzip.py

find pyunzip tests -name "*.py" -exec chmod 644 {} \;
find . -name "*.pyc" ! -path "*.venv*" -exec rm -rf {} \;
find . -name "*.sh" ! -path "*.venv*" -exec chmod 755 {} \;
find . -name "__pycache__" ! -path "*.venv*" -exec rm -rf {} \;
