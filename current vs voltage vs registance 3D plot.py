# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 07:49:30 2024

@author: sndkp
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting library

# Define the folder containing CSV files
folder_path = r"E:\Personal Data\Nbo2\2024\4 Apr\15\SET 2\upto threshold"

# Get a list of all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.startswith('IV_') and file.endswith('.csv')]

# Initialize lists to store resistance, device current, and voltage
resistance_list = []
device_current_list = []
voltage_list = []

# Iterate through each CSV file
for csv_file in csv_files:
    # Load CSV file into a DataFrame
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path, skiprows=0)

    # Extract resistance value from last three digits of file name
    resistance = float(os.path.splitext(csv_file)[0][-3:]) + 20  # Assuming the resistance is always at the end of the filename
    
    # Extract last data point
    last_row = df.iloc[-1]
    
    # Calculate device current and voltage
    device_current = last_row['Reading'] - (last_row['Value'] / resistance)
    voltage = last_row['Value']
    
    # Append values to respective lists
    resistance_list.append(resistance)
    device_current_list.append(device_current)
    voltage_list.append(voltage)

# Plot the data in 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(resistance_list, device_current_list, voltage_list, c='r', marker='o')

ax.set_xlabel('Resistance (Ohms)')
ax.set_ylabel('Device Current (mA)')
ax.set_zlabel('Voltage (V)')

plt.title('Resistance vs. Device Current vs. Voltage')
plt.show()
