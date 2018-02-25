#! /home/enigma/.pyenv/versions/2.7.13/bin/python
# -*- coding: utf-8 -*-

import pexpect
import sys

pexpect_list = [u"password", u"#", u">", u"$", pexpect.EOF, pexpect.TIMEOUT]

try:
    prc = pexpect.spawn("usr/bin/ssh 192.168.56.161")
    prc.logfile= sys.stdout
    prc.expect("assword:")
    prc.sendline("toor")
    index = prc.expect(pexpect_list)
    if index == 3:
        prc.sendline("ls -l")
    # prc.expect("$")
        index = prc.expect(pexpect_list)
        prc.close()
        index = prc.expect(pexpect_list)
except pexpect.EOF:
    print("eof")
except pexpect.TIMEOUT:
    print("timeout")
except:
    print("error")
