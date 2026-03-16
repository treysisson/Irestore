---
id: "freight"
title: "34. Freight & Supply Chain Logistics"
icon: "🚢"
order: 33
group: "company"
groupOrder: 12
---
## iRESTORE Import Data (Public Records)
<!-- id: freight-data -->

<p>Compiled from ImportYeti, ImportGenius, and FDA customs filings for <strong>Freedom Laser Therapy Inc.</strong> (iRESTORE's legal entity).</p>

<table>
  <tr><th>Data Point</th><th>Value</th><th>Source</th></tr>
  <tr><td><strong>Total recorded shipments</strong></td><td>54 ocean shipments</td><td>ImportYeti</td></tr>
  <tr><td><strong>Est. shipping spend</strong></td><td>$138,925 (87% coverage)</td><td>ImportYeti</td></tr>
  <tr><td><strong>Primary supplier</strong></td><td>Wellmike Technology Corporation (54 shipments)</td><td>ImportYeti</td></tr>
  <tr><td><strong>Supplier HQ</strong></td><td>New Taipei City, Taiwan</td><td>Public records</td></tr>
  <tr><td><strong>Factory location</strong></td><td>Guanlan Town, Longhua District, Shenzhen (~5,500 sqm)</td><td>Wellmike public profile</td></tr>
  <tr><td><strong>Second supplier</strong></td><td>Remax Medi-Tech (Shenzhen) Corp.</td><td>FDA filings</td></tr>
  <tr><td><strong>Remax factory</strong></td><td>Guanlan Street, Longhua District, Shenzhen</td><td>FDA 510(k)</td></tr>
  <tr><td><strong>Origin port</strong></td><td>Yantian, Shenzhen</td><td>Customs records</td></tr>
  <tr><td><strong>Destination port</strong></td><td>Port of Los Angeles</td><td>Customs records</td></tr>
  <tr><td><strong>Freight forwarder</strong></td><td>Topocean Consolidation Service (Los Angeles)</td><td>Customs records</td></tr>
  <tr><td><strong>HTS classification</strong></td><td>9013.80.9000 (liquid crystal/optical devices)</td><td>CBP ruling</td></tr>
  <tr><td><strong>Base duty rate</strong></td><td>4.5% ad valorem (MFN)</td><td>USITC</td></tr>
  <tr><td><strong>Section 301 tariff</strong></td><td>+7.5% ad valorem</td><td>USTR</td></tr>
  <tr><td><strong>Total duty rate</strong></td><td>~12% of declared FOB value</td><td>Combined</td></tr>
</table>

<div class="card">
  <div class="card-header">Key Observations</div>
  <ul>
    <li><strong>Both factories (Wellmike and Remax) are in the same area of Shenzhen</strong> — Guanlan/Longhua District. This is almost certainly Kevin's father's manufacturing network. Wellmike is the Taiwanese holding company; Remax is the Shenzhen factory entity listed on FDA filings.</li>
    <li><strong>Single-source supply chain</strong> — All 54 recorded shipments come from one supplier. This is typical for a family-factory relationship but creates concentration risk. The new body panel manufacturer (different Shenzhen factory) would be iRESTORE's first supply chain diversification.</li>
    <li><strong>Topocean as freight forwarder</strong> — They're an Asia-specialist NVOCC (Non-Vessel Operating Common Carrier). Solid mid-market choice. Not a digital-first platform like Flexport — more traditional relationship-based.</li>
    <li><strong>12% total duty rate is favorable</strong> — Many consumer electronics from China face 25-60%+ under Section 301. iRESTORE's HTS classification (optical devices) lands them at a much lower rate. This is a significant competitive advantage worth protecting. Any product reclassification or tariff expansion could be a major P&L hit.</li>
  </ul>
</div>

<div class="tip"><strong>Interview edge:</strong> Mentioning that you looked up their customs data and know they're shipping through Yantian via Topocean shows serious operational due diligence. Ask Brandon: "You're using Topocean for freight — how's that relationship? Are you getting competitive bids?"</div>

---

## Estimated Shipping Volume
<!-- id: freight-volume -->

<h3>Back-of-Envelope Math</h3>

<table>
  <tr><th>Assumption</th><th>Value</th><th>Notes</th></tr>
  <tr><td>Annual revenue</td><td>$90M+</td><td>Kevin's stated figure</td></tr>
  <tr><td>COGS margin</td><td>~35-40%</td><td>Typical for DTC electronics</td></tr>
  <tr><td>FOB product cost</td><td>~$31-36M</td><td></td></tr>
  <tr><td>Avg unit FOB cost</td><td>$50-150</td><td>Varies by device (helmet vs face mask)</td></tr>
  <tr><td>Units shipped/year</td><td>~100K-200K</td><td>Mix of helmets, masks, accessories</td></tr>
  <tr><td>Units per 40' container</td><td>~5,000-10,000</td><td>Depends on packaging; devices "cube out" before weighing out</td></tr>
  <tr><td><strong>Est. containers/year</strong></td><td><strong>15-30 FEU</strong></td><td>~1-3 containers per month</td></tr>
  <tr><td>Est. ocean freight cost</td><td>$75K-$150K/yr</td><td>At ~$4,000-5,000/FEU all-in</td></tr>
  <tr><td><strong>Est. annual duties</strong></td><td><strong>$3.7-4.3M</strong></td><td>12% on $31-36M FOB value</td></tr>
</table>

<div class="card card-yellow">
  <div class="card-header">The Real Cost Story</div>
  <p><strong>Freight is a rounding error. Tariffs are the real number.</strong></p>
  <p>At $90M revenue, ocean freight is ~$100K/yr — less than 0.15% of revenue. But duties at 12% of FOB value are $3.7-4.3M/yr. If tariff rates increase (Section 301 expansion, new executive orders), the exposure jumps fast. At 25% total duty, it's $7.5-9M/yr. At 50%, it's $15-18M/yr.</p>
  <p>A COO who can protect that 12% rate — or find ways to mitigate if it increases — delivers more value than any freight optimization.</p>
</div>

---

## Ocean Freight Crash Course
<!-- id: freight-101 -->

<h3>How It Works at iRESTORE's Scale</h3>

<p>At ~20 containers/year, iRESTORE is a <strong>small-to-mid-volume shipper</strong>. Here's how freight contracting works at this level vs. what you've done with Flexport:</p>

<table>
  <tr><th>Concept</th><th>What You Know (Flexport)</th><th>How It Works at Scale</th></tr>
  <tr>
    <td><strong>Booking</strong></td>
    <td>You book individual shipments through a platform</td>
    <td>At higher volume, you sign an <strong>annual service contract</strong> with a carrier (or through your forwarder). Contract season runs May 1 - Apr 30. You commit to a Minimum Quantity Commitment (MQC) — say 200+ TEUs — and get a locked rate.</td>
  </tr>
  <tr>
    <td><strong>Who carries it</strong></td>
    <td>Flexport picks the carrier</td>
    <td>You can contract directly with a <strong>BCO (Beneficial Cargo Owner)</strong> — the actual shipping line (COSCO, Maersk, etc.). Or use an <strong>NVOCC</strong> like Topocean or Flexport, who buys bulk space and resells it. iRESTORE uses Topocean (an NVOCC).</td>
  </tr>
  <tr>
    <td><strong>Pricing</strong></td>
    <td>Quoted per shipment, often opaque</td>
    <td><strong>Contract rate</strong> (locked for the year, ~$2,000-4,000/FEU currently) vs <strong>spot rate</strong> (volatile, changes weekly). Smart shippers do 60-70% contract, 30-40% spot to maintain flexibility.</td>
  </tr>
  <tr>
    <td><strong>Container types</strong></td>
    <td>You might not have specified</td>
    <td>Almost always <strong>40' High Cube (40'HC)</strong> for consumer electronics. Same price as standard 40' but 13% more cubic space. Products like helmets "cube out" (fill volume) before "weighing out" (hitting weight limit).</td>
  </tr>
