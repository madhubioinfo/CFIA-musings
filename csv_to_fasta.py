import csv

def csv_to_fasta(csv_file, output_file):
    with open(csv_file, 'r') as csvfile, open(output_file, 'w') as fastafile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if len(row) >= 7:
                sequence_id = row[1]
                sequence_id1 = row[4]
                sequence = row[6]
                fastafile.write(f'>{sequence_id}_{sequence_id1}\n{sequence}\n')
            else:
                print(f"Skipping incomplete row: {row}")

# Replace 'input.csv' and 'output12.fasta' with your file names
csv_to_fasta('virulence.csv', 'complete_old.fasta')
