#!/bin/bash

# Define the directory containing your fastq files
fastq_dir="/mnt/nas/users/madhu/nanopore_modelling/OLC0679_coverage_fastq"

# Define the reference file for minimap2
reference="/mnt/nas/users/madhu/nanopore_modelling/all_gdcs.fasta"

# Define the output directory for your bam and csv files
output_dir="/mnt/nas/users/madhu/nanopore_modelling/OLC0679_coverage_bam"

# Ensure the output directory exists
mkdir -p $output_dir

# Loop over each fastq file in the directory
for fastq_file in $fastq_dir/*.fastq
do
    # Extract the base name of the fastq file (without path and extension)
    base_name=$(basename $fastq_file .fastq)

    # Define the output bam file name
    bam_file="$output_dir/${base_name}.bam"

    # Run minimap2
    minimap2 -ax map-ont $reference $fastq_file | samtools view -@ 5 -bS - | samtools sort -o $bam_file -

    # Define the output csv file name
    # shellcheck disable=SC1073
    csv_file="$output_dir/${base_name}_coverage.csv"

    # Run samtools coverage and sort the output
    samtools coverage $bam_file | cut -f 1,4 | awk '$2 > 0' | sort -rnk 2,2 > $csv_file
done