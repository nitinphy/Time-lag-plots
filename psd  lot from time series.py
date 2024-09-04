# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 19:57:16 2023

@author: sndkp
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.ticker as ticker
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import matplotlib
# Configure font settings
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.weight'] = 'bold'
font = {'family': 'serif', 'serif': ['Times New Roman'], 'size': 24}
matplotlib.rc('font', **font)

# Define the folder where your text files are located
folder_path = r"X:\Personal Data\Nbo2\09 Sept\09262023\224\Noise\8min\psd_file"  # Replace with your actual folder path

# Initialize color and marker lists
color_list = ['black', 'red', 'blue', 'green', 'orange', 'purple']
marker_list = ['o', 's', '^', '*', 'X', 'p']

# Create a function to plot a group of files with the same color and marker
def plot_group(start_index, end_index, color_index):
    marker_index = 0  # Initialize marker index for each group
    for i in range(start_index, end_index + 1):
        filename = f"psd_{i:03d}.txt"
        file_path = os.path.join(folder_path, filename)
        
        # Read data from the file using Pandas
        data = pd.read_csv(file_path, sep='\t')
        
        # Extract 'f' and 'sx' columns and convert to NumPy arrays
        f = data['f'].to_numpy()
        sx = data['Sx'].to_numpy()
        
        # Plot the data on a log-log scale with the specified color and marker
        marker = marker_list[marker_index % len(marker_list)]
        plt.loglog(f, sx, label=f'File {i}', color=color_list[color_index], marker=marker, markersize=8, linewidth=1)
        
        marker_index += 1  # Increment marker index within each group

# Define the starting and ending file numbers as variables
start_file = 211  # Adjust this variable to set the starting file number
end_file = 222   # Adjust this variable to set the ending file number

# Validate that the total number of files is a multiple of 6
if (end_file - start_file + 1) % 6 != 0:
    raise ValueError("Total number of files must be a multiple of 6.")

# Plot the groups of files with the same color and marker
for group_start in range(start_file, end_file + 1, 6):
    group_end = min(group_start + 5, end_file)
    color_index = (group_start - start_file) // 6
    plot_group(group_start, group_end, color_index)

# Set labels, title, and legend
plt.xlabel('$f (Hz)$')
plt.ylabel(r'$S_I \left(\frac{I^2}{\mathrm{Hz}}\right)$')
plt.tick_params(axis="y", direction="in", length=6, width=2)
plt.tick_params(axis="x", direction="in", length=6, width=2)
plt.gcf().set_size_inches(12, 8)  # Set the size of the figure to 12 x 8 inches

# Save the plot as an image
plt.savefig(os.path.join(folder_path, '8.png'), dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
