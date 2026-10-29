"""Editable illustrations of job state, output streams, and log viewing."""


def workflow_diagram(name):
    diagrams = {
        'queue-state': '''
<div class="workflow-figure workflow-queue" role="img" aria-label="Illustrative progress of job 123456. PD means pending while waiting for resources. R means the job is running. After it leaves the queue, read slurm-123456.out and check the result. Leaving the queue does not prove success.">
  <div class="workflow-caption">Illustration: job 123456</div>
  <div class="workflow-queue-grid">
    <div class="workflow-state workflow-pending">
      <code class="workflow-state-code">PD</code>
      <strong>Pending</strong>
      <span>Queued; check the reason</span>
    </div>
    <b class="workflow-arrow" aria-hidden="true">→</b>
    <div class="workflow-state workflow-running">
      <code class="workflow-state-code">R</code>
      <strong>Running</strong>
      <span>Using allocated resources</span>
    </div>
    <b class="workflow-arrow" aria-hidden="true">→</b>
    <div class="workflow-state workflow-check-output">
      <span class="workflow-status-label">No longer listed</span>
      <strong>Read the output</strong>
      <code>slurm-123456.out</code>
    </div>
  </div>
  <div class="workflow-caution">Leaving the queue does not prove success.</div>
</div>''',
        'job-streams': '''
<div class="workflow-figure workflow-streams" role="img" aria-label="Illustration for analysis job 123457. Ordinary program output goes to analysis-123457.out. Error and diagnostic messages go to analysis-123457.err. Slurm end or failure events can send an email to the configured recipient. Slurm replaces percent j with the job ID in filenames. Diagnostic logs may also contain ordinary progress messages.">
  <div class="workflow-caption">Illustration: analysis job 123457. Slurm fills in <code>%j</code>.</div>
  <div class="workflow-stream-row">
    <div class="workflow-stream-source"><strong>Program output</strong><span>Ordinary messages</span></div>
    <b class="workflow-arrow" aria-hidden="true">→</b>
    <div class="workflow-stream-target workflow-output-file"><code>analysis-<b class="workflow-job-id">123457</b>.out</code></div>
  </div>
  <div class="workflow-stream-row">
    <div class="workflow-stream-source"><strong>Program diagnostics</strong><span>Errors and other messages</span></div>
    <b class="workflow-arrow" aria-hidden="true">→</b>
    <div class="workflow-stream-target workflow-error-file"><code>analysis-<b class="workflow-job-id">123457</b>.err</code></div>
  </div>
  <div class="workflow-stream-row">
    <div class="workflow-stream-source"><strong>Slurm events</strong><span><code>END</code> or <code>FAIL</code></span></div>
    <b class="workflow-arrow" aria-hidden="true">→</b>
    <div class="workflow-stream-target workflow-email"><span>Email to</span><code>YOUR_NETID@illinois.edu</code></div>
  </div>
  <div class="workflow-footnote">An <code>.err</code> file can also contain progress messages. Read its contents.</div>
</div>''',
        'log-viewer': '''
<div class="workflow-figure workflow-log" role="img" aria-label="Illustration of a batch job and its separate log viewer. Job 123457 writes analysis-123457.out. A terminal running tail -f reads that log. Control C stops the tail viewer while the batch job continues running.">
  <div class="workflow-caption">Illustration: a job and its log viewer</div>
  <div class="workflow-log-top">
    <div class="workflow-batch-job">
      <strong>Batch job</strong>
      <code>123457</code>
      <span class="workflow-running-badge">Continues running</span>
    </div>
    <div class="workflow-write-link"><span>writes</span><b class="workflow-arrow" aria-hidden="true">→</b></div>
    <div class="workflow-log-file"><span>Log file</span><code>analysis-123457.out</code></div>
  </div>
  <div class="workflow-log-read"><span><code>tail -f</code> reads this file</span><b aria-hidden="true">↓</b></div>
  <div class="workflow-terminal-viewer">
    <span class="workflow-viewer-label">Terminal log viewer</span>
    <code>tail -f analysis-123457.out</code>
    <div class="workflow-viewer-stop"><strong>Ctrl+C</strong><span>Stops this viewer</span></div>
  </div>
  <div class="workflow-footnote">The job and log viewer are separate processes.</div>
</div>''',
    }
    return diagrams[name]
