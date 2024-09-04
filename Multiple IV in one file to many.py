# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:52:34 2023

@author: sndkp
"""

import pandas as pd
import os

# Specify the path to your CSV file
input_folder = r"E:\Personal Data\Nbo2\12 dec\12262023\329\IV Stability"

# Specify the folder where you want to save the individual CSV files
output_folder = r"E:\Personal Data\Nbo2\12 dec\12262023\329\IV Stability\IV1"

# Read the CSV file skipping the first 8 rows
# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all input files (IV_001.csv to IV_010.csv)
for i in range(1, 11):
    # Generate the input file name
    input_file_name = f'IV_{str(i).zfill(3)}.csv'
    input_file_path = os.path.join(input_folder, input_file_name)

    # Read the CSV file, skipping the first 8 rows
    df = pd.read_csv(input_file_path, skiprows=8)

    # Split the dataframe into sets of 399 rows each
    sets_of_data = [df.iloc[j:j + 399] for j in range(0, len(df), 399)]

    # Save each set of data into a separate file
    for j, set_data in enumerate(sets_of_data):
        output_file_name = f'IV_{str((i-1) * 200 + j + 1).zfill(4)}.csv'
        output_file_path = os.path.join(output_folder, output_file_name)
        set_data.to_csv(output_file_path, index=False)

print("Files saved successfully.")