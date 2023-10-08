# AMG8833-Python-Arduino
This repo contains the Arduino Uno R3 and Python code to run AMG8833 Grid Eye (Sparkfun) module and was tested on Raspberry Pi (Linux 11 BullsEye).

I used Arduino Uno R3 and AMG8833 (INT and AOO pins unconnected).

# Connections:

| Arduino UNO  | AMG8833 |
| ------------- | ------------- |
| SCL  | SCL  |
| SDA  | SDA  |
| 3.3V  | VIN  |
| GND  | GND  |
|   | INT Not Connected to Arduino  |
|   | A00 Not Connected to Arduino  |   

# Circuit

![AMG8833-Uno](https://github.com/ParthaPRay/AMG8833-Python/assets/1689639/b6e6c6db-e98f-49a4-a00f-59c15ebb2626)


# Steps to Run:
1. Load the Arduino Uno R3 with the **AMG8833-Uno.ino** using Arduino IDE 1.8.19 (Tested)
   1. Keep the baud rate default 115200
 
2. To Run the **AMG8833-Uno.py**
   1. Firstly, Install serial, numpy, scipy, matplotlib using pip (e.g. **pip install pyserial, numpy, matplotlib, scipy**)''
   2. Also intsall **sudo apt-get install libopenblas-base**
   3. Then Run the python code
   4. A real-time plot appears that shows the average temperature in Celcius

![2023-10-08-135840_1280x1024_scrot](https://github.com/ParthaPRay/AMG8833-Python/assets/1689639/b8c2d3e3-0b3c-49d0-a60f-e754b5a21ead)


