import pandas as pd

# List to store all dataframes
all_files = []

# Read all files into pandas dataframes
for i in range(1, 11):
    filename = f'OLC0679_1.0x_{i}_coverage.txt'
    try:
        df = pd.read_csv(filename, delimiter='\t', header=None, names=['Gene', f'Value_{i}'], dtype={'Gene': str})
        all_files.append(df)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Skipping...")

# Merge dataframes based on the 'Gene' column with an outer join
if all_files:
    merged_data = all_files[0]
    for i in range(1, len(all_files)):
        merged_data = pd.merge(merged_data, all_files[i], on='Gene', how='outer')

    # Replace multiple 'NA' values with '0'
    merged_data = merged_data.fillna(0)

    # Save the merged dataframe to a new file
    merged_data.to_csv('combined_files.csv', index=False, sep='\t', float_format='%d')

    print("Combined file saved successfully.")
else:
    print("No files found for merging.")

