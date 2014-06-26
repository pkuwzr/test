#!/usr/bin/env python
# coding=utf-8

import requests
from BeautifulSoup import BeautifulSoup as BS

class Project:
    """
    This is the object for projects using jquery.
    """
    def __init__(self, n, ca, un, a, l):
        self.name = n
        self.codeAmount = ca
        self.userNumber = un
        self.activity = a
        self.link = l


def crawl_download_link(url):
    """
    Crawl the page that the url represents and return the download link of the project.
    """
    try:
        response = requests.get(url).content
        soup = BS(response)
        dl = soup.find('dl')
        dds = dl.findAll('dd')
        download_link = dds[1].text
    except AttributeError, ae:
        download_link = None
        print ae, url
    return download_link


def crawl_projects(url):
    """
    Crawl the page that the url represents and turn the content into a list of Project.
    """
    response = requests.get(url).content
    soup = BS(response)
    divs = soup.findAll('div', {'class':'project searchable well'})
    projects = []
    for div in divs:
        n = div.h2.a.text
        l = crawl_download_link("http://www.ohloh.net" + div.h2.a['href'])
        stat_div = div.find('div', {'class':'float_left'}).find('div', {'class':'stats float_left'})
        ps = stat_div.contents
        ca, un = ps[1].a.text, ps[7].a.text 
        activity_div = div.find('div', {'class':'float_left'}).find('div', {'class':'reviews-and-pai float_left'})
        a = activity_div.div.text
        project = Project(n, ca, un, a, l)
        projects.append(project)
    return projects



if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    for i in range(191, 217):
        url = 'http://www.ohloh.net/tags/jquery?page=' + str(i)
        for p in crawl_projects(url):
            print "%s|%s|%s|%s|%s" % (p.name, p.codeAmount, p.userNumber, p.activity, p.link)
