import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.ticker as ticker
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.weight'] = 'bold'
mpl.rcParams['axes.linewidth'] = 2
mpl.rcParams['xtick.labelsize'] = 14
mpl.rcParams['ytick.labelsize'] = 14
mpl.rcParams['axes.labelsize'] = 18
mpl.rcParams['axes.titlesize'] = 16


folder_path = r"E:\Personal Data\Nbo2\09 Sept\11022023\614"

csv_files = [file for file in os.listdir(folder_path) if file.startswith('VI_') and file.endswith('.csv')]

for file_num, csv_file in enumerate(csv_files, start=1):
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path, skiprows=8,nrows=None, low_memory=False, encoding_errors="ignore")

    voltage = df['Reading']
    current = df['Value']

    # Convert current and voltage data to NumPy arrays
    current_np = np.array(current)
    voltage_np = np.array(voltage)

    plt.figure()
    
    # Plot the line
    plt.plot( current_np*1000, voltage_np, label=f'Run {file_num}', linestyle='-', marker ='.', color = 'red', linewidth=1)
    
    # Plot points
    #plt.scatter(voltage_np, current_np * 1000, marker='o', s=20, color='red', label='Data Points')
    #plt.xscale('log')
    plt.xlabel('Current (mA)')
    plt.ylabel('Voltage (V)')
    plt.legend()
    plt.tick_params(axis="y",direction="in",length=6, width=2,)
    plt.tick_params(axis="x",direction="in",length=6, width=2,)
    # Create minor tick locators
    minor_locator_x = ticker.AutoMinorLocator(4)  # Example: 4 minor ticks between major ticks on x-axis
    minor_locator_y = ticker.AutoMinorLocator(4)  # Example: 4 minor ticks between major ticks on y-axis
    
    # Configure the minor tick locators for both x and y axes
    plt.gca().xaxis.set_minor_locator(minor_locator_x)
    plt.gca().yaxis.set_minor_locator(minor_locator_y)
    
    # Customize the minor tick width (linewidth) for both x and y axes
    plt.gca().tick_params(axis='both', which='minor', direction='in', length=6, width=2)

    
    plot_file_name = f'VI_Plot_{file_num}.png'
    plot_file_path = os.path.join(folder_path, plot_file_name)
    plt.savefig(plot_file_path, bbox_inches='tight',dpi = 300)
    plt.close()

print("Plots saved successfully.")
