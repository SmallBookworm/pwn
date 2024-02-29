# 这一类题目的基本做法
1. 利用一个程序已经执行过的函数去泄露它在程序中的地址，然后取末尾3个字节，去找到这个程序所使
用的libc的版本。

2. 程序里的函数的地址跟它所使用的libc里的函数地址不一样，程序里函数地址=libc里的函数地址+偏移
量，在1中找到了libc的版本，用同一个程序里函数的地址-libc里的函数地址即可得到偏移量

3. 得到偏移量后就可以推算出程序中其他函数的地址，知道其他函数的地址之后我们就可以构造rop去执
行system（’/bin/sh‘）这样的命令

# libc中找字符串：
1. `ROPgadget --binary libc6_2.27-0ubuntu3_amd64.so --string '/bin/sh'`
2. `from pwn import *`
`libc = ELF("./libc.so")`
`binsh = libc.search("/bin/sh").next()`

# 服务器返回‘timeout: the monitored command dumped core ’，说明有栈未平衡等报错