# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 12:12:02 2024

@author: sndkp
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Path to the folder containing CSV files
folder_path = r"F:\APS march meeting 2024\Data\Normalized\Noise neg\16min\time series"

# Get a list of all CSV files in the folder
csv_files = sorted([file for file in os.listdir(folder_path) if file.endswith('.csv')])

# Initialize the plot
plt.figure(figsize=(12, 6))

# Iterate through each set of three consecutive CSV files
for i in range(0, len(csv_files), 3):
    # Read the CSV files into pandas DataFrames, skipping the first 8 rows
    dfs = [pd.read_csv(os.path.join(folder_path, csv_files[j]), skiprows=8, nrows=None, low_memory=False, encoding_errors="ignore",on_bad_lines='skip') for j in range(i, i + 3)]

    # Plot reading vs relative time for each DataFrame
    for df in dfs:
        plt.plot(df['Relative Time'], df['Reading'])

# Set labels and title
plt.xlabel('Time (S)', fontsize=24, fontname='Times New Roman')
plt.ylabel('I (A)', fontsize=24, fontname='Times New Roman')
plt.xticks(fontsize=24, fontname='Times New Roman')
plt.yticks(fontsize=24, fontname='Times New Roman')
plt.title('Combined Plot', fontsize=24, fontname='Times New Roman')

# Save the plot
plot_filename = "combined_plot.png"
plt.savefig(os.path.join(folder_path, plot_filename), bbox_inches='tight')

# Optionally, you can display the plot
# plt.show()

# Close the plot to release memory
plt.close()
