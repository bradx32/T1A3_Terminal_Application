#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
python3 water_testing_app.py