</table>

<h3>Key Vocabulary</h3>

<table>
  <tr><th>Term</th><th>What It Means</th><th>Why It Matters</th></tr>
  <tr><td><strong>TEU / FEU</strong></td><td>Twenty-foot / Forty-foot Equivalent Unit. Most Trans-Pacific freight moves in 40' containers (FEUs). 1 FEU = 2 TEU.</td><td>Industry standard unit. Say "FEU" or "forty-foot container," not "box."</td></tr>
  <tr><td><strong>FOB vs CIF</strong></td><td><strong>FOB</strong> (Free on Board): buyer arranges freight from origin port. <strong>CIF</strong> (Cost, Insurance, Freight): seller arranges to destination port.</td><td>iRESTORE likely buys FOB since they use their own forwarder. FOB gives you control over carrier selection and costs.</td></tr>
  <tr><td><strong>Landed cost</strong></td><td>Total cost to get product into your warehouse: FOB cost + freight + duties + drayage + handling.</td><td>This is THE number. Not just product cost, not just freight — the fully loaded cost per unit.</td></tr>
  <tr><td><strong>Drayage</strong></td><td>Short truck haul: factory → port (origin) or port → warehouse (destination).</td><td>LA port → Inland Empire warehouse drayage is $400-900/container. A controllable cost.</td></tr>
  <tr><td><strong>Demurrage & Detention</strong></td><td>Penalty fees for slow pickup. <strong>Demurrage</strong>: container sitting at port past free time. <strong>Detention</strong>: keeping the container at your warehouse too long.</td><td>$150-400/day after free time (usually 4-5 days). The #1 controllable freight cost. Shows you understand port ops.</td></tr>
  <tr><td><strong>Bill of Lading (B/L)</strong></td><td>The shipping document — contract of carriage + proof of ownership. Like a title deed for cargo in transit.</td><td>Original B/L must be surrendered to claim cargo. "Telex release" is the electronic alternative.</td></tr>
  <tr><td><strong>HTS code</strong></td><td>Harmonized Tariff Schedule classification. Determines your duty rate.</td><td>iRESTORE is classified under 9013.80.9000 at 4.5% + 7.5% Section 301 = 12% total. Getting this classification right (or wrong) is a million-dollar decision.</td></tr>
  <tr><td><strong>FCL / LCL</strong></td><td><strong>FCL</strong>: Full Container Load (you fill the whole container). <strong>LCL</strong>: Less than Container Load (consolidated with other shippers).</td><td>At iRESTORE's volume, every shipment should be FCL. LCL is for companies doing a few pallets.</td></tr>
