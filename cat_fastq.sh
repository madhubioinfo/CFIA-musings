#!/bin/bash

# Check if the user provided an output directory
if [ -z "$1" ]; then
    echo "Usage: $0 /path/to/output_directory"
    exit 1
fi

# Use the provided output directory
output_dir="$1"
mkdir -p "$output_dir"

# Set base directory (modify if needed)
base_dir="."

# Loop through all barcode fastq files
find "$base_dir"/dir_*_dorado_demux -type f -name "*barcode*.fastq" | while read -r file; do
    # Extract barcode name from filename
    barcode=$(basename "$file" | grep -o "barcode[0-9]\{2\}")

    # Concatenate file content into one file per barcode
    cat "$file" >> "$output_dir/${barcode}.fastq"
done

