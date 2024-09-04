# -*- coding: utf-8 -*-
"""
Created on Fri May  5 12:49:01 2023

@author: sndkp
"""
import matplotlib as mpl
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.weight'] = 'bold'
mpl.rcParams['axes.linewidth'] = 2
mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18
mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['axes.titlesize'] = 16
# set the path to the directory containing the CSV files
path = r"X:\Personal Data\V2O5\2023\JUne\06292023\IV D1\IV"

# get a list of all CSV files in the directory
csv_files = glob.glob(os.path.join(path, '*.csv'))

# plot IV curves
for file in csv_files:
    # check if the first 2 letters of the file name are 'IV'
    if os.path.basename(file)[:2] == 'IV':
        # get the temperature from the file name
        temperature = os.path.basename(file)[3:5]

        # get the file number from the file name
        file_number = os.path.basename(file).split('_')[-1].replace('.csv', '')

        # read the CSV file into a pandas DataFrame
        df = pd.read_csv(file)

        # extract column 5 (current) and save it to an array
        current_arra = df.iloc[:, 4].values* 1000

        # extract column 6 (voltage) and save it to an array
        voltage_arra = df.iloc[:, 5].values

        # plot the voltage vs. current for this file
        #plt.plot(voltage_arra, current_arra, '-o',label=f'R = {file_number} k\u03A9')
        plt.plot(voltage_arra, current_arra, '-o',label=f' {file_number} k ohm')
# add a legend and labels to the plot
plt.ylabel('I (mA)',fontweight='bold')
plt.xlabel('V (V)',fontweight='bold')
plt.title('Voltage driven IV with different series resistance')
plt.legend(frameon=False)
plt.tick_params(axis='both', direction='in',length=6,width=2)
device_name = 'Device = D1'
sample_name = 'Sample = G1'
plt.text(0.05, 0.9, f'T = {temperature} K\n{device_name}\n{sample_name}')
plt.savefig(os.path.join(path, 'IV_curves.png'), dpi=300, bbox_inches='tight')
plt.figure()
plt.show()

# plot VI curves
for file in csv_files:
    # check if the first 2 letters of the file name are 'VI'
    if os.path.basename(file)[:2] == 'VI':
        # get the temperature from the file name
        temperature = os.path.basename(file)[3:5]

        # get the file number from the file name
        file_number = os.path.basename(file).split('_')[-1].replace('.csv', '')

        # read the CSV file into a pandas DataFrame
        df = pd.read_csv(file)

        # extract column 5 (current) and save it to an array
        current_array = df.iloc[:, 5].values * 1000

        # extract column 6 (voltage) and save it to an array
        voltage_array = df.iloc[:, 4].values

        # plot the voltage vs. current for this file
        plt.plot(voltage_array, current_array,'-o', label=f'R = {file_number} k\u03A9')

# add a legend and labels to the plot
plt.ylabel('I (mA)',fontweight='bold')
plt.xlabel('V (V)',fontweight='bold')
plt.title('Current driven IV with different series resistance')
plt.tick_params(axis='both', direction='in',length=6,width=2)
device_name = 'Device = DC'
sample_name = 'Sample = G1'
plt.text(0.05, 0.9, f'T = {temperature} K\n{device_name}\n{sample_name}')
plt.legend(frameon=False)
plt.savefig(os.path.join(path, 'VI_curves.png'), dpi=300, bbox_inches='tight')
plt.show()