</table>

---

## The Shipping Route: Yantian → LA
<!-- id: freight-route -->

<h3>iRESTORE's Supply Chain Flow</h3>

<table>
  <tr><th>Step</th><th>Location</th><th>Time</th><th>Details</th></tr>
  <tr><td>1. Manufacturing</td><td>Guanlan, Longhua, Shenzhen</td><td>2-4 weeks</td><td>Wellmike/Remax factory. Kevin's father's network.</td></tr>
  <tr><td>2. Factory → port</td><td>Guanlan → Yantian port</td><td>1-2 days</td><td>~30 min to 2 hrs by truck. Yantian is the primary export terminal for Shenzhen (14M+ TEU/year).</td></tr>
  <tr><td>3. Export customs + loading</td><td>Yantian</td><td>2-3 days</td><td>Container staged, loaded on vessel.</td></tr>
  <tr><td>4. Ocean transit</td><td>Yantian → Port of LA</td><td><strong>12-15 days</strong></td><td>Direct Trans-Pacific service. One of the world's busiest lanes.</td></tr>
  <tr><td>5. Terminal + customs</td><td>Port of Los Angeles</td><td>3-7 days</td><td>Unloading, CBP inspection, clearance. Can be longer if held for exam.</td></tr>
  <tr><td>6. Drayage</td><td>Port → La Mirada warehouse</td><td>1-2 days</td><td>Short haul, ~25 miles from port complex to warehouse.</td></tr>
  <tr><td>7. Receiving + putaway</td><td>La Mirada</td><td>1-3 days</td><td>QC, inventory system entry, shelving.</td></tr>
  <tr style="background: #e8f5e9;"><td><strong>Total door-to-door</strong></td><td></td><td><strong>4-6 weeks</strong></td><td>Plan on 5 weeks. This means ordering 2-3 months ahead of need (production + transit).</td></tr>
