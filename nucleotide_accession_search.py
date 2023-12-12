import os
import glob

def read_patterns_from_file(file_path):
    with open(file_path, 'r') as file:
        patterns = file.read().splitlines()
    return patterns

def find_files_by_pattern(root_dirs, patterns, output_file):
    with open(output_file, 'w') as out_file:
        out_file.write("Pattern\tFile Name\n")
        for root_dir in root_dirs:
            matching_dirs = glob.glob(root_dir)
            for directory in matching_dirs:
                for root, dirs, files in os.walk(directory):
                    for file in files:
                        file_path = os.path.join(root, file)
                        for pattern in patterns:
                            if pattern in open(file_path).read():
                                out_file.write(f"{pattern}\t{file}\n")

# Reading stx pattern files to be searched
patterns_file_path = '/mnt/nas/users/madhu/for_sarah_genomes/test'  
patterns_to_search = read_patterns_from_file(patterns_file_path)

# providing the output and the directories to be searched 
directories_to_search = ['/mnt/nas/users/madhu/stx_recent_work/stec_split/subdirectory_*']
output_filename = 'genome_filenames.tsv'

find_files_by_pattern(directories_to_search, patterns_to_search, output_filename)

