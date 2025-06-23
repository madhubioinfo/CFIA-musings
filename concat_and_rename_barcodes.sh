#!/bin/bash

###############################################################################
# concat_and_rename_barcodes.sh
#
# This script concatenates all barcode fastq files from subdirectories named
# dir_*_dorado_demux into one file per barcode in the specified output directory.
# Then, it renames the concatenated files according to a provided mapping file,
# and finally compresses all resulting .fastq files using gzip.
#
# Usage:
#   ./concat_and_rename_barcodes.sh /path/to/output_directory mapping_file.txt
#
# Arguments:
#   output_directory  Directory where concatenated, renamed, and compressed files
#                     will be saved.
#   mapping_file      A tab-delimited file with two columns:
#                     old_barcode_name new_barcode_name
#
# Example mapping file content:
#   barcode01 2025-MIN-0001
#   barcode02 2025-MIN-0002
#
###############################################################################

# Check if the user provided two arguments
if [ $# -ne 2 ]; then
    echo "Usage: $0 /path/to/output_directory mapping_file"
    exit 1
fi

output_dir="$1"
mapping_file="$2"

mkdir -p "$output_dir"

# Set base directory (modify if needed)
base_dir="."

# Step 1: Concatenate all barcode fastq files into one file per barcode
find "$base_dir"/dir_*_dorado_demux -type f -name "*barcode*.fastq" | while read -r file; do
    # Extract barcode name from filename (e.g. barcode01)
    barcode=$(basename "$file" | grep -o "barcode[0-9]\{2\}")

    # Append content to the corresponding output file in output_dir
    cat "$file" >> "$output_dir/${barcode}.fastq"
done

# Step 2: Rename concatenated files according to mapping file
while read -r oldname newname; do
    old_file="${output_dir}/${oldname}.fastq"
    new_file="${output_dir}/${newname}.fastq"
    if [ -f "$old_file" ]; then
        mv "$old_file" "$new_file"
        echo "Renamed $old_file → $new_file"
    else
        echo "Warning: $old_file not found"
    fi
done < "$mapping_file"

# Step 3: Compress all .fastq files in the output directory with gzip
echo "Compressing all .fastq files in $output_dir ..."
gzip -f "$output_dir"/*.fastq

echo "Done."

