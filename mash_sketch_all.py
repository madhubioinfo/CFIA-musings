import subprocess
import glob
### Author : Madhu Mathu.Malar@inspection.gc.ca/mmadhubioinfo@gmail.com##########
mash_path = '/mnt/nas2/virtual_environments/mash/bin/mash'
output_dir = '/mnt/nas2/redmine/bio_requests/14674/'
num_processors = 12

# Define the input file paths
sequence_path1 = '/mnt/nas2/processed_sequence_data/control_assemblies/*/BestAssemblies/*.fasta'
sequence_path2 = '/mnt/nas2/processed_sequence_data/hybrid_assemblies/*/BestAssemblies/*.fasta'
sequence_path3 = '/mnt/nas2/processed_sequence_data/miseq_assemblies/*/BestAssemblies/*.fasta'
sequence_path4 = '/mnt/nas2/processed_sequence_data/enterobase_assemblies/*/BestAssemblies/*.fasta'
sequence_path5 = '/mnt/nas2/processed_sequence_data/merged_assemblies/*/BestAssemblies/*.fasta'
sequence_path6 = '/mnt/nas2/processed_sequence_data/nanopore_assemblies/*/BestAssemblies/*.fasta'
sequence_path7 = '/mnt/nas2/processed_sequence_data/nextseq_assemblies/*/BestAssemblies/*.fasta'
sequence_path8 = '/mnt/nas2/processed_sequence_data/pacbio_assemblies/*/BestAssemblies/*.fasta'
sequence_path9 = '/mnt/nas2/processed_sequence_data/refseq_assemblies/*/BestAssemblies/*.fasta'
sequence_path10 = '/mnt/nas2/processed_sequence_data/ncbi/*/BestAssemblies/*.fasta'


# Expand the wildcard character in the input file paths
sequence_files1 = glob.glob(sequence_path1)
sequence_files2 = glob.glob(sequence_path2)
sequence_files3 = glob.glob(sequence_path3)
sequence_files4 = glob.glob(sequence_path4)
sequence_files5 = glob.glob(sequence_path5)
sequence_files6 = glob.glob(sequence_path6)
sequence_files7 = glob.glob(sequence_path7)
sequence_files8 = glob.glob(sequence_path8)
sequence_files9 = glob.glob(sequence_path9)
sequence_files10 = glob.glob(sequence_path10)

##################################################################################################################

# split the fasta files into groups of 200
file_groups1 = [sequence_files1[i:i+200] for i in range(0, len(sequence_files1), 200)]
file_groups2 = [sequence_files2[i:i+200] for i in range(0, len(sequence_files2), 200)]
file_groups3 = [sequence_files3[i:i+200] for i in range(0, len(sequence_files3), 200)]
file_groups4 = [sequence_files4[i:i+200] for i in range(0, len(sequence_files4), 200)]
file_groups5 = [sequence_files5[i:i+200] for i in range(0, len(sequence_files5), 200)]
file_groups6 = [sequence_files6[i:i+200] for i in range(0, len(sequence_files6), 200)]
file_groups7 = [sequence_files7[i:i+200] for i in range(0, len(sequence_files7), 200)]
file_groups8 = [sequence_files8[i:i+200] for i in range(0, len(sequence_files8), 200)]
file_groups9 = [sequence_files9[i:i+200] for i in range(0, len(sequence_files9), 200)]
file_groups10 = [sequence_files10[i:i+200] for i in range(0, len(sequence_files10), 200)]

# run the mash sketch command on each group of files
for i, file_group in enumerate(file_groups1):
    output_path = output_dir + f'part_1_{i}.msh'
    subprocess.run([mash_path, 'sketch', '-o', output_path, '-p', str(num_processors)] + file_group, check=True)
########################################################################################################################
# run the mash sketch command on each group of files
for i, file_group in enumerate(file_groups2):
    output_path = output_dir + f'part_2_{i}.msh'
    subprocess.run([mash_path, 'sketch', '-o', output_path, '-p', str(num_processors)] + file_group, check=True)
########################################################################################################################
# run the mash sketch command on each group of files
for i, file_group in enumerate(file_groups3):
    output_path = output_dir + f'part_3_{i}.msh'
    subprocess.run([mash_path, 'sketch', '-o', output_path, '-p', str(num_processors)] + file_group, check=True)
########################################################################################################################
# run the mash sketch command on each group of files
for i, file_group in enumerate(file_groups4):
    output_path = output_dir + f'part_4_{i}.msh'
    subprocess.run([mash_path, 'sketch', '-o', output_path, '-p', str(num_processors)] + file_group, check=True)
########################################################################################################################
# run the mash sketch command on each group of files
for i, file_group in enumerate(file_groups5):
    output_path = output_dir + f'part_5_{i}.msh'
    subprocess.run([mash_path, 'sketch', '-o', output_path, '-p', str(num_processors)] + file_group, check=True)
########################################################################################################################
# run the mash sketch command on each group of files
for i, file_group in enumerate(file_groups6):
    output_path = output_dir + f'part_6_{i}.msh'
    subprocess.run([mash_path, 'sketch', '-o', output_path, '-p', str(num_processors)] + file_group, check=True)
########################################################################################################################
# run the mash sketch command on each group of files
for i, file_group in enumerate(file_groups7):
    output_path = output_dir + f'part_7_{i}.msh'
    subprocess.run([mash_path, 'sketch', '-o', output_path, '-p', str(num_processors)] + file_group, check=True)
########################################################################################################################
# run the mash sketch command on each group of files
for i, file_group in enumerate(file_groups8):
    output_path = output_dir + f'part_8_{i}.msh'
    subprocess.run([mash_path, 'sketch', '-o', output_path, '-p', str(num_processors)] + file_group, check=True)
########################################################################################################################
# run the mash sketch command on each group of files
for i, file_group in enumerate(file_groups9):
    output_path = output_dir + f'part_9_{i}.msh'
    subprocess.run([mash_path, 'sketch', '-o', output_path, '-p', str(num_processors)] + file_group, check=True)
########################################################################################################################
# run the mash sketch command on each group of files
for i, file_group in enumerate(file_groups10):
    output_path = output_dir + f'part_10_{i}.msh'
    subprocess.run([mash_path, 'sketch', '-o', output_path, '-p', str(num_processors)] + file_group, check=True)
########################################################################################################################
# get a list of all temporary Mash sketches
temp_files = [f for f in os.listdir(output_dir) if f.startswith('part')]

# write the list of temp* files to list.txt
with open(output_dir + 'list.txt', 'w') as f:
    for file in temp_files:
        f.write(output_dir + file + '\n')


# run the Mash paste command
if os.path.exists(output_dir + 'final_sketch.msh'):
    os.rename(output_dir + 'final_sketch.msh', output_dir + 'final_sketch_old.msh')
subprocess.run([mash_path, 'paste',  output_dir + 'final_sketch.msh', '-l', output_dir + 'list.txt'], check=True)
# delete temporary files
for temp_file in temp_files:
    os.remove(os.path.join(output_dir, temp_file))
