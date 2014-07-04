#!/usr/bin/env python
# coding=utf-8

import sys
all_projects = []
for line in sys.stdin:
    try:
        items = line.strip().split('|')
        if (len(items) == 7):
            if items[1] not in all_projects:
                flag = False
                if items[5] != 'None':
                    flag = True
                else:
                    if items[6].startswith('http://') and items[6].startswith('svn://') and items[6].startswith('git://') and not items[6].endswith('...'):
                        flag = True
                if flag:
                    if '.git' in items[6]:
                        items[6] = items[6][0:items[6].index('.git') + 4]
                    print '|'.join(items)
                    all_projects.append(items[1])
    except Exception, e:
        pass

print len(all_projects)
