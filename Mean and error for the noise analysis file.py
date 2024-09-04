# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:12:12 2024

@author: sndkp
"""

import pandas as pd

# Load the Excel file
file_path = r'F:\Personal Data\Zif_8\Noise Run 6\16 Min\Noise_IV_Analysis.xlsx'
output_file_path = r'F:\Personal Data\Zif_8\Noise Run 6\16 Min\mean_std_dev.xlsx'

try:
    df = pd.read_excel(file_path)

    # Group the data into sets of three consecutive file numbers
    grouped_data = df.groupby((df.index // 3) + 1)

    # Calculate the mean and standard deviation for each column
    mean_values = grouped_data.mean()
    std_dev_values = grouped_data.std()

    # Customize headers for mean and standard deviation
    mean_headers = [f"{col}_mean" for col in mean_values.columns]
    std_dev_headers = [f"{col}_std" for col in std_dev_values.columns]

    # Assign customized headers to mean and standard deviation dataframes
    mean_values.columns = mean_headers
    std_dev_values.columns = std_dev_headers

    # Save the mean and standard deviation data to a new Excel file
    with pd.ExcelWriter(output_file_path) as writer:
        mean_values.to_excel(writer, sheet_name='Mean Values')
        std_dev_values.to_excel(writer, sheet_name='Standard Deviation Values')
    
    print(f"Mean and standard deviation values have been saved to {output_file_path}")

except Exception as e:
    print(f"An error occurred: {e}")
