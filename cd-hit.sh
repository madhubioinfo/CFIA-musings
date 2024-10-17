#!/bin/bash

# Number of nodes to request. Leave at 1 unless you're running an MPI job.
#SBATCH --job-name="cd-hit"
#SBATCH -N 1
# Set number of processors you want for your job here.
#SBATCH --ntasks=47 
# Set the amount of memory you want (in megabytes, so this is 100 gigs)
#SBATCH --mem=100000
# Set amount of time to give your job here. (D-HH:MM)
#SBATCH --time=6-00:00
# Standard out will go here (%j will be replaced by job ID when script is run).
#SBATCH -o /mnt/nas/users/madhu/slurm_logs/cd-hit_%j.out
# Standard error will go here (percent j replaced by job ID when script is run).
#SBATCH -e /mnt/nas/users/madhu/slurm_logs/cd-hit_%j.err

source activate /mnt/nas2/virtual_environments/cd-hit

cd-hit -i /mnt/nas/users/madhu/poresippr_db_recent_minimap2_cdhit/StxDB_nt_20240412.fasta -c 0.99 -n 5 -o /mnt/nas/users/madhu/poresippr_db_recent_minimap2_cdhit/stxdb_99
