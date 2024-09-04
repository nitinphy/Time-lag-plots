# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 15:47:20 2023

@author: sndkp
"""
import os
import numpy as np
import matplotlib.pyplot as plt

# Specify the folder path and file name separately
folder_path = r"X:\Personal Data\Nbo2\09 Sept\10012023\226\Noise\16min\positive\psd_file"
path_csv = r"X:\Personal Data\Nbo2\09 Sept\10012023\226\Noise\16min\positive\psd_file\new"

filenumber = 1
for filenumber in range(1,15):
    te = str(filenumber).zfill(3)
    
    file_format = 'psd_' + te + '.txt'
    
    file_list = os.listdir(folder_path)
    
    # Construct the full file path using os.path.join
    full_file_path = os.path.join(folder_path, file_format)
    
    # Read data from the text file
    data = np.genfromtxt(full_file_path, delimiter='\t', skip_header=1)
    
    # Assuming your file has two columns, Sx and f, in that order
    Sx = data[:, 0]
    f = data[:, 1]
    
    # Calculate f * Sx
    f_times_Sx = f * Sx
    
    plt.loglog(Sx, f_times_Sx, marker='o', markersize=5, color='b', label='Data Points')
    plt.xlabel('f')
    plt.ylabel('f * Sx')
    plt.title('Log-Log Plot: f * Sx vs. f')
    plt.grid(True)
    plt.show()

    # Show the plot
    #plt.legend()
 
    plot_file_name = f'IV_Plot_{filenumber}.png'
    plot_file_path = os.path.join(path_csv, plot_file_name)
    plt.savefig(plot_file_path, bbox_inches='tight', dpi=300)
    plt.close()