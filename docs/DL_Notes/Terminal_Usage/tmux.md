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

用ssh下载

```latex

```

运行python脚本

```latex
tmux new-session -d -s my_session \; send-keys "python3 test.py" Enter
```

查看正在运行的进程

```latex
tmux ls
```

杀死进程

```latex
tmux kill-session -t <session name>
```

```latex

```