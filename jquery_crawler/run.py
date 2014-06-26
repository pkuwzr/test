#!/usr/bin/env python
# coding=utf-8

import threading
import crawler
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

TOTAL_TASKS = 217
THREAD_NUM = 10
EACH_TASKS = TOTAL_TASKS / THREAD_NUM

class Crawler(threading.Thread):

    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.lower = self.id * EACH_TASKS + 1
        self.upper = self.lower + EACH_TASKS
        if self.id == THREAD_NUM:
            self.upper = TOTAL_TASKS + 1

    def run(self):
        for i in range(self.lower, self.upper):
            url = 'http://www.ohloh.net/tags/jquery?page='+str(i)
            for p in crawler.crawl_projects(url):
                print "%d|%s|%s|%s|%s|%s" % (i, p.name, p.codeAmount, p.userNumber, p.activity, p.link)

if __name__ == '__main__':
    for i in range(THREAD_NUM):
        t = Crawler(i)
        t.start()

