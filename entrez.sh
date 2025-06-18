cat accessions | \
xargs -n 1 -I {} efetch -db nuccore -id {} -format fasta > all_contigs.fasta
