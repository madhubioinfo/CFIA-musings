#!/bin/bash

input_dir="/mnt/nas2/raw_sequence_data/nanopore/20250530_MIN"
output_base="nanoplot_reports"

mkdir -p "$output_base"

shopt -s nullglob  # ensures *.fastq.gz expands to empty if no matches

for fastq_file in "$input_dir"/*.fastq.gz; do
    sample_name=$(basename "$fastq_file" .fastq.gz)
    output_dir="$output_base/$sample_name"
    
    echo "Running NanoPlot for $sample_name"
    NanoPlot --fastq "$fastq_file" -o "$output_dir" --threads 4
done
