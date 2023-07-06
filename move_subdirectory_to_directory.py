import os
import shutil

# Define the source directory containing the subdirectories
source_directory = "/home/malarm/Downloads/salmonella"

# Define the destination directory where the files will be moved
destination_directory = "/home/malarm/Downloads/test1"

# Iterate over the subdirectories
for root, _, files in os.walk(source_directory):
    for file_name in files:
        # Get the full path of the file
        file_path = os.path.join(root, file_name)

        # Move the file to the destination directory
        shutil.move(file_path, destination_directory)

        print(f"Moved {file_path} to {destination_directory}")

