# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:27:51 2024

@author: sndkp
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

# Specify the path to your CSV files
folder_path = r"F:\NbO2\50 nm\D4\IV\IV Before nosie"

# Get a list of all CSV files in the directory
csv_files = glob.glob(os.path.join(folder_path, 'IV_*.csv'))

# Create an empty DataFrame to store all results
all_results = pd.DataFrame()

# Process each file
for file_path in csv_files:
    data = pd.read_csv(file_path, skiprows=8)

    # Ensure 'Reading' and 'Value' columns exist
    if 'Reading' in data.columns and 'Value' in data.columns:
        # Calculate dI/dV
        data['dI/dV'] = np.gradient(data['Reading']) / np.gradient(data['Value'])

        # Extract file number from file name
        file_number = os.path.splitext(os.path.basename(file_path))[0][-3:]

        # Add dI/dV and V data to results DataFrame
        all_results['V'+file_number] = data['Value']
        all_results['dI/dV'+file_number] = data['dI/dV']

# Save all results to a new CSV file
all_results.to_csv(r"F:\NbO2\50 nm\D4\IV\IV Before nosie\All_dIdV.csv", index=False)
