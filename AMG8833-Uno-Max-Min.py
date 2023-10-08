# Partha Pratim Ray
#This code displays the average, minimum, and maximum temperature in real-time.

# 8 October, 2023

import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
import matplotlib.colors as mcolors

# Set up the serial line
ser = serial.Serial('/dev/ttyACM0', 115200)  # Change 'COM3' to your port name
ser.flushInput()

# Creating a colormap that goes from green to red
colors = [(0, "green"), (0.5, "yellow"), (1, "red")]
n_bins = 100
cmap_name = 'custom1'
cm = mcolors.LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

def animate(i, im, ax):
    try:
        ser_bytes = ser.readline()
        decoded_bytes = ser_bytes.decode("utf-8")
        data = decoded_bytes.split(',')
        float_data = [float(d) for d in data]
        np_data = np.array(float_data).reshape((8, 8))
        im.set_array(np_data)
        
        # Calculating the average, maximum, and minimum temperatures
        avg_temp = np.mean(np_data)
        max_temp = np.max(np_data)
        min_temp = np.min(np_data)
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ax.set_title(f"Temperature Measurement (DegC) - {current_time}\n" +
                     f"Average Temperature: {avg_temp:.2f} °C | " +
                     f"Maximum Temperature: {max_temp:.2f} °C | " +
                     f"Minimum Temperature: {min_temp:.2f} °C")

    except ValueError as e:
        print(f"Not enough data: {e}")

fig, ax = plt.subplots()
im = ax.imshow(np.zeros((8, 8)), cmap=cm, interpolation='bilinear', vmin=20, vmax=30)
cb = plt.colorbar(im, ax=ax)
ani = animation.FuncAnimation(fig, animate, fargs=(im, ax), interval=100)

plt.show()
