#!/bin/bash

# Directory containing the files
input_directory="/mnt/nas/users/madhu/poresippr_db_recent_minimap2_cdhit/stxdb_98/"
output_directory="/mnt/nas/users/madhu/poresippr_db_recent_minimap2_cdhit/stxdb_98/output_directory"

# Create the output directory if it doesn't exist
mkdir -p "$output_directory"

# Loop over all files in the input directory
for file in "$input_directory"/*.csv; do
  # Extract filename
  filename=$(basename "$file")
 
  # Remove the 3rd and 4th columns and save to the output directory
  awk '{print $1, $2}' "$file" > "$output_directory/$filename"
done
