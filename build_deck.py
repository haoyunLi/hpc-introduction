from pathlib import Path
import html, json, re, shutil
from concept_diagrams import concept_diagram

ROOT = Path(__file__).resolve().parent
E = html.escape
SOURCES = {
 'access': ('ICC · Accessing the System', 'https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/accessing.html'),
 'start': ('ICC · Getting Started', 'https://docs.ncsa.illinois.edu/systems/icc/en/latest/getting_started.html'),
 'request': ('Illinois Computes · Request resources', 'https://computes.illinois.edu/submitrequest/'),
 'routes': ('Campus Cluster · Access routes', 'https://campuscluster.illinois.edu/access/'),
 'jobs': ('ICC · Running Jobs', 'https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/running_jobs.html'),
 'storage': ('ICC · Storage and Data', 'https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html'),
 'software': ('ICC · Software and Modules', 'https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/software.html'),
 'prog': ('ICC · VS Code setup', 'https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/prog_env.html#visual-studio-code'),
 'ood': ('ICC · Open OnDemand', 'https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/ood.html'),
 'shell': ('Missing Semester · Introduction to the Shell (2026)', 'https://missing.csail.mit.edu/2026/course-shell/'),
 'cli': ('Missing Semester · Command-line Environment (2026)', 'https://missing.csail.mit.edu/2026/command-line-environment/'),
 'script': ('Missing Semester · Shell Tools and Scripting (2020)', 'https://missing.csail.mit.edu/2020/shell-tools/'),
 'wrangle': ('Missing Semester · Data Wrangling (2020)', 'https://missing.csail.mit.edu/2020/data-wrangling/'),
 'vscode': ('Microsoft · Remote - SSH', 'https://code.visualstudio.com/docs/remote/ssh'),
 'vscode_ui': ('Microsoft · VS Code user interface', 'https://code.visualstudio.com/docs/editing/getting-started/userinterface'),
 'vscode_setup': ('Microsoft · VS Code setup', 'https://code.visualstudio.com/docs/setup/setup-overview'),
 'transfer': ('Microsoft · File import and download implementation', 'https://github.com/microsoft/vscode/blob/main/src/vs/workbench/contrib/files/browser/fileImportExport.ts'),
 'markdown': ('Microsoft · Markdown preview', 'https://code.visualstudio.com/docs/languages/markdown'),
 'extensions': ('Microsoft · Remote extensions', 'https://code.visualstudio.com/docs/remote/faq#extensions-authors'),
 'csv': ('Rainbow CSV · Extension documentation', 'https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv'),
 'pdf': ('vscode-pdf · Extension documentation', 'https://marketplace.visualstudio.com/items?itemName=tomoki1207.pdf'),
 'jupyter': ('Microsoft · Jupyter extension', 'https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter'),
 'interactive': ('Microsoft · Python Interactive Window', 'https://code.visualstudio.com/docs/python/jupyter-support-py'),
 'sbatch': ('SchedMD · sbatch', 'https://slurm.schedmd.com/sbatch.html'),
 'srun': ('SchedMD · srun', 'https://slurm.schedmd.com/srun.html'),
 'sacct': ('SchedMD · sacct', 'https://slurm.schedmd.com/sacct.html'),
 'states': ('SchedMD · Job states', 'https://slurm.schedmd.com/job_state_codes.html'),
 'computes': ('Illinois Computes · Official photograph', 'https://computes.illinois.edu/'),
}

SOURCES.update({
 'python': ('Python Packaging · pip and venv', 'https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/'),
 'python_cli': ('Python · Command-line options', 'https://docs.python.org/3/using/cmdline.html'),
 'radmin': ('R · Installing packages and libraries', 'https://cran.r-project.org/doc/manuals/r-release/R-admin.html#Add_002don-packages'),
 'bioc': ('Bioconductor · Installation', 'https://bioconductor.org/install/'),
 'conda': ('Conda · Managing environments', 'https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html'),
 'scanpy': ('Scanpy · Installation', 'https://scanpy.readthedocs.io/en/stable/installation.html'),
 'seurat': ('Seurat · Installation', 'https://satijalab.org/seurat/articles/install_v5.html'),
 'reveal': ('Reveal.js · Vertical slides', 'https://revealjs.com/vertical-slides/'),
})

slides=[]
def code(text, label='', small=False):
    return (f'<div class="code-label">{E(label)}</div>' if label else '') + f'<pre class="{"small-code" if small else ""}"><code>{E(text.strip())}</code></pre>'
def transcript(text, label=''):
    lines='\n'.join(f'<span class="terminal-command">{E(line)}</span>' if line.startswith('$ ') else E(line) for line in text.strip().splitlines())
    return (f'<div class="code-label">{E(label)}</div>' if label else '') + f'<pre class="terminal-transcript"><code>{lines}</code></pre>'
