import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm  # Import LogNorm for log scale
import matplotlib.ticker as ticker
from scipy.interpolate import griddata
import pandas as pd
import math

plt.rcParams["font.family"] = "serif"
plt.rcParams["mathtext.fontset"] = "dejavuserif"
plt.rcParams.update({'font.size': 11, 'font.family': 'Times New Roman'})

# Step 1: Define the folder and file name

# Define the folder and file name
folder_path = r'F:\NbO2 manuscript\Data\Voltage driven time lag plots\Only 58'
file_prefix = 'it_'
file_extension = '.txt'

ab = 1
cd = ab+3
for i in range(1, 5):
    # Generate file name
    file_number = f'{i:03d}'
    file_name = f'{file_prefix}{file_number}{file_extension}'
    file_path = os.path.join(folder_path, file_name)
    
    # Step 2: Import the data from the text file, skipping the first column and header
    data = np.genfromtxt(file_path, dtype=float, delimiter=None, comments='#', usecols=0, skip_header=1)
    time = np.genfromtxt(file_path, dtype=float, delimiter=None, comments='#', usecols=1, skip_header=1)
    
    # Convert current to microamperes
    data_microamp = data * 1e1
    a = 0.06
    b = 0.065
    # Step 3: Choose lag order (number of time steps to lag by)
    lag_order = 5
    
    
    # Step 4: Create lagged data
    lagged_data = np.roll(data, lag_order)
    lagged_data_microamp = lagged_data * 1e0
    
    # Plot both line plot and hexbin plot vertically
    fig, axes = plt.subplots(2, 1, figsize=(2.6 , 2.8), gridspec_kw={'height_ratios': [1, 4]})
    
    # Plot line plot
    axes[0].plot(time, data_microamp)
    #axes[0].set_xlabel('Time')
    axes[0].set_ylabel('I (A)')
    #axes[0].set_title('Time Series Plot')
    axes[0].tick_params(axis='x', which='both', bottom=False, labelbottom=False) 
    # Plot hexbin plot
    hb = axes[1].hexbin(data_microamp, lagged_data_microamp, gridsize=1000, cmap='viridis', norm=LogNorm())
    axes[1].set_xlabel(r"$\mathrm{I_{t}}$ (A)")
    axes[1].set_ylabel(r"$\mathrm{I_{t-1}}$ (A)")
    # Assuming 'axes' is your subplot object
    
    #axes[1].set_xlim(a,b)  # Set the range for the x-axis from 0 to 1
    #axes[1].set_ylim(a,b)  # Set the range for the y-axis from 0 to 1

    
    #axes[1].set_title('Hexbin Plot with Color Bar')
    #plt.colorbar(hb, ax=axes[1])
    # Add file number as text
    axes[1].text(0.35, 0.95, f'File: {file_number}', ha='right', va='top', transform=axes[1].transAxes, fontsize=8)
    # Tight layout
    plt.tight_layout()
    
    # Save the combined plot
    plot_file_name = f'combined_plot_{file_name[-7:-4]}.png'
    plt.savefig(os.path.join(folder_path, plot_file_name), dpi=300)
    
    plt.show()
    plt.close()
