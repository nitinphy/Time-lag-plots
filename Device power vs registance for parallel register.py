# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 07:53:24 2024

@author: sndkp
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the folder containing CSV files
folder_path = r"E:\Personal Data\Nbo2\2024\4 Apr\15\SET 2\upto threshold"

# Get a list of all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.startswith('IV_') and file.endswith('.csv')]

# Initialize lists to store resistance, device current, voltage, and product of device current and voltage
resistance_list = []
product_list = []

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
    
    # Calculate product of device current and voltage
    product = device_current * voltage
    
    # Append values to respective lists
    resistance_list.append(resistance)
    product_list.append(product)

# Plot the data
plt.figure(figsize=(8, 6))
plt.plot(resistance_list, product_list, marker='o', linestyle='-', color='b')
plt.xlabel('Resistance (Ohms)')
plt.ylabel('Device Current * Voltage')
plt.title('Resistance vs. Device Current * Voltage')
plt.grid(True)
plt.show()
