#!/bin/bash

# Directory containing your .pod5 files
SRC_DIR="./"  # change this if your files are in a different folder

# Destination base directory
DEST_BASE="./pod5_dirs"

mkdir -p "$DEST_BASE"

# Counter for the directory number
dir_num=1
# Counter for the files in the current directory
file_count=0

# Create the first directory
current_dir="$DEST_BASE/dir_$dir_num"
mkdir -p "$current_dir"

# Loop over all .pod5 files
for file in "$SRC_DIR"/*.pod5; do
  # If file_count reaches 50, increment dir_num and reset file_count, create new directory
  if [ "$file_count" -ge 20 ]; then
    dir_num=$((dir_num + 1))
    file_count=0
    current_dir="$DEST_BASE/dir_$dir_num"
    mkdir -p "$current_dir"
  fi
  
  # Move file to current directory
  mv "$file" "$current_dir/"
  
  # Increment file count
  file_count=$((file_count + 1))
done

echo "Done splitting files into directories."

