# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:27:41 2024

@author: sndkp
"""
import os
import numpy as np
import matplotlib.pyplot as plt

# Path to the folder containing the text files
folder_path = r'F:\NbO2 manuscript\Data\Normalized v driven noise\Noise pos\16min\detrend_file'

# Get a list of all files in the folder
file_names = os.listdir(folder_path)

# Iterate over each file
for file_name in file_names:
    # Check if the file is a text file
    if file_name.endswith('.txt'):
        # Construct the full path to the file
        file_path = os.path.join(folder_path, file_name)
        
        # Load data from the text file, skipping the first row (header)
        data = np.loadtxt(file_path, skiprows=1)
        
        # Extract the second column
        second_column = data[:, 1]
        
        # Plot histogram
        plt.hist(second_column, bins=100, color='skyblue', edgecolor='black')
        plt.title('Histogram of Second Column')
        plt.xlabel('Values')
        #plt.xlim(-2e-7, 2e-7)
        plt.ylabel('Frequency')
        plt.grid(True)
        
        # Extract file name without extension
        file_name_without_extension = os.path.splitext(file_name)[0]
        
        # Save plot with corresponding file name in the same folder
        plot_file_path = os.path.join(folder_path, file_name_without_extension + '_histogram.png')
        plt.savefig(plot_file_path)
        
        # Clear the current plot to prepare for the next iteration
        plt.clf()

print("Histogram plots saved for all files in the folder.")
