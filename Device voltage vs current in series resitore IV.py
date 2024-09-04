# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:41:02 2024

@author: sndkp
"""


import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np  # Don't forget to import numpy
import matplotlib.animation as animation
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.ticker as ticker

# Set font and plot settings
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.weight'] = 'bold'
mpl.rcParams['axes.linewidth'] = 2
mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18
mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['axes.titlesize'] = 16

# Define the folder containing CSV files
folder_path = r"E:\Personal Data\Nbo2\2024\4 Apr\4\series registor\Just before transiton"

# Get a list of all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.startswith('IV_') and file.endswith('.csv')]

# Accumulate data from all CSV files
all_current_data = []
all_voltage_data = []

for file_num, csv_file in enumerate(csv_files, start=1):
    # Extract resistance value from file name
    resistance = float(os.path.splitext(csv_file)[0][-4:])  # Assuming the resistance is always at the end of the filename
    resistance = resistance
    # Load CSV file into a DataFrame
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path, skiprows=8)

    # Extract data as NumPy arrays
    current = df['Reading'].values
    voltage = df['Value'].values
    
    # Calculate device current
    device_voltage = voltage - (current* resistance)
    
    all_current_data.append(current)
    all_voltage_data.append(device_voltage)

# Create a plot for all traces
plt.figure(figsize=(10, 7))
for file_num, (current, device_voltage) in enumerate(zip(all_current_data, all_voltage_data), start=1):
    # Extract last three digits from file name
    legend_label = os.path.splitext(csv_files[file_num - 1])[0][-4:]
    plt.plot(device_voltage, current * 1000, label=f'Run {legend_label}', marker='.')

# Add labels and title
plt.xlabel('Voltage (V)')
plt.ylabel('Device Current (mA)')
plt.tick_params(axis="y", direction="in", length=8, width=2,)
plt.tick_params(axis="x", direction="in", length=8, width=2,)
plt.ylim(0, None)
plt.legend()

# Create minor tick locators
minor_locator_x = ticker.AutoMinorLocator(8)
minor_locator_y = ticker.AutoMinorLocator(8)
plt.gca().xaxis.set_minor_locator(minor_locator_x)
plt.gca().yaxis.set_minor_locator(minor_locator_y)
plt.gca().tick_params(axis='both', which='minor', direction='in', length=6, width=2)

# Uncomment to set plot title
# plt.title('Device Current vs Voltage')

# Save the plot
plot_file_path = os.path.join(folder_path, 'Current_vs_Device_Voltage.png')
plt.savefig(plot_file_path, bbox_inches='tight', dpi=300)

print("Plot of device current vs voltage saved successfully.")
