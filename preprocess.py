#!/bin/python3
# encoding=utf-8
import csv
import jieba

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

for x, w in jieba.analyse.extract_tags(data[0][2], withWeight=True):
    print('%s, %s' % (x, w))



