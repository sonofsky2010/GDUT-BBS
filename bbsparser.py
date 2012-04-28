#!/usr/bin/env python
# encoding: utf-8
"""
bbsparser.py

Created by li shunnian on 2012-04-19.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from lxml import etree
from lxml import html
import helper
topic_url = "http://bbs.gdut.edu.cn/ngpxbbs/50topic.php"
bbs_url_prex = "http://bbs.gdut.edu.cn/ngpxbbs/"
def get_hot_bbs_list():
    page_data = helper.data_from_url(topic_url)
#    html = change_code(html, 'gbk', 'utf-8')
    root = etree.HTML(page_data)
    trs = root.xpath('//tr')
    if len(trs) < 2:
        return None
    topics_tr = trs[1:]
    result = []
    for a_topic in topics_tr:
        a_dic = {}
        tds = a_topic.findall('td')
        td_title = tds[0]
        td_author = tds[1]
        title_link = td_title.find('a')
        title = title_link.text
        title_ref = title_link.get('href')
        author_link = td_author.find('a')
        author = author_link.text
        author_ref = author_link.get('href')
        a_dic['title'] = title
        a_dic['title_ref'] = title_ref
        a_dic['author'] = author
        a_dic['author_ref'] = author_ref
        result.append(a_dic)
    return result
def posts_from(url):
    pate_data = helper.data_from_url(url)
    root = 
    
def main():
    topics = get_hot_bbs_list()
    for a_topic in topics:
        print """title: %s
title href: %s
author: %s
author href: %s""" % (a_topic['title'], a_topic['title_ref'], a_topic['author'], a_topic['author_ref'])


if __name__ == '__main__':
    main()

