# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:05:27 2023

@author: sndkp
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.ticker as ticker

# Define the file path and filename
csv_file_path = r"X:\Personal Data\Nbo2\09 Sept\09262023\224\Noise neg\16min\time series\time series plots\combined_data.csv"
df = pd.read_csv(csv_file_path) # Read the CSV file into a DataFrame
a=112
b=113
c=114

num_file = 30 # this should be total number of voltage runs



for _ in range(num_file):
    
    
    # Extract the columns I_001 to I_003 and T_001 to T_003 as NumPy arrays
            
    i_001 = df['I_' + str(a).zfill(3)].to_numpy()
    i_002 = df['I_' + str(b).zfill(3)].to_numpy()
    i_003 = df['I_' + str(c).zfill(3)].to_numpy()
    t_001 = df['T_' + str(a).zfill(3)].to_numpy()
    t_002 = df['T_' + str(b).zfill(3)].to_numpy()
    t_003 = df['T_' + str(c).zfill(3)].to_numpy()


    
    # Create the plot
    plt.figure(figsize=(12, 4))
    
    # Plot I_001 in black
    plt.plot(t_001, i_001, 'k', label='I_001', linewidth=1, markersize=8)
    
    # Plot I_002 in blue
    plt.plot(t_002, i_002, 'b', label='I_002', linewidth=1, markersize=8)
    
    # Plot I_003 in red
    plt.plot(t_003, i_003, 'r', label='I_003', linewidth=1, markersize=8)
    
    # Customize the font style and size
    font = {'family': 'serif', 'serif': ['Times New Roman'], 'size': 24}
    plt.rc('font', **font)
    
    # Add labels and title (customize as needed)
    plt.xlabel('t (s)')
    plt.ylabel(r'$\delta I/<I>$')  # Using LaTeX notation for math
    
    plt.ylim(-0.15, 0.15)
    plt.xlim(0,2800)
  
        # Create minor tick locators
    minor_locator_x = ticker.AutoMinorLocator(4)  # Example: 4 minor ticks between major ticks on x-axis
    minor_locator_y = ticker.AutoMinorLocator(4)  # Example: 4 minor ticks between major ticks on y-axis
    
    # Configure the minor tick locators for both x and y axes
    plt.gca().xaxis.set_minor_locator(minor_locator_x)
    plt.gca().yaxis.set_minor_locator(minor_locator_y)
    
    # Customize the minor tick width (linewidth) for both x and y axes
    plt.gca().tick_params(axis='both', which='minor', direction='in', length=6, width=2)
    
    # Set the axis line thickness to 2 points
    ax = plt.gca()
    ax.spines['top'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
        # Add a legend
    #plt.legend()
    
    # Save the graph at the same location with specified DPI and size
    output_file_path = os.path.splitext(csv_file_path)[0] + str(a)+'_graph.png'
    plt.savefig(output_file_path, dpi=300, bbox_inches='tight')
    
    # Show the plot (optional)
    plt.show()
    
    # Close the plot
    plt.close()
    # Update the values of a, b, and c for the next iteration
    a += 3
    b += 3
    c += 3

