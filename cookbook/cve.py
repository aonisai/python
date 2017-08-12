#! /usr/bin/python
# -*- coding: utf-8 -*-

import def_scanner
import re


def firstword(line):
    # print line.split()[0]
    print line


def find_cve(line):
    # print re.findall('cve-....-....', line, re.IGNORECASE)
    string_list = re.findall('cve-....-....', line, re.IGNORECASE)
    if(len(string_list) == 0):
        pass
    else:
        rtn_list.append(string_list)
    # print string_list


def remove_room(line):
    removed_list = filter(lambda s: s != '', line)
    print removed_list

file = open('/home/enigma/temp/cve_note')
# file = open('/home/enigma/temp/test')
cve_list = []
rtn_list =[]
def_scanner.scanner(file, find_cve)
for v in rtn_list:
    for i in v:
        cve_list.append(i)
cve_list = list(set(cve_list))
print cve_list
# def_scanner.scanner(file, remove_room)

