#!/bin/bash

INPUT_FILE="accessions.txt"
OUTPUT_MAPPING="accession_srr_mapping.tsv"
> $OUTPUT_MAPPING

while read acc; do
    if [[ $acc == ERS* || $acc == SRS* ]]; then
        echo "Looking up SRRs for sample accession: $acc"
        curl -s "https://www.ebi.ac.uk/ena/portal/api/filereport?accession=$acc&result=read_run&fields=run_accession" \
        | tail -n +2 | awk -v a="$acc" '{print a "\t" $1}' >> $OUTPUT_MAPPING

    elif [[ $acc == GCA_* ]]; then
        echo "Looking up linked data for genome: $acc"
        GCF=$(echo $acc | sed 's/GCA_/GCF_/')
        curl -s "https://api.ncbi.nlm.nih.gov/datasets/v2alpha/genome/accession/$acc" > tmp.json

        # Try to extract BioSample ID
        biosample=$(jq -r '.genome.biosample' tmp.json)
        if [[ $biosample != "null" && $biosample != "" ]]; then
            echo "  → Found BioSample: $biosample"

            # Convert BioSample to SRR (via ENA)
            curl -s "https://www.ebi.ac.uk/ena/portal/api/filereport?accession=$biosample&result=read_run&fields=run_accession" \
            | tail -n +2 | awk -v a="$acc" '{print a "\t" $1}' >> $OUTPUT_MAPPING
        else
            echo "  → No BioSample found for $acc"
            echo -e "$acc\tNA" >> $OUTPUT_MAPPING
        fi

        rm -f tmp.json

    elif [[ $acc == SRR* ]]; then
        echo "$acc is already a run accession"
        echo -e "$acc\t$acc" >> $OUTPUT_MAPPING
    else
        echo "Skipping unrecognized accession: $acc"
        echo -e "$acc\tUNRECOGNIZED" >> $OUTPUT_MAPPING
    fi
done < $INPUT_FILE

echo "✅ Mapping written to $OUTPUT_MAPPING"

