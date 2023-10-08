# AMG8833-Python-Arduino
This repo contains the Arduino Mega 2560 and Python code to run AMG8833 Grid Eye (Sparkfun) module and was tested on Raspberry Pi (Linux 11 BullsEye).

I used Arduino Mega 2560 and AMG8833 (INT and AOO pins unconnected).

# Connections:

| Arduino UNO  | AMG8833 GridEye |
| ------------- | ------------- |
| GND  | GND  |
| 3.3V  | 3.3V  |
| SDA  | SDA  |
| SCL  | SCL  |
|  Not Connected | INT |


# Circuit

![9e1e2a22-1b49-4a3a-9ea4-0908614eb00c](https://github.com/ParthaPRay/AMG8833-Python/assets/1689639/29ae6597-67db-4f4b-be23-13561de6c466)



# Steps to Run:
1. Load the Arduino Uno R3 with the **AMG8833-Arduino.ino** using Arduino IDE 1.8.19 (Tested)
   1. Keep the baud rate default 115200
 
2. To Run the the AMG8833*.py code
   1. Firstly, Install serial, numpy, scipy, matplotlib using pip (e.g. **pip install pyserial, numpy, matplotlib, scipy**)''
   2. Also install **pip install -U scikit-learn** for K-Means clustering, Otherwise not needed
   3. Also intsall **sudo apt-get install libopenblas-base**
   4. Then Run the python code

   2.1.1. For **AMG8833-Arduino.py** A real-time plot appears that shows the average temperature in Celcius as shown below

![1](https://github.com/ParthaPRay/AMG8833-Python/assets/1689639/c90b3556-2271-47fa-8973-ef8e1ae5537a)

   2.1.2. For **AMG8833-Arduino-Max-Min.py** A real-time plot appears that shows the average, maximum and minimum temperature in Celcius as shown below

![2](https://github.com/ParthaPRay/AMG8833-Python/assets/1689639/76e7544f-e9ea-4ca0-8619-7c0037ab6eb2)

   2.1.3. For **AMG8833-Arduino-KMeans.py** A real-time plot appears that shows the average, maximum and minimum temperature in Celcius and K-Means clusters as shown below

![3](https://github.com/ParthaPRay/AMG8833-Python/assets/1689639/bb668709-3a90-46c8-9de4-21fd6bd0dd27)






