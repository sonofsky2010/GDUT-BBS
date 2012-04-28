#!/usr/bin/env python
# encoding: utf-8
"""
helper.py

Created by li shunnian on 2012-04-19.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import urllib2

def data_from_url(url):
    con = urllib2.urlopen(url)
    data = con.read()
    return data

def change_code(data, code_src, code_dest):
    a_unicode = data.decode(code_src)
    dest_data = a_unicode.encode(code_dest)
    return dest_data