</table>

<div class="tip"><strong>The 5-week pipeline is why demand forecasting matters so much.</strong> If Brandon is forecasting only 4-6 weeks out, he's operating hand-to-mouth. A COO should push for 12-16 week forecasting to give the factory enough lead time and avoid air freight emergencies (10x the cost of ocean).</div>

---

## Carrier Landscape
<!-- id: freight-carriers -->

<h3>Major Shipping Lines on the Trans-Pacific</h3>

<p>iRESTORE doesn't contract directly with carriers — their NVOCC (Topocean) does. But knowing the carrier landscape signals you understand the industry:</p>

<table>
  <tr><th>Alliance</th><th>Carriers</th><th>Notes</th></tr>
  <tr><td><strong>OCEAN Alliance</strong></td><td>COSCO, CMA CGM, Evergreen, OOCL</td><td>COSCO is dominant at Yantian. Chinese state-owned. If Kevin's family has relationships, likely with COSCO.</td></tr>
  <tr><td><strong>THE Alliance</strong></td><td>Hapag-Lloyd, ONE, Yang Ming, HMM</td><td>ONE is the merged Japanese carrier. Reliable Trans-Pacific coverage.</td></tr>
  <tr><td><strong>Independent</strong></td><td>Maersk, MSC</td><td>Left their 2M alliance in 2025. MSC is world's largest by capacity. Maersk is premium (10-15% more expensive, better tracking).</td></tr>
  <tr><td><strong>Independent</strong></td><td>ZIM</td><td>Israeli. Aggressive, nimble. Good for spot/overflow.</td></tr>
</table>

<h3>Current Market (Early 2026)</h3>

<table>
  <tr><th>Metric</th><th>Value</th></tr>
  <tr><td>Spot rate (Shanghai → LA)</td><td>~$2,000-2,500/FEU</td></tr>
  <tr><td>Contract rate range</td><td>~$1,500-2,100/FEU (locked annually)</td></tr>
  <tr><td>2026 forecast</td><td>Rates expected to drop 15-30% due to massive overcapacity (9M TEU of new ships delivering in 2026)</td></tr>
  <tr><td>Contract season</td><td>Negotiated in Q1 for May 1 - Apr 30 cycle</td></tr>
</table>

<div class="card">
  <div class="card-header">The All-In Cost Per Container (Yantian → La Mirada)</div>
  <table>
    <tr><th>Component</th><th>Cost</th></tr>
    <tr><td>Ocean freight (contract rate)</td><td>$1,500-2,500</td></tr>
    <tr><td>Surcharges (BAF, PSS, etc.)</td><td>$500-1,500</td></tr>
    <tr><td>Origin charges (THC, docs)</td><td>$300-600</td></tr>
    <tr><td>Customs brokerage (US)</td><td>$150-300</td></tr>
    <tr><td>Destination terminal handling</td><td>$300-500</td></tr>
    <tr><td>Drayage (port → La Mirada)</td><td>$400-700</td></tr>
    <tr><td>Chassis rental</td><td>$50-150</td></tr>
    <tr style="background: #e8f5e9;"><td><strong>Total per FEU</strong></td><td><strong>$3,200-6,250</strong></td></tr>
  </table>
  <p class="muted">This does NOT include duties/tariffs, which are assessed separately on the declared FOB value of the goods.</p>
</div>

---

## Tariff Risk & Optimization
<!-- id: freight-tariffs -->

<h3>iRESTORE's Current Tariff Position</h3>

