#! /usr/bin/python
# -*- coding: utf-8 -*-

def scanner(fileobject, linehandler):
    for line in fileobject:
        linehandler(line)

import scanner
def firstword(line):
    print line.split()[0]
file = open('/home/enigma/temp/cve_note')
scanner(file, firstword)
