#! /usr/bin/python
# -*- coding: utf-8 -*-

from urllib import urlopen

doc = urlopen("http://w ww.python.org").read()
print doc