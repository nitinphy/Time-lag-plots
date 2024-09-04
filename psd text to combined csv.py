# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:21:09 2023

@author: sndkp
"""

import os
import pandas as pd

# Specify the folder containing your text files
folder_path = r"X:\Personal Data\Nbo2\09 Sept\09262023\224\Noise\16min\psd_file"

# Initialize an empty DataFrame to store the data
result_df = pd.DataFrame()

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):  # Assuming your files have a .txt extension
        file_path = os.path.join(folder_path, filename)
        
        # Extract the last three digits of the file name
        column_name = filename[-7:-4]  # Adjust the indexing based on your file naming convention
        
        # Read the text file into a DataFrame
        df = pd.read_csv(file_path, sep='\t')  # Adjust the separator if necessary
        
        # Rename the 'f' and 'sx' columns with the extracted column_name
        df = df.rename(columns={'f': f'f_{column_name}', 'sx': f'sx_{column_name}'})
        
        # Concatenate the data to the result DataFrame
        result_df = pd.concat([result_df, df], axis=1)

# Save the result DataFrame to a CSV file in the same folder
output_file_path = os.path.join(folder_path, 'combined_data.csv')
result_df.to_csv(output_file_path, index=False)

print(f'Data saved to {output_file_path}')
