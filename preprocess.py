#!/bin/python3
# encoding=utf-8
import csv
import jieba.posseg as pseg
import os

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

sws = []

for f in os.listdir('stopwords'):
    data = open('stopwords/' + f)
    sws.append(data.readline())

#过滤出需要的词性
def filter_tag(c, taglist):
    return c in taglist

#从中止词中过滤掉不需要的内容
def filter_stopword(w):
    return w in sws

#关注英文，名词，专名
taglist = ['eng', 'n', 'nz']


res = [ w for w, f in pseg.cut(data[-1][2]) if filter_stopword(w) and filter_tag(f, taglist) ]

print(res)