<div class="card card-green">
  <div class="card-header">Good News: 12% Is Favorable</div>
  <p>iRESTORE's HTS classification (9013.80.9000) puts them at 4.5% base + 7.5% Section 301 = <strong>12% total</strong>. Many consumer electronics from China face 25-60%+ under various Section 301 tranches. iRESTORE's classification as an "optical device" rather than a generic consumer electronic gives them a significant advantage.</p>
</div>

<div class="card card-red">
  <div class="card-header">The Risk: Tariff Escalation</div>
  <p>If the current administration expands Section 301 tariffs or reclassifies iRESTORE's products, the impact is immediate and severe:</p>
  <table>
    <tr><th>Scenario</th><th>Duty Rate</th><th>Annual Duty Cost</th><th>Impact</th></tr>
    <tr style="background: #e8f5e9;"><td>Current</td><td>12%</td><td>~$4M</td><td>Manageable</td></tr>
    <tr style="background: #fff3e0;"><td>Moderate escalation</td><td>25%</td><td>~$8M</td><td>Material margin compression</td></tr>
    <tr style="background: #ffebee;"><td>Aggressive escalation</td><td>50%</td><td>~$16M</td><td>Existential threat to margins</td></tr>
  </table>
</div>

<h3>Tariff Mitigation Strategies</h3>

<ol>
  <li><strong>Protect the HTS classification</strong> — Engage a customs attorney to ensure 9013.80.9000 is defensible. If CBP challenges it, the cost of reclassification could be millions.</li>
  <li><strong>First Sale valuation</strong> — If goods flow through a trading company, you can declare the first (lower) transaction price as customs value. Requires documentation but can reduce dutiable value 10-20%.</li>
  <li><strong>Foreign Trade Zone (FTZ)</strong> — Import into an FTZ to defer duty payment until goods enter US commerce. Helps cash flow. Goods re-exported (e.g., to Canada) avoid US duties entirely.</li>
  <li><strong>Tariff engineering</strong> — Redesign product packaging/configuration to qualify under a different HTS code with a lower rate. Requires customs attorney but can save millions at scale.</li>
  <li><strong>Country diversification (China+1)</strong> — Moving manufacturing to Vietnam, Thailand, or Taiwan to avoid China-specific tariffs. 12-24 month project. For a company targeting $500M exit, this is a board-level conversation.</li>
</ol>

<div class="tip"><strong>COO talking point:</strong> "At $90M revenue, your tariff exposure is probably $4M/year. That's manageable at 12%, but if rates move to 25%, it doubles overnight. I'd want to audit the HTS classification in the first 30 days, model the tariff escalation scenarios, and have a China+1 contingency plan ready — not because we need it today, but because a buyer at $500M will ask about supply chain diversification."</div>

---

## Questions to Ask About Freight
<!-- id: freight-questions -->

<h3>For Brandon (Dir. of Ops)</h3>
<ol>
  <li>"Walk me through the freight process — how many containers are you bringing in per month, and who manages the Topocean relationship?"</li>
  <li>"Are you buying FOB or CIF from the factory? Who controls the carrier selection?"</li>
  <li>"What's your container utilization rate? Are you cubing out the 40-footers?"</li>
  <li>"How far out are you forecasting demand? What happens when you need to air-freight something?"</li>
  <li>"Have you gotten competitive bids from other forwarders recently, or has Topocean been the default?"</li>
  <li>"What's your average port dwell time, and are you eating any demurrage?"</li>
</ol>

<h3>For Kevin</h3>
<ol>
  <li>"What's your current HTS classification, and when's the last time it was reviewed? At $90M, a 1% tariff change is $300K."</li>
  <li>"Have you modeled the tariff escalation risk? If Section 301 moves from 7.5% to 25%, that's an extra $5M/year."</li>
  <li>"Has anyone looked at First Sale valuation or FTZ for duty optimization?"</li>
  <li>"With body panels coming from a different factory, does that change your freight dynamics? Different container requirements?"</li>
</ol>

---
