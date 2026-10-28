# Source review and teaching priorities

Reviewed 27 October 2026 against the supplied ICC guide and Missing Semester, with official upstream references for software installation and Slurm semantics. This is a coverage review for an introductory HPC lecture, not a review of analysis methods.

## What the lecture now covers

| Need in an actual analysis workflow | Topic / slides | Why it belongs |
| --- | --- | --- |
| A concrete result, account access, and login | Access, 1–5 | Establishes the expected calculation, cluster roles, approval prerequisites, login identity, and allocation details. |
| Local VS Code setup, storage choice, connection, and upload | Files in VS Code, 6–13 | Installs the interface, illustrates local versus remote work, selects the destination before uploading demo, and identifies the files that now exist remotely. |
| Everyday Unix commands for the uploaded project | Shell essentials, 14–22 | Command structure, paths, ls options, mkdir/cp/mv/rm, text previews, find/grep/wc/du, help and shortcuts. |
| A first batch job, including its result | Slurm jobs, 23–28 | Illustrates login and compute roles with shared storage, explains resources, submits hello.sbatch, checks the queue, and opens the expected message before adding analysis software. |
| Output files and email | Slurm jobs, 29 | Explains output/error filenames, the job ID token, email events and recipient settings. |
| GPU and named-node options | Slurm jobs, 30–31 | Decodes optional resource settings for projects that need them. |
| Interactive compute allocation | Slurm jobs, 32 | Opens the compute shell that remains in use for Python software preparation. |
| Prepare and verify the main Python environment | Software and packages, 33–37 | Loads Python, creates .venv, installs pandas, verifies the import, records versions, illustrates installation and activation lifetime, and returns to the login shell. |
| Alternative R package setup | Software and packages, 38 | Uses a separate allocated setup session, a writable project library, one package installation and loading check, and the R-to-shell exit sequence. |
| Alternative project-provided Conda environment | Software and packages, 39 | Recognizes another setup route, explains the environment file and name, and checks the import without nesting Conda in the main venv route. |
| Prepare, submit, and follow the analysis job | Run and check, 40–42 | Reuses the tested setup, visibly submits analysis.sbatch, and reads the logs belonging to its new job ID. |
| Verify and open the actual result | Run and check, 43–44 | Combines accounting, logs, and the expected CSV, then returns to VS Code to view or download it. |
| Run an R project | Run and check, 45 | Shows the alternative R job body with the same submission and result checks. |
| Troubleshooting and the completed project | Run and check, 46–47 | Connects errors to checks and identifies how each final project file was created. |
| References and support | Run and check, 48 | Gives a path to current system policy and account-specific assistance. |

## Findings from the supplied websites

[ICC access](https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/accessing.html) covers account routes, password/Duo authentication, hostnames, and connection reuse. Account and login steps remain in the core lecture. ControlMaster configuration is left for connection troubleshooting because it is not required to submit the first analysis.

[ICC running jobs](https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/running_jobs.html) extends far beyond basic submission. The useful first-workflow material includes login-node limits, account/partition pairing, interactive jobs, GPU requests, queue inspection, and cancellation. Those are included. Preemption, checkpointing, job arrays, MPI, and recurring jobs require a separate explanation and are not part of this introductory sequence.

[ICC storage](https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html) makes storage policy and data transfer part of the working routine. Home, project, scratch, disk usage, and the large-transfer role of Globus are included. Node-local scratch and detailed transfer endpoint setup are deferred.

[ICC software](https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/software.html) directly supports modules and installing R packages into writable locations. These are essential, not advanced extras. Exact available versions and permissions remain account/site-specific. The lecture records an example Python module while asking the presenter to verify it before use.

