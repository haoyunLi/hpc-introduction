# Small examples for the lecture

These are lecturer demonstrations, not audience exercises. The data are synthetic. The separate `demo/` folder contains the minimal Python project used throughout the lecture. This `examples/` folder contains the complete templates, including the R, Conda, and GPU alternatives. Copy only the files needed for the chosen route into its remote project, and submit from that project folder so relative input and output paths agree.

## Files

- `hello.sbatch`: the first job, which prints one message.
- `analysis.py`: reads `data/samples.csv` using pandas and writes `results/summary.csv`.
- `analysis.R`: the same small calculation with base R, writing `results/summary_R.csv`.
- `analysis.sbatch` and `analysis_R.sbatch`: complete CPU job templates with resource, output, and email settings.
- `gpu_check.sbatch`: a GPU allocation check, including GPU, email, and node-name syntax. It runs `nvidia-smi`, not a GPU analysis.
- `install_python.sh`: the Python environment setup sequence, performed once before an analysis submission.
- `install_R_packages.R`: a small CRAN installation and commented examples for Seurat and DESeq2.
- `environment.yml`: an alternative Conda setup example.
- `notes.txt` and `data/samples.tsv`: small files for graphical file operations and text inspection.

Replace every uppercase placeholder before a cluster submission. For email, use your real address or remove both mail directives. In the GPU template, replace the GPU type with one available in your authorized partition. Remove the `--nodelist` line unless you actually require a named node. A login-node name does not belong there.

The CPU resources are sized only for the tiny demonstration. They are not estimates for a real bulk, single-cell, or spatial analysis. Select resources from the actual tool's requirements and previous runs. Match the requested CPUs to the program's own worker settings.

## Python route

1. Open the uploaded remote project in VS Code. Keep the terminal in the same folder.
2. Obtain an appropriate interactive compute shell using the lecture's `srun` step. Confirm the Python module name. Run the setup commands in `install_python.sh` one at a time in that shell: load Python, create `.venv`, activate it, and install pandas. The documented example uses `python/3.11.11`.
3. Wait for installation to finish, then check that `python -c "import pandas; print(pandas.__version__)"` prints a version without an error. Save `python -m pip freeze > requirements.txt` while that environment is active.
4. Type `exit` once to leave the interactive allocation. Check `hostname` and `pwd` to confirm the login shell and project folder. The `.venv` files remain in shared storage; activation applies only to the shell that activated it.
5. Save the configured job file and submit with `sbatch analysis.sbatch`. Its setup commands load the same Python and activate `.venv` again.
6. Read the new job ID, check with `squeue -u YOUR_NETID`, and open its `.out` and `.err` files once they exist.
7. Check the final Slurm state and `results/summary.csv`: the expected values are **3 samples** and **3700 total_reads**.

Complete this install → verify → exit sequence before considering another software route. R and Conda are alternatives for other projects, not additional setup commands for this Python project. Running `install_python.sh` as a separate Bash process also performs its import check, but its activation does not change the parent terminal; activate explicitly if continuing work in that terminal.

The scripts use `set -e` so a failing setup command stops the shell script. The lecture explains the setup and run commands; this guard is included in the full templates.

## R route

Use the same R module version for package preparation and for the job. For this separate route, copy `analysis.R` and `analysis_R.sbatch` from this folder into the remote R project alongside `data/samples.csv`. Obtain an appropriate interactive compute shell and work from that project folder:

```bash
module load R
export R_LIBS_USER="$PWD/R-library"
mkdir -p "$R_LIBS_USER"
R
```

The `R` command changes from the shell to the R console, whose prompt is `>`. Inside R, use the package installation commands in the lecture or `install_R_packages.R`. Check the required package with `library(...)`, then return to the shell with `q(save = "no")`. This skips the R-workspace save question; it does not remove installed packages. Type `exit` at the shell prompt when setup is complete to release that interactive allocation.

The small base-R analysis itself requires no add-on packages. Configure and submit `analysis_R.sbatch` from the project folder in the login shell. Read the returned job's logs and state, then check `results/summary_R.csv`. The expected result is again 3 samples and 3700 total_reads.

Use a separate R library when changing R versions. Install in a writable location. Large builds can need more resources, system libraries, and network access than the tiny job example.

## Conda route

This replaces the Python venv route. The supplied `environment.yml` is in this `examples/` folder, not the minimal `demo/`. Upload it only when using this alternative. In a separate allocated setup shell, load the appropriate cluster Conda module, create the environment, and check the package:

```bash
conda env create -f environment.yml
conda run -n analysis python -c "import pandas; print(pandas.__version__)"
```

Here `-f` names the YAML file, and `-n analysis` selects the name declared by `name: analysis` in that file. Continue only after the version check succeeds, then leave the allocated shell with `exit`. In the configured analysis batch script, replace the venv setup with the same Conda module and `conda run -n analysis python analysis.py`. The YAML file is illustrative rather than a complete version lock for a real project.

## Validation boundaries

Local checks cover shell syntax, the small programs where runtimes are available, and the presentation's rendering and interactions. They do not confirm ICC eligibility, package installation on ICC, GPU availability, email delivery, or a real Slurm submission. Those depend on the presenter's authorized cluster setup.
