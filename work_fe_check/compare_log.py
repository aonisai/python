#! /home/enigma/.pyenv/versions/2.7.13/bin/python
# -*- coding: utf-8 -*-

# countlog = "countlog.csv"
# ac_report = "ac_report.csv"
countlog = "/home/enigma/temp/work/countlog.csv"
ac_report = "/home/enigma/temp/work/ac_report.csv"

with open(countlog, "r") as countlog:
    for line in countlog:
        devname, lognumber = line.split(",")
        lognumber = lognumber.replace("\n", "")
        with open(ac_report, "r") as ac:
            while True:
                acline = ac.readline()
                if acline.find(devname + ",FireEye") != -1:
                    print "found", devname
                    trash, ac_lognumber = acline.rsplit(",", 1)
                    ac_lognumber = int(lognumber)
                    if lognumber == ac_lognumber:
                        print "ログ件数一致"
                    else:
                        print "ログ件数不一致"
                    break
                elif not acline:
                    print "not found"
                    break
