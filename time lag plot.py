# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 18:36:07 2024

@author: sndkp
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm  # Import LogNorm for log scale
import matplotlib.ticker as ticker
from scipy.interpolate import griddata
import pandas as pd
import math
plt.rcParams["font.family"] = "serif"
plt.rcParams["mathtext.fontset"] = "dejavuserif"
plt.rcParams.update({'font.size': 18, 'font.family': 'Times New Roman'})

# Step 1: Define the folder and file name

# Define the folder and file name
folder_path = r'F:\NbO2 manuscript\Data\Voltage driven time lag plots\raw time series'
file_prefix = 'it_'
file_extension = '.txt'

# Iterate through all files from it_001.txt to it_058.txt
for i in range(1, 133):
    # Generate file name
    file_number = f'{i:03d}'
    file_name = f'{file_prefix}{file_number}{file_extension}'
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
    
    # Save the density data along with time t and t-1 into a CSV file
    #header = f"Data(t),Data(t-{lag_order}),Density_{file_name[-3:]}"
    #df = pd.DataFrame({'Data(t)': data, 'Data(t-1)': lagged_data, f'Density_{file_name[-3:]}': z_interp_resized.ravel()})
    #df.to_csv(os.path.join(folder_path, f'density_data_{file_name[-3:]}.csv'), index=False, header=header)
    
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
    # Calculate the center of your data range
    x_center = (data_microamp.min() + data_microamp.max()) / 2
    y_center = (lagged_data_microamp.min() + lagged_data_microamp.max()) / 2
    
    # Define the range for your ticks around the center
    x_range = 0.3 * (data_microamp.max() - data_microamp.min())  # Adjust the factor as needed
    y_range = 0.3 * (lagged_data_microamp.max() - lagged_data_microamp.min())  # Adjust the factor as needed
    
    # Set custom tick locations and labels for x-axis
    x_ticks = [x_center - x_range, x_center + x_range]
    plt.xticks(x_ticks, ['{:.4f}'.format(x) for x in x_ticks])
    
    # Set custom tick locations and labels for y-axis
    y_ticks = [y_center - y_range, y_center + y_range]
    plt.yticks(y_ticks, ['{:.4f}'.format(y) for y in y_ticks])
    
    
    ax = plt.gca()
    ax.spines['top'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    # Add color bar
    #plt.colorbar()
    # Add title
    #plt.title(f'Time Lag Plot with Color Bar (Lag Order: {lag_order})')
    
    # Set xlabel and ylabel with microampere unit
    plt.xlabel(r"$\mathrm{I_{t}}$ (mA)")
    plt.ylabel(r"$\mathrm{I_{t-1}}$ (mA)")
    #plt.ylabel(r"$\mathrm{I_{t-1}}$ (μA)")
    # Tight fit the image
    plt.tight_layout()
    
    # Save the plot with the last three digits of the file name
    plot_file_name = f'time_lag_plot_original_clr_{file_name[-7:-4]}.png'
    plt.savefig(os.path.join(folder_path, plot_file_name), dpi=100)
    
    plt.show()
    plt.close()
