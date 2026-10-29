# Source review and teaching priorities

Reviewed 27 October 2026 against the supplied ICC guide and Missing Semester, with official upstream references for software installation and Slurm semantics. This is a coverage review for an introductory HPC lecture, not a review of analysis methods.

## What the lecture now covers

| Need in an actual analysis workflow | Topic / slides | Why it belongs |
| --- | --- | --- |
| Account access and login | Access, 1–4 | Explains cluster roles, approval prerequisites, login identity, and allocation details. |
| Local VS Code setup, storage, connection, and upload | Files in VS Code, 5–12 | Introduces VS Code with an official interface screenshot, separates local and remote work, selects a destination, and transfers a folder. |
| Everyday Unix commands | Shell essentials, 13–21 | Command structure, paths, ls options, mkdir/cp/mv/rm, text previews, find/grep/wc/du, help and shortcuts. |
| A first batch job | Slurm jobs, 22–26 | Explains shared storage and resources, submits hello.sbatch, checks the queue, and reads its short message. |
| Output files and email | Slurm jobs, 27 | Explains output/error filenames, the job ID token, and email settings. |
| GPU and named-node options | Slurm jobs, 28–29 | Decodes optional resource settings. |
| Interactive compute allocation | Slurm jobs, 30 | Opens the compute shell used for software preparation. |
| Python environment and packages | Software and packages, 31–34 | Loads Python, creates .venv, installs pandas, verifies the import, records versions, and explains installation versus activation. A brief exit reminder replaces the separate return-to-login page. |
| Conda alternative | Software and packages, 35 | Explains an environment file and verifies the import in a separate setup session. |
| Prepare, submit, and follow a job | Run and check, 36–38 | Reuses the software setup, submits analysis.sbatch, and reads its logs. |
| Open outputs in VS Code | Run and check, 39 | Inspects output contents and explains viewing and downloading. |
| Run an R project | Run and check, 40 | Shows a base-R batch job without an add-on package prerequisite. |
| Troubleshooting | Run and check, 41 | Connects common errors to the first useful check. |
| References and support | Run and check, 42 | Links current system documentation and account-specific assistance. |

## Findings from the supplied websites

[ICC access](https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/accessing.html) covers account routes, password/Duo authentication, hostnames, and connection reuse. Account and login steps remain in the core lecture. ControlMaster configuration is left for connection troubleshooting because it is not required to submit the first analysis.

[ICC running jobs](https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/running_jobs.html) extends far beyond basic submission. The useful first-workflow material includes login-node limits, account/partition pairing, interactive jobs, GPU requests, queue inspection, and cancellation. Those are included. Preemption, checkpointing, job arrays, MPI, and recurring jobs require a separate explanation and are not part of this introductory sequence.

[ICC storage](https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html) makes storage policy and data transfer part of the working routine. Home, project, scratch, disk usage, and the large-transfer role of Globus are included. The reminders now specify the limited 100 GiB home soft quota, shared project capacity with no snapshots, and scratch purging typically after 30 days without access or earlier under storage pressure. These details were rechecked on 28 October 2026. Node-local scratch and detailed transfer endpoint setup are deferred.

[ICC software](https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/software.html) directly supports modules and installing R packages into writable locations. The lecture retains module selection and Python package setup. R package installation remains in the optional example reference rather than a separate slide. Exact available versions and permissions remain account/site-specific. The lecture records an example Python module while asking the presenter to verify it before use.

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

The lecture follows the operational steps from account access to reading job outputs. Small bundled files make command examples concrete, but the separate example introduction, file inventories, numerical result-check page, and completed-project recap have been removed. The full calculation and expected output remain in the supplementary demo documentation.

1. Establish identity, allocation, the project location, and the connection.
2. Choose storage, open the remote destination in VS Code, upload `demo/`, and inspect the input.
3. Open a terminal in that same folder. Read command structure and paths, organize files, and check the small CSV without changing it.
4. Submit `hello.sbatch` and inspect its expected message. This closes the first-job loop before adding analysis dependencies.
5. Obtain an interactive compute shell and keep it open for software preparation.
6. Load Python, create `.venv`, install pandas, verify the import, and record package versions. Explain that the environment files persist while activation belongs to the current shell. Then exit the compute shell once and confirm the login host and project directory. Conda follows as a separate alternative requiring its own appropriate allocated setup session; the base-R job example appears after the main result check.
7. Save `analysis.sbatch` with the same software setup and submit it. Keep the new analysis job ID separate from the earlier hello ID.
8. Follow the analysis logs after they exist, inspect the logs, then open the generated output and check its contents.
9. Use VS Code to view or download outputs; retain the inputs, scripts, and environment record with the results.

The minimal `demo/` folder supports this continuous Python route. The complete `examples/` collection retains R, Conda, and GPU templates. R and Conda are explicitly presented as alternative routes for other projects, not additional installations to perform in the main walkthrough. Conda setup uses a separate compute allocation. The later base-R job requires no package setup and is submitted from the login shell in its project folder.

The initial folder has neither `.venv` nor a generated summary. Hidden-environment listing appears only after creation, and log-following appears after submission. The import check does not run the analysis, so a pre-existing interactive result cannot be mistaken for the batch result. The official cluster overview, login banner, and Microsoft Remote - SSH figures retain short reading cues and source credits. Historical values and example paths in screenshots are labeled as such. All displayed cluster outputs are illustrative expectations. The materials do not claim an actual ICC job was run.

## Beginner review and repairs

