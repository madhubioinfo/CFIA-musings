import os
import re
import csv
from Bio import SeqIO

def calculate_n50(sequence_lengths):
    total_length = sum(sequence_lengths)
    half_length = total_length / 2
    sequence_lengths.sort(reverse=True)
    cumulative_length = 0
    for length in sequence_lengths:
        cumulative_length += length
        if cumulative_length >= half_length:
            return length

def analyze_fasta_files(directory_path):
    results = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".fasta"):
            file_path = os.path.join(directory_path, filename)
            contig_lengths = []
            total_length = 0
            with open(file_path, "r") as fasta_file:
                for record in SeqIO.parse(fasta_file, "fasta"):
                    sequence_length = len(record.seq)
                    contig_lengths.append(sequence_length)
                    total_length += sequence_length
            n50 = calculate_n50(contig_lengths)
            num_contigs = len(contig_lengths)
            results.append((filename, n50, total_length, num_contigs))
    return results

def update_csv(results, csv_file):
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        for result in results:
            writer.writerow(result)

if __name__ == "__main__":
    directory_path = "/mnt/nas/users/madhu/swapped_listeria_benchmarked"
    csv_file = "/mnt/nas/users/madhu/swapped_listeria_benchmarked/assembly_stats.csv"
    results = analyze_fasta_files(directory_path)
    update_csv(results, csv_file)

