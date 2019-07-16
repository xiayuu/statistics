#!/bin/bash

wget -q http://localhost:5000/results/dump/cnblog.csv
python preprocess.py | tail 
