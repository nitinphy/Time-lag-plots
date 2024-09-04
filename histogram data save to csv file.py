import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Specify the directory containing the CSV files
directory = r'F:\APS march meeting 2024\Data\325 current driven noise\Noise\16 Min'

# Initialize an empty DataFrame to store data for CSV
csv_df = pd.DataFrame()

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.startswith("it_") and filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)

        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path, skiprows=0, low_memory=False, encoding_errors="ignore", on_bad_lines='skip')

        # Get the value from the third row of the "Value" column
        value = df.loc[2, 'Value']  # Indexing starts from 0, so the third row is at index 2

        # Calculate minimum, maximum, and average of the 'Reading' column
        min_reading = df['Reading'].min()
        max_reading = df['Reading'].max()
        avg_reading = df['Reading'].mean()

        # Print statistics
        print(f"File: {filename}")
        print("Minimum Reading:", min_reading)
        print("Maximum Reading:", max_reading)
        print("Average Reading:", avg_reading)

        # Calculate the differences
        diff_min_avg = abs(min_reading - avg_reading)
        diff_max_avg = abs(max_reading - avg_reading)

        # Determine the x-axis limit
        x_limit = max(diff_min_avg, diff_max_avg)

        # Create a histogram plot
        hist_values, bin_edges = np.histogram(df['Reading'], bins=100, range=(avg_reading - x_limit, avg_reading + x_limit))
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2  # Calculate bin centers

        # Store bin centers and counts in a DataFrame with multi-index
        file_data = pd.DataFrame({f'Bin Center_{value}': bin_centers, f'Count_{value}': hist_values})
        
        # Concatenate data to the main DataFrame
        csv_df = pd.concat([csv_df, file_data], axis=1)

        # Plot histogram
        plt.bar(bin_centers, hist_values, width=bin_edges[1] - bin_edges[0], color='skyblue', edgecolor='black')
        plt.xlabel('V (V)')
        plt.ylabel('Count')
        plt.title('Histogram of Reading Values')
        plt.axvline(x=avg_reading, color='red', linestyle='--', label='Mean')

        # Save the plot in the same folder with the same filename
        plot_filename = os.path.splitext(filename)[0] + '_histogram.png'
        plot_path = os.path.join(directory, plot_filename)
        plt.savefig(plot_path)
        plt.close()  # Close the plot to free memory

        print(f"Plot saved as: {plot_filename}")

# Save the DataFrame to a CSV file in the same folder
csv_filename = os.path.join(directory, 'bin_average_readings.csv')
csv_df.to_csv(csv_filename)

print(f"CSV file with bin average readings saved as: {csv_filename}")
