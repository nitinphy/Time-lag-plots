# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:53:33 2023

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
folder_path = r"F:\Personal Data\NbO2\Size dependent study\IV_with RS\L5_D7"

# Get a list of all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.startswith('') and file.endswith('.csv')]

# Accumulate data from all CSV files
all_current_data = []
all_voltage_data = []

for file_num, csv_file in enumerate(csv_files, start=1):
    # Load CSV file into a DataFrame
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path,skiprows = 8)
        # Select only the first half of the data
    half_index = len(df) // 2
    df = df.iloc[:half_index]
    # Extract data as NumPy arrays
    #current = df['Current [A]'].values
   # voltage = df['Voltage [V]'].values
    # Extract data as NumPy arrays
    current = df['Reading'].values
    voltage = df['Value'].values
    
    all_current_data.append(current)
    all_voltage_data.append(voltage)

# Create a plot for all traces
plt.figure(figsize=(10, 7))
for file_num, (current, voltage) in enumerate(zip(all_current_data, all_voltage_data), start=1):
    # Extract last three digits from file name
    legend_label = os.path.splitext(csv_files[file_num - 1])[0][-3:]
    plt.plot(voltage, current * 1000, label=f'Run {legend_label}', marker='.')

# Add labels and title
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.tick_params(axis="y", direction="in", length=8, width=2,)
plt.tick_params(axis="x", direction="in", length=8, width=2,)
#plt.legend()

# Create minor tick locators
minor_locator_x = ticker.AutoMinorLocator(8)
minor_locator_y = ticker.AutoMinorLocator(8)
plt.gca().xaxis.set_minor_locator(minor_locator_x)
plt.gca().yaxis.set_minor_locator(minor_locator_y)
plt.gca().tick_params(axis='both', which='minor', direction='in', length=6, width=2)

# Uncomment to set plot title
# plt.title('IV Curve - All Traces')

# Save the plot
plot_file_path = os.path.join(folder_path, 'All_IV.png')
plt.savefig(plot_file_path, bbox_inches='tight', dpi=300)

print("Plot of all traces saved successfully.")
