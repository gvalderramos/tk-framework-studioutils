#!/bin/bash

find . -name "*.pyc" -delete
export PYTHONPATH="./python"
coverage run -m unittest discover -s "." -p '*_test.py'