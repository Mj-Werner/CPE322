# Lab 3 - Python
For this lab, we are learning the basics of different python codes and some extensions. The extensions being used are [Astral](https://astral.readthedocs.io/en/latest/), [GeoPy](https://geopy.readthedocs.io/en/stable/), [psutil](https://pypi.org/project/psutil/), and [jdcal](https://pypi.org/project/jdcal/). All the files used for this lab were found on the class repo [here](https://github.com/kevinwlu/iot/tree/master/lesson3). All scripts were run on a Unbuntu Linux environment with python3 installed.
---


`Script 1: julian.py`
```sh
$ python3 julian.py 
Calendar Date: 2025-02-18
Julian Date: 2460724.5
Modified Julian Date: 60724.0

```
[julain.py](julian.py)  
Displays the current Calander date the [Julian date](https://en.wikipedia.org/wiki/Julian_day) and the modified Julian date.


`Script 2: date_exampled.py`
```sh
$ python3 date_example.py 
Date: 2025-02-18
Date: 02-18-25
Day of Week: Tuesday
Month: February
Year: 2025
28 days after the first day of classes
78 days before the last day of classes
```
[date_example.py](date_example.py)  
Displays the current date in different formats, day of the week, month, year, and how many days after the first day of classes and how many days until the last day of classes for Stevens Institute of technology.

`Script 3: datetime_example.py`
```sh
$ python3 datetime_example.py 
2025-02-18 12:48:44.242273
2025-02-18 12:48:44.242322
2025-02-18 17:48:44.242328
1739900924.2423298
Tue Feb 18 12:48:44 2025
2025-02-18 12:48:44.242356
2025-02-18 17:48:44.242358
```
[datetime_example.py](datetime_example.py)  
Displays the current date and time in different formats.


`Script 4: time_example.py`
```sh
$ python3 time_example.py 
Tue Feb 18 12:52:53 2025
Tue Feb 18 12:53:03 2025
Tue Feb 18 12:53:13 2025
Tue Feb 18 12:53:23 2025
Tue Feb 18 12:53:33 2025
Tue Feb 18 12:53:43 2025
^C
```
[time_example.py](time_example.py)  
Displays the time in ten-second intervals until Ctrl-c is pressed on the keyboard.

`Script 5a: sun.py`
```sh
$ python3 sun.py "New York"
Information for New York/USA

Timezone: US/Eastern
Latitude: 40.72; Longitude: -74.00

Dawn:    2025-02-18 06:17:18.521002-05:00
Sunrise: 2025-02-18 06:45:43.214385-05:00
Noon:    2025-02-18 12:09:55-05:00
Sunset:  2025-02-18 17:34:35.676983-05:00
Dusk:    2025-02-18 18:03:01.938864-05:00
```
`Script 5b: sun.py`
```sh
$ python3 sun.py "Los Angeles"
Information for Los Angeles/USA

Timezone: US/Pacific
Latitude: 34.05; Longitude: -118.25

Dawn:    2025-02-18 06:08:22.357303-08:00
Sunrise: 2025-02-18 06:34:17.841413-08:00
Noon:    2025-02-18 12:06:55-08:00
Sunset:  2025-02-18 17:39:52.810119-08:00
Dusk:    2025-02-18 18:05:49.288804-08:00
```
[sun.py](sun.py)  
Displays multiple information  about the sun depending on what you put as the first argument on the command line. Shown with "New York" and "Los Angeles".

`Script 6: moon.py`
```sh
$ python3 moon.py 
2025-02-18 Moon Phase: 19
2025-02-19 Moon Phase: 19
2025-02-20 Moon Phase: 20
2025-02-21 Moon Phase: 21
2025-02-22 Moon Phase: 22
2025-02-23 Moon Phase: 23
2025-02-24 Moon Phase: 24
2025-02-25 Moon Phase: 25
2025-02-26 Moon Phase: 26
2025-02-27 Moon Phase: 27
2025-02-28 Moon Phase: 0
2025-03-01 Moon Phase: 1
2025-03-02 Moon Phase: 2
2025-03-03 Moon Phase: 3
2025-03-04 Moon Phase: 4
2025-03-05 Moon Phase: 5
2025-03-06 Moon Phase: 6
2025-03-07 Moon Phase: 7
2025-03-08 Moon Phase: 8
2025-03-09 Moon Phase: 9
2025-03-10 Moon Phase: 10
2025-03-11 Moon Phase: 11
2025-03-12 Moon Phase: 12
2025-03-13 Moon Phase: 13
2025-03-14 Moon Phase: 14
2025-03-15 Moon Phase: 15
2025-03-16 Moon Phase: 15
2025-03-17 Moon Phase: 16
2025-03-18 Moon Phase: 17
2025-03-19 Moon Phase: 18
```
[moon.py](moon.py)  
Displays the next 30 days of the Moon's phases based on the following chart:  ![MOON Phases](https://github.com/user-attachments/assets/9824d7be-450e-4e28-85eb-dfbefe04b279)


`Script 7: coordinates.py`
```sh
$ python3 coordinates.py "Samuel C. Williams Library"
Samuel C. Williams Library, Field House Road, Uptown, Hoboken, Hudson County, New Jersey, 07030, United States
(40.74480675, -74.02532861159351)
```
[coordinates.py](coordinates.py)  
Geolocates the address or object given and then displays the address and the latitude and longitude.

`Script 8: address.py`
```sh
$ python3 address.py "40.74480675, -74.0253286115931"
Stevens Institute of Technology, 1, Wittpenn Walk, Uptown, Hoboken, Hudson County, New Jersey, 07030, United States
(40.744809599999996, -74.0252392276461)
```
[address.py](address.py)  
Given a latitude and a longitude, this will print the address of those coordinates on the Earth.

`Script 9: cpu.py`
```sh
$ python3 cpu.py 
The number of physical cores =  11
The number of logical CPUs =  11
The utilization per second as a percentage for each CPU
[0.0, 0.0, 1.0, 0.0, 2.0, 1.0, 0.0, 1.0, 2.0, 2.0, 2.1]
[1.0, 1.0, 1.0, 2.0, 0.0, 2.0, 2.0, 1.0, 1.0, 1.0, 4.2]
[2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 2.0, 2.1]
[1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 2.0, 1.0, 0.0, 0.0, 1.1]
[2.0, 1.0, 3.0, 1.0, 3.0, 2.0, 1.0, 3.0, 3.0, 1.0, 2.2]
[1.0, 2.0, 1.0, 1.0, 0.0, 1.0, 2.0, 0.0, 1.0, 2.0, 1.1]
[1.0, 1.0, 0.0, 2.0, 2.0, 1.0, 2.0, 0.0, 0.0, 0.0, 3.2]
[2.0, 2.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 2.0, 1.0, 1.1]
[1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 2.2]
[1.0, 0.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 3.2]
```
[cpu.py](cpu.py)  
Displays the physical cores and the logical cores of the current CPU and displays their usage at the current moment.

`Script 10: battery.py`
```sh
$ python3 battery.py 
None
```
[battery.py](battery.py)  
Displays the current battery percentage of the Computer. Since I am running these commands on a desktop, there are no batteries attached.

`Script 11: documentstats.py`
```sh
$ python3 documentstats.py document.txt
Word Count: 1343
Top Ten Words: [('our', 26), ('their', 20), ('has', 20), ('he', 19), ('them', 15), ('these', 13), ('have', 11), ('we', 11), ('us', 11), ('people', 10)]
```
[documentstats.py](documentstats.py)  [document.txt](document.txt)
Reads in from a text file and displays the most popular words in the document that are not part of a certain subsection of words "stopwords" in the code.

