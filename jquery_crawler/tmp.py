#!/usr/bin/env python
# coding=utf-8

import sys
for line in sys.stdin:
    items = line.strip().split('|')
    if len(items) == 7 and items[5] == 'GIT' and not items[6].endswith('.git'):
        if not items[6].endswith('.git'):
            print items[6]
