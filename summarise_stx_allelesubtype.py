import pandas as pd

# Load the CSV file
file_path = 'combined_gene_counts_output.csv'  # Replace with the actual file path
data = pd.read_csv(file_path)

# Prepare a list to store the results
results = []

# Iterate through each row in the DataFrame
for index, row in data.iterrows():
    # Extract the subtype name (only the part before the first underscore)
    subtype_info = row['Gene'].split('|')[0].split('_')[0]  # Get the first part before '_'
    
    for col in data.columns[1:]:  # Skip the first column (Gene)
        count = row[col]
        if count > 0:  # Only consider non-zero counts
            sample_name = col
            results.append((sample_name, subtype_info, int(count)))  # Append sample, subtype, and count

# Create a DataFrame for better formatting
results_df = pd.DataFrame(results, columns=['Sample', 'Subtype', 'Count'])

# Group by Sample and Subtype, then sum the counts
summarized_results = results_df.groupby(['Sample', 'Subtype'], as_index=False).sum()

# Print the results in the desired format
for _, row in summarized_results.iterrows():
    print(f"{row['Sample']}\t{row['Subtype']}\t{row['Count']}")

