"""Adjacent workflow steps combined without removing commands or their meanings."""
from html import escape
from workflow_diagrams import workflow_diagram


def pre(text):
    return '<pre><code>' + escape(text) + '</code></pre>'


def heading(text):
    return '<h2 class="merge-heading">' + text + '</h2>'


def consolidated_page(name):
    if name == 'hello':
        return '<div class="merge-two">' + '<div>' + heading('1 · Submit the saved hello.sbatch') + pre('pwd\nls hello.sbatch\nsbatch hello.sbatch') + '<p class="merge-hint">Example response: <code>Submitted batch job 123456</code></p></div><div>' + heading('2 · Check the queue') + pre('squeue -u YOUR_NETID') + '<p><code>-u</code> selects your user.<br>Run it again for a fresh status snapshot.</p><p class="merge-hint">Use the job ID returned by your submission.</p></div></div>' + workflow_diagram('queue-state') + '<div class="merge-two merge-hello-end"><div>' + heading('3 · Read the output after the job ends') + pre('cat slurm-123456.out') + '<p class="merge-hint">Expected message: <strong>My first HPC job</strong></p></div><div>' + heading('Optional · Cancel an unwanted job') + pre('scancel 123456') + '<p class="merge-hint">Let hello finish here; cancellation stops that job.</p></div></div>'
    if name == 'environment':
        return '<p class="small">Continue in the same compute shell and remote demo folder.</p><div class="merge-two merge-env-columns"><div>' + heading('1 · Create, activate, and install') + pre('python -m venv .venv\nsource .venv/bin/activate\npython -m pip install pandas\nls -a') + '''<dl class="merge-definitions"><dt>-m venv</dt><dd>Run Python’s venv tool to create .venv.</dd><dt>source</dt><dd>Select .venv/bin/python in this shell.</dd><dt>-m pip</dt><dd>Run this Python’s package installer.</dd><dt>ls -a</dt><dd>Show hidden names, including .venv.</dd></dl></div><div>''' + heading('2 · Verify pandas, then record versions') + pre('python -c \\\n  "import pandas; print(pandas.__version__)"') + '<p><code>-c</code> runs the quoted code. Expect a version number with no import error.</p>' + pre('python -m pip freeze > requirements.txt') + '<p><code>freeze</code> lists installed package versions.<br><code>&gt;</code> writes them to the file, replacing existing contents.</p></div></div><p class="callout">Wait for pip to finish before checking the import. Keep this compute shell open.</p>'
    if name == 'analysis':
        return heading('1 · Edit analysis.sbatch, then save it — read left column, then right') + '<div class="merge-script-columns"><div>' + pre('#!/bin/bash\n#SBATCH --job-name=analysis\n#SBATCH --account=YOUR_ACCOUNT\n#SBATCH --partition=YOUR_PARTITION\n#SBATCH --nodes=1\n#SBATCH --ntasks=1\n#SBATCH --cpus-per-task=1\n#SBATCH --mem=1G\n#SBATCH --time=00:05:00') + '</div><div>' + pre('#SBATCH --output=analysis-%j.out\n#SBATCH --error=analysis-%j.err\n\nset -e\nmodule load python/3.11.11\nsource .venv/bin/activate\npython analysis.py') + '<p class="merge-hint"><code>set -e</code> stops on setup failure.<br>Use your account, partition, and available Python module.</p></div></div><div class="merge-analysis-submit"><div>' + heading('2 · Submit from the login shell in demo') + pre('pwd\nls data/samples.csv analysis.py analysis.sbatch\nsbatch analysis.sbatch') + '</div><div>' + heading('3 · Record the new job ID and check') + '<p class="merge-hint">Example response: <code>Submitted batch job 123457</code></p>' + pre('squeue -u YOUR_NETID') + '<p class="merge-hint">Use that ID in <code>analysis-JOBID.out</code><br>and <code>analysis-JOBID.err</code>.</p></div></div>'
    raise ValueError(name)
