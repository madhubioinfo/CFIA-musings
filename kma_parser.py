import pandas as pd

# Load the data from an Excel file
df = pd.read_excel('240711_KMA33873_Benchmark.xlsx', header=None)

# Select only the first two columns
df = df.iloc[:, :2]

# Remove rows where first column is 'SeqID'
df = df[df[0] != 'SeqID']

# Rename columns
df.columns = ['SeqID', '#Template']

# Group by 'SeqID' and join '#Template' values together
df_grouped = df.groupby('SeqID')['#Template'].apply(','.join).reset_index()

# Remove '|<digits>nt' from the '#Template' column
df_grouped['#Template'] = df_grouped['#Template'].str.replace(r'\|\d+nt', '', regex=True)

# Write DataFrame to TSV file
df_grouped.to_csv('kma_output.tsv', sep='\t', index=False)