# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 12:30:28 2024

@author: sndkp
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
file_path = r'F:\APS march meeting 2024\Data\325 current driven noise\Noise\16 Min\bin_average_avg_reading.csv'
df = pd.read_csv(file_path)

# Select the three columns
df = df[['I', 'V', 'N']]

# Ensure no negative or zero values in 'N' column
df = df[df['N'] > 100]
df = df[df['I'] > 0.000009]

# Sort the dataframe by 'I' and 'V'
df.sort_values(by=['I', 'V'], inplace=True)

# Use pivot_table to handle duplicate entries
pivot_df = df.pivot_table(index='I', columns='V', values='N', aggfunc=np.mean)

# Define the grid
xi = pivot_df.index.values
yi = pivot_df.columns.values
zi = pivot_df.values

# Create meshgrid
X, Y = np.meshgrid(xi[:-1], yi[:-1])

# Create the plot
plt.pcolormesh(X, Y, zi[:-1, :-1], shading='auto', cmap='viridis')




plt.colorbar(label='N (log scale)')
plt.xlabel('I')
plt.ylabel('V')
plt.title('pcolormesh Plot with Logarithmic Color Scale')
plt.show()
