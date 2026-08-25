import pandas as pd
import os

def parse_mash_distances(distance_file, pvalue_cutoff, matching_hashes_threshold):
    """
    Parse Mash distance file, filter results based on p-value and matching hashes threshold,
    and identify closest replacements while excluding self-matching cases.
    """
    try:
        # Read the Mash distance output file
        df = pd.read_csv(
            distance_file,
            sep="\t",
            header=None,
            names=["query", "reference", "distance", "p-value", "matching_hashes"]
        )

        # Normalize file names to handle path differences (compare only the base file names)
        df["query_base"] = df["query"].apply(os.path.basename)
        df["reference_base"] = df["reference"].apply(os.path.basename)

        # Process the "matching_hashes" column to handle NaN or improperly formatted values
        df["matching_hashes"] = (
            df["matching_hashes"]
            .str.split("/")
            .str[0]  # Extract the numerator
            .fillna("0")  # Replace NaN with "0"
            .astype(int)  # Convert to integers
        )

        # Exclude self-matching cases (based on normalized file names)
        df = df[df["query_base"] != df["reference_base"]]

        # Filter by p-value and matching hashes threshold
        df_filtered = df[
            (df["p-value"] <= pvalue_cutoff) &
            (df["matching_hashes"] >= matching_hashes_threshold)
        ]

        # Identify the closest match for each query genome
        replacements = {}
        for genome in df_filtered["query"].unique():
            matches = df_filtered[df_filtered["query"] == genome]
            # Sort by distance (primary) and p-value (secondary) to get the best match
            closest_match = matches.sort_values(by=["distance", "p-value"]).iloc[0]
            replacements[genome] = {
                "replacement": closest_match["reference"],
                "distance": closest_match["distance"],
                "p-value": closest_match["p-value"],
                "matching_hashes": closest_match["matching_hashes"]
            }
        
        return replacements

    except Exception as e:
        print(f"Error while parsing Mash distances: {e}")
        return {}

def write_replacements_to_file(replacements, output_file):
    """
    Write the replacement statistics to a file.
    """
    try:
        with open(output_file, "w") as f:
            f.write("Query\tReplacement\tDistance\tP-value\tMatching_hashes\n")
            for query, details in replacements.items():
                f.write(
                    f"{query}\t{details['replacement']}\t{details['distance']}\t"
                    f"{details['p-value']}\t{details['matching_hashes']}\n"
                )
    except Exception as e:
        print(f"Error writing to file {output_file}: {e}")

def generate_statistics(replacements, stats_file):
    """
    Generate and save statistics about the replacements.
    """
    try:
        total_replacements = len(replacements)
        replaced_genomes = list(replacements.keys())
        replacement_genomes = [details["replacement"] for details in replacements.values()]

        with open(stats_file, "w") as f:
            f.write(f"Total genomes replaced: {total_replacements}\n")
            f.write("\nReplaced Genomes:\n")
            f.write("\n".join(replaced_genomes))
            f.write("\n\nReplacement Genomes:\n")
            f.write("\n".join(replacement_genomes))
    except Exception as e:
        print(f"Error writing statistics to file {stats_file}: {e}")

def main():
    # Input Mash distance file
    distance_file = "modified_mash_dist.tab"  # Replace with your file path
    # Output files
    replacements_file = "replacements.txt"
    stats_file = "replacements_stats.txt"
    # Filters
    pvalue_cutoff = 0.05
    matching_hashes_threshold = 980  # Adjust the threshold as needed

    # Parse the Mash distances and find replacements
    replacements = parse_mash_distances(distance_file, pvalue_cutoff, matching_hashes_threshold)

    # Write replacements to a file
    write_replacements_to_file(replacements, replacements_file)

    # Generate statistics about the replacements
    generate_statistics(replacements, stats_file)

    print("Replacement analysis completed.")
    print(f"Replacements written to: {replacements_file}")
    print(f"Statistics written to: {stats_file}")

if __name__ == "__main__":
    main()

