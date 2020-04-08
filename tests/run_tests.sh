#!/bin/bash

find . -name "*.pyc" -delete
export PYTHONPATH="."
coverage run -m unittest discover -s "." -p '*_test.py'