# Getting started on the Illinois Campus Cluster

An English lecture following one small data-analysis project from requesting access to checking its result. There are 47 slides in six topics, with no exercises or audience tasks. Slide content has no course-duration labels or timing table.

## Presentation and downloads

- **[Open the online presentation](https://haoyunli.github.io/hpc-introduction/)**
- [Read the lecturer guide](https://haoyunli.github.io/hpc-introduction/lecturer-notes.html)
- [Download the PDF](https://github.com/haoyunLi/hpc-introduction/releases/latest/download/HPC_Introduction.pdf)
- [Download the complete offline package](https://github.com/haoyunLi/hpc-introduction/releases/latest/download/HPC_Introduction_Offline.zip)

The offline package includes the presentation, images, PDF, notes, and example files. Unzip it, keep the folder together, and open `HPC_Introduction/index.html`.

## Open and navigate

Open `index.html` in a desktop browser. The presentation, official diagrams and screenshots, original illustrations, cover photograph, and Reveal.js runtime are bundled for offline use. External documentation links require internet access. Keep the folder together.

- Left / right: change topic
- Up / down: move within a topic
- Space: follow all slides in reading order
- C / Contents: choose any topic or slide
- N / Notes: show the current English lecturer notes
- F / Full screen: full screen
- L / Laser: toggle a red laser pointer that follows the mouse, including in full screen
- Esc: view the topic stacks
- Click a line of the small batch script: read its explanation
- GitHub button in the bottom toolbar: open [Haoyun Li’s profile](https://github.com/haoyunLi)

The six topics are Access, Files in VS Code, Shell essentials, Slurm jobs, Software and packages, and Run and check. Use Contents to navigate directly; there is no course-map slide. The PDF follows the same order, flattening each vertical topic into consecutive pages. The ten line explanations for `hello.sbatch` are printed in the PDF as well as available interactively in the browser.

Use `lecturer-notes.html` for the complete guide. `SOURCE_REVIEW.md` records coverage of the two supplied websites and identifies topics that need more teaching time. `SOURCES.md` contains references and image credits.

The separate Reveal.js presenter window works best through a local server. From this folder:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8765/`. Double-click presentation and in-window notes also work without a server.

## Scope

The main route follows `demo/data/samples.csv` through `analysis.py` to `demo/results/summary.csv`. The input has three sample rows containing 1000, 1500, and 1200 reads. The expected result is 3 samples and 3700 total reads. That goal appears near the beginning and is checked again after the analysis job.

The sequence chooses storage before uploading the supplied `demo/` folder through VS Code. It then uses everyday shell commands to inspect the same files, submits `hello.sbatch` to check scheduling, prepares Python and pandas in an interactive compute shell, verifies the import, records versions, explains why activation is specific to one shell, and returns to the login shell. The prepared project then continues with `analysis.sbatch`, its logs, and its result. Log-following commands are introduced when the analysis log exists. The illustrated hello and analysis job IDs are different.

The shell material includes navigation, hidden files and listing options, folder creation, copying/moving/deleting, text previews, file and text search, line counts, disk usage, help, and shortcuts. GPU requests, node count, named nodes, and interactive compute sessions are retained. Output filenames are explained with the analysis job; email directives remain optional in the supplied templates.

Use `demo/` for the continuous Python walkthrough. It starts with the input and saved scripts, without an environment or generated result. `examples/` contains the fuller set of templates, including R, Conda, and GPU alternatives. The R and Conda slides come after the Python setup has been verified and its compute shell has been closed. They explain choices for other projects, not commands to run in the returned login shell or extra steps for the Python walkthrough. Copy the relevant alternative files into a separate project and obtain a separate suitable compute allocation when demonstrating those routes.

The beginner review makes local versus remote actions, command prompts, placeholders, option meanings, and expected results explicit. It also distinguishes commands to run in sequence from optional reference commands such as cancellation or leaving a shell.

Four simple diagrams explain local versus remote work (slide 7), login versus compute nodes with shared project storage (slide 23), nodes, tasks, and CPUs per task (slide 25), and installation versus activation (slide 35). They use the same `demo/` project and retain all official diagrams and screenshots. The installation diagram shows persistent package files separately from the environment selected by each shell or job.

All data are synthetic. The programs are not research-analysis pipelines or resource recommendations. Replace allocation, queue, GPU, node, and email placeholders before an authorized live run. Use the actual returned job IDs instead of the illustrative IDs on the slides.

## Edit

Edit the English slides and notes in `course_content.py`. The editable teaching diagrams are in `concept_diagrams.py`. `build_deck.py` supplies reusable formatting helpers and generates `index.html`, `print.html`, `lecturer-notes.html`, `slides.json`, and `SOURCES.md`. Run `python3 build_deck.py` after a content change. `app.js` handles navigation and `theme.css` controls appearance. Export the PDF separately from the flattened `print.html`.

The source review was performed on 27 October 2026. Site policy, available modules, queue access, and GPU names should be rechecked for the actual presenter before a live demonstration. No private cluster was accessed while preparing the materials.
