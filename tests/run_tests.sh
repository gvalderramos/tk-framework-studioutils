#!/bin/bash

find . -name "*.pyc" -delete
export PYTHONPATH="./python"
#python -Wd -m unittest discover -s "." -p '*_test.py'
coverage run -m unittest discover -s "." -p '*_test.py'