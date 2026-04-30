# iRESTORE COO Interview Prep — Claude Instructions

## Who
Trey Sisson, interviewing for COO/Integrator at iRESTORE (CEO: Kevin Chen). DTC beauty device company, ~$90M+ revenue, 80% YoY growth, targeting $500M exit in 2-4 years.

## Current Status
**Offer negotiation** — Offer received (1.5% phantom equity, $300K base). Counter-offer model finalized: asking 5.18% equity (~$4M net at $300M exit, 53.75% combined tax rate). Kevin-facing presentation tab built in counter_offer_v2.xlsx. Call with Kevin upcoming. See `Offer/` folder for all negotiation files.

## Reference Docs (read these for context)
All in `.claude/docs/`:
- **`architecture.md`** — Project structure, build system, directory layout, build commands
- **`file-inventory.md`** — Complete list of all workspace files and content files
- **`interview-intel.md`** — Key intel from both interviews, people, comp strategy, current status

## Sub-projects
- **`acquirers-tracker/`** — Dashboard tracking potential iRESTORE M&A acquirers (strategics, PE, etc.). Daily-refreshing leave-behind artifact for Kevin. Currently in brainstorming/spec phase. Read `acquirers-tracker/CLAUDE.md` and `acquirers-tracker/STATUS.md` before working on it. Eventually extracts to its own private repo.

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

## PR Creation
- **Do NOT use `gh` CLI or GitHub MCP tools** — they don't work in this environment
- Instead, give Trey a clickable GitHub compare URL to create the PR manually:
  `https://github.com/treysisson/Irestore/compare/master...<branch-name>?expand=1`

## Tools & Capabilities (Cowork mode)
- **Claude in Chrome** MCP tools available for LinkedIn, Twitter/X, YouTube (egress proxy blocks WebFetch for these)
- Chrome tabs persist between sessions
