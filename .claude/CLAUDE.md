# iRESTORE COO Interview Prep — Claude Instructions

## Who
Trey Sisson, interviewing for COO/Integrator at iRESTORE (CEO: Kevin Chen). DTC beauty device company, ~$90M+ revenue, 80% YoY growth, targeting $500M exit in 2-4 years.

## Current Status
**Advancing to onsite** — full-day office visit expected Mar 20-27, 2026. Includes team meetings, NDA, and live exercise with real business data. Two Zoom interviews completed (Feb 25, Mar 13).

## Reference Docs (read these for context)
All in `.claude/docs/`:
- **`architecture.md`** — Project structure, build system, directory layout, build commands
- **`file-inventory.md`** — Complete list of all workspace files and content files
- **`interview-intel.md`** — Key intel from both interviews, people, comp strategy, current status

**Read the relevant doc before starting work.** For example, read `architecture.md` before any build tasks. Read `interview-intel.md` before any content/strategy work.

## Quick Reference

### Build Command (main webapp)
```bash
cd irestore-prep && python3 build.py 2>&1 && cp dist/index.html ../interview_prep.html
```

### Build Command (shareable version)
```bash
cd irestore-prep-shareable && python3 build.py 2>&1
```

### Key Directories
- `irestore-prep/content/*.md` — 30 content files (YAML frontmatter + HTML body)
- `irestore-prep-shareable/` — Kevin-safe version (no interview/comp content)
- Root: transcripts, resumes, source docs

### Content File Rules
- Body content must be **HTML, not markdown** — the build does NOT convert markdown
- Subsections: `## Header` + `<!-- id: xxx -->` comment
- Frontmatter: `id`, `title`, `icon`, `order`, `group`, `groupOrder`

## Preferences
- Trey prefers targeted, specific improvements over broad audits
- Keep recommendations surgical — no comprehensive audits unless asked
- Always check local files FIRST before searching elsewhere
- Trey's email tone: casual, direct, no corporate-speak, asks real questions
- When writing emails for Trey: sound human, not strategic or polished

## Tools & Capabilities (Cowork mode)
- **Claude in Chrome** MCP tools available for LinkedIn, Twitter/X, YouTube (egress proxy blocks WebFetch for these)
- Chrome tabs persist between sessions
