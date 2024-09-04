# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 21:48:58 2023

@author: sndkp
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 15:16:35 2023

@author: sndkp
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress  # Import linregress from scipy.stats
import os
# Input file path and name
input_file_path = r"C:\Users\sndkp\OneDrive\Desktop\PPT Prof\Normalized\Noise neg\16min\psd_file"  # Replace with the folder path
text_files = [file for file in os.listdir(input_file_path) if file.endswith(".txt")]
path_image = r"C:\Users\sndkp\OneDrive\Desktop\PPT Prof\Normalized\Noise neg\16min\psd_file\psd plots" 
path_csv= r"C:\Users\sndkp\OneDrive\Desktop\PPT Prof\Normalized\Noise neg\16min"
output_folder_path = os.path.join(input_file_path, "text_files")

for input_file_name in text_files:
    
    #input_file_name = '\psd_001.txt' # Replace with the file name
    file_parts = input_file_name.split('.')
    
    # Extract the part of the file name before the '.' and remove any non-numeric characters
    file_number = ''.join(filter(str.isdigit, file_parts[0]))
    
    # Convert the extracted number to an integer
    filenumber = int(file_number)
    file_path = os.path.join(input_file_path, input_file_name)
    
    
    # Read the CSV file into a DataFrame
    df = pd.read_table(file_path, delimiter='\t')  
    
    # Take the first 12 rows
    df1 = df.head(12)
    df2 = df[(df['f'] >= 0.1) & (df['f'] <= 0.4)]
    df3 = df[(df['f'] >= 0.4) & (df['f'] <= 0.7)]
    df4 = df[(df['f'] >= 0.7) & (df['f'] <= 1.0)]
    df5 = df[(df['f'] >= 1.0) & (df['f'] <= 4.0)]
    
    df1_length = len(df1)
    df2_length = len(df2)
    df3_length = len(df3)
    df4_length = len(df4)
    df5_length = len(df5)
    
    #print(df2)
    # Calculate the average of 'sx' and 'f' columns for every three rows
    averages = []
    for i in range(0, len(df1), 2):
        chunk = df1.iloc[i:i+1]
        avg_sx = chunk['Sx'].mean()
        avg_f = chunk['f'].mean()
        averages.append([avg_sx, avg_f])
        
    for i in range(0, len(df2), 4):
        chunk = df2.iloc[i:i+3]
        #print(chunk)
        avg_sx = chunk['Sx'].mean()
        #print(avg_sx)
        avg_f = chunk['f'].mean()
        averages.append([avg_sx, avg_f])
        #print(i)
        
    for i in range(0, len(df3), 6):
        chunk = df3.iloc[i:i+5]
        #print(chunk)
        avg_sx = chunk['Sx'].mean()
        #print(avg_sx)
        avg_f = chunk['f'].mean()
        averages.append([avg_sx, avg_f])
        #print(i)
        
    for i in range(0, len(df4), 8):
        chunk = df4.iloc[i:i+7]
        #print(chunk)
        avg_sx = chunk['Sx'].mean()
        #print(avg_sx)
        avg_f = chunk['f'].mean()
        averages.append([avg_sx, avg_f])
        #print(i)
        
    for i in range(0, len(df5), 20):
        chunk = df5.iloc[i:i+19]
        #print(chunk)
        avg_sx = chunk['Sx'].mean()
        #print(avg_sx)
        avg_f = chunk['f'].mean()
        averages.append([avg_sx, avg_f])
        #print(i)
        
    # Create a new DataFrame to store the averages
    result_df = pd.DataFrame(averages, columns=['Average_sx', 'Average_f'])
    
    a = '\psd_112_avg.csv'
    
    # Set the fitting range for the original data
    fit_min_original = 0.05  # Adjust this value as needed
    fit_max_original = 4.0   # Adjust this value as needed
    
    # Create a log-log scatter plot for the original data
    #plt.scatter(df['f'], df['Sx'], label='Original Data', s=100)
    plt.xscale('log')
    plt.yscale('log')
    
    # Fit a linear regression model to the original data within the specified range
    #mask_original = (df['f'] >= fit_min_original) & (df['f'] <= fit_max_original)
    #slope, intercept, r_value, p_value, std_err = linregress(np.log10(df['f'][mask_original]), np.log10(df['Sx'][mask_original]))
    
    # Calculate the fitted line for the specified range
    #fit_line_x = np.logspace(np.log10(fit_min_original), np.log10(fit_max_original), num=100)
    #fit_line_y = 10 ** (intercept + slope * np.log10(fit_line_x))
    
    # Print the slope and R-squared value on the graph
   # plt.text(0.02, 0.15, f'Original Data Slope: {slope:.2f}\nOriginal Data R-squared: {r_value**2:.2f}', transform=plt.gca().transAxes, color='blue', fontsize=8)
    
    # Plot the fitted line
    #plt.plot(fit_line_x, fit_line_y, color='blue', linestyle='--', label='Fitted Line (Original Data)')
    
    # Set the fitting range for the average data
    fit_min_average = fit_min_original  # Adjust this value as needed
    fit_max_average = fit_max_original  # Adjust this value as needed
    
    # Create a log-log scatter plot for the average data
    plt.scatter(result_df['Average_f'], result_df['Average_sx'], label='Average Data', c='red', s=100)
    
    # Fit a linear regression model to the average data within the specified range
    mask_average = (result_df['Average_f'] >= fit_min_average) & (result_df['Average_f'] <= fit_max_average)
    slope_avg, intercept_avg, r_value_avg, p_value_avg, std_err_avg = linregress(np.log10(result_df['Average_f'][mask_average]), np.log10(result_df['Average_sx'][mask_average]))
    
    # Calculate the fitted line for the specified range for average data
    fit_line_x_avg = np.logspace(np.log10(fit_min_average), np.log10(fit_max_average), num=100)
    fit_line_y_avg = 10 ** (intercept_avg + slope_avg * np.log10(fit_line_x_avg))
    
    # Print the slope and R-squared value on the graph for average data
    plt.text(0.02, 0.05, f'Average Data Slope: {slope_avg:.2f}\nAverage Data R-squared: {r_value_avg**2:.2f}', transform=plt.gca().transAxes, color='red', fontsize=8)
    print(slope_avg)
    # Plot the fitted line for average data
    plt.plot(fit_line_x_avg, fit_line_y_avg, color='red', linestyle='--', label='Fitted Line (Average Data)')
    
    plt.xlabel('Log Frequency (f)')
    plt.ylabel('Log Sx')
    #plt.legend()
    plt.xlim(0.03, 4)
    plt.show()
    plot_file_name = f'Avg_psd_{filenumber}.png'
    plot_file_path = os.path.join(path_image, plot_file_name)
    plt.savefig(plot_file_path, bbox_inches='tight', dpi=300)
    plt.close()
    
    # Specify the path to save the new CSV file
    output_csv_path = input_file_path+a
    
    # Save the new CSV file
    result_df.to_csv(output_csv_path, index=False)
    
    #print(f"Averages of 'sx' and 'f' columns saved to {output_csv_path}")
 
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder_path, exist_ok=True)
    
    for input_file_name in text_files:
          # Fit line data for the specified range
          
        fit_line_data = pd.DataFrame({f'fit_f_{filenumber}': fit_line_x_avg, f'fit_Sx_{filenumber}': fit_line_y_avg})
        
        # Save the averaged data to a text file with column names including the file number
        text_file_name = f'averaged_data_{filenumber}.txt'
        text_file_path = os.path.join(output_folder_path, text_file_name)
        
        with open(text_file_path, 'w') as text_file:
            text_file.write(f"Frequency_{filenumber} Sx_{filenumber}\n")
            for index, row in result_df.iterrows():
                text_file.write(f"{row['Average_f']} {row['Average_sx']}\n")
        
        # Save the fit line data to a separate text file
        fit_line_file_name = f'fit_line_data_{filenumber}.txt'
        fit_line_file_path = os.path.join(output_folder_path, fit_line_file_name)
        
        fit_line_data.to_csv(fit_line_file_path, sep='\t', index=False)
        
        #import xlwt
        #import xlrd
        #import xlutils
        #from xlwt import Workbook
    import xlrd
        #from xlrd import open_workbook
    from xlutils.copy import copy 
    from os.path import join
    
        
        # Workbook is created
        
        # directory for Noise Analysis Parameters
    path_NoiseData = path_csv
        
    rb=xlrd.open_workbook(join(path_NoiseData,'Noise_IV_Analysis.xls'))
    wb = copy(rb)
        
        
        
        # add_sheet is used to create sheet.
    sheet1 = wb.get_sheet('NoiseData')
        
    
    sheet1.write(0, 4, 'new slope 0.05_4')
        
    sheet1.write(int(filenumber), 4, slope_avg)
        #File name of excel file
    wb.save(join(path_NoiseData,'Noise_IV_Analysis.xls'))
        
    print('Data Saved')
