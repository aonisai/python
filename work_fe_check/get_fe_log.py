#! /home/enigma/.pyenv/versions/2.7.13/bin/python
# -*- coding: utf-8 -*-

import pexpect

expect_list = ["(yes/no)", "(?!)password:", "#", ">"]
log = "log_test"
devlist = "ssh_list.txt"
command_list = ["ls", "echo test"]

with open(devlist, "r") as devlist, open(log, "w") as logf:
    for line in devlist:
        no, ip, user, pw = line.split(",")
        pw = pw.replace("\n", "")
        try:
            prc = pexpect.spawn("usr/bin/ssh %s@%s" % (user, ip), logfile=logf)
            prc.write("****** connect %s *****\n" % ip)
            for i in range(4):
                index = prc.expect(expect_list)
                if index == 0:
                    prc.sendline("yes")
                elif index == 1:
                    prc.sendline(pw)
                elif index == 2:
                    prc.sendline(command_list[1])
                elif index == 3:
                    prc.sendline(command_list[0])
                    index = prc.expect(expect_list)
                    prc.write("%%%%%% session closed %s %%%%%%\n" % ip)
                    prc.close
                    break
        except pexpect.ExceptionPexpect as ep:
            print ep
        except:
            print "error"
