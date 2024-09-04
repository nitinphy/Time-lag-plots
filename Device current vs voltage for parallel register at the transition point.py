# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:13:43 2024

@author: sndkp
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the folder containing CSV files
folder_path = r"E:\Personal Data\Nbo2\2024\4 Apr\15\SET 2\upto threshold"

# Get a list of all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.startswith('IV_') and file.endswith('.csv')]

# Initialize lists to store last data points
last_device_current = []
last_voltage = []

# Iterate through each CSV file
for csv_file in csv_files:
    # Load CSV file into a DataFrame
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path, skiprows=0)

    # Extract resistance value from file name
    resistance = float(os.path.splitext(csv_file)[0][-3:]) + 20  # Assuming the resistance is always at the end of the filename
    #print(len(df))
    # Extract last data point
    last_row = df.iloc[-1]
    #print(last_row)
    last_device_current.append(last_row['Reading'] - (last_row['Value'] / resistance))
    last_voltage.append(last_row['Value'])
    #print(last_voltage)
# Create a table
table_data = {'Last Device Current (mA)': last_device_current, 'Last Voltage (V)': last_voltage}
table_df = pd.DataFrame(table_data)

# Print the table
print("Last Data Points from Each File:")
print(table_df)

# Plot the last data points
plt.figure(figsize=(8, 6))
plt.plot(last_voltage, last_device_current, marker='o', linestyle='None', color='r')
plt.xlabel('Voltage (V)')
plt.ylabel('Device Current (mA)')
plt.title('Last Data Points from Each File')
plt.grid(True)
plt.show()
