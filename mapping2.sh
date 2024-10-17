#!/bin/bash

# Define variables
fasta_file="/mnt/nas/users/madhu/poresippr_db_recent_minimap2_cdhit/stxdb_98.fasta"
fastq_dir="/mnt/nas/users/madhu/poresippr_db_recent_minimap2_cdhit/fastq"
output_dir="/mnt/nas/users/madhu/poresippr_db_recent_minimap2_cdhit/stxdb_98"

# Loop through the FASTQ files and run minimap2 and samtools
for fastq_file in "${fastq_dir}"/*.fastq.gz; do
    filename=$(basename "$fastq_file" .fastq.gz)
    output_bam="${output_dir}/${filename}-sorted.bam"

    echo "Processing ${filename}"
    echo "FASTQ File: $fastq_file"
    echo "Output BAM: $output_bam"

    minimap2 -x map-ont -t 15 -a "$fasta_file" "$fastq_file" | samtools sort -@ 15 -o "$output_bam"

    echo "Processed ${filename}"
done

echo "All files processed."

