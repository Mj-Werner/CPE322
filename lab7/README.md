# Lab 7 - ThingSpeak and Google Sheets
The goal of today's lab was to use [ThingSpeak](https://thingspeak.mathworks.com/) and a [Google Sheets API](https://console.cloud.google.com/welcome/) to publish data to both of the websites. Once again, all labs are run on my Ubuntu virtual machine.
All information about the steps to complete the lab can be found [here](https://github.com/kevinwlu/iot/tree/master/lesson5):


## Part 1 -ThingSpeak
The beginning of the lab involved setting up a [ThingSpeak](https://thingspeak.mathworks.com/) account and creating a new project. Then, after generating the API key, it was added to the [thingspeak_cpu_loop.py](thingspeak_cpu_loop.py)
to attach the two ends.

`Terminal Output for thingspeak_cpu_loop.py`
```sh
$ python3 thingspeak_cpu_loop.py 
0.0
13005.9453125
Mon, 24 Mar 2025 12:36:58
200 OK
0.7
13014.953125
Mon, 24 Mar 2025 12:37:58
200 OK
...
3.7
12869.83984375
Mon, 24 Mar 2025 15:08:57
200 OK
```
![Part 1 Thing Speak](https://github.com/user-attachments/assets/307e2c8b-671b-4d68-a4aa-59f097b02714)



## Part 2 - Google Sheets
For this lab section, we are publishing data directly into a Google Sheet using a [JSON](https://fileinfo.com/extension/json) [API](https://aws.amazon.com/what-is/api-key/) Key. For this section the "temperature" column never updated even after downloading
and completing the lab steps again. The following are the Terminal output and the Google Sheets screenshot. The output for the [rpi_spreadsheet.py](rpi_spreadsheet.py) is shown below.

`Terminal Output for Part 2`
```sh
$ python3 rpi_spreadsheet.py 
Free RAM: 2047 (14627)
Number of processes: 317
Up time:  1:33
Number of connections: 0
Temperature in C: 0
IP-address: 10.0.2.15
/bin/sh: 1: /usr/bin/vcgencmd: not found
CPU speed in MHz: 
Logging sensor measurements to rpidata every 10 seconds.
Press Ctrl-C to quit.
2025-03-24 15:29:39.817331
CPU Usage:   2.7 %
Temperature: 0.0 C
Wrote a row to rpidata
```

![Before Spreadsheet](https://github.com/user-attachments/assets/b1b7490b-fd43-4149-ab3e-a7b4734205f8)  
![After Spreadsheet](https://github.com/user-attachments/assets/ce2f8b9a-2fe4-466b-a23e-6bd8190b0f78)

