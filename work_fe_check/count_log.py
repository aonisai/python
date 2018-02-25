#! /home/enigma/.pyenv/versions/2.7.13/bin/python
# -*- coding: utf-8 -*-

import csv

# log = "log_test"
# csvfile = "countlog.csv"
log = "/home/enigma/temp/work/log_test"
csvfile = "/home/enigma/temp/work/countlog.csv"

def main():
    count_line = 1
    devname = ""
    # count_log = 0
    with open(log, "r") as logf:
        while True:
            line0 = logf.readline()
            connect_exist = line0.find("connect")
            if connect_exist != -1:
                count_log = 0
                log_start_line, log_end_line = 0

                while True:
                    line1 = logf.readline()
                    enable_exist = line1.find("> enable")
                    close_exist = line1.find("session closed")
                    if enable_exist != -1:
                        devname = line1[1:enable_exist-1]
                        print "enable", count_line
                        break
                    elif close_exist != -1:
                        print "error : found 'session closed'"
                        break
                    elif not line1:
                        print "error : not found 'enable'"
                        break
                    count_line += 1
                count_line += 1

                while True:
                    line2 = logf.readline()
                    show_exist = line2.find("show")
                    close_exist = line2.find("session closed")
                    if show_exist != -1:
                        log_start_line = count_line+2
                        print "show", count_line
                        count_line += 1
                        break
                    elif close_exist != -1:
                        print "error : found 'session closed'"
                        break
                    elif not line2:
                        print "error : not found 'show'"
                        break
                    count_line += 1

                while True:
                    line3 = logf.readline()
                    k_exist = line3.find("[K")
                    close_exist = line3.find("session closed")
                    if k_exist != -1:
                        log_end_line = count_line
                        print "[K", count_line
                        count_line += 1
                        count_log = log_end_line - log_start_line
                        break
                    elif close_exist != -1:
                        count_log = 0
                        print "closed", count_line
                        count_line += 1
                        break
                    elif not line3:
                        print "error : not found log end"
                        break
                    count_line += 1

                if not devname:
                    devname_and_count = [devname, count_log]
                    with open(csvfile, "w") as csvf:
                        writer = csv.writer(csvf)
                        writer.writerow(devname_and_count)

            elif not line0:
                if not devname:
                    print "error : not found any devices"
                else:
                    print "finish"
                break
            count_line += 1

if __name__ == '__main__':
    main()