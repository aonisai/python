#! /home/enigma/.pyenv/versions/2.7.13/bin/python
# -*- coding: utf-8 -*-

import csv

countlog = "countlog.csv"
ac_report = "ac_report.csv"
count_dict = {}

try:
    with open(countlog, "r", encoding="shift_jis") as countlog:
        reader = csv.reader(countlog, delimiter='\n', quotechar='"')
        # next(reader)
        for line in reader:
            devname, lognumber = line.split(",")
            count_dict[devname] = lognumber
except csv.Error as e:
    print e

    # for line in countlog:
    #    devname, lognumber = line.split(",")
    #    lognumber = int(lognumber.replace("\n", ""))
    #    ac_lognumber = 0

try:
    with open(ac_report, "r", encoding="shift_jis") as ac:
        ac_reader = csv.reader(ac, delimiter='\n', quotechar='"')
        next(ac_reader)
        for ac_line in ac_reader:
            device_exist = ac_line.find(devname + ",FireEye")
            if device_exist != -1:
                trash, ac_lognumber = ac_line.rsplit(",", 1)
                ac_lognumber = int(ac_lognumber)
                if lognumber == ac_lognumber:
                    print "ログ件数一致"
                    break
                else:
                    print "ログ件数不一致"
                    break
        if lognumber == 0:
            print "ログ件数一致"
except csv.Error as e:
    print e
