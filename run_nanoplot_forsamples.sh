#!/bin/bash

input_dir="/mnt/nas2/raw_sequence_data/nanopore/20250522_MIN/combined_barcodes"
output_base="nanoplot_reports"

mkdir -p "$output_base"

for fastq_file in "$input_dir"/*.fastq; do
    sample_name=$(basename "$fastq_file" .fastq)
    output_dir="$output_base/$sample_name"

    echo "Running NanoPlot for $sample_name"
    NanoPlot --fastq "$fastq_file" -o "$output_dir" --threads 4
done

