---
id: "sops"
title: "SOP Framework"
icon: ""
order: 5
group: "strategy"
groupOrder: 2
---
## The Problem
<!-- id: sops-problem -->

<div class="insight"><strong>Three departures in 60 days.</strong> Daniel (Chief of Staff, 8.5 years), CX Director (25-person team), and a Product Manager — each carrying institutional knowledge that walks out with them. Every undocumented process becomes a gap.</div>

<p>Most companies solve this with a documentation sprint that produces a 200-page ops manual nobody reads. That manual is outdated within a month.</p>

<p>A better approach: lightweight, AI-maintained SOPs covering the 15-20 processes that actually matter — drafted fast, kept current automatically, and published in a format anyone can use regardless of technical skill.</p>

---

## How It Works
<!-- id: sops-approach -->

<h3>Three-Layer System</h3>

<table>
  <tr><th>Layer</th><th>Who Uses It</th><th>What It Looks Like</th></tr>
  <tr style="background: var(--purple-light)"><td><strong>Source Files</strong></td><td>Leadership / AI-savvy team</td><td>Markdown files in a shared repo. Version-controlled, searchable, diffable. Claude drafts and updates these.</td></tr>
  <tr><td><strong>Published Pages</strong></td><td>Everyone</td><td>Auto-built into clean web pages (or pushed to Notion/Confluence). Non-technical team members read and follow these — no special tools needed.</td></tr>
  <tr style="background: var(--cream)"><td><strong>AI Assistant</strong></td><td>Everyone</td><td>Team members ask questions in plain English: "How do I process a Costco return?" AI answers from the SOP library. No searching through docs.</td></tr>
</table>

<div class="tip"><strong>The key insight:</strong> The people who create and maintain SOPs work in AI-native tools. The people who consume SOPs see clean, simple web pages. Nobody is forced to learn new technology — the system meets each person where they are.</div>

---

## SOP Template
<!-- id: sops-template -->

<p>Every SOP follows the same structure. Consistency matters more than comprehensiveness — a one-page SOP that people actually read beats a ten-page manual that collects dust.</p>

<div class="card">
  <div class="card-header">Standard SOP Format</div>
  <table>
    <tr><th width="25%">Field</th><th>Purpose</th></tr>
    <tr><td><strong>Process Name</strong></td><td>Clear, specific title</td></tr>
    <tr><td><strong>Owner</strong></td><td>A role, not a person — survives turnover</td></tr>
    <tr><td><strong>Last Updated</strong></td><td>Date — AI flags anything older than 90 days for review</td></tr>
    <tr><td><strong>Frequency</strong></td><td>Daily / per-event / weekly / monthly</td></tr>
    <tr><td><strong>Purpose</strong></td><td>One sentence on why this process exists</td></tr>
    <tr><td><strong>Steps</strong></td><td>Numbered sequence — each step is one action</td></tr>
    <tr><td><strong>Decision Points</strong></td><td>If X → do Y. If Z → escalate to [role]. Covers the forks.</td></tr>
    <tr><td><strong>Tools Used</strong></td><td>Systems, logins, or platforms involved</td></tr>
    <tr><td><strong>Common Mistakes</strong></td><td>What goes wrong and how to avoid it</td></tr>
  </table>
</div>

---

## Priority SOPs
<!-- id: sops-priority -->

<p class="muted">Start with the processes most at risk from the three departures and the Q2 product launches. Not everything at once — just the ones where a gap creates real pain.</p>

<h3>Immediate (Weeks 1-4): Capture Before Departure</h3>
<table>
  <tr><th>SOP</th><th>At Risk From</th><th>Why It's Urgent</th></tr>
  <tr style="background: var(--red-light)"><td><strong>Return processing & negotiation scripts</strong></td><td>CX Director departure</td><td>These scripts dropped return rates from 17% to 10%. Losing the playbook is a direct revenue hit.</td></tr>
  <tr style="background: var(--red-light)"><td><strong>CX escalation routing & decision authority</strong></td><td>CX Director departure</td><td>25-person team needs clear routing rules. Without them, everything escalates to leadership.</td></tr>
  <tr style="background: var(--red-light)"><td><strong>Kevin's reporting cadence & decision flow</strong></td><td>Daniel departure</td><td>8.5 years of institutional knowledge about how Kevin wants to receive information and make decisions.</td></tr>
  <tr><td><strong>Product launch checklist</strong></td><td>PM departure + Q2 launches</td><td>6-7 launches in 2026. A repeatable playbook prevents reinventing the wheel each time.</td></tr>
  <tr><td><strong>Channel-specific SKU setup</strong></td><td>PM departure</td><td>Different specs/pricing per channel (DTC, Amazon, Costco). This is tribal knowledge today.</td></tr>
</table>

<h3>Near-Term (Weeks 5-8): Operational Foundation</h3>
<table>
  <tr><th>SOP</th><th>Category</th></tr>
  <tr><td><strong>Amazon listing management & bundle strategy</strong></td><td>Channel Ops</td></tr>
  <tr><td><strong>Costco replenishment & return handling</strong></td><td>Channel Ops</td></tr>
  <tr><td><strong>Warehouse receiving & quality inspection</strong></td><td>Fulfillment</td></tr>
  <tr><td><strong>Shenzhen manufacturer coordination & PO process</strong></td><td>Supply Chain</td></tr>
  <tr><td><strong>Monthly financial close & channel reconciliation</strong></td><td>Finance</td></tr>
</table>

<h3>Medium-Term (Weeks 9-12): Scale Enablers</h3>
<table>
  <tr><th>SOP</th><th>Category</th></tr>
  <tr><td><strong>International market entry playbook</strong></td><td>Expansion</td></tr>
  <tr><td><strong>Clinical study initiation & management</strong></td><td>Product</td></tr>
  <tr><td><strong>B2B sales & clinic onboarding</strong></td><td>New Channel</td></tr>
  <tr><td><strong>QVC live commerce operations</strong></td><td>New Channel</td></tr>
</table>

---

## How AI Accelerates This
<!-- id: sops-ai -->

<table>
  <tr><th>Task</th><th>Traditional</th><th>AI-Assisted</th></tr>
  <tr><td><strong>Draft an SOP</strong></td><td>2-4 hours of writing per process</td><td>15-minute conversation → AI generates draft from description or meeting notes</td></tr>
  <tr><td><strong>Capture departing knowledge</strong></td><td>Shadowing sessions, manual documentation</td><td>Record exit interviews / walkthroughs → AI transcribes and structures into SOP format</td></tr>
  <tr><td><strong>Keep SOPs current</strong></td><td>Quarterly review meetings nobody wants to attend</td><td>AI flags stale docs (>90 days, references departed employees, mentions deprecated tools)</td></tr>
  <tr><td><strong>Answer process questions</strong></td><td>Search wiki, ask a colleague, guess</td><td>Ask AI: "How do we handle a Costco return over $500?" → instant answer from SOP library</td></tr>
  <tr><td><strong>Onboard new hires</strong></td><td>Shadow someone for 2 weeks</td><td>Role-specific SOP reading list + AI available to answer follow-up questions</td></tr>
</table>

<div class="tip"><strong>The speed advantage matters right now.</strong> With 3 people leaving in 60 days, there isn't time for a traditional documentation project. AI makes it possible to capture the critical 15-20 processes in weeks instead of months — while the people who know them are still around to validate the output.</div>

---
