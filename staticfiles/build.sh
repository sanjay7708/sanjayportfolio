#!/usr/bin/env bash
set -oerrexit
pip install -r requirements.txt
python3 managa.py collectstatic --no-input

python3 manage.py migrate
