# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 15:58:56 2024

@author: sndkp
"""
%matplotlib qt

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

# Your data (replace with your actual data)
temperature = [25, 50, 75, 100, 125]
voltage_up = [1.707623762,1.405049505,1.01980198,0.86980198,0.75]
voltage_down = [1.49970297, 1.192277228,0.747623762,0.65990099,0.63019802]
error_up = [0.01313664,0.15666464,0.001980198,0.001980198,0]
error_down = [0.002970297,0.033681125,0.00810189,0.000990099,0.001980198]

plt.figure(figsize=(11.5, 8))

# Calculate bottom and top values for each bar
bottom_values = np.array(voltage_down) - np.array(error_down)
top_values = np.array(voltage_up) + np.array(error_up)

# Use the "rainbow" colormap for colors
colors = plt.cm.rainbow(np.linspace(0, 1, len(temperature)))

# Create a bar plot with the "rainbow" colormap
bars = plt.bar(temperature, top_values - bottom_values, bottom=bottom_values, color=colors, alpha=0.7, width=10)

# Add error bars based on the error data
for bar, top, bottom, error_up, error_down, color in zip(bars, top_values, bottom_values, error_up, error_down, colors):
    plt.plot([bar.get_x() + bar.get_width() / 2, bar.get_x() + bar.get_width() / 2], [bottom, top], color=color, linewidth=3)
    plt.errorbar(bar.get_x() + bar.get_width() / 2, top, yerr=error_up, fmt='-', color=color, linewidth=3, capsize=1, lolims=True)
    plt.errorbar(bar.get_x() + bar.get_width() / 2, bottom, yerr=error_down, fmt='-', color=color, linewidth=3, capsize=1, uplims=True)
    
    # Add horizontal lines at the ends of the error bars
    plt.hlines(y=top+error_up, xmin=bar.get_x(), xmax=bar.get_x() + bar.get_width(), color=color, linewidth=3)
    plt.hlines(y=bottom-error_down, xmin=bar.get_x(), xmax=bar.get_x() + bar.get_width(), color=color, linewidth=3)

# Set the font to Times New Roman, size to 24, and weight to bold
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 28
plt.rcParams["font.weight"] = "bold"

# Set the width of the axes
plt.gca().spines['left'].set_linewidth(2)
plt.gca().spines['bottom'].set_linewidth(2)
plt.gca().spines['right'].set_linewidth(2)
plt.gca().spines['top'].set_linewidth(2)

# Add minor ticks to the y-axis
plt.gca().yaxis.set_minor_locator(AutoMinorLocator())

# Set the direction and size of the ticks
plt.tick_params(axis='y', which='major', direction='in', pad=15, width=2, length=10)
plt.tick_params(axis='y', which='minor', direction='in', pad=15, width=2, length=5)

# Remove the x-axis labels
plt.gca().xaxis.set_ticklabels([])

for i, temp in enumerate(temperature):
    plt.bar(0, 0, color=colors[i], label=str(temp) + " °C")

# Add the legend with title, best location and no frame
legend = plt.legend(title="Temperature", loc="best", frameon=False)

# Set the font weight of the legend text and title to normal
plt.setp(legend.get_texts(), fontweight='normal')
plt.setp(legend.get_title(), fontweight='normal')

# Set the limits of the x-axis and y-axis
plt.xlim(15, 135)
plt.ylim(0.3, 2.4)

# Set the x-axis ticks to match the temperatures shown in the legend
plt.xticks(temperature, [str(temp) + "" for temp in temperature])
# Customize the plot
plt.ylabel('V (V)',fontweight='bold')
#plt.xlabel('T (°C)',fontweight='bold')

# Adjust the layout
plt.tight_layout()

# Save the figure
plt.savefig(r'F:\APS march meeting 2024\Data\Hyst box plot\D81 hyst box plot.png', dpi=600)

# Display the plot
plt.show()
