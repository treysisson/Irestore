#!/usr/bin/env python3
"""
Build script: reads .md content files and compiles them into a single HTML webapp.

Each .md file has YAML frontmatter (id, title, icon, order, group, groupOrder) and
subsections delimited by ## headers with <!-- id: xxx --> comments.

Usage:
    python3 build.py              # builds dist/index.html
    python3 build.py --watch      # rebuilds on file changes (requires watchdog)
"""

import os
import re
import json
import sys
from collections import OrderedDict

CONTENT_DIR = os.path.join(os.path.dirname(__file__), 'content')
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'template.html')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), 'dist', 'index.html')

# Canonical group definitions: id, title, icon, order
GROUPS = [
    {"id": "company",   "title": "Company & Leadership",  "icon": "🏢"},
    {"id": "strategy",  "title": "Strategy & Operations",  "icon": "📊"},
    {"id": "market",    "title": "Products & Market",      "icon": "🔬"},
    {"id": "growth",    "title": "Growth & Expansion",     "icon": "🚀"},
]


def parse_frontmatter(text):
    """Extract YAML-like frontmatter from --- delimited block."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if not match:
        return {}, text
    fm_text = match.group(1)
    body = text[match.end():]
    fm = {}
    for line in fm_text.strip().split('\n'):
        key, _, val = line.partition(':')
        val = val.strip().strip('"')
        if key.strip() in ('order', 'groupOrder'):
            try:
                val = int(val)
            except ValueError:
                pass
        fm[key.strip()] = val
    return fm, body


def parse_subsections(body):
    """Split body into subsections based on ## headers and <!-- id: xxx --> comments."""
    subs = []
    parts = re.split(r'^## (.+)$', body, flags=re.MULTILINE)
    i = 1
    while i < len(parts):
        title = parts[i].strip()
        content = parts[i + 1] if i + 1 < len(parts) else ''
        id_match = re.search(r'<!--\s*id:\s*(\S+)\s*-->', content)
        sub_id = id_match.group(1) if id_match else title.lower().replace(' ', '-')
        content = re.sub(r'<!--\s*id:\s*\S+\s*-->\s*', '', content)
        content = re.sub(r'\n---\s*$', '', content.rstrip())
        subs.append({
            'id': sub_id,
            'title': title,
            'html': content.strip()
        })
        i += 2
    return subs


def load_sections():
    """Load all .md files, parse, and return grouped structure."""
    sections = []
    for filename in sorted(os.listdir(CONTENT_DIR)):
        if not filename.endswith('.md'):
            continue
        filepath = os.path.join(CONTENT_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        fm, body = parse_frontmatter(text)
        subs = parse_subsections(body)
        sections.append({
            'id': fm.get('id', filename.replace('.md', '')),
            'title': fm.get('title', filename),
            'icon': fm.get('icon', '📄'),
            'order': fm.get('order', 99),
            'group': fm.get('group', 'company'),
            'groupOrder': fm.get('groupOrder', 99),
            'subs': subs,
        })

    # Sort sections within each group by groupOrder
    sections.sort(key=lambda s: (s['order'], s['groupOrder']))

    # Build grouped output
    groups_out = []
    for g in GROUPS:
        group_sections = [s for s in sections if s['group'] == g['id']]
        group_sections.sort(key=lambda s: s['groupOrder'])
        # Strip internal fields
        clean = []
        for s in group_sections:
            clean.append({
                'id': s['id'],
                'title': s['title'],
                'icon': s['icon'],
                'subs': s['subs'],
            })
        groups_out.append({
            'id': g['id'],
            'title': g['title'],
            'icon': g['icon'],
            'sections': clean,
        })

    return groups_out


def build():
    """Build the final HTML file."""
    groups = load_sections()

    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()

    groups_json = json.dumps(groups, ensure_ascii=False, indent=2)
    html = template.replace('%%SECTIONS_DATA%%', groups_json)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(html)

    total_sections = sum(len(g['sections']) for g in groups)
    total_subs = sum(len(s['subs']) for g in groups for s in g['sections'])
    print(f"✓ Built {OUTPUT_PATH}")
    print(f"  {len(groups)} groups, {total_sections} sections, {total_subs} subsections, {len(html):,} chars")
    return html


if __name__ == '__main__':
    build()
