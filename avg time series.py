# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:49:39 2023

@author: sndkp
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the folder path
folder_path = r"X:\Personal Data\Nbo2\09 Sept\10012023\226\Noise\16min\Negative\time series"

# Create an empty DataFrame to store the data
result_df = pd.DataFrame()

# Loop through all CSV files in the folder
for filename in os.listdir(folder_path):
    if filename.startswith("it_"):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)

        # Read the CSV file into a DataFrame, skipping the first 8 rows
        df = pd.read_csv(file_path, skiprows=0)

        # Calculate the average of the 'Reading' column
        avg_reading = df['Reading'].mean()

        # Subtract the average from the 'Reading' column
        df['Reading'] -= avg_reading
        # Divide the 'Reading' column by the average
        
        df['Reading'] /= avg_reading  # This line was added

        # Extract the last three digits from the filename
        file_suffix = filename[-7:-4]

        # Rename the columns for the DataFrame
        df.rename(columns={'Reading': f'I_{file_suffix}', 'Relative Time': f'T_{file_suffix}'}, inplace=True)

        # Select and append only the 'I_XXX' and 'T_XXX' columns to the result DataFrame
        result_df = pd.concat([result_df, df[['T_' + file_suffix, 'I_' + file_suffix]]], axis=1)

# Save the combined DataFrame with only the selected columns to a CSV file
combined_csv_name = 'combined_data.csv'
combined_csv_path = os.path.join(folder_path, combined_csv_name)
result_df.to_csv(combined_csv_path, index=False)

# Print a message indicating the successful saving of the combined CSV file
print(f"Combined data saved as {combined_csv_path}")
