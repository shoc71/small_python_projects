# the following installations are required for this background to run
# pip install os pillow tqdm
import os
from PIL import Image 
from tqdm import tqdm

# Path to the folder containing PNG images
input_folder = "input_folder"

# Path to the folder to save the processed images
output_folder = "output_folder"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get a list of all PNG files in the input folder
png_files = [file for file in os.listdir(input_folder) if file.endswith(".png")]

# Process the PNG images
for png_file in tqdm(png_files, desc="Processing PNGs", unit="image"):
    # Open the image
    image = Image.open(os.path.join(input_folder, png_file))
    
    # Convert the image to RGBA mode (with transparency)
    image = image.convert("RGBA")
    
    # Create a new image with transparent background
    transparent_image = Image.new("RGBA", image.size, (0, 0, 0, 0))
    
    # Iterate over each pixel and copy it to the new image, preserving transparency
    for x in range(image.width):
        for y in range(image.height):
            r, g, b, a = image.getpixel((x, y))
            transparent_image.putpixel((x, y), (r, g, b, a))
    
    # Save the processed image with transparent background
    transparent_image.save(os.path.join(output_folder, png_file))

# Process completed
print("Processing completed.")
