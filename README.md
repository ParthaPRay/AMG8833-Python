# AMG8833-Python-Arduino
This repo contains the Arduino Mega 2560 and Python code to run AMG8833 Grid Eye (Sparkfun) module and was tested on Raspberry Pi (Linux 11 BullsEye).

I used Arduino Mega 2560 and AMG8833 (INT and AOO pins unconnected).

# Connections:

| Arduino UNO  | AMG8833 |
| ------------- | ------------- |
| SCL  | SCL  |
| SDA  | SDA  |
| 3.3V  | VIN  |
| GND  | GND  |
|  INT |  Not Connected to Arduino  |
| ------------- | ------------- |

# Circuit

![9e1e2a22-1b49-4a3a-9ea4-0908614eb00c](https://github.com/ParthaPRay/AMG8833-Python/assets/1689639/29ae6597-67db-4f4b-be23-13561de6c466)



# Steps to Run:
1. Load the Arduino Uno R3 with the **AMG8833-Uno.ino** using Arduino IDE 1.8.19 (Tested)
   1. Keep the baud rate default 115200
 
2. To Run the the AMG8833*.py code
   1. Firstly, Install serial, numpy, scipy, matplotlib using pip (e.g. **pip install pyserial, numpy, matplotlib, scipy**)''
   2. Also install **pip install -U scikit-learn** for K-Means clustering, Otherwise not needed
   3. Also intsall **sudo apt-get install libopenblas-base**
   4. Then Run the python code

      
      2.1.1. For **AMG8833-Uno.py** A real-time plot appears that shows the average temperature in Celcius as shown below

![2023-10-08-135840_1280x1024_scrot](https://github.com/ParthaPRay/AMG8833-Python/assets/1689639/b8c2d3e3-0b3c-49d0-a60f-e754b5a21ead)


      2.1.2. For **AMG8833-Uno-Max-Min.py** A real-time plot appears that shows the average, maximum and minimum temperature in Celcius as shown below

![2023-10-08-141200_1280x1024_scrot](https://github.com/ParthaPRay/AMG8833-Python/assets/1689639/44d1ca93-bea6-45e6-8148-05989467cf01)



      2.1.3. For **AMG8833-Uno-KMeans.py** A real-time plot appears that shows the average, maximum and minimum temperature in Celcius and K-Means clusters as shown below

![2023-10-08-141124_1280x1024_scrot](https://github.com/ParthaPRay/AMG8833-Python/assets/1689639/7170def0-8474-4d7d-b186-a0b6051d8314)