[Missing Semester’s shell introduction](https://missing.csail.mit.edu/2026/course-shell/) and [command-line environment lecture](https://missing.csail.mit.edu/2026/command-line-environment/) provide the conceptual basis for commands, arguments, paths, files, streams, and processes. The lecture uses a small project to teach the commands most likely to appear when preparing and checking an analysis. Command structure comes before options. The shell section explicitly distinguishes filenames from file contents, hidden files from missing files, disk usage from remaining quota, and line counts from sample counts. The shell section focuses on individual commands. Output redirection is explained later where package versions are saved. Pipes, shell scripting, job-control internals, and automation are deferred. The rest of the current Missing Semester syllabus, including Git, profiling, packaging, and code quality, is valuable further study rather than a prerequisite for this first HPC workflow.

## Details that needed clarification

- A node is a computer. `--ntasks` describes tasks/processes, while `--cpus-per-task` reserves CPUs for each task. The lecture follows the [upstream Slurm definition](https://slurm.schedmd.com/sbatch.html) rather than treating tasks as a synonym for threads.
- Reserving CPUs or a GPU does not make arbitrary code use them. The program must support and be configured for those resources.
- `--mem` requests CPU RAM per node. GPU device memory is a separate constraint.
- `--nodes` is a count; `--nodelist` names machines. A named node request can increase waiting and must be eligible for the account/partition.
- Slurm directives belong before executable commands. `sbatch` interprets them; running the file directly with Bash does not submit a job.
- A log subdirectory must exist before submission if it appears in an output filename. The introductory examples avoid that extra dependency by writing logs into the submission folder.
- Package installation, environment activation, and importing/loading a package are separate actions. The job repeats setup, not installation.
- Use a compatible R version when returning to a project package library. Bioconductor installation and version matching are further-reading topics outside the simplified example.
- VS Code file browsing, notebook viewing, and an allocated compute shell are different things. Starting an interactive Slurm shell does not move every VS Code execution feature to that node.

## Does the sequence work from zero?

The lecture follows one concrete calculation from beginning to end: `data/samples.csv` contains three sample rows, `analysis.py` uses pandas to read them, and the expected `results/summary.csv` contains 3 samples and 3700 total reads. The expected result is shown before setup and checked after the batch job.

1. Establish identity, allocation, the project location, and the connection.
2. Choose storage, open the remote destination in VS Code, upload `demo/`, and inspect the input.
3. Open a terminal in that same folder. Read command structure and paths, organize files, and check the small CSV without changing it.
4. Submit `hello.sbatch` and inspect its expected message. This closes the first-job loop before adding analysis dependencies.
5. Obtain an interactive compute shell and keep it open for software preparation.
6. Load Python, create `.venv`, install pandas, verify the import, and record package versions. Explain that the environment files persist while activation belongs to the current shell. Then exit the compute shell once and confirm the login host and project directory. R and Conda follow as explicitly separate alternatives, each requiring its own appropriate allocated setup session.
7. Save `analysis.sbatch` with the same software setup and submit it. Keep the new analysis job ID separate from the earlier hello ID.
8. Follow the analysis logs after they exist, inspect the final job state, and compare `summary.csv` with the original expected calculation.
9. Open or download that same result through VS Code, then identify the inputs, environment record, job file, logs, and output in the completed project.

The minimal `demo/` folder supports this continuous Python route. The complete `examples/` collection retains R, Conda, and GPU templates. R and Conda are explicitly presented as alternative routes for other projects, not additional installations to perform in the main walkthrough. The presenter can explain those choices after the main Python setup has been verified and its allocation released, without changing the prepared Python project. The alternative commands are not run in the returned login shell.

The initial folder has neither `.venv` nor a generated summary. Hidden-environment listing appears only after creation, and log-following appears after submission. The import check does not run the analysis, so a pre-existing interactive result cannot be mistaken for the batch result. The official cluster overview, login banner, and Microsoft Remote - SSH figures retain short reading cues and source credits. Historical values and example paths in screenshots are labeled as such. All displayed cluster outputs are illustrative expectations. The materials do not claim an actual ICC job was run.

## Beginner review and repairs

The review asked whether a first-time listener could identify where to act, read the command and its options, recognize the expected result, and understand why the next action follows. It led to these changes rather than adding more advanced material:

| Gap identified | Clarification now provided |
| --- | --- |
| Login and upload assumed a prepared laptop | The slides identify the local terminal, decode the SSH command, cover local VS Code and extension installation, and locate demo in the unzipped package. |
| Instructions, placeholders, prompts, and output could be confused | Uppercase replacements and command-entry conventions are explained. The quoted-path illustration no longer asks the listener to open an absent file. Navigation commands have matching output examples; optional exit and cancellation commands are distinguished from the worked sequence. |
| Command outcomes were shown without all relevant option meanings | The search and disk-usage material is split into two slides. The displayed shell, Slurm, Python, R, and Conda options and symbols receive explicit explanations on slides or in their accompanying notes. |
| The compute-shell transition and software lifetime were easy to miss | srun, --pty bash, and line continuation are decoded. Python installation is immediately followed by import verification, version recording, an explanation of persistent files versus per-shell activation, and an explicit return to the login shell. |
| Alternative language routes could interrupt or accidentally reuse the main setup session | R and Conda appear after the verified Python route has exited. Each alternative calls for its own allocated setup session; the R prompt and its return to the shell are identified. |
| A job identifier or quiet log could be mistaken for success | The first and analysis jobs use distinct illustrative IDs. Queue state, final accounting, log messages, and the expected CSV are checked together. Optional cancellation is not presented as a step to perform on the successful example. |
| The interactive batch explanation was incomplete in the static handout | All ten hello.sbatch line explanations are included in the printed PDF, while the browser retains clickable lines. |

The review preserves all original figures, the basic-command coverage, six horizontal topics with vertical slides, and the single demo calculation. Remaining uncertainties are account-specific values, available software versions, queue waiting, and installation behavior; the slides identify the values to confirm instead of presenting them as universal guarantees.

The 48-slide version includes four simple teaching diagrams. Slide 7 separates the local VS Code window from remote project files and terminal processes. Slide 23 shows submission on the login node, Slurm allocation, execution on a compute node, and one shared demo folder. Slide 25 uses one node containing two tasks with two CPUs each to explain the resource hierarchy and the total of four requested CPUs; it explicitly keeps hello.sbatch at its original 1/1/1 settings. Slide 36 separates installation into persistent .venv files from activation in the current shell or a later batch job. The official ICC overview and Microsoft architecture figure remain in the deck; the simpler diagrams focus on these distinctions without replacing their source material.

## Topics that need more teaching time

These estimates are for the presenter, not labels on the slides.

| Extra explanation or live demonstration | Suggested additional time | Why |
| --- | --- | --- |
| Installing both a Python environment and a large R/Bioconductor package set live | 15–25 minutes of explanation, plus unpredictable download/build time | Dependency compilation and repository access can dominate a live session. Explain the sequence and show a prepared success check in the main lecture. |
| Full Globus endpoint selection and a large dataset transfer | 10–15 minutes, excluding transfer duration | Authentication, source selection, folder permissions, and transfer verification need their own walkthrough. |
| GPU framework/CUDA compatibility and measuring GPU use | 10–15 minutes | A GPU request is simple; a working tool-specific software stack may not be. |
| Selecting resources for a particular bulk / single-cell / spatial pipeline | 15–30 minutes | Input scale, tool version, thread settings, and peak memory must be discussed for that actual pipeline. |
| Raw-data processing and analysis methods | A separate session | Alignment, quantification, preprocessing, statistics, and interpretation are analysis training beyond HPC operation. |
| Arrays, workflow managers, containers, and preemptible queues | A separate follow-up session | These become useful after one reproducible job works. |

For an approximately one-hour explanation, keep returning to the same input, project directory, and expected result. Spend the most attention on the folder-navigation transcript, the first job submission and message, and the transition from package setup to the analysis job. The nine shell slides are explanations, not exercises; log following comes later when a job has created its files. Use prepared outputs and keep Python plus pandas as the main worked route. Explain the R and Conda slides as brief alternatives rather than executing every installation. Do not spend the lecture waiting for a large installation or queue allocation. No audience exercise is needed.

## Navigation implementation

The deck follows [Reveal.js vertical slides](https://revealjs.com/vertical-slides/): six top-level `<section>` stacks, each containing its topic’s slides. `navigationMode: "default"` preserves left/right topic changes, up/down within-topic movement, and Space through the full sequence. The Course map slide has been removed; the Contents control still provides direct navigation. The PDF flattens that same reading order. No course duration, cumulative timing, or timing table appears in the presentation.
