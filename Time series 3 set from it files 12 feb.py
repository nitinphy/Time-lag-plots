# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:57:34 2024

@author: sndkp
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

# Path to the folder containing CSV files
folder_path = r"F:\NbO2\50 nm\D4\Noise\1500 ohms\Raw data"

# Get a list of all CSV files in the folder
csv_files = sorted([file for file in os.listdir(folder_path) if file.endswith('.csv')])

# Iterate through each set of three consecutive CSV files
for i in range(0, len(csv_files), 3):
    # Read the CSV files into pandas DataFrames
    dfs = [pd.read_csv(os.path.join(folder_path, csv_files[j])) for j in range(i, i + 3)]

    # Initialize the plot
    plt.figure(figsize=(12, 6))

    # Plot reading vs relative time for each DataFrame
    for df in dfs:
        plt.plot(df['Relative Time'], df['Reading'], label=df['Relative Time'].iloc[0])

    plt.xlabel('Time (S)', fontsize=24, fontname='Times New Roman')
    plt.ylabel('I (A)', fontsize=24, fontname='Times New Roman')
    plt.xticks(fontsize=24, fontname='Times New Roman')
    plt.yticks(fontsize=24, fontname='Times New Roman')
    #plt.legend(fontsize=24, loc='best')
    plt.tight_layout()

    # Save the plot as a PNG file with a suffix _combined_plot
    plot_filename = "_".join([os.path.splitext(csv_files[j])[0] for j in range(i, i + 3)]) + '_combined_plot.png'
    plt.savefig(os.path.join(folder_path, plot_filename), bbox_inches='tight')

    # Optionally, you can display the plot
    # plt.show()

    # Close the plot to release memory
    plt.close()
