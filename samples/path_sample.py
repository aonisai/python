#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

#
print __file__
print("__file__: %s " % __file__)
print("dirname: %s" % (os.path.dirname(__file__)))
print("abspath: %s" % (os.path.abspath(__file__)))
print("%s" % (os.path.dirname(os.path.abspath(__file__))))
print("path.join: %s" % (os.path.abspath(os.path.join(os.path.dirname(__file__), 'test09.py'))))
print("base: %s" % (os.path.basename(__file__)))
print("cwd: %s" % (os.getcwd()))
