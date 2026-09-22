#!/usr/bin/env bash
set -e
python3 -m venv .venv
.venv/bin/pip install --quiet -r requirements.txt
.venv/bin/python src/run_analysis.py