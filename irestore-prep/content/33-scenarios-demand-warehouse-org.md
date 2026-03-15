---
id: "scenarios-batch3"
title: "34. Scenarios: Demand, Warehouse, Org"
icon: "📦"
order: 33
group: "gameday"
groupOrder: 6
---
## Scenario 7: Demand Planning / Inventory Forecasting
<!-- id: sc7-demand -->

<div class="card">
<h3>📦 "Here's Our Sales History — Build a Forecast"</h3>
<p>Historical sales data, seasonality, upcoming launches, and marketing calendar. This is the exact failure mode Kevin described — Brandon got blindsided by a Costco promo that 10x'd volume.</p>
</div>

<h4>Example Data Kevin Might Show You</h4>
<table>
<tr><th>Month</th><th>2024 Revenue</th><th>2025 Revenue</th><th>YoY Growth</th><th>Notes</th></tr>
<tr><td>Jan</td><td>$2.8M</td><td>$5.0M</td><td>79%</td><td>Post-holiday slowdown</td></tr>
<tr><td>Feb</td><td>$2.5M</td><td>$4.5M</td><td>80%</td><td>Valentine's small bump</td></tr>
<tr><td>Mar</td><td>$3.0M</td><td>$5.4M</td><td>80%</td><td>Spring sale begins</td></tr>
<tr><td>Apr</td><td>$3.2M</td><td>$5.8M</td><td>81%</td><td>Spring promo peak</td></tr>
<tr><td>May</td><td>$3.5M</td><td>$6.3M</td><td>80%</td><td>Mother's Day</td></tr>
<tr><td>Jun</td><td>$3.3M</td><td>$5.9M</td><td>79%</td><td>Summer lull begins</td></tr>
<tr><td>Jul</td><td>$3.0M</td><td>$5.4M</td><td>80%</td><td>Prime Day lift</td></tr>
<tr><td>Aug</td><td>$3.2M</td><td>$5.8M</td><td>81%</td><td>Back-to-routine</td></tr>
<tr><td>Sep</td><td>$4.0M</td><td>$7.2M</td><td>80%</td><td>Costco season ramp</td></tr>
<tr><td>Oct</td><td>$5.5M</td><td>$9.9M</td><td>80%</td><td>Prime Big Deal Days + Costco in-store</td></tr>
<tr><td>Nov</td><td>$8.0M</td><td>$14.4M</td><td>80%</td><td>🔥 Black Friday / Cyber Monday</td></tr>
<tr><td>Dec</td><td>$8.0M</td><td>$14.4M</td><td>80%</td><td>🔥 Holiday gifting peak</td></tr>
<tr style="background:#e8f5e9"><td><strong>Total</strong></td><td><strong>$50.0M</strong></td><td><strong>$90.0M</strong></td><td><strong>80%</strong></td><td></td></tr>
</table>

<h4>How to Read This — Seasonality Pattern</h4>
<div class="card card-green">
<h3>🎯 Key Patterns to Call Out</h3>
<ol>
<li><strong>Q4 is ~33% of annual revenue.</strong> Nov + Dec alone are $28.8M on $90M. This means: inventory for Q4 must be ordered by June-July (5+ month lead time from Shenzhen). Any PO decision made after July is too late for ocean freight — you'd need to air freight at 5-10x the cost.</li>

