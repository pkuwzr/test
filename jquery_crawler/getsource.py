#!/usr/bin/env python
# coding=utf-8

import sys, os

GOOD_SUFFIX = ('.html', '.htm', '.xhtml', '.jsp', '.php', '.js')


def contains_script(f):
    try:
        with open(f) as tmp_f:
            for l in tmp_f:
                if 'type="text/javascript"' in l:
                    return True
        return False
    except Exception, e:
        print '______________________________________'
        print os.getcwd()
        print e


def testAndRemove():
    '''
    Depth first walk the directory tree of the target directory.
    '''
    try:
        fs = os.listdir('.')
        for f in fs:
            if os.path.isdir(f):
                os.chdir(f)
                testAndRemove()
                os.chdir('..')
                result = len(os.listdir(f))
                if not result:
                    os.removedirs(f)
            else:
                f_suff = os.path.splitext(f)[-1]
                if f_suff not in GOOD_SUFFIX:
                    os.remove(f)
                if f_suff in GOOD_SUFFIX[:-1]:
                    if not contains_script(f):
                        os.remove(f)
    except Exception, e:
        print os.getcwd()
        print e


if __name__ == '__main__':
    target = sys.argv[1]
    LAST_WD = os.getcwd()
    os.chdir(target)
    testAndRemove()
    os.chdir(LAST_WD)