def p(text, cls=''): return f'<p class="{cls}">{text}</p>'
def rows(items): return '<div class="rows">'+''.join(f'<div class="row"><strong>{a}</strong><span>{b}</span></div>' for a,b in items)+'</div>'
def table(headers,data,cls=''):
    return f'<table class="{cls}"><thead><tr>'+''.join(f'<th>{x}</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{x}</td>' for x in r)+'</tr>' for r in data)+'</tbody></table>'
def cols(a,b,ratio=''): return f'<div class="cols {ratio}"><div>{a}</div><div>{b}</div></div>'
def img(file,alt,caption='',cls=''): return f'<figure class="{cls}"><img src="assets/{file}" alt="{E(alt)}">'+(f'<figcaption>{caption}</figcaption>' if caption else '')+'</figure>'
def note(text): return p(text,'callout')
def annotated(lines):
    buttons=''.join(f'<button type="button" class="code-line {"active" if i==2 else ""}" data-explain="{E(meaning)}"><span>{i+1:02}</span>{E(line)}</button>' for i,(line,meaning) in enumerate(lines))
    explanations=''.join(f'<div><b>{i+1:02}</b><span>{E(meaning)}</span></div>' for i,(_,meaning) in enumerate(lines))
    return '<div class="annotated"><div class="annotation-code">'+buttons+'</div><div class="annotation-text"><div class="code-label screen-only">Select a line</div><p class="line-explanation screen-only">'+E(lines[2][1])+'</p><div class="print-only annotation-list">'+explanations+'</div></div></div>'
def S(title,body,notes,sources=(),section='',cls=''):
    slides.append(dict(title=title,body=body,notes=notes.strip(),sources=list(sources),section=section,cls=cls))

exec(compile((ROOT/'course_content.py').read_text(),str(ROOT/'course_content.py'),'exec'))

