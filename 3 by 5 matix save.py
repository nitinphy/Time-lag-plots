# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:59:52 2024

@author: sndkp
"""

import os
from PIL import Image

# Define the directory containing the images
image_directory = r'F:\Personal Data\Zif_8\Noise Run 1\16 Min\text_file'

# Get a list of all .png files in the directory
image_files = [f for f in os.listdir(image_directory) if f.endswith('.png')]
image_files.sort()  # Sort to ensure correct order

# Count the number of .png files
file_count = len(image_files)

# Calculate set_count
set_count = file_count / 3

# Check if the number of files is divisible by 3
if file_count % 3 != 0:
    print("Something is missing")
else:
    # Define the dimensions of the page
    columns, rows = 5, 3  # 5 columns and 3 rows
    images_per_page = columns * rows

    # Get the dimensions of the first image to set the size of each cell
    sample_image = Image.open(os.path.join(image_directory, image_files[0]))
    img_width, img_height = sample_image.size

    # Create pages of 3x5 matrix of images
    page_number = 1
    for i in range(0, file_count, images_per_page):
        # Create a new blank image for the page
        page = Image.new('RGB', (columns * img_width, rows * img_height))

        for col in range(columns):
            for row in range(rows):
                index = i + col * rows + row
                if index < file_count:
                    img = Image.open(os.path.join(image_directory, image_files[index]))
                    page.paste(img, (col * img_width, row * img_height))
        
        # Save the page
        page.save(os.path.join(image_directory, f'page_{page_number}.png'), quality=95)
        page_number += 1

    print(f"Successfully created {page_number - 1} pages.")
