# The project used throughout the lecture

This is a tiny synthetic Python project for the lecturer to explain. It is not an audience exercise or a research pipeline. The complete R, Conda, and GPU alternatives are in the separate `examples/` folder.

Input: `data/samples.csv`, with three samples and read counts 1000, 1500, and 1200.

Expected output: `results/summary.csv` containing:

```csv
samples,total_reads
3,3700
```

## Follow the project from beginning to end

1. Obtain approved ICC access, the valid account/partition pair, and an authorized project location.
2. Connect with VS Code Remote - SSH. Open the project location, upload this entire `demo` folder through Explorer, then open the remote `demo` folder.
3. Open a new remote terminal. Confirm `hostname` and `pwd`; navigate to the same folder. Inspect `data/samples.csv`. The shell examples create `results` and make disposable copies of `notes.txt`.
4. Replace the account and partition placeholders in `hello.sbatch`, save, and submit `sbatch hello.sbatch`. Use the returned ID with `squeue`/`sacct` and read `slurm-JOBID.out`. Expect `My first HPC job`.
5. Obtain an interactive compute shell with the valid allocation and suitable resources. Stay in the remote `demo` folder. Check the available Python module, load it, create `.venv`, activate it, and install pandas. Wait for installation to finish and the shell prompt to return.
6. In that same shell, check that importing pandas prints its version without an error, then record installed versions. Type `exit` once to return from the allocated shell to the login shell, and confirm `hostname` and `pwd`. No summary result should exist yet. The environment files remain; activation belongs only to the shell that activated them.
7. Configure `analysis.sbatch` with the allocation and the same Python module. Replace the email address or remove both mail directives. Save and submit `sbatch analysis.sbatch` from `demo`.
8. Use this new job ID for `analysis-JOBID.out`, `analysis-JOBID.err`, and `sacct`. After successful completion, check `results/summary.csv` against the expected contents above.
9. Open the result in VS Code. Download it through Explorer only if a local copy is useful.

## Python setup commands

Inside an appropriate allocated compute shell, from this directory, enter each command in order and wait for it to finish:

```bash
module avail python
module load python/3.11.11
python -m venv .venv
source .venv/bin/activate
python -m pip install pandas
python -c "import pandas; print(pandas.__version__)"
python -m pip freeze > requirements.txt
```

If installation or the import check reports an error, fix it before continuing. A pandas version number confirms the import check. After recording versions, leave the allocated shell and confirm the original login host and project folder:

```bash
exit
hostname
pwd
```

The lecture completes this Python install → verify → exit sequence without switching environments. Its later R and Conda pages are alternatives for other projects. Their extra files are in `examples/`; they are not needed for this minimal demo. In the R alternative, `q(save = "no")` leaves the R console before `exit` releases its allocated shell.

The shown module is the lecture example. Verify its availability and keep the chosen compatible version consistent between setup and `analysis.sbatch`. Do not copy a laptop virtual environment onto the cluster.

The job settings are only for this tiny demonstration. Use requirements appropriate to the actual tool and dataset for research work. No account access or Slurm submission is performed by opening these files.
