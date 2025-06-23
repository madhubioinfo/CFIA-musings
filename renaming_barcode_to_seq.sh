#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 mapping_file"
    exit 1
fi

mapping_file="$1"

while read -r oldname newname; do
    old_file="${oldname}.fastq"
    new_file="${newname}.fastq"
    if [ -f "$old_file" ]; then
        mv "$old_file" "$new_file"
        echo "Renamed $old_file → $new_file"
    else
        echo "Warning: $old_file not found"
    fi
done < "$mapping_file"

