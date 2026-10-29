# Getting started on the Illinois Campus Cluster

An English beginner lecture covering account access, remote file management, everyday shell commands, software setup, job submission, and reading outputs. There are 38 slides: a standalone introduction followed by six numbered topics, with no exercises or audience tasks. Slide content has no course-duration labels or timing table.

## Presentation and downloads

- **[Open the online presentation](https://haoyunli.github.io/hpc-introduction/)**
- [Read the English speaking script](https://haoyunli.github.io/hpc-introduction/lecturer-notes.html)
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
- S: open the separate presenter window with the current slide, upcoming slide, and notes
- F / Full screen: full screen
- L / Laser: toggle a red laser pointer that follows the mouse, including in full screen
- Esc: view the topic stacks
- Click a line of the small batch script: read its explanation
- GitHub button in the bottom toolbar: open [Haoyun Li’s profile](https://github.com/haoyunLi)

The title page has its own horizontal Introduction unit. Press Right or Space to enter 01 · Access; use Down to move within that topic. The six numbered topics are Access, Files in VS Code, Shell essentials, Slurm jobs, Software and packages, and Run and check. Use Contents to navigate directly; there is no course-map slide. The PDF follows the same order, flattening each vertical topic into consecutive pages. The ten line explanations for `hello.sbatch` are printed in the PDF as well as available interactively in the browser.

Use `lecturer-notes.html` for the full English speaking script. The notes use conversational English throughout, matching the opening introduction: short sentences, natural explanations, and transitions that connect each step to the next. Command meanings, expected outputs, and important distinctions remain explicit. `SOURCE_REVIEW.md` records coverage of the two supplied websites and identifies topics that need more teaching time. `SOURCES.md` contains references and image credits.

For two displays, open the online presentation and press **S** to open the presenter window (allow popups if prompted). Put the main presentation on the audience display and use **F** there for full screen. Keep the presenter window on your own display. Click **Laser (L)** in the presenter window or press **L**, then move the mouse over its **current slide** preview: the audience sees the red dot at the matching position. Leaving that preview, turning Laser off, or changing slides clears the dot. The upcoming preview does not control the laser. **N / Notes** shows notes in the main window; use **S** when the audience should not see your notes.

Presenter laser synchronization works between these two connected windows in the same browser. For offline use, serve the folder locally instead of opening it with `file://`:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8765/`. Double-click presentation and in-window notes also work without a server.

## Scope

The slides focus on practical HPC operations. Small files in `demo/` supply concrete paths and commands; the separate example-goal, file-inventory, numerical-result, and completed-project pages have been removed. The complete runnable example and its expected output remain documented in `demo/README.md`.

Chapter 2 starts by defining VS Code and introducing Explorer, the editor, and the terminal in an official interface screenshot. The sequence then chooses storage before uploading a folder through VS Code, then introduces everyday shell commands, a small batch script, resource options, and software setup. A brief reminder beside the environment diagram explains how to leave the compute shell. Job preparation and submission lead directly to following logs and opening outputs in VS Code. Log-following commands are introduced when the log exists; the illustrated hello and analysis job IDs are different.

The shell material includes navigation, hidden files and listing options, folder creation, copying/moving/deleting, text previews, file and text search, line counts, disk usage, help, and shortcuts. GPU requests, node count, named nodes, and interactive compute sessions are retained. Output filenames and optional email directives have their own explanation page and remain in the supplied templates.

Use `demo/` for the continuous Python walkthrough. It starts with the input and saved scripts, without an environment or generated result. `examples/` contains the fuller set of templates, including R, Conda, and GPU alternatives. The Conda alternative follows the completed Python setup and uses its own allocated setup session. The R job example appears after opening outputs in VS Code and uses base R without additional package installation. Copy the relevant alternative files into their intended remote project; neither route is an extra step for the Python walkthrough.

The language review rewrites all 38 notes as spoken English and makes actions and success checks explicit: which host or folder to use, what to replace, what command output to expect, and what to do after an error. The storage table states limits and actions; the disk-usage slide distinguishes `du` from `quota`. The beginner review makes local versus remote actions, command prompts, placeholders, option meanings, and expected results explicit. It also distinguishes commands to run in sequence from optional reference commands such as cancellation or leaving a shell.

Four simple diagrams explain local versus remote work (slide 6), login versus compute nodes with shared project storage (slide 21), nodes, tasks, and CPUs per task (slide 23), and installation versus activation (slide 31). They use the same `demo/` project. The local/remote diagram combines the earlier architecture overview and file-location explanation into one page. The installation diagram shows persistent package files separately from the environment selected by each shell or job.

The visual walkthrough uses numbered Microsoft screenshots for Remote - SSH installation, connection, folder selection, and the terminal (slides 7, 8, 10, 12). The upload and result pages (11, 35) use explicitly labeled illustrations. Three further diagrams show queue progression (24), output/error/email destinations (25), and the difference between a running batch job and its log viewer (34). The installation slide also shows a close-up screenshot of the Extensions icon in the left Activity Bar. Screenshot sample hosts and paths are identified as Microsoft examples; no screenshot claims a live ICC connection.

Three adjacent action/check pairs are consolidated: submit and monitor hello (24), create/install/verify the Python environment (30), and prepare/submit the analysis (33). The merged pages keep the commands, expected job IDs, and option meanings. The shell-command section, resource diagram, GPU/node/email settings, Conda, and R remain intact.

All data are synthetic. The programs are not research-analysis pipelines or resource recommendations. Replace allocation, queue, GPU, node, and email placeholders before an authorized live run. Use the actual returned job IDs instead of the illustrative IDs on the slides.

## Edit

Edit the English slides and notes in `course_content.py`. The editable teaching diagrams are in `concept_diagrams.py` and `workflow_diagrams.py`. `vscode_visuals.py` supplies the annotated screenshots and file-operation illustrations; their styles are in `vscode-visuals.css` and `workflow-visuals.css`. `build_deck.py` supplies reusable formatting helpers and generates `index.html`, `print.html`, `lecturer-notes.html`, `slides.json`, and `SOURCES.md`. Run `python3 build_deck.py` after a content change. `consolidated_pages.py` and `consolidated-pages.css` define the combined workflow pages. `app.js` handles navigation and `theme.css` controls appearance. Export the PDF separately from the flattened `print.html`.

The source review was performed on 27 October 2026. Site policy, available modules, queue access, and GPU names should be rechecked for the actual presenter before a live demonstration. No private cluster was accessed while preparing the materials.
