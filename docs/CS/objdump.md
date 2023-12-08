# Objdump工具

源代码文件名mytest.c

```bash
gcc -c -g -o mytest mytest.c
objdump -s -d main.o > main.o.txt
```

目标文件反汇编，同时显示源代码

```bash
gcc -g -c -o main.o main.c
objdump -S -d main.o > main.o.txt
```

显示源代码的同时显示行号

```bash
objdump -j .text -ld -C -S main.o > main.o.txt
```

可执行文件反汇编

```bash
gcc -o main main.c
objdump -s -d main > main.txt
```

同时显示源代码

```bash
gcc -g -o main main.c
objdump -S -d main > main.txt
```