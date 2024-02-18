#思路
1. 首先下发了ld和libc文件，使用 `patchelf --set-interpreter`替换加载器，`patchelf --replace-needed`替换动态加载的库
2. 通过程序提供的puts函数地址确定libc的基址
3. 使用ROPgadget获取程序和libc中可利用的代码段