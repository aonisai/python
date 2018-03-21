#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import tempfile
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("setting.ini")

tmp = tempfile.TemporaryFile()
section1 = "development"
try:
    tmp.write(section1+"\n")
    for i, j in config.items(section1):
        i = i.capitalize()
        tmp.write("  " + i + "  " + j + "\n")
    tmp.seek(0)
    print tmp.read()
finally:
    tmp.close()
