#!/bin/bash
#SBATCH --job-name=analysis_R
#SBATCH --account=YOUR_ACCOUNT
#SBATCH --partition=YOUR_PARTITION
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --time=00:05:00
#SBATCH --output=analysis_R-%j.out
#SBATCH --error=analysis_R-%j.err
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=YOUR_NETID@illinois.edu

# Stop if setup fails. Use the same R module version as package installation.
set -e
module load R
export R_LIBS_USER="$PWD/R-library"
Rscript analysis.R
