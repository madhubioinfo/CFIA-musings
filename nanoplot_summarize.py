import os
import csv

# Set the directory where NanoPlot reports are located
base_dir = "nanoplot_reports"
output_csv = "NanoPlot_summary.csv"

# Define the columns you want to extract from each NanoStats.txt
fields_to_extract = {
    "Number of reads": "Num Reads",
    "Mean read length": "Mean Length",
    "Read length N50": "N50",
    "Longest read": "Max Length",
    "Mean basecall quality": "Mean Q Score"
}

# Initialize CSV data
header = ["Sample"] + list(fields_to_extract.values())
data = []

# Walk through each sample report
for sample_folder in sorted(os.listdir(base_dir)):
    stats_path = os.path.join(base_dir, sample_folder, "NanoStats.txt")
    if not os.path.isfile(stats_path):
        continue

    stats = {}
    with open(stats_path, "r") as f:
        for line in f:
            if ":" not in line:
                continue
            key, value = [x.strip() for x in line.split(":", 1)]
            if key in fields_to_extract:
                stats[fields_to_extract[key]] = value

    row = [sample_folder] + [stats.get(col, "NA") for col in header[1:]]
    data.append(row)

# Write summary to CSV
with open(output_csv, "w", newline="") as out_f:
    writer = csv.writer(out_f)
    writer.writerow(header)
    writer.writerows(data)

print(f"Summary written to {output_csv}")