<li><strong>The Costco "surprise" risk.</strong> Sep-Oct ramp is Costco-driven. If Costco does an unplanned promo (which happened before — it 10x'd volume), you need 3-4 weeks of safety stock specifically for that channel. Brandon's failure was not having this buffer.</li>

<li><strong>Summer (Jun-Aug) is the inventory building window.</strong> Revenue is lower, so warehouse capacity opens up. This is when you pre-stage Q4 inventory. If you're still selling through spring inventory in August, you're already behind on Q4.</li>

<li><strong>New product launches in Q2 make forecasting harder.</strong> Body panels, belt, and skincare wand all launching Q2 2026. Zero historical data. You need scenario planning, not point forecasts.</li>
</ol>
</div>

<h4>Building a 2026 Forecast</h4>
<div class="card">
<h3>Three-Scenario Approach</h3>
<table>
<tr><th></th><th>Conservative (55% growth)</th><th>Base (65% growth)</th><th>Upside (80% growth)</th></tr>
<tr><td>Existing products</td><td>$120M</td><td>$130M</td><td>$140M</td></tr>
<tr><td>Body panels (new)</td><td>$2M</td><td>$5M</td><td>$10M</td></tr>
<tr><td>Red light belt (new)</td><td>$1M</td><td>$3M</td><td>$6M</td></tr>
<tr><td>Skincare wand (new)</td><td>$2M</td><td>$5M</td><td>$8M</td></tr>
<tr><td>B2B division</td><td>$1M</td><td>$2M</td><td>$4M</td></tr>
<tr><td>QVC (if launched)</td><td>$2M</td><td>$5M</td><td>$8M</td></tr>
<tr style="background:#e8f5e9"><td><strong>Total 2026</strong></td><td><strong>$128M</strong></td><td><strong>$150M</strong></td><td><strong>$176M</strong></td></tr>
<tr><td><strong>YoY Growth</strong></td><td>42%</td><td>67%</td><td>96%</td></tr>
</table>

<p><strong>What to say:</strong> "Kevin told me you're trending 65% growth before any launches. With body panels, belt, wand, B2B, and QVC all launching in 2026, the upside case is $175M+. But I'd plan inventory to the base case and have a rapid-response plan for upside. The worst outcome isn't missing demand — it's sitting on $5M of body panel inventory that doesn't sell."</p>
</div>

<h4>Sub-Scenario: "How Do You Handle the Costco Surprise?"</h4>
<div class="card card-yellow">
<p><strong>This is Kevin's trauma test. Brandon failed this exact scenario.</strong></p>

<p><strong>Your answer — a 3-layer demand planning system:</strong></p>
<ol>
<li><strong>Base forecast:</strong> Historical trend × growth rate × seasonality index. Updated monthly. This is the "what we expect."</li>
<li><strong>Scenario overlays:</strong> Marketing calendar events (promos, launches, Prime Day, BFCM) each get a demand multiplier based on historical performance. A Costco roadshow might be 3-5x normal Costco weekly volume.</li>
<li><strong>Safety stock by SKU tier:</strong>
<table>
<tr><th>SKU Tier</th><th>Weeks of Safety Stock</th><th>Why</th></tr>
<tr><td>Hero products (Pro, Elite, Face Mask)</td><td>6-8 weeks</td><td>Stockout = lost revenue AND lost Amazon ranking</td></tr>
<tr><td>Growing products (Eye Mask, body panels)</td><td>4-6 weeks</td><td>Demand uncertain, need buffer but not overcommit</td></tr>
<tr><td>Stable products (accessories, consumables)</td><td>3-4 weeks</td><td>Predictable demand, lower stockout cost</td></tr>
<tr><td>New launches (first 90 days)</td><td>8-12 weeks</td><td>No historical data, need runway to learn demand curve</td></tr>
</table>
</li>
</ol>

<p><strong>The Costco-specific playbook:</strong></p>
<ul>
<li>"I'd require 4 weeks advance notice on any Costco promo. This is standard for vendor agreements. If Costco won't agree, we build a permanent Costco safety stock buffer into our planning."</li>
<li>"For Costco roadshows (in-store demos), historical data shows 3-10x daily volume. I'd stage product at the nearest Costco DC 2 weeks before any roadshow."</li>
<li>"If a surprise promo hits: first call is to the factory for expedited production, second call is to evaluate air freight for bridge inventory, third call is to marketing to manage expectations on delivery timelines."</li>
</ul>
</div>

<h4>The Net-150 Factor</h4>
<div class="card">
<p><strong>Key context:</strong> iRESTORE pays suppliers net-150 days (5 months!) because of the family relationship with Kevin's father's Shenzhen factory. This is a massive working capital advantage but creates forecasting complexity:</p>
<ul>
<li>You're ordering inventory 5+ months before you need it (ocean freight) and paying for it 5 months after receipt</li>
<li>That means POs placed in January are for June delivery and paid for in November</li>
<li>A bad Q4 forecast made in June doesn't hit your cash until November — but the inventory is already on the water</li>
<li><strong>What to say:</strong> "The net-150 terms are an incredible advantage — you're essentially getting free inventory financing for 5 months. But it also means forecasting errors compound. A wrong call in June turns into excess inventory in October and a cash hit in March. I'd build a monthly PO review process where we revisit the next 3 months of orders against the latest demand signals."</li>
</ul>
</div>

---

## Scenario 8: Warehouse Capacity Planning
<!-- id: sc8-warehouse -->

<div class="card">
<h3>🏭 "We're Running Out of Space — What's the Plan?"</h3>
<p>La Mirada warehouse is near capacity again after moving in May. Kevin is leaning toward a 3PL east coast node. Body panels launching Q2 will make it worse.</p>
</div>

<h4>Example Data Kevin Might Show You</h4>
<table>
<tr><th>Metric</th><th>Current</th><th>6 Months (est.)</th><th>12 Months (est.)</th></tr>
<tr><td>Warehouse Size</td><td>~30-40K sq ft (est.)</td><td>Same</td><td>Need expansion</td></tr>
<tr><td>Capacity Utilization</td><td>~85%</td><td>~95% (with body panels)</td><td>100%+ (crisis)</td></tr>
<tr><td>SKU Count</td><td>~52</td><td>~60 (new launches)</td><td>~65+</td></tr>
<tr><td>Daily Orders (avg)</td><td>~400-600</td><td>~550-800</td><td>~700-1,000</td></tr>
<tr><td>Peak Daily Orders (BFCM)</td><td>~2,000-3,000</td><td>~3,000-5,000</td><td>~4,000-6,000</td></tr>
<tr><td>Returns Processing</td><td>~50-70/day</td><td>~70-100/day</td><td>~100-130/day</td></tr>
<tr><td>Fulfillment FTEs</td><td>~15-20 (est.)</td><td>~20-25</td><td>~25-30</td></tr>
</table>

<h4>The Decision Matrix: Expand vs. 3PL vs. Both</h4>
<div class="card card-green">
<table>
<tr><th>Option</th><th>Pros</th><th>Cons</th><th>Cost (est.)</th><th>Timeline</th></tr>
<tr style="background:#e8f5e9">
<td><strong>A: East Coast 3PL</strong></td>
<td>• 1-2 day shipping to 50%+ of US pop<br>• Variable cost model<br>• No lease commitment<br>• Kevin is already leaning this way</td>
<td>• Less control over quality<br>• Split inventory management<br>• 3PL markup on pick/pack<br>• Body panels/refurb too complex for most 3PLs</td>
<td>$300-500K setup<br>$8-15/order variable</td>
<td>3-6 months</td>
</tr>
<tr>
<td><strong>B: Expand La Mirada</strong></td>
<td>• Full control<br>• Team already trained<br>• Handles refurb/reverse logistics<br>• No split inventory headache</td>
<td>• SoCal real estate is expensive<br>• Doesn't solve shipping time to East Coast<br>• Lease commitment (3-5 yr)</td>
<td>$200-400K build-out<br>$15-25K/mo lease</td>
<td>2-4 months</td>
</tr>
<tr style="background:#fff3e0">
<td><strong>C: Both (Recommended)</strong></td>
<td>• Best of both worlds<br>• La Mirada handles complex ops (refurb, B2B, new launches)<br>• 3PL handles commodity shipping (consumables, accessories, repeat orders)</td>
<td>• Highest upfront cost<br>• Most complex to manage<br>• Requires inventory allocation system</td>
<td>$500-800K total<br>Combined variable</td>
<td>4-6 months</td>
</tr>
</table>
</div>

<h4>Your Recommendation</h4>
<div class="card">
<p><strong>"I'd do both, but with a clear split of responsibilities:"</strong></p>

<table>
<tr><th>La Mirada (Company-Operated)</th><th>East Coast 3PL</th></tr>
<tr><td>All new product launches (first 90 days)</td><td>Established SKUs with predictable demand</td></tr>
<tr><td>Refurbishment & reverse logistics</td><td>Consumables & accessories (subscribe & save)</td></tr>
<tr><td>B2B orders (higher complexity)</td><td>Standard DTC orders (East Coast + Midwest)</td></tr>
<tr><td>Costco fulfillment</td><td>Simple Amazon FBA replenishment</td></tr>
<tr><td>Body panels (oversized, complex packaging)</td><td>Helmets, face masks (standardized packaging)</td></tr>
<tr><td>Influencer seeding program</td><td>Gift orders</td></tr>
</table>

<p><strong>The shipping math:</strong></p>
<table>
<tr><th>Ship From</th><th>Zone 2-3 Coverage</th><th>Avg Ship Cost</th><th>Avg Transit</th></tr>
<tr><td>La Mirada only</td><td>~25% of US</td><td>$18-25 per order</td><td>4-6 days to East Coast</td></tr>
<tr><td>La Mirada + East Coast 3PL</td><td>~75% of US</td><td>$12-18 per order</td><td>1-3 days nationwide</td></tr>
<tr style="background:#e8f5e9"><td><strong>Savings per order</strong></td><td></td><td><strong>$4-8</strong></td><td><strong>2-3 days faster</strong></td></tr>
</table>
<p>At 150K+ orders/year from East Coast customers, that's <strong>$600K-$1.2M in annual shipping savings</strong> plus faster delivery → higher conversion and lower return rates.</p>
</div>

<h4>Sub-Scenario: "What About Body Panel Storage?"</h4>
<div class="card card-yellow">
<p><strong>Body panels are physically 3-4x larger than helmets.</strong> This is a real operational challenge:</p>
<ul>
<li><strong>Storage:</strong> Panels may not fit standard racking. May need floor stacking or custom racking. Each pallet holds fewer units.</li>
<li><strong>Picking:</strong> Two-person lift likely required for large panels. Changes pick/pack workflow and labor requirements.</li>
<li><strong>Shipping:</strong> Oversized/overweight surcharges from UPS/FedEx. DIM weight pricing makes panels much more expensive to ship per unit.</li>
<li><strong>Returns:</strong> Return shipping on a 40lb panel in a 36" box is $50-100. Who pays — iRESTORE or customer? At 12% return rate, this adds $6-12 per unit sold to effective cost.</li>
</ul>
<p><strong>What to say:</strong> "Before we accept the $500K body panel PO, I need to see the warehouse plan. If La Mirada is at 85% capacity with current SKUs, adding pallets of body panels could push us over 100% before Q4. I'd either carve out a dedicated body panel zone at La Mirada or stage body panel inventory at a separate local overflow facility for the first 6 months."</p>
</div>

---

## Scenario 9: Org Chart Redesign
<!-- id: sc9-org -->

<div class="card">
<h3>📋 "Three People Are Leaving. Redesign the Org."</h3>
<p>Daniel Ju (Chief of Staff), CX Director (Amanda), and a Product Manager are all departing simultaneously. Kevin doesn't want everything funneling through one person.</p>
</div>

<h4>Current State: What You Know</h4>
<table>
<tr><th>Departing</th><th>Role</th><th>Leaving When</th><th>Context</th></tr>
<tr><td>Daniel Ju</td><td>Chief of Staff / HR</td><td>End of April</td><td>8.5 years, Kevin's college friend. Amicable. "Just a messenger" — Kevin's words.</td></tr>
<tr><td>Amanda Schoep</td><td>Dir. of CX</td><td>Being let go</td><td>Not implementing AI. 25-person team viewed as bloated.</td></tr>
<tr><td>Product Manager</td><td>PM (physical products)</td><td>Departing</td><td>Details unknown</td></tr>
</table>

<table>
<tr><th>Staying</th><th>Role</th><th>Reports To</th><th>Your Read</th></tr>
<tr><td>Brandon</td><td>Director of Ops</td><td>Kevin (directly)</td><td>Reliable executor, not strategic. Kevin says it's "way smoother" direct.</td></tr>
<tr><td>Longchuan Huang</td><td>Head of Product Dev</td><td>Kevin</td><td>New (~3 months). PhD UPenn, from Wella. Owns product innovation — Kevin's domain.</td></tr>
<tr><td>Junior Reyes</td><td>VP Growth & Data</td><td>Kevin</td><td>Remote (NYC). Tech-forward. Likely owns analytics, growth marketing.</td></tr>
<tr><td>AI Consultant</td><td>External</td><td>Kevin</td><td>Weekly calls, building N8N automations, influencer bot</td></tr>
<tr><td>Fractional CFO</td><td>External</td><td>Kevin</td><td>Handles budgeting and financial reporting</td></tr>
</table>

<h4>Kevin's Explicit Requirements</h4>
<div class="card card-red">
<ul>
<li><strong>"I don't want everything going through one person."</strong> — Kevin explicitly rejected the traditional V/I (Visionary/Integrator) model where all functions report to the COO.</li>
<li><strong>Kevin owns: marketing, sales, product innovation, distribution</strong> — he calls this "value creation"</li>
<li><strong>COO owns: operations, finance, CX, supply chain</strong> — he calls this "value protection"</li>
<li><strong>Kevin hated Daniel being "just a messenger"</strong> — he wants someone who makes decisions autonomously, then informs</li>
<li><strong>Brandon reporting directly to Kevin is "way smoother"</strong> — tread carefully here</li>
</ul>
</div>

<h4>Your Proposed Org Chart</h4>
<div class="card card-green">
<h3>🎯 The "Dual Domain" Structure</h3>

<p><strong>Kevin's Domain (Value Creation):</strong></p>
<table>
<tr><th>Direct Report</th><th>Function</th><th>Notes</th></tr>
<tr><td>Longchuan Huang</td><td>Head of Product Development</td><td>Stays with Kevin. Product innovation is Kevin's passion and competitive advantage.</td></tr>
<tr><td>Junior Reyes (NYC)</td><td>VP Growth & Data</td><td>Stays with Kevin. Marketing strategy, paid media, analytics.</td></tr>
<tr><td>New: B2B Sales Lead</td><td>B2B Division</td><td>Just hired. Reports to Kevin initially — this is a new revenue bet Kevin wants to personally shepherd.</td></tr>
</table>

<p><strong>COO's Domain (Value Protection → Value Multiplication):</strong></p>
<table>
<tr><th>Direct Report</th><th>Function</th><th>Notes</th></tr>
<tr><td>Brandon</td><td>Director of Ops (Warehouse, Fulfillment, Supply Chain)</td><td>⚠️ Sensitive. Kevin says "way smoother" direct. My approach: dotted line to COO for first 90 days, then evaluate. Brandon needs a strategic partner, not a new boss.</td></tr>
<tr><td>New Hire: CX Leader</td><td>Head of Customer Experience</td><td>🔥 First hire. Must be someone who will implement AI, restructure the team, and build a data-driven CX operation. Not a traditional "CX Manager."</td></tr>
<tr><td>New Hire: People Ops Lead</td><td>HR / People Operations</td><td>Replaces Daniel's HR functions. Junior role — not a Chief of Staff. Handles recruiting, benefits, compliance, culture programs.</td></tr>
<tr><td>Fractional CFO (existing)</td><td>Finance & Accounting</td><td>Elevate from external to COO direct report relationship. Weekly P&L review, cash flow forecasting, board reporting.</td></tr>
</table>

<p><strong>Shared / Collaborative:</strong></p>
<table>
<tr><th>Function</th><th>Kevin + COO</th><th>How It Works</th></tr>
<tr><td>New Product Launches</td><td>Kevin owns product, COO owns launch ops</td><td>Joint weekly launch readiness review. Kevin decides what to launch, COO ensures it launches on time and on budget.</td></tr>
<tr><td>AI Initiatives</td><td>COO leads execution, Kevin sponsors</td><td>COO takes over AI consultant relationship. Drives CX automation, transcript analysis, demand forecasting.</td></tr>
<tr><td>Channel Strategy</td><td>Kevin + Junior own growth, COO owns economics</td><td>Growth team decides where to sell, COO ensures each channel is profitable. Veto power on unprofitable expansion.</td></tr>
</table>
</div>

<h4>Sub-Scenario: "Should Brandon Report to You?"</h4>
<div class="card card-yellow">
<p><strong>This is a trap. Kevin told you directly that Brandon reporting to him is "way smoother."</strong></p>

<p><strong>Your answer: "Not on Day 1 — and maybe not at all."</strong></p>
<ul>
<li>"Kevin, you told me the direct reporting with Brandon is working well. I'm not going to break something that works just to draw a clean org chart."</li>
<li>"What I would do: build a collaborative relationship with Brandon. Joint weekly ops review. I bring the strategic lens (3PL expansion, demand planning framework, capacity modeling), he brings the execution knowledge (how the warehouse actually runs, vendor relationships, team capabilities)."</li>
<li>"If over 6 months it becomes clear that Brandon would benefit from more strategic direction — not management, direction — then we can revisit. But I'm not going to walk in Day 1 and reorganize reporting lines. That's exactly the kind of disruption you don't need during 3 simultaneous departures."</li>
<li><strong>The real point:</strong> "My value isn't in managing Brandon's daily work. It's in building the systems and frameworks that make his daily work more effective — demand planning, KPI dashboards, cross-functional launch processes. He can keep reporting to you and still benefit enormously from what I build."</li>
</ul>
</div>

<h4>Sub-Scenario: "What's the Hiring Priority?"</h4>
<div class="card">
<table>
<tr><th>Priority</th><th>Role</th><th>Why First</th><th>Timeline</th><th>Comp Range</th></tr>
<tr style="background:#e8f5e9"><td><strong>#1</strong></td><td>Head of CX (AI-forward)</td><td>CX director is being fired NOW. 25-person team needs leadership. Biggest immediate cost savings opportunity. Kevin's top frustration.</td><td>Hire in 30-45 days</td><td>$120-160K base + bonus</td></tr>
<tr><td>#2</td><td>People Ops Lead</td><td>Daniel leaves end of April. HR functions (payroll, benefits, compliance, recruiting) need continuity. Doesn't need to be senior — junior/mid-level is fine.</td><td>Hire in 45-60 days</td><td>$70-100K</td></tr>
<tr><td>#3</td><td>Product Manager replacement</td><td>Important but less urgent — Longchuan can absorb some PM duties short-term. Wait until you understand the product launch cadence.</td><td>Hire in 60-90 days</td><td>$100-140K</td></tr>
</table>

<p><strong>What NOT to backfill:</strong></p>
<ul>
<li><strong>Don't hire a Chief of Staff.</strong> Kevin's experience with Daniel showed this role became a bottleneck. The COO IS the integrator. You don't need a CoS as an intermediary.</li>
<li><strong>Don't hire a CX Director who's a "people manager."</strong> Hire a CX operations leader who sees AI as a force multiplier, not a threat. The person who got fired didn't implement AI — the replacement must make AI implementation their Day 1 priority.</li>
</ul>
</div>

<h4>Key Talking Points for Org Scenario</h4>
<div class="card card-yellow">
<ul>
<li><strong>"Three departures at once is actually an opportunity to redesign, not just backfill."</strong> Don't hire 3 replacements — hire 2 better roles and let the COO absorb the strategic functions of the third.</li>
<li><strong>"The org chart should reflect where the business is going, not where it's been."</strong> A $90M company with 80% growth needs different roles than the $50M company that hired these people.</li>
<li><strong>"I wouldn't put everything through me — that's what killed the Daniel model."</strong> Kevin, you keep marketing, sales, product innovation, and distribution. I'll own ops, CX, finance, and supply chain. We collaborate on launches and channel strategy. No single bottleneck.</li>
<li><strong>"My first week: 1-on-1s with every team lead."</strong> Not to evaluate — to listen. What's working, what's broken, what do they need from a COO. I'll know within 2 weeks who's an A-player and where the gaps are.</li>
</ul>
</div>

---
