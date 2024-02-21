# 每次进程重启后的Canary是不同的，但是同一个进程中的Canary都是一样的。并且 通过 fork 函数创建的子进程的 Canary 也是相同的，因为 fork 函数会直接拷贝父进程的内存。
1. 首先利用read覆盖canary第一个字节0x00从而打印获取到canary的值
