# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:37:55 2023

@author: sndkp
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the folder path
folder_path = r"X:\Personal Data\Nbo2\09202023\206\noise final set\16min\time series\time series plots"

# Loop through all CSV files in the folder
for filename in os.listdir(folder_path):
    if filename.startswith("it_0"):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)

        # Read the CSV file into a DataFrame, skipping the first 8 rows
        df = pd.read_csv(file_path, skiprows=0)

        # Calculate the average of the 'Reading' column
        avg_reading = df['Reading'].mean()

        # Subtract the average from the 'Reading' column
        df['Reading'] -= avg_reading

        # Initialize lists to store data
        relative_times = df['Relative Time']
        average_readings = df['Reading']

        # Create a plot for the scatter points in red
        plt.figure(figsize=(8, 6))
        plt.scatter(relative_times, average_readings, c='red', label='$\Delta I/I$')
        plt.xlabel('T (s)')
        plt.ylabel('$\Delta I/I$')
        #plt.title(f'Scatter Plot of Reading - Average vs. Relative Time (Red) - {filename}')
        
        # Save the scatter plot with 300 dpi in the same folder
        scatter_plot_name = f'Time series_{filename}.png'
        scatter_plot_path = os.path.join(folder_path, scatter_plot_name)
        plt.savefig(scatter_plot_path, bbox_inches='tight',dpi=300)
        plt.close()
        
        #print(f"Scatter plot saved as {scatter_plot_path}")