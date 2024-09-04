# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 18:45:39 2023

@author: sndkp
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.ticker import AutoMinorLocator
import matplotlib.ticker as ticker

mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.weight'] = 'bold'
mpl.rcParams['axes.linewidth'] = 2
mpl.rcParams['xtick.labelsize'] = 14
mpl.rcParams['ytick.labelsize'] = 14
mpl.rcParams['axes.labelsize'] = 18
mpl.rcParams['axes.titlesize'] = 16

def plot_data(folder_path, file_prefix):
    csv_files = [file for file in os.listdir(folder_path) if file.startswith(file_prefix) and file.endswith('.csv')]

    for file_num, csv_file in enumerate(csv_files, start=1):
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path, skiprows=8)

        if file_prefix == 'IV_':
            current = df['Reading']
            voltage = df['Value']
        elif file_prefix == 'VI_':
            current = df['Value']
            voltage = df['Reading']
        else:
            raise ValueError("Invalid file prefix. Use 'IV_' or 'VI_'.")

        # Convert current and voltage data to NumPy arrays
        current_np = np.array(current)
        voltage_np = np.array(voltage)

        plt.figure()

        # Plot the line
        plt.plot(voltage_np, current_np * 1000, label=f'Run {file_num}', linestyle='-', marker='.', color='red', linewidth=1)

        plt.ylabel('Current (mA)')
        plt.xlabel('Voltage (V)')
        plt.legend()
        plt.tick_params(axis="y", direction="in", length=6, width=2, )
        plt.tick_params(axis="x", direction="in", length=6, width=2, )

        # Create minor tick locators
        minor_locator_x = ticker.AutoMinorLocator(4)
        minor_locator_y = ticker.AutoMinorLocator(4)

        # Configure the minor tick locators for both x and y axes
        plt.gca().xaxis.set_minor_locator(minor_locator_x)
        plt.gca().yaxis.set_minor_locator(minor_locator_y)

        # Customize the minor tick width (linewidth) for both x and y axes
        plt.gca().tick_params(axis='both', which='minor', direction='in', length=6, width=2)

        plot_file_name = f'{file_prefix}Plot_{file_num}.png'
        plot_file_path = os.path.join(folder_path, plot_file_name)
        plt.savefig(plot_file_path, bbox_inches='tight', dpi=300)
        plt.close()

    print(f"Plots for {file_prefix} saved successfully.")

# Example usage for IV plots
plot_data(r"F:\NbO2 manuscript\Data\325 current driven noise\IV After noise", 'IV_')

# Example usage for VI plots
plot_data(r"F:\NbO2 manuscript\Data\325 current driven noise\IV After noise", 'VI_')
