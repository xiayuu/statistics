#!/bin/bash

wget http://localhost:5000/results/dump/cnblog.csv
python preprocess.py | tail 
