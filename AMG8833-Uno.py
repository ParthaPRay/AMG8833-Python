#pip isntall serial, numpy, matplotlib, scipy
# Change the upsclae factor for desired value  and sigma 


import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from datetime import datetime
from scipy.ndimage import zoom, gaussian_filter


# Prompt the user for port and baud rate
port = input("Enter the port (e.g., /dev/ttyACM0): ")
baud_rate = int(input("Enter the baud rate (e.g., 115200): "))

try:
    baud_rate = int(baud_rate)
    ser = serial.Serial(port, baud_rate)
except serial.SerialException:
    print(f"Error: Could not open port {port}. Please check the port name and try again.")
    exit(1)
except ValueError:
    print(f"Error: Invalid baud rate '{baud_rate}'. Please enter a valid number and try again.")
    exit(1)

# Define the custom colormap
colors = [(0, 1, 0), (1, 1, 0), (1, 0, 0)]  # Green to yellow to red
cmap_name = 'custom_div_cmap'
cm = LinearSegmentedColormap.from_list(cmap_name, colors, N=100)

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111)

# Initialize colorbar object, this will be updated in the loop
cbar = None

# Upscale factor for the grid Default 10
upscale_factor = 10

while True:
    try:
        # Read a line from the serial port and decode
        try:
            line = ser.readline().decode().strip()
        except UnicodeDecodeError:
            continue

        readings = [float(x) for x in line.split(',') if x]

        # Check if the readings list has the correct length
        if len(readings) != 64:
            continue

        # Convert the list to an 8x8 numpy array
        grid = np.array(readings).reshape((8, 8))

        # Upscale and smooth the grid
        grid_upscaled = zoom(grid, upscale_factor)
        grid_smooth = gaussian_filter(grid_upscaled, sigma=1)

        # Display the smoothed, upscaled grid using the custom colormap
        im = ax.imshow(grid_smooth, cmap=cm)

        # Set the title for the plot with current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ax.set_title(f"Temperature Measurement (DegC) - {current_time}")

        # If colorbar does not exist, create it. Otherwise, update it.
        if cbar is None:
            cbar = fig.colorbar(im, ax=ax, orientation='vertical', pad=0.1)
        else:
            cbar.update_normal(im)

        plt.pause(0.1)

        if not plt.get_fignums():
            break

        ax.clear()

    except KeyboardInterrupt:
        ser.close()
        break

