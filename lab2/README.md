# Lab 2 - Command Line 
For this lab, the task is to learn basic command-line interface commands and clone a GitHub repository directly to your computer. Each section will have a command and the resolution after running on my laptop. In the absence of a Linux terminal, I used the Ubuntu Linux environment as a replacement. I used the following website to get the description for each command [website](https://www.geeksforgeeks.org/linux-commands-cheat-sheet/).


`Command 1: hostname`
```sh
$ hostname
ubuntu
```
Displays the hostname portion of the full computer name of the computer.

`Command 2: env`
```sh
$ env
SHELL=/bin/bash
SESSION_MANAGER=local/ubuntu:@/tmp/.ICE-unix/2716,unix/ubuntu:/tmp/.ICE-unix/2716
QT_ACCESSIBILITY=1
COLORTERM=truecolor
XDG_CONFIG_DIRS=/etc/xdg/xdg-ubuntu:/etc/xdg
SSH_AGENT_LAUNCHER=gnome-keyring
XDG_MENU_PREFIX=gnome-
GNOME_DESKTOP_SESSION_ID=this-is-deprecated
GNOME_SHELL_SESSION_MODE=ubuntu
SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
XMODIFIERS=@im=ibus
DESKTOP_SESSION=ubuntu
GTK_MODULES=gail:atk-bridge
PWD=/home/ubuntu/shared/ee322/lab2
LOGNAME=ubuntu
XDG_SESSION_DESKTOP=ubuntu
XDG_SESSION_TYPE=wayland
SYSTEMD_EXEC_PID=2756
XAUTHORITY=/run/user/1000/.mutter-Xwaylandauth.RJAR12
HOME=/home/ubuntu
USERNAME=ubuntu
IM_CONFIG_PHASE=1
LANG=en_US.UTF-8
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
XDG_CURRENT_DESKTOP=ubuntu:GNOME
VTE_VERSION=6800
WAYLAND_DISPLAY=wayland-0
GNOME_TERMINAL_SCREEN=/org/gnome/Terminal/screen/2ecce4b9_8d1f_4e3d_a611_7e6576aa2c9e
GNOME_SETUP_DISPLAY=:1
LESSCLOSE=/usr/bin/lesspipe %s %s
XDG_SESSION_CLASS=user
TERM=xterm-256color
LESSOPEN=| /usr/bin/lesspipe %s
USER=ubuntu
GNOME_TERMINAL_SERVICE=:1.99
DISPLAY=:0
SHLVL=1
QT_IM_MODULE=ibus
XDG_RUNTIME_DIR=/run/user/1000
XDG_DATA_DIRS=/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin
GDMSESSION=ubuntu
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
_=/usr/bin/env
OLDPWD=/home/ubuntu/shared/ee322
```
This command displayed all of my environment Variables on my computer. These variables are user-definable values that can affect the way running processes will behave on a computer. Environment variables are part of the environment in which a process runs. For example, a running process can query the value of the TEMP environment variable to discover a suitable location to store temporary files, or the HOME or USERPROFILE variable to find the directory structure owned by the user running the process. [WIKI Article](https://en.wikipedia.org/wiki/Environment_variable). 

`Command 3: ps`
```sh
$ ps
 PID TTY          TIME CMD
   3340 pts/0    00:00:00 bash
   4574 pts/0    00:00:00 ps
```
Displays the running processes.

`Command 4: Print Working Directory`
```sh
$ pwd
/home/ubuntu/shared/ee322/lab2
```
This command will display the current directory.

`Command 5: git clone`
```sh
$ git clone https://github.com/kevinwlu/iot.git
Cloning into 'iot'...
remote: Enumerating objects: 25066, done.
remote: Counting objects: 100% (106/106), done.
remote: Compressing objects: 100% (82/82), done.
remote: Total 25066 (delta 54), reused 13 (delta 13), pack-reused 24960 (from 3)
Receiving objects: 100% (25066/25066), 33.53 MiB | 1.79 MiB/s, done.
Resolving deltas: 100% (16144/16144), done.
Updating files: 100% (405/405), done.
```
The command will clone a git repository to another folder. In this case, I took the iot GitHub repo from Professor Kevin Lu and cloned it directly to my pc in my labs folder. For this command, I had to install git on my environment first which was done by going to the git [website](https://git-scm.com/downloads). [documentation](https://git-scm.com/docs/git-clone)

`Command 6: cd`
```sh
$ cd iot
$ \iot
```
Moves into the folder/path that was specified in the parameter. It will move up to the parent folder if no parameters are specified.

`Command 7: ls`
```sh
$ ls
apps       health    lesson11  lesson5  lesson9    special_problems
cases      hype      lesson2   lesson6  make       standards
design     lesson1   lesson3   lesson7  projects   systems
economics  lesson10  lesson4   lesson8  README.md  tools
```
Lists all the files in the current directory.

`Command 8: disk free`
```sh
$ ds
Filesystem     1K-blocks      Used Available Use% Mounted on
tmpfs             400984      1576    399408   1% /run
/dev/sda3       25106692  17841408   5964600  75% /
tmpfs            2004904         0   2004904   0% /dev/shm
tmpfs               5120         4      5116   1% /run/lock
/dev/sda2         524252      6228    518024   2% /boot/efi
shared         999116796 211078388 788038408  22% /mnt/shared
tmpfs             400980       136    400844   1% /run/user/1000
```
Gets the file information of your computer.

`Command 9: mkdir`
```sh
$ mkdir demo
$ ls
apps    economics  lesson10  lesson4  lesson8   README.md         tools
cases   health     lesson11  lesson5  lesson9   special_problems
demo    hype       lesson2   lesson6  make      standards
design  lesson1    lesson3   lesson7  projects  systems
```
Makes a directory of the specified name in the parameter. As seen now, "demo" is now part of the directory 

`Command 10: nano`
```sh
$ nano file
$ ls
file.txt
```
Creates a new text file with the name in the parameter. I wrote some text within the file with the editor, which will be shown next.

`Command 11: cat`
```sh
$ cat file.txt 
Hello World
```
This gets the contents of the files. It displays what I wrote in the previous command that was showcased.

`Command 11: cp`
```sh
$ cp file.txt file1.txt
$ ls
file1.txt  file.txt
$ cat file1.txt 
Hello World
```
The command will copy the contents of one file to another file. Because there was no "file1.txt" it created the file and copied all the content from "file.txt" to it.

`Command 12: mv`
```sh
$ mv file.txt file2.txt
$ ls
file1.txt  file2.txt
```
This command will move a file to another path as specified in the parameters. Since we specified a file that did not exist the command renamed the "file.txt" to "file1.txt".

`Command 13: rm`
```sh
$ rm file2.txt
$ ls
file1.txt
```
Removes the file in the parameter. 

`Command 14: clear`
```sh
$ clear
```
Clears all previous inputs in the terminal. 

`Command 15: man uname`
```sh
$ man uname
UNAME(1)                         User Commands                        UNAME(1)

NAME
       uname - print system information

SYNOPSIS
       uname [OPTION]...

DESCRIPTION
       Print certain system information.  With no OPTION, same as -s.

       -a, --all
              print  all  information,  in the following order, except omit -p
              and -i if unknown:

       -s, --kernel-name
              print the kernel name

       -n, --nodename
              print the network node hostname

       -r, --kernel-release
              print the kernel release

       -v, --kernel-version
              print the kernel version

       -m, --machine
              print the machine hardware name

       -p, --processor
              print the processor type (non-portable)

       -i, --hardware-platform
              print the hardware platform (non-portable)

       -o, --operating-system
              print the operating system

       --help display this help and exit

       --version
              output version information and exit

AUTHOR
       Written by David MacKenzie.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report any translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright © 2020 Free Software Foundation, Inc.   License  GPLv3+:  GNU
       GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This  is  free  software:  you  are free to change and redistribute it.
       There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       arch(1), uname(2)

       Full documentation <https://www.gnu.org/software/coreutils/uname>
       or available locally via: info '(coreutils) uname invocation'

GNU coreutils 8.32               February 2024                        UNAME(1)
```
There are two commands here "man" which displays the manual/help of the next argument and "uname" which we will talk about in the next command. 

`Command 16: uname -a`
```sh
$ uname -a
Linux ubuntu 6.8.0-45-generic #45~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Wed Sep 11 15:25:05 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
```
Displays all system information.

`Command 17: ifconfig`
```sh
$ ifconfig
enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fe80::3c5c:2281:1ac5:c2d  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:4a:36:4f  txqueuelen 1000  (Ethernet)
        RX packets 623606  bytes 937494338 (937.4 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 26450  bytes 1996693 (1.9 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 1025  bytes 123794 (123.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1025  bytes 123794 (123.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


```
Display network interface information.

`Command 18: ping localhost`
```sh
$ ping -c 10 localhost
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.037 ms
64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.026 ms
64 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.069 ms
64 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.039 ms
64 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.033 ms
64 bytes from localhost (127.0.0.1): icmp_seq=6 ttl=64 time=0.040 ms
64 bytes from localhost (127.0.0.1): icmp_seq=7 ttl=64 time=0.308 ms
64 bytes from localhost (127.0.0.1): icmp_seq=8 ttl=64 time=0.049 ms
64 bytes from localhost (127.0.0.1): icmp_seq=9 ttl=64 time=0.029 ms
64 bytes from localhost (127.0.0.1): icmp_seq=10 ttl=64 time=0.040 ms

--- localhost ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9546ms
rtt min/avg/max/mdev = 0.026/0.067/0.308/0.081 ms
```
Verifies IP-level connectivity to another TCP/IP computer by sending Internet Control Message Protocol (ICMP) echo Request messages. The receipt of the corresponding echo Reply messages is displayed, along with round-trip times. ping is the primary TCP/IP command used to troubleshoot connectivity, reachability, and name resolution. The localhost in this case is our computer and there the connection is good. I choose to ping 10 times in order to verify the connection.

`Command 19: netstat`
```sh
$ netstat
Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
udp        0      0 ubuntu:bootpc           _gateway:bootps         ESTABLISHED
Active UNIX domain sockets (w/o servers)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  2      [ ]         DGRAM                    14775    
unix  3      [ ]         STREAM     CONNECTED     9405     
unix  3      [ ]         STREAM     CONNECTED     4022     /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     15695    /run/user/1000/at-spi/bus
unix  3      [ ]         STREAM     CONNECTED     15472    /run/user/1000/at-spi/bus
...
unix  3      [ ]         STREAM     CONNECTED     13572    /run/user/1000/bus
```
Displays active TCP connections, ports on which the computer is listening, Ethernet statistics, the IP routing table, IPv4 statistics (for the IP, ICMP, TCP, and UDP protocols), and IPv6 statistics (for the IPv6, ICMPv6, TCP over IPv6, and UDP over IPv6 protocols). Used without parameters, this command displays active TCP connections. I cut the list down for readability.



