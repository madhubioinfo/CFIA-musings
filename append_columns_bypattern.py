import re
import csv

# Step 1: Extract patterns from pattern file
patterns = []
with open('patterns.txt', 'r') as f:
    for line in f:
        patterns.append(line.strip())

# Step 2: Find lines in file1 that match the patterns
csv_data = []
with open('updated_metadata.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        for pattern in patterns:
            if re.search(pattern, row[0]):
                csv_data.append(row)

# Step 3: Read contents of file2
with open('MOD_metadata.txt', 'r') as f:
    file2_data = f.readlines()

# Step 4: Add contents of file2 to matching rows in CSV data
for i, row in enumerate(csv_data):
    row.append(file2_data[i].strip())

# Step 5: Write updated CSV data back to file1
with open('updated_metadata.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)

