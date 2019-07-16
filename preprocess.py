#!/bin/python3

import csv

dest = 'csdn.csv'
with open(dest,  encoding='utf-8') as dest_f:
    data_iter = csv.reader(dest_f)
    data = [ data for data in data_iter ]

for l in data:
    print('url:   %s' % l[0])
    print('title: %s' % l[1])
    print('view:  %s' % l[3])



