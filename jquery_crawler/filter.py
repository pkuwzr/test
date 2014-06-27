#!/usr/bin/env python
# coding=utf-8

import sys
all_projects = []
for line in sys.stdin:
    try:
        items = line.strip().split('|')
        if (len(items) == 6):
            if items[1] not in all_projects:
                all_projects.append(items[1])
    except Exception, e:
        pass

print len(all_projects)
