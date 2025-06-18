find /home/malarm/BDS_vtec_seq_extraction/new_analysis/genome_zips/ -type f -name "*.fna" | while read fna; do
    parent_dir=$(basename "$(dirname "$fna")")
        mv "$fna" "./${parent_dir}.fna"
done

