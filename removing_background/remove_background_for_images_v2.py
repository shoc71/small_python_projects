# the following installations are required for this background to run
# pip install os 
# pip install opencv2-python
# pip install numpy
# pip install tqdm
import os
import cv2
import numpy as np
from tqdm import tqdm

# Path to the folder containing images
input_folder = "input_folder"

# Path to the folder to save the processed images
output_folder = "output_folder"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get a list of all image files in the input folder
image_files = [file for file in os.listdir(input_folder) if file.endswith((".png", ".jpg", ".jpeg", ".gif"))]

# Process the images
for image_file in tqdm(image_files, desc="Processing Images", unit="image"):
    # Load the image with alpha channel (transparency)
    image = cv2.imread(os.path.join(input_folder, image_file), cv2.IMREAD_UNCHANGED)
    
    # Extract the alpha channel
    alpha_channel = image[:, :, 3]
    
    # Create a mask by thresholding the alpha channel
    _, mask = cv2.threshold(alpha_channel, 0, 255, cv2.THRESH_BINARY)
    
    # Apply the mask to the image
    image = cv2.bitwise_and(image, image, mask=mask)
    
    # Save the processed image with transparent background
    cv2.imwrite(os.path.join(output_folder, image_file), image)

# Process completed
print("Processing completed.")
