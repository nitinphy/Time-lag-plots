# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 19:39:56 2023

@author: sndkp
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

# Folder containing the CSV files
folder_path = r"F:\Personal Data\NbO2\Size dependent study\Line 1\D11 or D10"
# Lists to store resistance values, max current values, and corresponding file numbers for both cases
resistance_values_1 = []
resistance_values_2 = []
max_current_values = []
file_numbers = []

# Loop through CSV files in the folder
for file_name in os.listdir(folder_path):
    
    if file_name.endswith(".csv"):
        file_path = os.path.join(folder_path, file_name)
        # Extract file number from the file name (assuming file name format: IV_XXX.csv)
        file_number = int(file_name.split("_")[1].split(".")[0])
        file_numbers.append(file_number)
        
        # Read CSV file using pandas
        df = pd.read_csv(file_path, skiprows=8)
        # Filter rows where Voltage is approximately 0.1 (assuming there might be slight variations)
        filtered_df = df[(df["Value"] >= 0.099) & (df["Value"] <= 0.101)]
        # Calculate resistance (R = V/I) for both cases
        
        # Store the maximum current value before filtering
        max_current_before_filtering = df["Reading"].max()*1000
        max_current_values.append(max_current_before_filtering)
        
        if not filtered_df.empty:
            voltage_1 = filtered_df["Value"].iloc[0]
            current_1 = filtered_df["Reading"].iloc[0]
            resistance_1 = voltage_1 / current_1
            resistance_values_1.append(resistance_1)
            # Check if there's a second row with voltage approximately 0.1
            if len(filtered_df) > 1:
                voltage_2 = filtered_df["Value"].iloc[1]
                current_2 = filtered_df["Reading"].iloc[1]
                resistance_2 = voltage_2 / current_2
                resistance_values_2.append(resistance_2)
            else:
                resistance_values_2.append(None)  # Handle cases where second voltage = 0.1 not found
            # Store maximum current value in max_current_values array
           
        else:
            resistance_values_1.append(None)
            resistance_values_2.append(None)
            max_current_values.append(None)

# Create a DataFrame to store file numbers and resistance values
resistance_data = pd.DataFrame({'FileNumber': file_numbers, 'Resistance1': resistance_values_1, 'Resistance2': resistance_values_2})

# Define the path where you want to save the CSV file
csv_output_path = r"F:\Personal Data\NbO2\Size dependent study\Line 1\D11 or D10\resistance_data.csv"

# Save the DataFrame to a CSV file
resistance_data.to_csv(csv_output_path, index=False)

# Print a message to confirm that the data has been saved
print(f"Resistance data saved to {csv_output_path}")

set_size = 3  # You can adjust this value as needed

# Calculate the number of sets based on the set size
num_sets = (len(file_numbers) + set_size-1) // set_size

# Define the start and end indices for each set
set_ranges = [(i * set_size, min((i + 1) * set_size, len(file_numbers))) for i in range(num_sets)]

# Plot the resistance values for both cases as functions of file number
plt.figure(figsize=(10, 6))

# Plot the resistance values for both cases as functions of file number
plt.plot(file_numbers, resistance_values_1, marker='o', linestyle='', label="Up Resistance")
plt.plot(file_numbers, resistance_values_2, marker='o', linestyle='', label="Down Resistance")

# Add file numbers as labels on the points
# Define the maximum number of annotations to show and distribute
max_annotations = 100  # You can adjust this value as needed

# Calculate the step size to distribute annotations equally across the entire range
step_size = len(file_numbers) * 2 // max_annotations

annotation_indices = [i for i in range(0, len(file_numbers), step_size)]

annotation_counter = 0  # Counter for annotations added

for i, file_number in enumerate(file_numbers):
    if annotation_counter >= max_annotations:
        break  # Stop adding annotations once the maximum is reached
        
    if i in annotation_indices:
        if resistance_values_1[i] is not None:
            #plt.annotate(str(file_number), (file_number, resistance_values_1[i]), textcoords="offset points", xytext=(0, 10), ha='center')
            annotation_counter += 1
        
        if resistance_values_2[i] is not None:
            annotation_y = resistance_values_2[i] * 0.9
            #plt.annotate(str(file_number), (file_number, resistance_values_2[i]), textcoords="offset points", xytext=(0, -20), ha='center')
            annotation_counter += 1

plt.yscale('log')
plt.xlabel("#")
plt.ylabel("Resistance [Ohms]")
#plt.title("Resistance as a Function of File Number")
plt.legend()
# Find the maximum resistance value for determining the Y position of the text
max_resistance = max(max(resistance_values_1), max(resistance_values_2))

# Add background colors with text
# Adding Background Colors with Max Current Annotations
ax = plt.gca()  # Get the current Axes object
for set_index, (start_index, end_index) in enumerate(set_ranges):
    background_color = plt.cm.tab20(set_index % 20)
    
    # Calculate the middle file number for the current set
    middle_index = (start_index + end_index - 1) // 2
    middle_file_number = file_numbers[middle_index]
   
    
    # Find the corresponding row in the DataFrame and get the max current

    max_current = max_current_values[middle_file_number]

    
    x_center = (file_numbers[start_index] + file_numbers[end_index - 1]) / 2
    y_position = max_resistance * 1.1  # Adjust the factor as needed
    ax.axvspan(file_numbers[start_index], file_numbers[end_index - 1], color=background_color, alpha=0.2)
    
    # Add max current annotation just below the background region
    annotation_text = f"{max_current:.2f}"  # Format the max current value
    annotation_y = max_resistance * 0.9 # Adjust the Y position of the annotation
    plt.annotate(annotation_text, xy=(x_center, annotation_y), xytext=(0, -20), textcoords="offset points", ha='center')


plt.show()