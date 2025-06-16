!/bin/bash

# Set working path (change to your actual base directory if needed)
base_dir="."

# Create output directory
output_dir="combined_barcodes"
mkdir -p "$output_dir"

# Loop through all barcode fastq files
find "$base_dir"/dir_*_dorado_demux -type f -name "*barcode*.fastq" | while read -r file; do
    # Extract barcode name from filename
    barcode=$(basename "$file" | grep -o "barcode[0-9]\{2\}")

    # Concatenate file content into one file per barcode
    cat "$file" >> "$output_dir/${barcode}.fastq"
done

