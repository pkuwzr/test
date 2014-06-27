#!/usr/bin/env python
# coding=utf-8

import requests
from BeautifulSoup import BeautifulSoup as BS

class Project:
    """
    This is the object for projects using jquery.
    """
    def __init__(self, n, ca, un, a, s, l):
        self.name = n
        self.codeAmount = ca
        self.userNumber = un
        self.activity = a
        self.scm = s
        self.link = l


def crawl_download_link(url):
    """
    Crawl the page that the url represents and return the download link of the project.
    """
    scm = None
    download_link = None
    try:
        # get the browse code link from home page of the project.
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            soup = BS(response.content)
            browse_code_btn = soup.find('a', {'class':'btn btn-info browse_code_button'})
            # if find the browse code btn, get the download link
            if browse_code_btn:
                browse_code_link = browse_code_btn['href']
                # get the svn or git address of the project from browse code page.
                response = requests.get(browse_code_link).content
                soup = BS(response)
                basic_info_table = soup.find('table', {'id':'basic_info'})
                if basic_info_table:
                    location_number = int(basic_info_table.contents[1].contents[3].span.text)
                    # source code management type: git or svn
                    scm = basic_info_table.contents[3].contents[3].span.span.text
                    codeloc_div = soup.find('div', {'class':'codeloc'})
                    if location_number == 1:
                        download_link = codeloc_div.div.p.text
                    else:
                        download_link = codeloc_div.select.option.text
            # else return the code location label.
            else:
                dl = soup.find('dl')
                dds = dl.findAll('dd')
                download_link = dds[1].text
    except AttributeError, ae:
        print ae, url
    except Exception, e:
        print e, url
    return scm, download_link


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
        s, l = crawl_download_link("http://www.ohloh.net" + div.h2.a['href'])
        stat_div = div.find('div', {'class':'float_left'}).find('div', {'class':'stats float_left'})
        ps = stat_div.contents
        ca, un = ps[1].a.text, ps[7].a.text 
        activity_div = div.find('div', {'class':'float_left'}).find('div', {'class':'reviews-and-pai float_left'})
        a = activity_div.div.text
        project = Project(n, ca, un, a, s, l)
        projects.append(project)
    return projects



if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    sum = 0
    for i in range(1, 217):
        url = 'http://www.ohloh.net/tags/jquery?page=' + str(i)
        for p in crawl_projects(url):
            sum += 1
            print "%d|%s|%s|%s|%s|%s|%s" % (sum, p.name, p.codeAmount, p.userNumber, p.activity, p.scm, p.link)
