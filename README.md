# AMG8833-Python-Arduino
This repo contains the Arduino Uno R3 and Python code to run AMG8833 module and was tested on Ubuntu 22.04 LTS.

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
 
2. To Run the **AMG8833-Uno.py** from Ubuntu 22.04 LTS
   1. Firstly, Install serial, numpy, scipy, matplotlib using pip (e.g. **pip install pyserial, numpy, matplotlib, scipy**) from Ubuntu terminal (e.g. **python AMG8833-Uno.py**)
   2.  _"Enter the port (e.g., /dev/ttyACM0): "_
   3.  _"Enter the baud rate (e.g., 115200): "_
   4.  A real-time plot appears that shows the temperature in Celcius


![Screenshot from 2023-08-18 15-26-46](https://github.com/ParthaPRay/AMG8833-Python/assets/1689639/461c61cd-5a2f-4579-849b-0a0f76f0c4c1)

![Screenshot from 2023-08-18 15-28-59](https://github.com/ParthaPRay/AMG8833-Python/assets/1689639/8fc41f4f-33c0-48f6-a38a-c65a8b1205b1)



