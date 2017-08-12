#! /usr/bin/python
# -*- coding: utf-8 -*-

import requests
import lxml.html

URL = "http://make.bcde.jp/category/1/"

req = requests.get(URL)
root = lxml.html.fromstring(req.text)

anchors = root.xpath('//a')
# for anchor in anchors:
#    print anchor.attrib['href']

h1s = root.xpath('//p')
print "p\n"
# for h1 in h1s:
#    print h1.text


bodys = root.xpath('//body')
print "body\n"
for h1 in bodys:
    print h1.text

content1 = root.get_element_by_id('content1').text
# print content1

content = root.get_element_by_id('content').text_content
# print content