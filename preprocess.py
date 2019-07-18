#!/bin/python3
# encoding=utf-8
import csv
import pkuseg

seg = pkuseg.pkuseg()

dest = 'cnblog.csv'

with open(dest,  encoding='utf-8') as dest_f:
    data_iter = csv.reader(dest_f)
    data = [ data for data in data_iter ]

"""
for l in data:
    print('url:   %s' % l[0])
    print('title: %s' % l[2])
    print('view:  %s' % l[1])
"""

def filter():
    pass


print(seg.cut(data[-1][2]))



