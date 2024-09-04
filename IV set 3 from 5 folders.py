# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:30:14 2024

@author: sndkp
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:30:14 2024

@author: sndkp
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.ticker as ticker

# Set font and plot settings
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.weight'] = 'bold'
mpl.rcParams['axes.linewidth'] = 2
mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18
mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['axes.titlesize'] = 16

# Path to the master folder
master_folder = r"F:\Personal Data\NbO2\Size dependent study\IV_with RS"

# List of subfolders
subfolders = ['L1_D13', 'L2_D5', 'L3_D5', 'L4_D5', 'L5_D7']

# List of files to plot
files_to_plot = ['IV_001.csv', 'IV_002.csv', 'IV_003.csv']

# Initialize an empty DataFrame to hold the combined data
combined_df = pd.DataFrame()

# Loop through each subfolder and each file
for subfolder in subfolders:
    subfolder_path = os.path.join(master_folder, subfolder)
    
    for file in files_to_plot:
        file_path = os.path.join(subfolder_path, file)
        
        if os.path.exists(file_path):
            # Read the CSV file, skipping the first 8 rows
            df = pd.read_csv(file_path, skiprows=8)
            
            # Check if 'Value' and 'Reading' columns exist
            if 'Value' in df.columns and 'Reading' in df.columns:
                # Add additional columns for subfolder and file information
                df['Subfolder'] = subfolder
                df['File'] = file
                
                # Append the data to the combined DataFrame
                combined_df = pd.concat([combined_df, df], ignore_index=True)
            else:
                print(f"Columns 'Value' and 'Reading' not found in {file_path}")
        else:
            print(f"{file_path} does not exist")

# Save the combined DataFrame to a new CSV file
combined_csv_path = os.path.join(master_folder, 'combined_data.csv')
combined_df.to_csv(combined_csv_path, index=False)

# Create a single plot
plt.figure(figsize=(15, 10))

# Plot the combined data
for name, group in combined_df.groupby(['Subfolder', 'File']):
    plt.plot(group['Value'], group['Reading']*1000, marker='o', linestyle='-', label=f'{name[0]} - {name[1]}')

# Add labels and title
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.tick_params(axis="y", direction="in", length=8, width=2)
plt.tick_params(axis="x", direction="in", length=8, width=2)
plt.legend()

# Create minor tick locators
minor_locator_x = ticker.AutoMinorLocator(8)
minor_locator_y = ticker.AutoMinorLocator(8)
plt.gca().xaxis.set_minor_locator(minor_locator_x)
plt.gca().yaxis.set_minor_locator(minor_locator_y)
plt.gca().tick_params(axis='both', which='minor', direction='in', length=6, width=2)

# Show the plot
plt.show()
