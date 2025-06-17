#!/bin/bash

SECONDS=0

read -p "Enter the directory path containing pod5 subdirectories (e.g. /path/to/pod5_dirs): " pod5_base_dir

if [ ! -d "$pod5_base_dir" ]; then
    echo "Invalid directory path."
    exit 1
fi

dorado_path="/home/mathum/dorado-1.0.0-linux-x64/bin/dorado"
output_base_dir="/mnt/datadrive"

for pod5_directory in "$pod5_base_dir"/*/ ; do
    dir_name=$(basename "$pod5_directory")

    echo "Processing pod5 directory: $dir_name"

    reads_bam="${output_base_dir}/${dir_name}_reads.bam"

    # Basecalling
    "${dorado_path}" basecaller --device "cuda:all" sup "${pod5_directory}" --kit-name SQK-RBK114-96 > "${reads_bam}"

    demux_output_directory="${output_base_dir}/${dir_name}_dorado_demux"
    mkdir -p "${demux_output_directory}"

    # Demux [ this code just deletes the bam file]
    "${dorado_path}" demux --kit-name SQK-RBK114-96 --emit-fastq --output-dir "${demux_output_directory}" "${reads_bam}"

    echo "Dorado demultiplexing completed for ${dir_name}. Results in: ${demux_output_directory}"

    # Delete BAM to save space
    rm -f "${reads_bam}"
    echo "Deleted BAM file: ${reads_bam}"
    echo ""
done

echo "Total processing time: $SECONDS seconds"

