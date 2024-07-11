import pandas as pd

# Load the data from an Excel file
df = pd.read_excel('/home/jshay/Downloads/240711_GeneSeekr34067_Benchmark.xlsx', header=0)

# Select only the first and third columns
df = df[['seq_id', 'subject_id']]

# Remove rows where first column is 'SeqID'
df = df[df['seq_id'] != 'SeqID']

# Group by 'seq_id' and join 'subject_id' values together
df_grouped = df.groupby('seq_id')['subject_id'].apply(','.join).reset_index()

# Remove '|<digits>nt' from the 'subject_id' column
df_grouped['subject_id'] = df_grouped['subject_id'].str.replace(r'\|\d+nt', '', regex=True)

# Write DataFrame to TSV file
df_grouped.to_csv('geneseekrparsed_output.tsv', sep='\t', index=False)