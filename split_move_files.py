import os
import shutil

# Define the source directory containing the FASTA files
source_directory = "/home/malarm/Downloads/genomes"

# Define the destination directory where the subdirectories will be created
destination_directory = "/home/malarm/Downloads/salmonella"

# Define the number of files per subdirectory
files_per_subdirectory = 100000

# Get a list of all files in the source directory
files = os.listdir(source_directory)

# Create subdirectories and move files
subdirectory_count = len(files) // files_per_subdirectory + 1
for i in range(subdirectory_count):
    # Create a subdirectory
    subdirectory_name = f"subdirectory_{i + 1}"
    subdirectory_path = os.path.join(destination_directory, subdirectory_name)
    os.makedirs(subdirectory_path, exist_ok=True)

    # Determine the range of files to move to this subdirectory
    start_index = i * files_per_subdirectory
    end_index = (i + 1) * files_per_subdirectory

    # Move files to the subdirectory
    for file_name in files[start_index:end_index]:
        file_path = os.path.join(source_directory, file_name)
        shutil.move(file_path, subdirectory_path)

    print(f"Moved {end_index - start_index} files to {subdirectory_name}")