The review asked whether a first-time listener could identify where to act, read the command and its options, recognize the expected result, and understand why the next action follows. It led to these changes rather than adding more advanced material:

| Gap identified | Clarification now provided |
| --- | --- |
| Login and upload assumed a prepared laptop | The slides identify the local terminal, decode the SSH command, cover local VS Code and extension installation, and locate demo in the unzipped package. |
| Instructions, placeholders, prompts, and output could be confused | Uppercase replacements and command-entry conventions are explained. The quoted-path illustration no longer asks the listener to open an absent file. Navigation commands have matching output examples; optional exit and cancellation commands are distinguished from the worked sequence. |
| Command outcomes were shown without all relevant option meanings | The search and disk-usage material is split into two slides. The displayed shell, Slurm, Python, R, and Conda options and symbols receive explicit explanations on slides or in their accompanying notes. |
| The compute-shell transition and software lifetime were easy to miss | srun, --pty bash, and line continuation are decoded. Python installation is immediately followed by import verification, version recording, an explanation of persistent files versus per-shell activation, and a short reminder to exit the allocation and confirm the login host. |
| Alternative language routes could interrupt or accidentally reuse the main setup session | Conda setup requires its own allocated shell after the main Python setup ends. The later R example uses base R and is submitted as a batch job without a separate package-installation session. |
| A job identifier or quiet log could be mistaken for success | The first and analysis jobs use distinct illustrative IDs. The first job is followed by its expected message. For the analysis job, the slides connect queue status, logs, and opening the actual output. Detailed accounting and numerical example checks remain in supplementary material. Optional cancellation is not presented as a step to perform on the successful example. |
| The interactive batch explanation was incomplete in the static handout | All ten hello.sbatch line explanations are included in the printed PDF, while the browser retains clickable lines. |

The review preserves all original figures, the basic-command coverage, six horizontal topics with vertical slides, and the runnable example files. Remaining uncertainties are account-specific values, available software versions, queue waiting, and installation behavior; the slides identify the values to confirm instead of presenting them as universal guarantees.

The 42-slide version includes four simple teaching diagrams. Slide 7 separates the local VS Code window from remote project files and terminal processes. Slide 22 shows submission on the login node, Slurm allocation, execution on a compute node, and one shared demo folder. Slide 24 uses one node containing two tasks with two CPUs each to explain the resource hierarchy and the total of four requested CPUs; it explicitly keeps hello.sbatch at its original 1/1/1 settings. Slide 34 separates installation into persistent .venv files from activation in the current shell or a later batch job. The official ICC overview and Microsoft architecture figure remain in the deck; the simpler diagrams focus on these distinctions without replacing their source material.

## Speaker-script and wording review — 28 October 2026

Applied the research-talk-slides principles of one purpose per page, plain wording, and explicit transitions to this instructional course. All 42 notes are now spoken English paragraphs rather than directions to a presenter. Titles, order, diagrams, examples, and existing commands are preserved.

The review checks each instruction for a location, action, and observable outcome. Changes include naming the connected host in VS Code, using the job ID returned by the actual submission, stating that Slurm substitutes `%j`, identifying an error-free package-version output as the import check, and giving concrete first actions for common errors. The verified `quota` command now appears beside `du` so storage usage is not confused with the storage allowance. Conda remains an optional alternative; no extra exercises or advanced workflow pages were added.

## Topics that need more teaching time

These estimates are for the presenter, not labels on the slides.

| Extra explanation or live demonstration | Suggested additional time | Why |
| --- | --- | --- |
| Installing both a Python environment and a large R/Bioconductor package set live | 15–25 minutes of explanation, plus unpredictable download/build time | Dependency compilation and repository access can dominate a live session. Treat large R package installations as an optional follow-up; the main lecture demonstrates Python package setup. |
| Full Globus endpoint selection and a large dataset transfer | 10–15 minutes, excluding transfer duration | Authentication, source selection, folder permissions, and transfer verification need their own walkthrough. |
| GPU framework/CUDA compatibility and measuring GPU use | 10–15 minutes | A GPU request is simple; a working tool-specific software stack may not be. |
| Selecting resources for a particular bulk / single-cell / spatial pipeline | 15–30 minutes | Input scale, tool version, thread settings, and peak memory must be discussed for that actual pipeline. |
| Raw-data processing and analysis methods | A separate session | Alignment, quantification, preprocessing, statistics, and interpretation are analysis training beyond HPC operation. |
| Arrays, workflow managers, containers, and preemptible queues | A separate follow-up session | These become useful after one reproducible job works. |

For an approximately one-hour explanation, focus on the connection, working directory, software environment, and job state. Spend the most attention on the folder-navigation transcript, the first job submission and message, and the transition from package setup to the analysis job. The nine shell slides are explanations, not exercises; log following comes later when a job has created its files. Use prepared outputs and keep Python plus pandas as the main worked route. Explain the R and Conda slides as brief alternatives rather than executing every installation. Do not spend the lecture waiting for a large installation or queue allocation. No audience exercise is needed.

## Navigation implementation

The deck follows [Reveal.js vertical slides](https://revealjs.com/vertical-slides/): six top-level `<section>` stacks, each containing its topic’s slides. `navigationMode: "default"` preserves left/right topic changes, up/down within-topic movement, and Space through the full sequence. The Course map slide has been removed; the Contents control still provides direct navigation. The PDF flattens that same reading order. No course duration, cumulative timing, or timing table appears in the presentation.
