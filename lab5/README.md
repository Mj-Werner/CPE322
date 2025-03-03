# Lab 5 - Paho and MQTT
The goal of today's lab was to use [Paho](https://wiki.eclipse.org/Paho/) and [MQTT](https://www.youtube.com/watch?v=t5b7gGYAezQ) to show the process of using these programs to send data/information from one terminal to
the next.  
Before we get into the lab, I downloaded the latest version of Paho-MQTT. The info for install and more information about the topics can be found [here](https://github.com/kevinwlu/iot/tree/master/lesson5):

`Downloading Paho-MQTT`
```sh
$ sudo pip3 install paho-mqtt
[sudo] password for ubuntu: 
Collecting paho-mqtt
  Downloading paho_mqtt-2.1.0-py3-none-any.whl (67 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 67.2/67.2 KB 3.3 MB/s eta 0:00:00
Installing collected packages: paho-mqtt
Successfully installed paho-mqtt-2.1.0
```

## Running subcpu.py and pubcpu.py
In this section, I will show running both the [subcpu.py](subcpu.py) and the [pubcpu.py](pubcpu.py) Python files and the information that they send to each other. The following is the terminal's output.

`subcpu.py terminal`
```sh
$ python3 subcpu.py 
/mnt/shared/iot/lesson5/subcpu.py:8: DeprecationWarning: Callback API version 1 is deprecated, update to latest version
  client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
Connected with result code 0
MyCPU 2025-03-03 15:11:01
MyCPU CPU Usage:   7.6 %
MyCPU 2025-03-03 15:11:11
MyCPU CPU Usage:   0.3 %
MyCPU 2025-03-03 15:11:21
MyCPU CPU Usage:   0.4 %
MyCPU 2025-03-03 15:11:32
MyCPU CPU Usage:   0.3 %
MyCPU 2025-03-03 15:11:42
MyCPU CPU Usage:   0.3 %
MyCPU 2025-03-03 15:11:52
MyCPU CPU Usage:   0.2 %
MyCPU 2025-03-03 15:12:02
MyCPU CPU Usage:   0.1 %
MyCPU 2025-03-03 15:12:12
MyCPU CPU Usage:   0.2 %
MyCPU 2025-03-03 15:12:22
MyCPU CPU Usage:   0.2 %
MyCPU 2025-03-03 15:12:32
MyCPU CPU Usage:   0.2 %
MyCPU 2025-03-03 15:12:42
MyCPU CPU Usage:   0.2 %
MyCPU 2025-03-03 15:12:52
MyCPU CPU Usage:   0.2 %
MyCPU 2025-03-03 15:13:02
MyCPU CPU Usage:   0.2 %
MyCPU 2025-03-03 15:13:12
MyCPU CPU Usage:   0.2 %
MyCPU 2025-03-03 15:13:22
MyCPU CPU Usage:   0.3 %
^CTraceback (most recent call last):
  File "/mnt/shared/iot/lesson5/subcpu.py", line 14, in <module>
    client.loop_forever()
  File "/usr/local/lib/python3.10/dist-packages/paho/mqtt/client.py", line 2297, in loop_forever
    rc = self._loop(timeout)
  File "/usr/local/lib/python3.10/dist-packages/paho/mqtt/client.py", line 1663, in _loop
    socklist = select.select(rlist, wlist, [], timeout)
KeyboardInterrupt
```

`pubcpu.py terminal`
```sh
$ python3 pubcpu.py 
/mnt/shared/iot/lesson5/pubcpu.py:6: DeprecationWarning: Callback API version 1 is deprecated, update to latest version
  mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
2025-03-03 15:11:01
CPU Usage:   7.6 %
2025-03-03 15:11:11
CPU Usage:   0.3 %
2025-03-03 15:11:21
CPU Usage:   0.4 %
2025-03-03 15:11:32
CPU Usage:   0.3 %
2025-03-03 15:11:42
CPU Usage:   0.3 %
2025-03-03 15:11:52
CPU Usage:   0.2 %
2025-03-03 15:12:02
CPU Usage:   0.1 %
2025-03-03 15:12:12
CPU Usage:   0.2 %
2025-03-03 15:12:22
CPU Usage:   0.2 %
2025-03-03 15:12:32
CPU Usage:   0.2 %
2025-03-03 15:12:42
CPU Usage:   0.2 %
2025-03-03 15:12:52
CPU Usage:   0.2 %
2025-03-03 15:13:02
CPU Usage:   0.2 %
2025-03-03 15:13:12
CPU Usage:   0.2 %
2025-03-03 15:13:22
CPU Usage:   0.3 %
```
As seen, the information on both terminal windows is the same. Using the publish and subscribe file, the user can transfer the data between them.  
![Both Terminals](https://github.com/user-attachments/assets/56b66e16-b87e-41a4-990e-65cea9c873a4)



