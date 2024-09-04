# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:17:44 2024

@author: sndkp
"""
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

# Specify the Excel file path
excel_file = 'F:/NbO2 manuscript/Slope data.xlsx'

# Read the data from the single sheet
df = pd.read_excel(excel_file)

# Fill NaN values with the mean of each column
df_cleaned = df.fillna(df.mean())

# Create a box and whisker plot for S1, S2, and S3 with different colors
plt.figure(figsize=(8, 6))

# Customize the box colors
box_colors = ['black', 'red', 'blue']
bp = plt.boxplot([df_cleaned['S1'], df_cleaned['S2'], df_cleaned['S3']], labels=['Before transitions', 'Around Transitions', 'After transitions'], patch_artist=True)

# Set individual box colors
for box, color in zip(bp['boxes'], box_colors):
    box.set(facecolor=color)

plt.title(r"Value of $\alpha$ from 5 samples")
#plt.xlabel("Columns")
plt.ylabel(r"$\alpha$")

plt.show()

