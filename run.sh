#!/bin/bash

wget -q http://localhost:5000/results/dump/cnblog.csv
tail cnblog.csv
python3 preprocess.py | tail
