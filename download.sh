#!/bin/bash

# Ensure output directory exists
mkdir -p genome_zips

# Loop through each accession in the input file
while read -r acc; do
	  # Skip empty lines or lines starting with #
	    [[ -z "$acc" || "$acc" =~ ^# ]] && continue

	      echo "Downloading $acc..."
	        datasets download genome accession "$acc" --filename "genome_zips/${acc}.zip"

		  # Check if download succeeded
		    if [[ $? -ne 0 ]]; then
			        echo "❌ Download failed for $acc" >&2
				  else
					      echo "✅ Downloaded $acc successfully"
					        fi

					done < GCA_list

