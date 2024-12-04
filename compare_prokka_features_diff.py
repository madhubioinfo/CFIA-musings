import pandas as pd

# Function to parse the .tbl file and extract feature start, end, and length
def parse_tbl(file_path):
    features = []
    with open(file_path, 'r') as file:
        for line in file:
            # Parse only lines with start-end ranges (ignoring metadata lines)
            parts = line.strip().split()
            if len(parts) >= 3 and parts[0].isdigit() and parts[1].isdigit():
                start, end = int(parts[0]), int(parts[1])
                feature_length = abs(end - start) + 1
                features.append((start, end, feature_length))
    return features

# Load the files
file1_path = '/path/to/PROKKA_11282024.tbl'
file2_path = '/path/to/PROKKA_MIN0129.tbl'

# Parse the files to extract feature information
features_file1 = parse_tbl(file1_path)
features_file2 = parse_tbl(file2_path)

# Compare lengths and differences
comparison_results = []
for feature1, feature2 in zip(features_file1, features_file2):
    start1, end1, length1 = feature1
    start2, end2, length2 = feature2
    comparison_results.append({
        'File1_Start': start1, 'File1_End': end1, 'File1_Length': length1,
        'File2_Start': start2, 'File2_End': end2, 'File2_Length': length2,
        'Length_Difference': abs(length1 - length2)
    })

# Convert results to a DataFrame
df_comparison = pd.DataFrame(comparison_results)

# Filter features with length differences
df_differences = df_comparison[df_comparison['Length_Difference'] != 0]

# Save the detailed report to a CSV file
detailed_report_path = "length_differences_report.csv"
df_differences.to_csv(detailed_report_path, index=False)

# Output summary
print(f"Total Features: {len(comparison_results)}")
print(f"Features with Differences: {len(df_differences)}")
print(f"Detailed report saved to: {detailed_report_path}")

