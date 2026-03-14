# Project Architecture

## Overview
Interview prep webapp for Trey Sisson pursuing COO/Integrator role at iRESTORE.
Python build system compiles markdown content files into a single-page HTML app.

## Directory Structure
```
iRestore/                              # Root workspace (Dropbox/Trey Sisson/iRestore/)
├── .claude/
│   ├── CLAUDE.md                      # Main instructions (read first every session)
│   └── docs/
│       ├── architecture.md            # THIS FILE — project structure & build system
│       ├── file-inventory.md          # All files in the workspace
│       └── interview-intel.md         # Key intel from interviews, current status
├── irestore-prep/                     # MAIN BUILD SYSTEM (also a git repo)
│   ├── build.py                       # Python build script
│   ├── template.html                  # HTML template
│   ├── content/                       # 30 markdown files with YAML frontmatter
│   │   ├── 01-kevin.md               # Kevin Chen profile
│   │   ├── 02-org.md                 # Org chart & team
│   │   ├── ...                        # (see file-inventory.md for full list)
│   │   └── 29-interview2-debrief.md  # Mar 13 interview debrief
│   └── dist/
│       └── index.html                 # Built output
├── irestore-prep-shareable/           # SHAREABLE VERSION (stripped of interview content)
│   ├── build.py                       # Same build system, different GROUPS config
│   ├── template.html                  # Modified title/header
│   ├── content/                       # 16 files (company/strategy/market/growth)
│   └── dist/
│       └── index.html                 # Built output
├── interview_prep.html                # MAIN WEBAPP — copy of irestore-prep/dist/index.html
├── mock_interview_practice.md         # 20 mock Q&As with coaching notes
└── (various source docs, transcripts, resumes — see file-inventory.md)
```

## Build Commands

### Main webapp
```bash
cd irestore-prep && python3 build.py 2>&1 && cp dist/index.html ../interview_prep.html
```

### Shareable version
```bash
cd irestore-prep-shareable && python3 build.py 2>&1
```

## Build System Details
- `build.py` reads all `content/*.md` files
- Each .md has YAML frontmatter: `id`, `title`, `icon`, `order`, `group`, `groupOrder`
- Groups are defined in `GROUPS` array in build.py (main: 5 groups, shareable: 4 groups)
- Subsections split on `## headers` with `<!-- id: xxx -->` comments
- Body content is HTML (NOT markdown) — the build does not convert markdown syntax
- Output is a single HTML file with JSON data embedded

## Content File Conventions
- Frontmatter fields: `id`, `title`, `icon`, `order`, `group`, `groupOrder`
- Groups (main): company, role, pitch, interview, gameday
- Groups (shareable): company, strategy, market, growth
- Use HTML for all body content (not markdown lists/headers)
- Subsection IDs via `<!-- id: xxx -->` after `## Header`

## Git Repos
- `irestore-prep/` — connected to GitHub, deployed to Netlify
- `irestore-prep-shareable/` — subfolder inside the same repo
- Netlify config: base dir `irestore-prep-shareable`, build cmd `python3 build.py`, publish `dist`

## Webapp Stats (as of Mar 14, 2026)
- Main: 5 groups, 30 sections, 187 subsections, ~803K chars
- Shareable: 4 groups, 16 sections, 85 subsections, ~285K chars
