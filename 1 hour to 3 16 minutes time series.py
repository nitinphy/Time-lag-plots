import pandas as pd
import os

# Define the folder paths for input and output
input_folder = r"F:\Personal Data\Zif_8\Noise Run 6\Raw"
output_folder = r"F:\Personal Data\Zif_8\Noise Run 6\16 MIn"

# Loop over num values from start to END+1
for num in range(1, 39):
    # Specify the input CSV file name
    input_file = 'it_' + str(num).zfill(3) + '.csv'
    print(input_file)
    # Construct the full path to the input CSV file
    input_file_path = os.path.join(input_folder, input_file)

    # Check if the input CSV file exists
    if not os.path.isfile(input_file_path):
        print(f"File '{input_file_path}' not found.")
        continue  # Skip to the next iteration if the file doesn't exist

    # Read the CSV file
    try:
        df = pd.read_csv(input_file_path, skiprows=8, encoding="utf8", encoding_errors='ignore', on_bad_lines='skip', engine='python')
    except FileNotFoundError:
        print(f"File '{input_file_path}' not found.")
        continue  # Skip to the next iteration if there's an error reading the file

    # Get the total number of rows in the CSV file
    total_rows = len(df)

    # Specify the output file names
    number = num * 3 -2
    output_file1 = 'it_' + str(number).zfill(3) + '.csv'
    output_file2 = 'it_' + str(number + 1).zfill(3) + '.csv'
    output_file3 = 'it_' + str(number + 2).zfill(3) + '.csv'

    # Construct the full paths to the output CSV files
    output_file_path1 = os.path.join(output_folder, output_file1)
    output_file_path2 = os.path.join(output_folder, output_file2)
    output_file_path3 = os.path.join(output_folder, output_file3)
    print("saved till"+ output_file3)
    # Check if the specified rows are within the total number of rows
    if total_rows < 1440000:
        print(f"Error: The CSV file '{input_file}' does not contain 1,440,000 rows.")
    else:
        # Extract and save the first 480,000 rows
        df[0:480000].to_csv(output_file_path1, index=False)

        # Extract and save the next 480,000 rows
        df[480000:960000].to_csv(output_file_path2, index=False)

        # Extract and save the last 480,000 rows
        df[960000:1440000].to_csv(output_file_path3, index=False)

        #print(f"Saved {output_file_path1} (1 to 480,000 rows), {output_file_path2} (480,001 to 960,000 rows), and {output_file_path3} (960,001 to 1,440,000 rows) successfully.")
