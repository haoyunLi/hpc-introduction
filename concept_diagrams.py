"""Editable, semantic diagrams for beginner HPC concepts."""

def concept_diagram(kind):
    diagrams = {
        'local-remote': '''
<div class="concept-figure local-remote-figure" role="img" aria-label="The VS Code window is on the laptop. An SSH connection reaches project files and a terminal on the cluster. Saving edits updates the remote project file.">
  <div class="place local-place">
    <div class="place-heading">LOCAL <strong>Your laptop</strong></div>
    <div class="editor-window"><div class="window-label">VS Code window</div><div class="editor-content"><strong>View and edit</strong><code>analysis.py</code><span>Your screen, keyboard, and mouse</span></div></div>
  </div>
  <div class="connection"><strong>Remote - SSH</strong><div class="two-way-arrow" aria-hidden="true">⟷</div><span>View · edit · save</span></div>
  <div class="place remote-place">
    <div class="place-heading">REMOTE <strong>The cluster</strong></div>
    <div class="remote-project"><strong>Project files</strong><code>demo/analysis.py</code><span>Save updates this file.</span></div>
    <div class="remote-shell"><strong>Remote terminal</strong><span>Commands run on the cluster.</span></div>
  </div>
</div>''',
        'login-compute': '''
<div class="concept-figure nodes-figure" role="img" aria-label="On the login node, prepare and submit hello.sbatch. Slurm waits for resources and allocates a compute node, where the job runs. Both nodes access the same demo folder. Submitting a batch job leaves the terminal on the login node.">
  <div class="node-flow">
    <div class="node login-node"><div class="place-heading">LOGIN NODE</div><strong>Prepare and submit</strong><code>hello.sbatch</code><span>Your terminal stays here.</span></div>
    <div class="flow-link"><code>sbatch</code><b aria-hidden="true">→</b></div>
    <div class="scheduler"><strong>Slurm</strong><span>Wait for resources</span><small>The scheduler</small></div>
    <div class="flow-link"><span>Allocate</span><b aria-hidden="true">→</b></div>
    <div class="node compute-node"><div class="place-heading">COMPUTE NODE</div><strong>Run the job</strong><code>hello.sbatch</code><span>The program runs here.</span></div>
  </div>
  <div class="shared-connectors" aria-hidden="true"><span>↕</span><span>↕</span></div>
  <div class="shared-project"><strong>Same shared <code>demo/</code> folder</strong><span>Input · scripts · output</span></div>
</div>''',
        'install-activate': '''
<div class="concept-figure environment-figure" role="img" aria-label="With the environment active, pip install writes pandas into the shared demo/.venv folder. Activation selects that existing environment for one shell. A later job activates the same folder again; closing a shell does not delete the package files.">
  <div class="install-flow">
    <div class="environment-action"><strong>Install packages</strong><code>python -m pip install pandas</code><span>After creating and activating .venv</span></div>
    <div class="flow-link"><span>Write files</span><b aria-hidden="true">→</b></div>
    <div class="environment-folder"><div class="folder-tab">Shared project storage</div><code>demo/.venv/</code><span>Python + installed packages</span><strong>These files remain.</strong></div>
  </div>
  <div class="activation-heading"><strong>Activate in each new shell or job</strong><code>source .venv/bin/activate</code></div>
  <div class="activation-flow">
    <div class="shell-choice"><strong>Current compute shell</strong><div><code>python</code><b aria-hidden="true">→</b><code>.venv/bin/python</code></div></div>
    <div class="same-environment"><span>Same existing</span><strong>.venv</strong><span>No reinstall</span></div>
    <div class="shell-choice"><strong>A later batch job</strong><div><code>python</code><b aria-hidden="true">→</b><code>.venv/bin/python</code></div></div>
  </div>
</div>''',
        'resource-hierarchy': '''
<div class="concept-figure resource-figure" role="img" aria-label="Example resource request: one node contains two tasks. Each task has two CPUs reserved, for four requested CPUs total. Nodes count computers; ntasks counts tasks in the whole job; cpus-per-task counts CPUs for each task.">
  <div class="resource-layout">
    <div class="resource-definitions">
      <div><code>--nodes=1</code><span>1 computer</span></div>
      <div><code>--ntasks=2</code><span>2 tasks in the whole job</span></div>
      <div><code>--cpus-per-task=2</code><span>2 CPUs reserved for each task</span></div>
    </div>
    <div class="resource-node">
      <div class="resource-node-label"><strong>Node 1</strong><span>One computer</span></div>
      <div class="resource-tasks">
        <div class="resource-task"><strong>Task 1</strong><span>One program process</span><div class="resource-cpus"><span>CPU</span><span>CPU</span></div></div>
        <div class="resource-task"><strong>Task 2</strong><span>One program process</span><div class="resource-cpus"><span>CPU</span><span>CPU</span></div></div>
      </div>
    </div>
  </div>
  <div class="resource-equation"><strong>2 tasks × 2 CPUs/task = 4 CPUs requested</strong><span>ntasks is already the total; do not multiply by nodes again.</span></div>
</div>''',
    }
    return diagrams[kind]
