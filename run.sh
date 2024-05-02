#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
pip3 install Rich
python3 water_testing_app.py

