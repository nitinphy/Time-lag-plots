# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:15:52 2024

@author: sndkp
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm  # Import LogNorm for log scale

# Set up plot parameters
plt.rcParams["font.family"] = "serif"
plt.rcParams["mathtext.fontset"] = "dejavuserif"
plt.rcParams.update({'font.size': 11, 'font.family': 'Times New Roman'})

# Define the folder and file name
folder_path = r'F:\NbO2 manuscript\Data\Voltage driven time lag plots\Only 58'
file_name = 'it_001.txt'
file_path = os.path.join(folder_path, file_name)

# Import the data from the text file, skipping the first column and header
data = np.genfromtxt(file_path, dtype=float, delimiter=None, comments='#', usecols=0, skip_header=1)
time = np.genfromtxt(file_path, dtype=float, delimiter=None, comments='#', usecols=1, skip_header=1)

# Convert current to microamperes
data_microamp = data * 1e1

# Loop through lag orders from 1 to 100
for lag_order in range(1, 1001):
    
    # Create lagged data
    lagged_data = np.roll(data, lag_order)
    lagged_data_microamp = lagged_data * 1e0
    
    # Plot both line plot and hexbin plot vertically
    fig, axes = plt.subplots(2, 1, figsize=(2.6 , 2.8), gridspec_kw={'height_ratios': [1, 4]})
    
    # Plot line plot
    axes[0].plot(time, data_microamp)
    axes[0].set_ylabel('I (A)')
    axes[0].tick_params(axis='x', which='both', bottom=False, labelbottom=False) 

    # Plot hexbin plot
    hb = axes[1].hexbin(data_microamp, lagged_data_microamp, gridsize=1000, cmap='viridis', norm=LogNorm())
    axes[1].set_xlabel(r"$\mathrm{I_{t}}$ (A)")
    axes[1].set_ylabel(r"$\mathrm{I_{t-1}}$ (A)")
    
    # Add lag order as text
    axes[1].text(0.35, 0.95, f'Lag Order: {lag_order}', ha='right', va='top', transform=axes[1].transAxes, fontsize=8)
    
    # Tight layout
    plt.tight_layout()
    
    # Save the combined plot
    plot_file_name = f'combined_plot_{lag_order:03d}.png'
    plt.savefig(os.path.join(folder_path, plot_file_name), dpi=300)
    
    plt.close()  # Close the figure to free up memory
