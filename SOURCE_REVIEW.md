# Source coverage and teaching sequence

Source coverage reviewed 27 October 2026. The sequence was streamlined on 28 October 2026, from 47 to 39 slides, while retaining the steps needed to request access, submit a job and verify its result.

## The continuous main route

| Step | Slides | What the listener can identify before moving on |
| --- | --- | --- |
| Understand the example and obtain access | 1–5 | Expected result, account approval, NetID, allocation/partition pair, project path, and successful SSH login. |
| Connect VS Code and upload the supplied project | 6–11 | Local versus remote actions, extension installation, connection, storage, completed upload, and each remote project file. |
| Inspect the input with everyday shell commands | 12–18 | Current host/directory, command structure, complete cd/pwd and ls examples, file operations, searching, line counts and disk usage. |
| Submit and verify the first small job | 19–23 | Login/compute roles, saved hello.sbatch, resources, returned ID, queue states, final accounting and expected message. |
| Allocate a shell and prepare Python | 24–29 | Compute shell, Python module, .venv, pandas installation/import, version record, and explicit return to login. |
| Submit the analysis and check its output | 30–34 | Same module/environment in analysis.sbatch, new job ID, matching logs, accounting, expected CSV and remote viewing. |
| Optional adaptations after the main result | 35–37 | GPU or named-node requests when required, or a separate R setup and job route. |
| Troubleshooting and references | 38–39 | First checks for common errors and official documentation/support. |

The main route uses one project throughout. data/samples.csv has three sample rows with counts 1000, 1500 and 1200. analysis.py uses pandas to write results/summary.csv with 3 samples and 3700 total reads. The expected result appears at the beginning and is checked after the batch job.

## Consolidation

- One simple local/remote diagram replaces two explanations. The Microsoft architecture figure remains in assets/ as supporting material.
- Opening the remote destination and uploading share one screenshot-led sequence, with a direct download link.
- One head example explains command syntax and shows the actual input; cat/less and help remain concise alternatives.
- Terminal shortcuts appear where they are used instead of on a separate reference page.
- First submission and queue checking share one page; final accounting and the actual message remain a separate check.
- GPU and named-node requests share one optional page after the Python result. R setup and the R job are adjacent there too.
- The completed-project tree is integrated into viewing the result in VS Code. Conda remains in examples/README.md.

Complete cd/pwd and ls transcripts, the four concept diagrams, import verification, activation lifetime, explicit compute-shell exit and final result verification remain because they establish different steps and outcomes.

## Source coverage

[ICC access](https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/accessing.html) supports account routes, hostnames and password/Duo authentication. Approval, the account/partition pair and an approved project path precede connection. Connection multiplexing and advanced SSH configuration are left for troubleshooting.

[ICC running jobs](https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/running_jobs.html) supports allocation selection, batch/interactive jobs, GPU requests, queue checking and cancellation. The resource diagram follows [upstream Slurm](https://slurm.schedmd.com/sbatch.html) for tasks versus CPUs per task. Arrays, MPI, preemption and checkpointing are beyond the introductory route.

[ICC storage](https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html) supports selecting storage before transfer. Home, approved project storage, temporary scratch and disk usage remain. Large transfers are referred to the group’s supported service, commonly Globus; endpoint setup and node-local scratch are further topics.

[ICC software](https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/software.html) and upstream Python/R instructions support modules and writable package locations. The same compatible Python module must be used for setup and the batch job. Available versions require confirmation in the actual session.

[Missing Semester’s shell introduction](https://missing.csail.mit.edu/2026/course-shell/) and [command-line environment lecture](https://missing.csail.mit.edu/2026/command-line-environment/) support commands, arguments, paths and files. This lecture applies them to the uploaded project and distinguishes filenames/file contents, hidden/missing files, disk usage/quota, and lines/samples. Output redirection appears when saving package versions. Pipes, shell programming, Git and profiling remain further study.

[Microsoft Remote – SSH](https://code.visualstudio.com/docs/remote/ssh) supports the local editor/remote project workflow. The connection and Open Folder screenshots remain. Remote viewing or editing does not itself allocate compute resources.

## Continuity checks

1. The upload page supplies the material link, waits for transfer completion, and opens the remote demo folder before inspecting the CSV.
2. Explorer and the terminal use the same approved folder. A fresh demo has no .venv or generated summary; file inspection does not run the analysis.
3. hello.sbatch has its own job ID, final record and message before software preparation begins.
4. The allocated shell stays open through module selection, installation, import checking and version recording. The import check does not produce summary.csv.
5. Installation creates persistent files; activation selects them in a shell. exit returns to login, followed by hostname/pwd checks.
6. The next page prepares analysis.sbatch with the same module and environment. The minimal demo has no unseen email placeholder; optional mail settings remain in examples/.
7. The analysis has a new ID. Its logs are opened after they exist; Ctrl+C stops the log viewer without cancelling the job.
8. The final accounting, logs and expected CSV must agree. That same result is then opened or downloaded in VS Code.
9. Optional R setup uses a separate allocation. q(save = "no") leaves R before exit releases the shell; the following R job uses the same version and library.

The local/remote, login/compute, resource and installation/activation diagrams are on slides 6, 19, 21 and 28. The ICC overview, login banner and VS Code screenshots retain source credits and reading cues. Historical screenshot values are examples, not current resource guarantees.

## Further teaching and boundaries

Large package builds, GPU software compatibility, large-data transfer setup, resource sizing for a specific pipeline, workflow managers, containers and analysis methods need separate teaching time. Conda and full optional job templates remain available in examples/.

All data are synthetic and displayed cluster outputs are illustrative. No cluster account was accessed or Slurm job submitted while preparing the materials. Eligibility, module availability, installation behavior and queue waiting depend on the authorized setup.

The deck retains six horizontal topics with vertical slides, following [Reveal.js navigation](https://revealjs.com/vertical-slides/). The PDF uses the same order. There is no course-map slide, exercise, course-duration label or timing table. Contents, fullscreen and the laser pointer remain available.
