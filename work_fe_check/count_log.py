#! /home/enigma/.pyenv/versions/2.7.13/bin/python
# -*- coding: utf-8 -*-

import csv

log = "log_test"
csvfile = "countlog.csv"

count_line = 1
devname = ""
device_name_and_count = []

# count_log = 0
with open(log, "r") as read_log:
    phase = 0

    for read_line in read_log:
        if phase == 0:
            connect_exist = read_line.find("connect")
            if connect_exist != -1:
                count_log = 0
                log_start_line = 0
                log_end_line = 0
                phase = 1

        elif phase == 1:
            show_exist = read_line.find("show")
            if show_exist != -1:
                devname = read_line[1:show_exist-1]
                log_start_line = count_line + 2
                phase = 2

        elif phase == 2:
            close_exist = read_line.find("session closed")
            if close_exist != -1:
                log_end_line = count_line
                count_log = log_end_line - log_start_line
                device_name_and_count = [devname, count_log]

        count_line += 1

if device_name_and_count is not None:
    try:
        with open(csvfile, "w", encoding="shift_jis") as csvf:
            writer = csv.writer(csvf)
            for i in device_name_and_count:
                print i
                # writer.writerow(i)
    except csv.Error as e:
        print e
else:
    print "error : failed to write csv"
