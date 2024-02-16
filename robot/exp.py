from pwn import *

#r=process('./as')
r=remote("train2024.hitctf.cn",26191)

for i in range(0,100):
    s=r.recvuntil(b"= ")
    s=s.split(b':')[1]
    nums=s[:-2].split(b'*')
    nums=[int(num) for num in nums]
    r.sendline(bytes(str(nums[0]*nums[1]),encoding="ascii"))
r.interactive()