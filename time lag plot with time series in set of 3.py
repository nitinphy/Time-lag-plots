import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import matplotlib.ticker as ticker
from scipy.interpolate import griddata
import pandas as pd
import math

plt.rcParams["font.family"] = "serif"
plt.rcParams["mathtext.fontset"] = "dejavuserif"
plt.rcParams.update({'font.size': 11, 'font.family': 'Times New Roman'})

# Define the folder and file name
folder_path = r'F:\Personal Data\NbO2\Time sereis for voltage driven noise till april 2024\206'
file_prefix = 'it_'
file_extension = '.txt'

# Define the number of files per group
files_per_group = 3

# Calculate the total number of groups
total_groups = math.ceil(54 / files_per_group)

for group in range(total_groups):
    # Initialize a figure with 2 rows and 3 columns for each group
    fig, axes = plt.subplots(2, 3, figsize=(12, 8), gridspec_kw={'height_ratios': [3, 1]})
    
    # Iterate over each file in the group
    for i in range(files_per_group):
        file_index = group * files_per_group + i + 1
        
        if file_index > 54:
            break
        
        # Generate file name
        file_number = f'{file_index:03d}'
        file_name = f'{file_prefix}{file_number}{file_extension}'
        file_path = os.path.join(folder_path, file_name)

        # Import the data from the text file, skipping the first column and header
        data = np.genfromtxt(file_path, dtype=float, delimiter=None, comments='#', usecols=0, skip_header=1)
        time = np.genfromtxt(file_path, dtype=float, delimiter=None, comments='#', usecols=1, skip_header=1)

        # Convert current to microamperes
        data_microamp = data * 1e3

        # Choose lag order (number of time steps to lag by)
        lag_order = 1

        # Create lagged data
        lagged_data = np.roll(data, lag_order)
        lagged_data_microamp = lagged_data * 1e3

        # Determine the position of the subplot in the figure
        row_index = i // 3
        col_index = i % 3

        # Plot line plot
        axes[1, col_index].plot(time, data_microamp)
        axes[1, col_index].set_ylabel('I (mA)')
        axes[1, col_index].tick_params(axis='x', which='both', bottom=False, labelbottom=False)

        # Plot hexbin plot
        hb = axes[0, col_index].hexbin(data_microamp, lagged_data_microamp, gridsize=200, cmap='viridis', norm=LogNorm())
        axes[0, col_index].set_xlabel(r"$\mathrm{I_{t}}$ (mA)")
        axes[0, col_index].set_ylabel(r"$\mathrm{I_{t-1}}$ (mA)")
        axes[0, col_index].text(0.35, 0.95, f'File: {file_number}', ha='right', va='top', transform=axes[0, col_index].transAxes, fontsize=8)

    # Add a colorbar for the last subplot
    cax = fig.add_axes([0.92, 0.15, 0.02, 0.7])
    plt.colorbar(hb, cax=cax)

    # Save the combined plot for the group
    plot_file_name = f'combined_plots_group_{group + 1}.png'
    plt.savefig(os.path.join(folder_path, plot_file_name), dpi=300, transparent=True)

    plt.show()
    plt.close()
