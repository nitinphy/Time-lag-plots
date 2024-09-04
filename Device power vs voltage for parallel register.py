# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 20:36:18 2024

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
folder_path = r"E:\Personal Data\Nbo2\2024\4 Apr\15\SET 2\upto threshold"

# Get a list of all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.startswith('IV_') and file.endswith('.csv')]

# Accumulate data from all CSV files
all_power_data = []
all_voltage_data = []

for file_num, csv_file in enumerate(csv_files, start=1):
    # Extract resistance value from file name
    resistance = float(os.path.splitext(csv_file)[0][-3:])  # Assuming the resistance is always at the end of the filename
    resistance = resistance + 5
    # Load CSV file into a DataFrame
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path, skiprows=0)

    # Extract data as NumPy arrays
    current = df['Reading'].values
    voltage = df['Value'].values
    
    # Calculate device power (current * voltage)
    device_power = current * voltage
    
    all_power_data.append(device_power)
    all_voltage_data.append(voltage)

# Create a plot for all traces
plt.figure(figsize=(10, 7))
for file_num, (device_power, voltage) in enumerate(zip(all_power_data, all_voltage_data), start=1):
    # Extract last three digits from file name
    legend_label = os.path.splitext(csv_files[file_num - 1])[0][-3:]
    plt.plot(voltage, device_power, label=f'Run {legend_label}', marker='.')

# Add labels and title
plt.xlabel('Voltage (V)')
plt.ylabel('Device Power (mW)')
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
# plt.title('Device Power vs Voltage')

# Save the plot
plot_file_path = os.path.join(folder_path, 'Device_Power_vs_Voltage.png')
plt.savefig(plot_file_path, bbox_inches='tight', dpi=300)

print("Plot of device power vs voltage saved successfully.")
    