# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 10:02:58 2023

@author: Nitin Kumar

columns should be named as Current [A] and Voltage [V]
File name's last three dgits will be used to name the column

"""

import pandas as pd
import os

# Specify the folder where your CSV files are located
folder_path = r"E:\Personal Data\Nbo2\2024\4 Apr\15\Data just before transiton"

# Create an empty list to store DataFrames
dfs = []

# Loop through all CSV files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path, skiprows=8)
        
        # Extract the columns (adjust column names as needed)
        if "Reading" in df.columns and "Value" in df.columns:
            df = df[["Reading", "Value"]]
            
            # Rename columns with "I" and "V" followed by the last three digits of the file name
            file_name_without_extension = os.path.splitext(filename)[0]
            last_three_digits = file_name_without_extension[-3:]
            df.columns = ["I" + last_three_digits, "V" + last_three_digits]
            
            # Append the DataFrame to the list
            dfs.append(df)

# Concatenate all DataFrames in the list
combined_data = pd.concat(dfs, axis=1)    
# Specify the path for the new CSV file to be created
output_csv_path = r"F:\NbO2\50 nm\D4\IV\IV Before nosie\combined_data.csv"

# Save the combined data to a new CSV file
combined_data.to_csv(output_csv_path, index=False)

print(f"Combined data saved to {output_csv_path}")
