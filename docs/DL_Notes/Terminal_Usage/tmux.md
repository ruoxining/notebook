install
```latex
git clone https://github.com/tmux/tmux.git
cd tmux
sh autogen.sh
./configure && make
```

```latex
# Ubuntu 或 Debian
$ sudo apt-get install tmux

# CentOS 或 Fedora
$ sudo yum install tmux

# Mac
$ brew install tmux
```

开启新进程的通用命令
```latex
tmux new-session -d -s my_session \; send-keys "<command>" Enter
```

上传文件用ssh到服务器
```latex
tmux new-session -d -s my_session \; send-keys "rsync filename username@ip_address:/home/username" Enter
```

运行python脚本
```latex
tmux new-session -d -s <session name> \; send-keys "python3 <program name>.py" Enter
```

查看正在运行的进程
```latex
tmux ls
```

杀死进程
```latex
tmux kill-session -t <session name>
```

通过重定向输出实现tmux会话中与正在运行的程序通信。
```latex
tmux new-session -d -s <session name> \; send-keys "python3 <program name>.py > output.txt" Enter
```

查看output.txt的内容
```Python
cat output.txt
```

实时监测文件的变化
可以在终端中随时显示output.txt的内容
```latex
tail -f output.txt
```


```latex
ssh username@server_address tmux ls
```

```latex
ssh username@server_address tmux ls -t <session_name>
```