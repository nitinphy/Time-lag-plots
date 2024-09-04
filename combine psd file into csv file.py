# -*- coding: utf-8 -*-
"""
Created on Thu May 16 09:41:50 2024

@author: sndkp
"""

import os
import csv

def extract_data_from_files(folder_path, file_numbers):
    data_dict = {}
    for num in file_numbers:
        filename = f"psd_{num:03d}.txt"
        filepath = os.path.join(folder_path, filename)
        if os.path.exists(filepath):
            data_dict[num] = {'f': [], 'sx': []}
            with open(filepath, 'r') as file:
                for line in file:
                    columns = line.strip().split()
                    if len(columns) >= 2:
                        f_value = columns[0]
                        sx_value = columns[1]
                        data_dict[num]['f'].append(f_value)
                        data_dict[num]['sx'].append(sx_value)
        else:
            print(f"File {filename} not found.")
    
    return data_dict

def save_to_csv(data, folder_path):
    csv_filename = "output.csv"
    csv_filepath = os.path.join(folder_path, csv_filename)
    with open(csv_filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        headers = []
        for key in data:
            headers.extend([f'f_{key:03d}', f'sx_{key:03d}'])
        writer.writerow(headers)  # Write header
        num_rows = max(len(data[key]['f']) for key in data)
        for i in range(num_rows):
            row = []
            for key in data:
                if i < len(data[key]['f']):
                    row.extend([data[key]['f'][i], data[key]['sx'][i]])
                else:
                    row.extend(['', ''])
            writer.writerow(row)

if __name__ == "__main__":
    folder_path = r"F:\NbO2 manuscript\Data\325 current driven noise\Noise\16 Min\psd_file"
    file_numbers = range(1, 1000, 3)
    data = extract_data_from_files(folder_path, file_numbers)
    save_to_csv(data, folder_path)
    print("CSV file saved successfully.")
