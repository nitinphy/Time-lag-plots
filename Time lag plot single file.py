# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 22:15:31 2024

@author: sndkp
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 18:36:07 2024

@author: sndkp
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import matplotlib.ticker as ticker
from scipy.interpolate import griddata
import pandas as pd
import math
plt.rcParams["font.family"] = "serif"
plt.rcParams["mathtext.fontset"] = "dejavuserif"
plt.rcParams.update({'font.size': 10, 'font.family': 'Times New Roman'})

# Step 1: Define the folder and file name

# Define the folder and file name
folder_path = r'F:\NbO2 manuscript\Data\Voltage driven time lag plots\Only 58'
file_name = 'it_001.txt'  # Specify the file you want to process
file_path = os.path.join(folder_path, file_name)

# Step 2: Import the data from the text file, skipping the first column and header
data = np.genfromtxt(file_path, dtype=float, delimiter=None, comments='#', usecols=0, skip_header=1)
time = np.genfromtxt(file_path, dtype=float, delimiter=None, comments='#', usecols=1, skip_header=1)
plt.plot(time, data)

# Step 3: Choose lag order (number of time steps to lag by)
lag_order = 50

# Step 4: Create lagged data
lagged_data = np.roll(data, lag_order)

# Step 5: Compute density values manually
hb, xedges, yedges = np.histogram2d(data, lagged_data, bins=100, density=True)

# Reshape hb to match the size of the input data arrays
x, y = np.meshgrid(xedges[:-1], yedges[:-1])

# Interpolate the density values to fill in any missing values
x_flat = x.flatten()
y_flat = y.flatten()
hb_flat = hb.flatten()
x_interp, y_interp = np.meshgrid(np.linspace(x.min(), x.max(), len(xedges)-1),
                                  np.linspace(y.min(), y.max(), len(yedges)-1))
z_interp = griddata((x_flat, y_flat), hb_flat, (x_interp, y_interp), method='cubic')

# Resize the interpolated density array to match the size of the input data arrays
z_interp_resized = np.resize(z_interp, data.shape)

# Convert current to microamperes
data_microamp = data * 1e3
lagged_data_microamp = lagged_data * 1e3

# Plot time lag plot with hexbin and color bar

plt.figure(figsize=(4, 3.15))
plt.hexbin(data_microamp, lagged_data_microamp, gridsize=200, cmap='viridis', norm=LogNorm())

# Remove grid
plt.grid(False)

# Show minor ticks
plt.minorticks_on()

# Show both minor and major ticks inside
plt.tick_params(which='both', direction='in', width=2)

# Set custom tick locations and labels for x-axis
x_center = (data_microamp.min() + data_microamp.max()) / 2
y_center = (lagged_data_microamp.min() + lagged_data_microamp.max()) / 2
x_range = 0.3 * (data_microamp.max() - data_microamp.min())
y_range = 0.3 * (lagged_data_microamp.max() - lagged_data_microamp.min())
x_ticks = [x_center - x_range, x_center + x_range]
plt.xticks(x_ticks, ['{:.4f}'.format(x) for x in x_ticks])
y_ticks = [y_center - y_range, y_center + y_range]
plt.yticks(y_ticks, ['{:.4f}'.format(y) for y in y_ticks])

ax = plt.gca()
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)

# Set xlabel and ylabel with microampere unit
plt.xlabel(r"$\mathrm{I_{t}}$ (mA)")
plt.ylabel(r"$\mathrm{I_{t-1}}$ (mA)")

# Tight fit the image
plt.tight_layout()

# Save the plot with the last three digits of the file name
plot_file_name = f'time_lag_plot_original_clr_{file_name[-7:-4]}.png'
plt.savefig(os.path.join(folder_path, plot_file_name), dpi=100)

plt.show()
plt.close()
