#! /usr/bin/python
# -*- coding: utf-8 -*-

import def_scanner
from cStringIO import StringIO

def firstword(line):
    print line.split()[0]
# file = open('/home/enigma/temp/test')
# def_scanner.scanner(file, firstword)

# string = StringIO('one\ntwo xxx\nhree\n')
# def_scanner.scanner(string, firstword)

class MyStream(object):
    def __iter__(self):
        return iter(['a\n', 'b c d\n'])
object = MyStream()
def_scanner.scanner(object, firstword)