#!/bin/bash
echo "MinION,Illumina_R1,Illumina_R2,OutName" > input.csv

if [[ ! -f "seqid_mapping.tsv" ]]; then
    echo "Error: seqid_mapping.tsv not found" >&2
    exit 1
fi

for minion_file in *-MIN-*.fastq.gz; do
    # Extract full MIN-ID (yyyy-MIN-xxxx) without extension
    min_id="${minion_file%.fastq.gz}"

    # Get SEQ-ID using 'seqid_mapping.tsv' file (skipping header)
    seq_id=$(awk -F'\t' -v minid="$min_id" 'NR>1 && $1 == minid {print $2; exit}' seqid_mapping.tsv)

    if [[ -z "$seq_id" ]]; then
        echo "Warning: No SEQ-ID found for MIN-ID $min_id" >&2
        continue
    fi

    # Use original Illumina logic: search for R1 and R2 files in /mnt/nas2/raw_sequence_data/
    illumina_r1=$(find /mnt/nas2/raw_sequence_data/ -name "*${seq_id}*_R1*.fastq.gz" -print -quit 2>/dev/null)
    illumina_r2=$(find /mnt/nas2/raw_sequence_data/ -name "*${seq_id}*_R2*.fastq.gz" -print -quit 2>/dev/null)

    if [[ -f "$illumina_r1" && -f "$illumina_r2" ]]; then
        echo "${PWD}/${minion_file},${illumina_r1},${illumina_r2},${min_id}" >> input.csv
    else
        echo "Warning: Missing Illumina files for SEQ-ID ${seq_id} (MIN-ID ${min_id})" >&2
    fi
done
