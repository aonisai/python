#! /home/enigma/.pyenv/versions/2.7.13/bin/python
# -*- coding: utf-8 -*-

import pexpect

expect_list = [u"#", u">"]
log = "log_test"
devlist = "sshlist.txt"
command_list = ["ls", "echo test"]

with open(devlist, "r") as devlist, open(log, "w") as logf:
    for line in devlist:
        no, ip, user, pw = line.split(",")
        pw = pw.replace("\n", "")
        try:
            prc = pexpect.spawn("usr/bin/ssh %s@%s" % (user, ip), logfile=logf)
            prc.write("****** connect %s *****\n" % ip)
            prc.expect("(?!)password:")
            prc.sendline(pw)
            prc.expect("$")
            # prc.expect(">")
            prc.sendline(command_list[1])
            # prc.expect("$")
            prc.expect("#")
            prc.sendline(command_list[0])
            prc.expect(expect_list)
            prc.write("%%%%%% session closed %s %%%%%%\n" % ip)
            prc.close()
        except pexpect.EOF as eof:
            print("eof")
            print(eof)
        except pexpect.TIMEOUT as timeout:
            print("timeout")
            print(timeout)
        except:
           print("error")