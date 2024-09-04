# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:00:29 2023

@author: sndkp
"""

import pandas as pd
import os

# Define the folder paths for input and output
input_folder = r"X:\Personal Data\Nbo2\09 Sept\09262023\224\Noise\raw"
output_folder = r"X:\Personal Data\Nbo2\09 Sept\09262023\224\Noise\8min"

# Loop over num values from 6 to 43
for num in range(1, 44):
    # Specify the input CSV file name
    input_file = 'it_' + str(num).zfill(3) + '.csv'
    print(input_file)
    # Construct the full path to the input CSV file
    input_file_path = os.path.join(input_folder, input_file)

    # Check if the input CSV file exists
    if not os.path.isfile(input_file_path):
        print(f"File '{input_file_path}' not found.")
        continue  # Skip to the next iteration if the file doesn't exist

    # Read the CSV file
    try:
        df = pd.read_csv(input_file_path, skiprows=8, encoding="utf8", encoding_errors='ignore', on_bad_lines='skip')
    except FileNotFoundError:
        print(f"File '{input_file_path}' not found.")
        continue  # Skip to the next iteration if there's an error reading the file

    # Get the total number of rows in the CSV file
    total_rows = len(df)

    # Specify the output file names
    number = num * 6 -5
    output_file1 = 'it_' + str(number).zfill(3) + '.csv'
    output_file2 = 'it_' + str(number + 1).zfill(3) + '.csv'
    output_file3 = 'it_' + str(number + 2).zfill(3) + '.csv'
    output_file4 = 'it_' + str(number + 3).zfill(3) + '.csv'
    output_file5 = 'it_' + str(number + 4).zfill(3) + '.csv'
    output_file6 = 'it_' + str(number + 5).zfill(3) + '.csv'

    # Construct the full paths to the output CSV files
    output_file_path1 = os.path.join(output_folder, output_file1)
    output_file_path2 = os.path.join(output_folder, output_file2)
    output_file_path3 = os.path.join(output_folder, output_file3)
    output_file_path4 = os.path.join(output_folder, output_file4)
    output_file_path5 = os.path.join(output_folder, output_file5)
    output_file_path6 = os.path.join(output_folder, output_file6)
    
    
    
    
    print("saved till"+ output_file6)
    # Check if the specified rows are within the total number of rows
    if total_rows < 1440000:
        print(f"Error: The CSV file '{input_file}' does not contain 1,440,000 rows.")
    else:
        # Extract and save the first 480,000 rows
        df[0:240000].to_csv(output_file_path1, index=False)

        # Extract and save the next 480,000 rows
        df[240000:480000].to_csv(output_file_path2, index=False)

        # Extract and save the last 480,000 rows
        df[480000:720000].to_csv(output_file_path3, index=False)
                # Extract and save the first 480,000 rows
        df[720000:960000].to_csv(output_file_path4, index=False)

        # Extract and save the next 480,000 rows
        df[960000:1200000].to_csv(output_file_path5, index=False)

        # Extract and save the last 480,000 rows
        df[1200000:1440000].to_csv(output_file_path6, index=False)

        #print(f"Saved {output_file_path1} (1 to 480,000 rows), {output_file_path2} (480,001 to 960,000 rows), and {output_file_path3} (960,001 to 1,440,000 rows) successfully.")
