# iRESTORE COO Interview Prep — Claude Instructions

## Environment Limitations
- Cannot open Typora or other local Mac apps directly. When user wants to open a file, provide the `open -a Typora <path>` command for them to run.
- Cannot access local project folders outside this repo or external GitHub repos not mounted. Ask user to paste relevant content instead of attempting to read.
- Cannot access Granola directly; ask user to export and commit transcript files to the repo.

## Git Workflow
- User edits files locally on master branch; Claude works on a feature branch. Always check which branch has the latest edits before making changes.
- When user reports local edits, offer to pull their changes or have them paste the current content rather than assuming the branch state.
- Prefer committing directly to master or coordinate branch strategy explicitly at session start.

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

## PR Creation
- **Do NOT use `gh` CLI or GitHub MCP tools** — they don't work in this environment
- Instead, give Trey a clickable GitHub compare URL to create the PR manually:
  `https://github.com/treysisson/Irestore/compare/master...<branch-name>?expand=1`

## Tools & Capabilities (Cowork mode)
- **Claude in Chrome** MCP tools available for LinkedIn, Twitter/X, YouTube (egress proxy blocks WebFetch for these)
- Chrome tabs persist between sessions

## Negotiation Coaching Style
- When user asks for 'creative deal structures,' avoid proposals that are mathematically equivalent reshufflings of the same money (gross-ups, ratchets, loan-to-equity, transaction bonuses). Focus on genuine value-creating levers like strike-price reduction, vesting acceleration, or changing the underlying valuation assumption.
- Double-check math on equity comparisons (phantom vs real equity, loan vs grant) before presenting.
