# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:16:00 2024

@author: sndkp
"""
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



# Specify the directory containing the CSV files
directory = r'F:\NbO2 manuscript\Data\Normalized v driven noise\Noise pos\16min'

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.startswith("it_") and filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)

        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path, skiprows=0,low_memory=False, encoding_errors="ignore", on_bad_lines='skip')

        # Calculate minimum, maximum, and average of the 'Reading' column
        min_reading = df['Reading'].min()
        max_reading = df['Reading'].max()
        avg_reading = df['Reading'].mean()

        print(f"File: {filename}")
        print("Minimum Reading:", min_reading)
        print("Maximum Reading:", max_reading)
        print("Average Reading:", avg_reading)

        # Calculate the differences
        diff_min_avg = abs(min_reading - avg_reading)
        diff_max_avg = abs(max_reading - avg_reading)

        # Determine the x-axis limit
        x_limit = max(diff_min_avg, diff_max_avg)

        # Create a histogram plot
        plt.hist(df['Reading'], bins=100, color='black', edgecolor='black', range=(avg_reading - x_limit, avg_reading + x_limit))
        plt.xlabel('I (A)')
        plt.ylabel('Count')
        #plt.title('Histogram of Reading Values')
        plt.axvline(x=avg_reading, color='red', linestyle='--', label='Mean')
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
        # Save the plot in the same folder with the same filename
        plot_filename = os.path.splitext(filename)[0] + '_histogram.png'
        plot_path = os.path.join(directory, plot_filename)
        plt.savefig(plot_path, bbox_inches='tight', dpi=300)
        plt.close()  # Close the plot to free memory
        print(f"Plot saved as: {plot_filename}")
