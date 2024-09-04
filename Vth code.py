# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 13:56:47 2023

@author: sndkp

"""
import pandas as pd
from scipy.signal import argrelextrema
import os

# Directory containing all the CSV files
directory = r"E:\Personal Data\Nbo2\Data from albany\125C\111"

# Initialize an empty list to store the results
results_list = []

# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)

        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path,skiprows=55)

        # Differentiate the 'Reading' column
        df['Differentiated_Reading'] = df.iloc[:,2].diff()

        # Extract differentiated current, voltage, and reading
        diff_reading = df['Differentiated_Reading']
        
        voltage = pd.to_numeric(df.iloc[:,1], errors='coerce')
        reading = pd.to_numeric(df.iloc[:,2], errors='coerce')

        # Find local maxima and minima indices in the differentiated current
        maxima_indices = argrelextrema(diff_reading.values, comparator=lambda x, y: x > y)[0]
        minima_indices = argrelextrema(diff_reading.values, comparator=lambda x, y: x < y)[0]

        # Sort maxima and minima indices based on differentiated current values
        sorted_maxima_indices = sorted(maxima_indices, key=lambda i: diff_reading[i], reverse=True)
        sorted_minima_indices = sorted(minima_indices, key=lambda i: diff_reading[i])

        # Select the top two maxima and the bottom two minima
        top_two_maxima_indices = sorted_maxima_indices[:2]
        bottom_two_minima_indices = sorted_minima_indices[:2]

        # Extract file number from the filename
        file_number = int(filename.split('_')[1].split('.')[0])

        # Append results to the results list
        results_list.append({
                             'File_Number': file_number,
                             'Voltage_Max_1': voltage[top_two_maxima_indices[0]],
                             'Differentiated_Current_Max_1': diff_reading[top_two_maxima_indices[0]],
                             'Reading_Max_1': reading[top_two_maxima_indices[0]],
                             'Voltage_Max_2': voltage[top_two_maxima_indices[1]],
                             'Differentiated_Current_Max_2': diff_reading[top_two_maxima_indices[1]],
                             'Reading_Max_2': reading[top_two_maxima_indices[1]],
                             'Voltage_Min_1': voltage[bottom_two_minima_indices[0]],
                             'Differentiated_Current_Min_1': diff_reading[bottom_two_minima_indices[0]],
                             'Reading_Min_1': reading[bottom_two_minima_indices[0]],
                             'Voltage_Min_2': voltage[bottom_two_minima_indices[1]],
                             'Differentiated_Current_Min_2': diff_reading[bottom_two_minima_indices[1]],
                             'Reading_Min_2': reading[bottom_two_minima_indices[1]]})

# Create a DataFrame from the results list
results_df = pd.DataFrame(results_list)

# Save the results to a new CSV file
results_df.to_csv(os.path.join(directory, 'results.csv'), index=False)
