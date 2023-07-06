#!/bin/bash

# Path to Hisat2 executable
hisat2="/usr/bin/hisat2"

# Path to the reference genome index
index="/home/madhu/assembly_2"

# Directory containing the paired-end read files
input_dir="/home/madhu/thesis"

# Output directory for the BAM files
output_dir="/home/madhu/thesis"

# Iterate over the paired-end read files
for file in "$input_dir"/*_1.fastq; do
    # Get the base filename (without the extension)
    base=$(basename "$file" _1.fastq)

    # Define the input files
    read1="$input_dir/$base"_1.fastq
    read2="$input_dir/$base"_2.fastq

    # Define the output file
    output="$output_dir/$base.sam"

    # Run Hisat2 alignment
    "$hisat2" -p 15 -x "$index" -1 "$read1" -2 "$read2" -S "$output"  --summary-file "$output_summary.txt"

    # Convert SAM to BAM
   samtools view -@ 15 -bS "$output" > "$output_dir/$base.bam"

    # Sort the BAM file
    samtools sort -@ 15 "$output_dir/$base.bam" -o "$output_dir/$base.sorted.bam"

    # Index the sorted BAM file
#    samtools index "$output_dir/$base.sorted.bam"

    # Remove the intermediate BAM and SAM files
    rm "$output" "$output_dir/$base.bam"
done
