# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:52:30 2023

@author: sndkp
"""

import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to extract the 4-digit number from the file name
def extract_number(file_name):
    match = re.search(r'\d{4}', file_name)
    if match:
        return int(match.group())
    else:
        return None

# Directory containing the IV files
directory = r"E:\Personal Data\Nbo2\12 dec\12262023\329\IV Stability\IV1"

# List to store dataframes and numbers
dfs = []
numbers = []


# Read each file and extract data
for filename in os.listdir(directory):
    if filename.startswith("IV_") and filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        number = extract_number(filename)

        if number is not None:
            df = pd.read_csv(file_path)
            dfs.append(df)
            numbers.append(number)

# Create a single dataframe
merged_df = pd.concat(dfs, keys=numbers, names=['Number'])

# Plotting with lines connecting the points
fig, ax = plt.subplots()

# Scatter plot
scatter = ax.scatter(x=merged_df['Value'], y=merged_df['Reading'], c=merged_df.index.get_level_values('Number'), cmap='gist_rainbow', marker='o', s=10)

# Connect points with lines
for number in numbers:
    subset_df = merged_df.xs(key=number, level='Number')
    ax.plot(subset_df['Value'], subset_df['Reading'], marker='_', linestyle='-', color=scatter.cmap(scatter.norm(number)))

# Colorbar
cbar = fig.colorbar(scatter)
cbar.set_label('#Run')

# Customize plot labels and title
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
#plt.title('IV Curves with Colorbar and Lines Connecting Points')

# Show the plot
plt.show()