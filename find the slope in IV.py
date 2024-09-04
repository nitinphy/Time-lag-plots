# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 10:56:41 2023

@author: sndkp
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy import stats

mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.weight'] = 'bold'
mpl.rcParams['axes.linewidth'] = 2
mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18
mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['axes.titlesize'] = 16

folder_path = r"X:\Personal Data\Nbo2\09022023"

csv_files = [file for file in os.listdir(folder_path) if file.startswith('IV_') and file.endswith('.csv')]

# Define a function for linear regression
def perform_linear_regression(x, y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return slope, intercept, r_value

for file_num, csv_file in enumerate(csv_files, start=1):
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path, skiprows=0)

    current = df['Current [A]']
    voltage = df['Voltage [V]']

    # Convert current and voltage data to NumPy arrays
    current_np = np.array(current)
    voltage_np = np.array(voltage)

    plt.figure()

    # Plot the line
    plt.plot(voltage_np, current_np * 1000, label=f'Run {file_num}', linestyle='-',marker='o', linewidth=2)

    # Define the region for linearization within the data
    start_index = 60
    end_index = 100

    # Extract the region for linearization within the data
    voltage_linear = voltage_np[start_index:end_index]
    current_linear = current_np[start_index:end_index]

    # Perform linear regression within the data region
    slope, intercept, r_value = perform_linear_regression(voltage_linear, current_linear)
# Calculate the inverse of the slope
    inverse_slope = 1.0 / slope

    # Extend the voltage range beyond the data in both directions
    extension = 2.0  # Adjust the extension as needed
    extended_voltage_left = np.linspace(max(0, voltage_np[0] - extension), voltage_linear[0], 100)
    extended_voltage_right = np.linspace(voltage_linear[-1], voltage_np[-1] + extension, 100)

    # Calculate the corresponding current values for the extensions
    extended_current_left = slope * extended_voltage_left + intercept
    extended_current_right = slope * extended_voltage_right + intercept

    # Plot the linear fit within the data region
    plt.plot(voltage_linear, current_linear * 1000, label='Linear Fit',  linestyle='--', color='orange')

    # Plot the extrapolated linear fit on both sides
    plt.plot(extended_voltage_left, extended_current_left * 1000, linestyle='--', color='green', alpha=0.7)
    plt.plot(extended_voltage_right, extended_current_right * 1000, linestyle='--', color='green', alpha=0.7)

    # Plot points

    plt.text(0.1, 0.9, f'Slope: {inverse_slope:.4f}', transform=plt.gca().transAxes, fontsize=14)
    plt.text(0.1, 0.85, f'R-squared: {r_value**2:.4f}', transform=plt.gca().transAxes, fontsize=14)
    
    # Set x-axis and y-axis limits to display only positive values
    plt.xlim(0, )
    plt.ylim(0, )

    plt.xlabel('Voltage (V)')
    plt.ylabel('Current (mA)')
    plt.legend()

    plot_file_name = f'IV_Plot_{file_num}.png'
    plot_file_path = os.path.join(folder_path, plot_file_name)
    plt.savefig(plot_file_path, bbox_inches='tight', dpi=300)
    plt.close()

print("Plots with extrapolated linear fit and positive values on x and y axes saved successfully.")
