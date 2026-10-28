#!/bin/bash
#SBATCH --job-name=gpu_check
#SBATCH --account=YOUR_ACCOUNT
#SBATCH --partition=YOUR_GPU_PARTITION
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --time=00:05:00
#SBATCH --gres=gpu:GPU_TYPE:1
#SBATCH --output=gpu-%j.out
#SBATCH --error=gpu-%j.err
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=YOUR_NETID@illinois.edu
#SBATCH --nodelist=NODE_NAME

# Replace every placeholder. Remove the nodelist line unless a node is needed.
# This job checks the allocation; it does not run a GPU analysis.
# Replace nvidia-smi with a GPU-aware program only after preparing its software.
set -e
nvidia-smi
