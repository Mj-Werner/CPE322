# Lab 1 - GHDL and GTKWave Download and Implementation
The goal of this lab was to download, install, and run example files for [GHDL](https://github.com/ghdl/ghdl) and [GTKWave](https://sourceforge.net/projects/gtkwave/).

## 1) Downloading and Installing Software
I followed the video tutorial found [here](https://www.youtube.com/watch?v=H2GyAIYwZbw).
I was able to download and install each of the programs to my system using the same versions as stated in the EE-322 [tutorial](https://github.com/kevinwlu/dsd/tree/master/ghdl).

#### Files Downloaded
"ghdl-0.37-mingw32-mcode.zip"  
"gtkwave-3.3.100-bin-win32"

## 2) Building and Running Each of the Templates.

### [Half adder (ha)](lab1/ha)
For this file, I followed the video referenced above to create my file and run the demonstration on my computer without using the files that are present in the EE-322 GHDL folder. The main difference in my implementation
is the use of "o" as completed in the video tutorial, instead of "s" mentioned in the EE-322 example file. The following is a picture of the results after running the following commands and viewing the results in GTKWave:  

```sh
$ ghdl -a ha.vhdl
$ ghdl -a ha_tb.vhdl
$ ghdl -e ha_tb
$ ghdl -r ha_tb --vcd=ha.vcd
ha_tb.vhdl:48:16:@5ns:(assertion error): Reached end of test
$gtkwave ha.vcd
```

![ha_pic](/lab1/ha/half_adderWaveform.png)

### [4-to-1 Multiplexer (mux)](lab1/mux)
For these files, I downloaded the example files that were in the provided [repo](https://github.com/kevinwlu/dsd/tree/master/ghdl). I edited the corresponding [mux_tb](lab1/mux/mux_tb.vhdl) file to assert the same error 
as the previous file to know when the tests have been completed. You will see the same assert error within the command line arguments below. The picture is the result of running the command line arguments on the 
files and viewing the results within GTKWave:

```sh
$ ghdl -a .\mux.vhdl
$ ghdl -a .\mux_tb.vhdl
$ ghdl -e mux_tb
$ ghdl -r mux_tb --vcd=mux.vcd
.\mux_tb.vhdl:71:10:@500ns:(assertion error): Reached end of test
$gtkwave mux.vcd
```
![mux_pic](/lab1/mux/4_to_1_mux.png)

