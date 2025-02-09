# Lab 2 - Command Line 
For this lab, the task is to learn basic command line interface commands and clone a GitHub repository directly to your computer. Each section will have a command and the resolution after running on my laptop. In the absence of a Linux terminal. I used the Windows Powershell as a replacement for it. As a result, some commands have been changed so I can run them on my Windows machine. I used this [website](https://threatpicture.com/blog/linux-to-powershell/) to change most of the commands to run them.


`Command 1: hostname`
```sh
$ hostname
Bullpen
```
Displays the hostname portion of the full computer name of the computer. [Documentation](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/hostname)

`Command 2: dir env:`
```sh
$ dir env:

Name                           Value
----                           -----
__PSLockDownPolicy             0
ALLUSERSPROFILE                C:\ProgramData
APPDATA                        C:\Users\matty\AppData\Roaming
CommonProgramFiles             C:\Program Files\Common Files
CommonProgramFiles(x86)        C:\Program Files (x86)\Common Files
CommonProgramW6432             C:\Program Files\Common Files
COMPUTERNAME                   BULLPEN
ComSpec                        C:\WINDOWS\system32\cmd.exe
configsetroot                  C:\WINDOWS\ConfigSetRoot
DriverData                     C:\Windows\System32\Drivers\DriverData
HOMEDRIVE                      C:
HOMEPATH                       \Users\matty
LOCALAPPDATA                   C:\Users\matty\AppData\Local
LOGONSERVER                    \\BULLPEN
NUMBER_OF_PROCESSORS           20
OneDrive                       C:\Users\matty\OneDrive
OS                             Windows_NT
Path                           C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPo...
PATHEXT                        .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.CPL
PROCESSOR_ARCHITECTURE         AMD64
PROCESSOR_IDENTIFIER           Intel64 Family 6 Model 151 Stepping 2, GenuineIntel
PROCESSOR_LEVEL                6
PROCESSOR_REVISION             9702
ProgramData                    C:\ProgramData
ProgramFiles                   C:\Program Files
ProgramFiles(x86)              C:\Program Files (x86)
ProgramW6432                   C:\Program Files
PSModulePath                   C:\Users\matty\OneDrive\Documents\WindowsPowerShell\Modules;C:\Program Files\WindowsP...
PUBLIC                         C:\Users\Public
SESSIONNAME                    Console
SystemDrive                    C:
SystemRoot                     C:\WINDOWS
TEMP                           C:\Users\matty\AppData\Local\Temp
TMP                            C:\Users\matty\AppData\Local\Temp
USERDOMAIN                     BULLPEN
USERDOMAIN_ROAMINGPROFILE      BULLPEN
USERNAME                       matty
USERPROFILE                    C:\Users\matty
VBOX_MSI_INSTALL_PATH          C:\Program Files\Oracle\VirtualBox\
windir                         C:\WINDOWS
WSLENV                         WT_SESSION:WT_PROFILE_ID:
WT_PROFILE_ID                  {61c54bbd-c2c6-5271-96e7-009a87ff44bf}
WT_SESSION                     396e12f8-9b7a-4bdf-88dd-526a10e27c22
ZES_ENABLE_SYSMAN              1
```
This command displayed all of my environment Variables on my computer. These variables are user-definable values that can affect the way running processes will behave on a computer. Environment variables are part of the environment in which a process runs. For example, a running process can query the value of the TEMP environment variable to discover a suitable location to store temporary files, or the HOME or USERPROFILE variable to find the directory structure owned by the user running the process. [WIKI Article](https://en.wikipedia.org/wiki/Environment_variable). 

`Command 3: Get-Process`
```sh
$ ps

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
    690      36    10916      28352              6140   0 afwServ
    330      14     4396      17984             12088   0 AggregatorHost
    731      33    57104      69356       0.47  10988   1 ApplicationFrameHost
   1758      64   408300     425888              5212   0 aswEngSrv
   1071      33    66364      88144             12140   0 aswidsagent
    320      14    23804      24824      59.27   3672   0 audiodg
    889      14     3972      12844              2824   0 AvDump
    175      10     2560      17288       0.08  13144   1 backgroundTaskHost
   1204      19    16768      33840             20476   0 CC_Engine_x64
     77       8     1204       6372             19540   0 conhost
    957      82    20220      88760       1.61  24812   1 CrossDeviceService
...
    866      37    12132      67352       2.64  12960   1 Widgets
    332      19     5240      27496       0.47  13440   1 WidgetService
    829      37    70884     101212      11.19  16120   1 WindowsTerminal
    135      11     1552       8868              1240   0 wininit
    295      14     3132      14752              1416   1 winlogon
    123       9     1416       8340              6048   0 wlanext
    187      12     4116      14568             16524   0 WmiPrvSE
    447      21    15928      33632             16632   0 WmiPrvSE
    377      21     4024      13448             16700   0 WmiPrvSE
    262      14     2872      14976              6688   0 WMIRegistrationService
    329      13     4360      16156              2728   0 wsc_proxy
```
Retrieves the list of all running applications and processes on a local or remote computer. It shows the process owner, the process ID, or even where on disk the process is located. I cut the list down for readability. The following are what each of the columns mean:
- Handles: The number of handles that the process has opened.
- NPM(K): The amount of non-paged memory that the process is using, in kilobytes.
- PM(K): The amount of pageable memory that the process is using, in kilobytes.
- WS(K): The size of the working set of the process, in kilobytes. The working set consists of the pages of memory that were recently referenced by the process.
- VM(M): The amount of virtual memory that the process is using, in megabytes. Virtual memory includes storage in the paging files on disk.
- CPU(s): The amount of processor time that the process has used on all processors, in seconds.
- ID: The process ID (PID) of the process.
- ProcessName: The name of the process.  
[Article](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process?view=powershell-7.5)

`Command 4: Print Working Directory`
```sh
$ pwd

Path
----
C:\Documents\Stevens2025S\EE322\labs

```
This command will display the current directory.

`Command 5: git clone`
```sh
$ git clone https://github.com/kevinwlu/iot.git
Cloning into 'iot'...
remote: Enumerating objects: 25062, done.
remote: Counting objects: 100% (102/102), done.
remote: Compressing objects: 100% (78/78), done.
remote: Total 25062 (delta 51), reused 13 (delta 13), pack-reused 24960 (from 3)
Receiving objects: 100% (25062/25062), 33.53 MiB | 11.46 MiB/s, done.
Resolving deltas: 100% (16140/16140), done.
```
The command will clone a git repository to another folder. In this case, we took the iot GitHub repo from Professor Kevin Lu and cloned it directly to my pc in my labs folder. [documentation](https://git-scm.com/docs/git-clone)

`Command 6: Get-Location`
```sh
$ cd iot
$ \iot\>
```
Moves into the folder/path that was specified in the parameter. It will move up to the parent folder if no parameters are specified. [Documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-location?view=powershell-7.5)

`Command 7: ls`
```sh
$ ls


    Directory: C:\Documents\Stevens2025S\EE322\labs\iot


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----          2/9/2025   1:53 PM                apps
d-----          2/9/2025   1:53 PM                cases
d-----          2/9/2025   1:53 PM                design
d-----          2/9/2025   1:53 PM                economics
d-----          2/9/2025   1:53 PM                health
d-----          2/9/2025   1:53 PM                hype
d-----          2/9/2025   1:53 PM                lesson1
d-----          2/9/2025   1:53 PM                lesson10
d-----          2/9/2025   1:53 PM                lesson11
d-----          2/9/2025   1:53 PM                lesson2
d-----          2/9/2025   1:53 PM                lesson3
d-----          2/9/2025   1:53 PM                lesson4
d-----          2/9/2025   1:53 PM                lesson5
d-----          2/9/2025   1:53 PM                lesson6
d-----          2/9/2025   1:53 PM                lesson7
d-----          2/9/2025   1:53 PM                lesson8
d-----          2/9/2025   1:53 PM                lesson9
d-----          2/9/2025   1:53 PM                make
d-----          2/9/2025   1:53 PM                projects
d-----          2/9/2025   1:53 PM                special_problems
d-----          2/9/2025   1:53 PM                standards
d-----          2/9/2025   1:53 PM                systems
d-----          2/9/2025   1:53 PM                tools
-a----          2/9/2025   1:53 PM          20626 README.md
```
Lists all the files in the current directory. [Article](https://shellgeek.com/powershell-ls-command/)

`Command 8: disk free`
```sh
$ Get-PSDrive

Name           Used (GB)     Free (GB) Provider      Root                                               CurrentLocation
----           ---------     --------- --------      ----                                               ---------------
Alias                                  Alias
C                 643.77       1244.14 FileSystem    C:\                                 ...Stevens2025S\EE322\labs\iot
Cert                                   Certificate   \
Env                                    Environment
Function                               Function
HKCU                                   Registry      HKEY_CURRENT_USER
HKLM                                   Registry      HKEY_LOCAL_MACHINE
Variable                               Variable
WSMan                                  WSMan

```
Gets the file information of your computer. I changed this command from "df" since the Windows Powershell does not have the "df command. [Documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-psdrive?view=powershell-7.5)

`Command 9: mkdir`
```sh
$ mkdir demo

    Directory: C:\Documents\Stevens2025S\EE322\labs\iot


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----          2/9/2025   2:18 PM                demo
```
Makes a directory of the specified name in the parameter. [Documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/new-item?view=powershell-7.5)

`Command 10: nano`
```sh
$  New-Item -Path . -Name "file.txt" -ItemType "file" -Value ""


    Directory: C:\Documents\Stevens2025S\EE322\labs\iot\demo


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          2/9/2025   2:27 PM              0 file.tx
```
Creates a new text file with the name in the parameter. I changed the command to be able to run inside the PowerShell. [Documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/new-item?view=powershell-7.5)

`Command 11: cat`
```sh
$ Get-Content file.txt
$
```
This gets the contents of the files. Since it is empty nothing was displayed on the screen [Doucmentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-content?view=powershell-7.5)

`Command 11: cp`
```sh
$ cp .\file.txt file2.txt
$ ls
    Directory: C:\Documents\Stevens2025S\EE322\labs\iot\demo


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          2/9/2025   2:27 PM              0 file.txt
-a----          2/9/2025   2:27 PM              0 file2.txt


```
The command will copy the contents of one file to another file. Because there was no "file2.txt" it created the file and copied all the content from "file.txt" to it. [Documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.5)

`Command 11: cp`
```sh
$ mv file.txt file1.txt
$ ls

    Directory: C:\Documents\Stevens2025S\EE322\labs\iot\demo


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          2/9/2025   2:27 PM              0 file1.txt
-a----          2/9/2025   2:27 PM              0 file2.txt

```
This command will move a file to another path as specified in the parameters. Since we specified a file that did not exist the command renamed the "file.txt" to "file1.txt". You can also use the "ren" command in the Powershell to achieve the same thing. [Documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/rename-item?view=powershell-7.5)

`Command 12: rm`
```sh
$ rm .\file2.txt
$ ls


    Directory: C:\Documents\Stevens2025S\EE322\labs\iot\demo


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          2/9/2025   2:27 PM              0 file1.txt
```
Removes the file in the parameter. [Documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item?view=powershell-7.5)

`Command 13: clear`
```sh
$ clear
```
Clears all previous inputs in the terminal. [Documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/clear-host?view=powershell-7.5)

`Command 14: man uname`
```sh
$ man Get-CimInstance

NAME
    Get-CimInstance

SYNTAX
    Get-CimInstance [-ClassName] <string> [-ComputerName <string[]>] [-KeyOnly] [-Namespace <string>]
    [-OperationTimeoutSec <uint32>] [-QueryDialect <string>] [-Shallow] [-Filter <string>] [-Property <string[]>]
    [<CommonParameters>]

    Get-CimInstance -CimSession <CimSession[]> -ResourceUri <uri> [-KeyOnly] [-Namespace <string>]
    [-OperationTimeoutSec <uint32>] [-Shallow] [-Filter <string>] [-Property <string[]>]  [<CommonParameters>]

    Get-CimInstance -CimSession <CimSession[]> -Query <string> [-ResourceUri <uri>] [-Namespace <string>]
    [-OperationTimeoutSec <uint32>] [-QueryDialect <string>] [-Shallow]  [<CommonParameters>]

    Get-CimInstance [-ClassName] <string> -CimSession <CimSession[]> [-KeyOnly] [-Namespace <string>]
    [-OperationTimeoutSec <uint32>] [-QueryDialect <string>] [-Shallow] [-Filter <string>] [-Property <string[]>]
    [<CommonParameters>]

    Get-CimInstance [-InputObject] <ciminstance> -CimSession <CimSession[]> [-ResourceUri <uri>] [-OperationTimeoutSec
    <uint32>]  [<CommonParameters>]

    Get-CimInstance [-InputObject] <ciminstance> [-ResourceUri <uri>] [-ComputerName <string[]>] [-OperationTimeoutSec
    <uint32>]  [<CommonParameters>]

    Get-CimInstance -ResourceUri <uri> [-ComputerName <string[]>] [-KeyOnly] [-Namespace <string>]
    [-OperationTimeoutSec <uint32>] [-Shallow] [-Filter <string>] [-Property <string[]>]  [<CommonParameters>]

    Get-CimInstance -Query <string> [-ResourceUri <uri>] [-ComputerName <string[]>] [-Namespace <string>]
    [-OperationTimeoutSec <uint32>] [-QueryDialect <string>] [-Shallow]  [<CommonParameters>]


ALIASES
    None


REMARKS
    Get-Help cannot find the Help files for this cmdlet on this computer. It is displaying only partial help.
        -- To download and install Help files for the module that includes this cmdlet, use Update-Help.
        -- To view the Help topic for this cmdlet online, type: "Get-Help Get-CimInstance -Online" or
           go to https://go.microsoft.com/fwlink/?LinkId=227961.

```
There are two commands here "man" which displays the manual/help of the next argument and "name" which we will talk about in the next command. [Documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-help?view=powershell-7.5)

`Command 15: uname -a`
```sh
$ Get-CimInstance

cmdlet Get-CimInstance at command pipeline position 1
Supply values for the following parameters:
ClassName: Win32_OperatingSystem

SystemDirectory     Organization BuildNumber RegisteredUser             SerialNumber            Version
---------------     ------------ ----------- --------------             ------------            -------
C:\WINDOWS\system32              XXXXX       xxxxxxxxxxxxx@outlook.com 00XXX-XXXXX-XXXXX-XXXXX 10.0.26100

```
The Get-CimInstance cmdlet gets the CIM instances of a class from a CIM server. You can specify either the class name or a query for this cmdlet. This cmdlet returns one or more CIM instance objects representing a snapshot of the CIM instances present on the CIM server. [Documentation](https://learn.microsoft.com/en-us/powershell/module/cimcmdlets/get-ciminstance?view=powershell-7.5)

`Command 16: ifconfig`
```sh
$ Get-NetIPAddress

IPAddress         : 
InterfaceIndex    : 5
InterfaceAlias    : Local Area Connection* 4
AddressFamily     : IPv6
Type              : Unicast
PrefixLength      : 64
PrefixOrigin      : WellKnown
SuffixOrigin      : Link
AddressState      : Deprecated
ValidLifetime     :
PreferredLifetime :
SkipAsSource      : False
PolicyStore       : ActiveStore

...

IPAddress         : 
InterfaceIndex    : 1
InterfaceAlias    : Loopback Pseudo-Interface 1
AddressFamily     : IPv4
Type              : Unicast
PrefixLength      : 8
PrefixOrigin      : WellKnown
SuffixOrigin      : WellKnown
AddressState      : Preferred
ValidLifetime     :
PreferredLifetime :
SkipAsSource      : False
PolicyStore       : ActiveStore

```
Gets the IP address configuration for all connected devices. I will not be displaying the full IP addresses but if run in a terminal they would be displayed. I cut the list for readability. [Documentation](https://learn.microsoft.com/en-us/powershell/module/nettcpip/get-netipaddress?view=windowsserver2025-ps)

`Command 17: ping localhost`
```sh
$ ping localhost

Pinging Bullpen [::1] with 32 bytes of data:
Reply from ::1: time<1ms
Reply from ::1: time<1ms
Reply from ::1: time<1ms
Reply from ::1: time<1ms

Ping statistics for ::1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```
Verifies IP-level connectivity to another TCP/IP computer by sending Internet Control Message Protocol (ICMP) echo Request messages. The receipt of the corresponding echo Reply messages is displayed, along with round-trip times. ping is the primary TCP/IP command used to troubleshoot connectivity, reachability, and name resolution. The localhost in this case is our computer and there the connection is good. [Documentation](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ping)

`Command 18: netstat`
```sh
$ netstat

Active Connections

  Proto  Local Address          Foreign Address        State
  TCP    10.155.34.91:XXXXX     XX:https               CLOSE_WAIT
  TCP    10.155.34.91:XXXXX     XXX:https              ESTABLISHED
  TCP    10.155.34.91:XXXXX     XX.XXX.XXX.XX:https    ESTABLISHED
  TCP    10.155.34.91:XXXXX     XX:https               ESTABLISHED
  TCP    10.155.34.91:XXXXX     XX:XXXX                ESTABLISHED
  TCP    10.155.34.91:XXXXX     XX.XX.XXX.XX:https     ESTABLISHED
  ...
  TCP    XXX.0.0.1:XXXXX        Bullpen:14622          ESTABLISHED
```
Displays active TCP connections, ports on which the computer is listening, Ethernet statistics, the IP routing table, IPv4 statistics (for the IP, ICMP, TCP, and UDP protocols), and IPv6 statistics (for the IPv6, ICMPv6, TCP over IPv6, and UDP over IPv6 protocols). Used without parameters, this command displays active TCP connections. I cut the list down and removed the exact IPs.
![Table of Parameters](https://github.com/user-attachments/assets/af083e4d-fc5a-4ed5-b953-30d01ffb20ba)  

[Documentation](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netstat)


