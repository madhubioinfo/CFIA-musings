import pandas as pd

# Read each CSV file into a DataFrame
df_98 = pd.read_csv('gene_counts_98_output.csv')
df_99 = pd.read_csv('gene_counts_99_output.csv')
df_100 = pd.read_csv('gene_counts_100_output.csv')

# Merge the DataFrames on the 'Gene' column
combined_df = df_98.merge(df_99, on='Gene', how='outer', suffixes=('_98', '_99'))
combined_df = combined_df.merge(df_100, on='Gene', how='outer', suffixes=('', '_100'))

# Fill missing values with 0 (optional)
combined_df.fillna(0, inplace=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('combined_gene_counts_output.csv', index=False)

print("Combined file created: combined_gene_counts_output.csv")

