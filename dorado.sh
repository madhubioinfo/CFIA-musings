#!/bin/bash

# Set the base directory and model path
base_dir="/home/mathum/230602_MN26299_fast5/fast5_pass"

# Automatically detect barcode directories
barcode_dirs=("$base_dir"/barcode*)

# Loop through each barcode directory
for barcode_dir in "${barcode_dirs[@]}"; do
    if [[ -d "$barcode_dir" ]]; then
        barcode_name=$(basename "$barcode_dir")
        echo "Processing $barcode_name..."
        /home/mathum/dorado-0.3.4-linux-x64/bin/dorado basecaller --batchsize 50 --emit-fastq --device "cuda:all" /home/mathum/dorado-0.3.4-linux-x64/dna_r10.4.1_e8.2_260bps_sup_v3.5.2 "$barcode_dir" > "$barcode_dir/$barcode_name.fastq"
    fi
done

echo "Basecalling complete for all barcode directories."

