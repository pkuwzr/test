#!/usr/bin/env python
# coding=utf-8

import sys
sum = 0
for line in sys.stdin:
    try:
        items = line.strip().split('|')
        if (len(items) >= 4):
            if (items[5].startswith('http://') or items[5].startswith('git://')) and not items[5].endswith('...'):
                print items[5]
                sum += 1
    except Exception, e:
        pass

print sum
