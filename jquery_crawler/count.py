#!/usr/bin/env python
# coding=utf-8

def count_scm():
    import sys
    dic = {}
    for line in sys.stdin:
        items = line.strip().split('|')
        if items[5] not in dic:
            dic[items[5]] = 1
        else:
            dic[items[5]] += 1
    for d in dic:
        print d, dic[d]


if __name__ == '__main__':
    count_scm()
