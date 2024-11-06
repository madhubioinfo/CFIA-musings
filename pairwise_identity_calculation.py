from Bio import SeqIO, pairwise2
from Bio.pairwise2 import format_alignment

def calculate_percentage_identity(alignment):
    """Calculate the percentage identity of an alignment."""
    matches = sum(1 for a, b in zip(alignment[0], alignment[1]) if a == b)
    return 100 * matches / len(alignment[0])

def calculate_query_coverage(alignment, query_len):
    """Calculate the query coverage of an alignment."""
    aligned_query = alignment[1].replace("-", "")  # Ignore gaps in query
    return 100 * len(aligned_query) / query_len

# Load all reference sequences
references = []
with open("stx2_seq.fa") as ref_file:
    references = [record for record in SeqIO.parse(ref_file, "fasta")]

# Load query sequences
queries = []
with open("stx2_seq.fa") as query_file:
    queries = [record for record in SeqIO.parse(query_file, "fasta")]

# Perform pairwise alignment for each reference-query pair
results = []
for query_record in queries:
    for ref_record in references:
        # Skip self-hits
        if query_record.id == ref_record.id:
            continue
       
        # Perform alignment
        alignments = pairwise2.align.globalxx(ref_record.seq, query_record.seq)
        for alignment in alignments:
            query_coverage = calculate_query_coverage(alignment, len(query_record.seq))
            if query_coverage > 99:
                percentage_identity = calculate_percentage_identity(alignment)
               
                # Store result for this alignment
                results.append((ref_record.id, query_record.id, percentage_identity, query_coverage))
               
                # Print alignment details
                print(f"\nAlignment between {ref_record.id} (reference) and {query_record.id} (query):")
                print(format_alignment(*alignment))
                print(f"Percentage Identity: {percentage_identity:.2f}%")
                print(f"Query Coverage: {query_coverage:.2f}%\n")
                break  # Only keep the top alignment for each reference-query pair

# Optionally, save results to a file
with open("identity_results_stx2_combinations.txt", "w") as output_file:
    for ref_id, query_id, identity, coverage in results:
        output_file.write(f"{query_id}\t{ref_id}\t{identity:.2f}%\n")

print("Pairwise alignment for all combinations completed.")

