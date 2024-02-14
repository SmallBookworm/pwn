# 用IDApro打开pwn1，从main函数按下Tab键到‘presudcode’界面中，找到漏洞：gets(s, argv);
# 双击main函数到其stack中，计算s距离返回地址：0xf+0x8
# 由于堆栈平衡，需要利用main函数中retn指令，找到其地址0x0401185,找到可以利用的函数fun的地址0x0401186 