#! /usr/bin/python
# -*- coding: utf-8 -*-

def scanner(fileobject, linehandler):
    for line in fileobject:
        linehandler(line)
