# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:11:58 2024

@author: sndkp
"""

import cv2
import os

# Path to the folder containing images
image_folder = r'F:\NbO2 manuscript\Data\Voltage driven time lag plots\Only 58'

# Video settings
video_name = 'output_video_file.mp4'
fps = 10  # Frames per second

# Get list of image files
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort()  # Ensure the images are in the correct order

# Get the dimensions of the first image
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# Initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # For mp4 output
video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

# Write each image to the video
for image in images:
    img_path = os.path.join(image_folder, image)
    video.write(cv2.imread(img_path))

# Release the video writer
video.release()
cv2.destroyAllWindows()

print(f"Video created successfully as {video_name}")