def render():
    chapters=list(dict.fromkeys(s['section'] for s in slides))
    used_sources={k for s in slides for k in s['sources']} | {'reveal'}
    chapter_html=[]; all_sections=[]; note_pages=[]
    for h,chapter in enumerate(chapters):
        grouped=[s for s in slides if s['section']==chapter];sections=[]
        for v,s in enumerate(grouped):
            i=len(all_sections)
            s.update(index=i,h=h,v=v,anchor=f'{h}/{v}')
            refs=' · '.join(f'<a href="{SOURCES[k][1]}" target="_blank" rel="noopener">{E(SOURCES[k][0])}</a>' for k in s['sources'])
            notes=''.join(f'<p>{E(x)}</p>' for x in s['notes'].split('\n\n'))
            title=s['title'];plain=re.sub('<[^>]+>',' ',title)
            section=f'''<section class="lecture-slide {s['cls']}" data-title="{E(plain)}" data-section="{E(chapter)}" data-index="{i}" data-h="{h}" data-v="{v}"><div class="slide-inner"><header><div class="section-name">{h+1:02} · {E(chapter)}</div><h1>{title}</h1></header><main class="slide-body">{s['body']}</main><footer><div class="sources">{refs}</div><span class="page-number">{i+1:02} / {len(slides)}</span></footer></div><aside class="notes">{notes}<p>{refs}</p></aside></section>'''
            sections.append(section);all_sections.append(section)
            note_pages.append(f'<article id="slide-{i+1}"><div class="meta">{h+1}.{v+1} · SLIDE {i+1:02} · {E(chapter)}</div><h2>{title}</h2>{notes}<div class="refs">{refs}</div></article>')
        chapter_html.append(f'<section class="chapter-stack" data-chapter="{E(chapter)}">'+''.join(sections)+'</section>')
    top='''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Getting started on the Illinois Campus Cluster</title><link rel="stylesheet" href="vendor/reveal/dist/reveal.css"><link rel="stylesheet" href="theme.css?v=language-reviewed"></head><body><div class="reveal"><div class="slides">'''
    bottom='''</div></div><nav id="tools" aria-label="Presentation tools"><button id="contents-btn" title="Contents (C)">Contents</button><button id="notes-btn" title="Speaker notes (N)">Notes</button><button id="fullscreen-btn">Full screen</button><button id="laser-btn" aria-pressed="false" title="Toggle laser pointer (L)">Laser</button><a href="lecturer-notes.html" target="_blank">Lecturer guide ↗</a><a id="github-profile-link" href="https://github.com/haoyunLi" target="_blank" rel="noopener noreferrer" title="Haoyun Li on GitHub">GitHub ↗</a><span class="nav-help">← → Topics &nbsp; ↑ ↓ Within topic</span><span id="position-label"></span></nav><dialog id="contents"><div class="dialog-header"><h2>Course contents</h2><button class="close-dialog" aria-label="Close contents">×</button></div><div id="contents-list"></div></dialog><aside id="notes-panel" hidden><button id="close-notes" aria-label="Close notes">×</button><div id="note-content"></div></aside><script src="vendor/reveal/dist/reveal.js"></script><script src="vendor/reveal/plugin/notes/notes.js"></script><script src="app.js?v=presenter-laser"></script></body></html>'''
    (ROOT/'index.html').write_text(top+''.join(chapter_html)+bottom)
    print_css='''@page{size:1440px 810px;margin:0}html,body{margin:0;padding:0;width:1440px}.reveal,.slides{width:1440px}.reveal .slides>section{display:block;position:relative;width:1440px;height:810px;break-after:page;overflow:hidden}.slide-inner{width:1440px;height:810px}aside.notes{display:none}.print-only{display:block}.screen-only{display:none}.annotation-text .print-only p{font-size:25px;line-height:1.4;margin:22px 0}.chapter-map button{color:#132b47}'''
    (ROOT/'print.html').write_text('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>ICC lecture</title><link rel="stylesheet" href="theme.css?v=language-reviewed"><style>'+print_css+'</style></head><body><div class="reveal"><div class="slides">'+''.join(all_sections)+'</div></div></body></html>')
    (ROOT/'slides.json').write_text(json.dumps(slides,indent=2))
    guide_css='''body{font:19px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:#172c44;background:#f4f2ed;margin:0}main{max-width:900px;margin:55px auto;padding:0 28px}h1{font-size:42px;line-height:1.1}h2{font-size:27px;line-height:1.25}article{background:#fff;padding:30px 40px;margin:25px 0;break-inside:avoid}.meta{font:700 14px/1.4 sans-serif;color:#aa3d16;letter-spacing:1px}.refs{font-size:13px}a{color:#1b6078}header{margin-bottom:40px}@media print{body{font-size:12pt;background:white}main{margin:0;max-width:none;padding:0}article{padding:12px 0;margin:0 0 22px;border-bottom:1px solid #ccc}header{break-after:page}.refs{font-size:9pt}}@page{size:A4;margin:18mm}'''
    (ROOT/'lecturer-notes.html').write_text('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Lecturer guide · ICC</title><style>'+guide_css+'</style></head><body><main><header><p class="meta">ENGLISH SPEAKING SCRIPT</p><h1>Getting started on the Illinois Campus Cluster</h1><p>Use left/right to change topic, up/down within a topic, and Space to follow all slides. C opens Contents, N opens notes, F enters full screen, S opens the separate presenter window, L toggles the laser pointer, and Esc opens the overview. In the presenter window, point inside the current slide preview to show the laser on the audience display. The script lines are clickable.</p><p>Each numbered section is a spoken English script for its matching slide. The lecture uses a small example project. Outputs are illustrative unless explicitly identified as local checks. Replace allocation placeholders before a live run. No cluster login or Slurm submission was performed while preparing the materials.</p><p><a href="index.html">Presentation</a> · <a href="SOURCE_REVIEW.md">Source coverage and teaching priorities</a> · <a href="SOURCES.md">References</a></p></header>'+''.join(note_pages)+'</main></body></html>')
    assets=json.loads((ROOT/'assets/SOURCES.json').read_text())
    visible_assets=[a for a in assets if a['file'] in ''.join(all_sections)]
    (ROOT/'SOURCES.md').write_text('# Sources and credits\n\nReviewed 27 October 2026. Independent educational adaptation.\n\n## References\n\n'+'\n'.join(f'- [{name}]({url})' for key,(name,url) in SOURCES.items() if key in used_sources)+'\n\n## Images and examples\n\n'+'\n'.join(f'- `{a["file"]}`: {a["caption"]} Credit: {a["credit"]}. [Source]({a["source_page"]}); [asset]({a["asset_url"]}).' for a in visible_assets)+'\n- The original HTML workflow diagrams are illustrations, not live screenshots. Official diagrams and example UI screenshots retain their source credits.\n- Commands and small example datasets are adapted or newly written for explanation. They do not report a real research analysis.\n\n## Reuse\n\nMissing Semester publishes its materials under CC BY-NC-SA. Original lecture prose and examples are supplied under CC BY-NC-SA 4.0. Third-party photographs retain their owners’ rights. Reveal.js is bundled under its MIT license.\n\n## Scope\n\nModule names, resource eligibility, GPU types, limits, and storage permissions must be checked for the presenter’s account. The course does not request a new allocation, install packages on ICC, or submit jobs automatically.\n')
    print(f'Built {len(slides)} slides in {len(chapters)} horizontal topics: '+', '.join(f'{c} ({sum(s["section"]==c for s in slides)})' for c in chapters))

if __name__=='__main__': render()
