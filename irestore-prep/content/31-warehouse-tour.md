---
id: "warehouse-tour"
title: "32. Warehouse Tour Questions"
icon: "🏭"
order: 31
group: "gameday"
groupOrder: 4
---
## Why This Matters
<!-- id: tour-context -->

<div class="card card-yellow">
<p><strong>Kevin's email:</strong> <em>"we'll do a warehouse tour"</em> — this is sandwiched between meeting the team and the live exercise. It's not filler. Kevin wants to see how you observe operations in real time. Brandon runs this warehouse and reports directly to Kevin. Every question you ask reflects whether you're a curious operator or a back-seat critic.</p>

<p><strong>The rules:</strong></p>
<ul>
<li>Ask questions, don't make pronouncements. You're a guest, not a consultant.</li>
<li>Frame everything as curiosity, not criticism. "How do you handle X?" not "Why don't you do Y?"</li>
<li>Brandon is loyal, reliable, and Kevin trusts him. Any perceived dig at Brandon = dig at Kevin's judgment.</li>
<li>Show you've been in warehouses before. Use the right vocabulary. Know what you're looking at.</li>
</ul>
</div>

---

## Inbound & Receiving
<!-- id: tour-inbound -->

<h3>Questions to Ask at the Receiving Dock / Inbound Area</h3>
<ul>
<li><strong>"How many containers are you receiving per month right now?"</strong> — Sets the baseline. At $90M and ~200K units/year, they're probably getting 3-5 40-ft containers/month. If it's more, ask about split shipments (inefficient).</li>
<li><strong>"Walk me through what happens when a container shows up — who inspects it, how do you log it into Fulfil?"</strong> — Shows you care about process, not just throughput. Reveals whether they have QC on inbound or just trust the factory.</li>
<li><strong>"Are you doing any inbound QC sampling, or does the factory handle all quality checks?"</strong> — Important because Kevin's father runs the factory. If they're not sampling, that's trust-based QC, which works until it doesn't.</li>
<li><strong>"What's your receiving-to-putaway cycle time?"</strong> — How long from container arrival to product on shelf and scannable in WMS? Best-in-class is same-day. If it's 2-3 days, that's a capacity or process issue.</li>
<li><strong>"Where are the body panels going to stage? They're going to need a different racking setup, right?"</strong> — Shows you're already thinking about the Q2 launch. Body panels are oversized — standard pallet racking won't work. Floor-stacked or custom racking is $20-50K.</li>
</ul>

---

## Storage & Inventory Layout
<!-- id: tour-storage -->

<h3>Questions to Ask While Walking the Floor</h3>
<ul>
<li><strong>"How are you organized — by SKU, by channel, or by velocity?"</strong> — Best practice is high-velocity SKUs near packing stations. If the Pro Helmet (42% of revenue) is in the back corner, that's a pick-path problem.</li>
<li><strong>"What's your max pallet capacity vs. current utilization?"</strong> — Are they at 70%? 90%? If they're above 85%, they're going to hit a wall when body panels arrive. This naturally leads to the 3PL conversation without you having to force it.</li>
<li><strong>"Are you separating Amazon FBA prep from DTC outbound?"</strong> — These are different workflows. FBA has specific labeling, packaging, and palletizing requirements. If they're comingled, it creates errors and chargebacks.</li>
<li><strong>"Do you have dedicated zones for each channel — DTC, Amazon, Costco?"</strong> — Costco has strict pallet build and labeling requirements. If Costco orders are built ad-hoc in the same area as DTC, compliance errors are almost guaranteed.</li>
<li><strong>"How do you handle inventory counts — cycle counts, full physicals, or both?"</strong> — Reveals inventory accuracy. If they're only doing annual physicals, shrinkage and misships are probably higher than they think.</li>
<li><strong>"What's your current square footage, and what's the lease situation?"</strong> — Practical question. If the lease is up in 12-18 months, that's a natural trigger to evaluate whether to expand here or add a second node.</li>
</ul>

---

## Pick, Pack & Ship
<!-- id: tour-pick-pack -->

<h3>Questions to Ask at the Packing Stations</h3>
<ul>
<li><strong>"What's your peak daily throughput — orders per day at your busiest?"</strong> — Sizes the operation. At $90M with avg order ~$400, they're shipping roughly 600-800 DTC orders/day in peak. If peak throughput is 500, they were scrambling in Q4.</li>
<li><strong>"Are pickers using scan guns or paper pick lists?"</strong> — Scan guns integrated with Fulfil.io = low error rate. Paper pick lists = higher misship rate and no real-time inventory deduction.</li>
<li><strong>"How do you handle multi-item orders? Are kitting and bundling done at pick or pre-staged?"</strong> — If they're selling helmet + serum bundles, the pick logic matters. Pre-kitted bundles are faster to ship but tie up inventory. Pick-at-order is flexible but slower.</li>
<li><strong>"What carriers are you using for DTC, and are you rate shopping?"</strong> — UPS/FedEx/USPS rate shopping (via ShipStation, EasyPost, etc.) can save 10-15% on shipping costs. If they're on a single carrier agreement, there's savings on the table.</li>
<li><strong>"How do you handle same-day cutoff? What time do orders need to be in by to ship today?"</strong> — Shows you understand the DTC customer experience. Amazon has trained everyone to expect fast shipping. If their cutoff is noon and competitors ship until 3pm, they're losing on delivery speed.</li>
<li><strong>"What does your Q4 staffing look like — do you bring on temps?"</strong> — At 39% of revenue in Q4, they need 2-3x normal labor. Temp agencies, overtime, weekend shifts? This tells you how well they plan for peak.</li>
</ul>

---

## Returns & Reverse Logistics
<!-- id: tour-returns -->

<h3>Questions to Ask in the Returns Area</h3>
<ul>
<li><strong>"Walk me through the returns flow — from when a box shows up to when the unit is dispositioned."</strong> — The money question. Are returned units inspected, tested, categorized (restock, refurb, recycle), and logged? Or do they pile up?</li>
<li><strong>"How many returns are you processing per day/week right now?"</strong> — At ~10% return rate and ~200K+ units/year, that's ~20K returns/year or ~400/week. This is a real operation, not a side task.</li>
<li><strong>"What percentage of returns are actually defective vs. 'didn't like it' or 'didn't see results'?"</strong> — This data drives the return reduction strategy. If 60% of returns are non-defective, better pre-purchase content and a "save the sale" call could cut returns by 3-4 points.</li>
<li><strong>"What happens to refurbished units? Are you reselling them, using them for influencer seeding, or writing them off?"</strong> — This is where your refurb-to-B2B idea from the interview comes in. If they're writing off functional units, that's $2-4M of recoverable value.</li>
<li><strong>"Do Amazon returns come back here or go through Amazon's process?"</strong> — Important distinction. FBA returns are handled by Amazon and often end up in liquidation. FBM returns come back to La Mirada. Understanding the split affects the refurb opportunity sizing.</li>
<li><strong>"Is there a returns dashboard in Fulfil that tracks reason codes and trends?"</strong> — If not, that's a quick win. You can't reduce returns without knowing why they're happening. Offer this as a "first 30 days" deliverable.</li>
</ul>

---

## Technology & Systems
<!-- id: tour-tech -->

<h3>Questions to Ask About the Tech Stack</h3>
<ul>
<li><strong>"How integrated is Fulfil.io with the warehouse floor? Do pick tickets and receiving auto-update inventory?"</strong> — Reveals whether Fulfil is a real WMS or just an ERP they're using for order management while the warehouse runs on spreadsheets.</li>
<li><strong>"Are you using barcode/scan verification at pack-out?"</strong> — Scan-verify before sealing a box catches misships. If they're not doing this, their misship rate is probably 1-3%. Industry best practice is &lt;0.5%.</li>
<li><strong>"Do you have real-time inventory visibility across all channels — DTC, Amazon FBA, Costco?"</strong> — Multichannel inventory is hard. If FBA inventory is managed separately from Fulfil, they're probably over-ordering or running out in one channel while overstocked in another.</li>
<li><strong>"What reporting does Brandon see daily? Is there an ops dashboard?"</strong> — Connects to the KPI dashboard scenario in the live exercise. If Brandon is running on gut feel, the warehouse works but doesn't optimize.</li>
</ul>

---

## People & Culture
<!-- id: tour-people -->

<h3>Questions to Ask About the Warehouse Team</h3>
<ul>
<li><strong>"How big is the warehouse team right now?"</strong> — Gives you cost context. If it's 15-20 people at $18-22/hr in La Mirada, that's ~$600K-$900K in warehouse labor. Important for the 3PL cost comparison.</li>
<li><strong>"How long has the core team been here?"</strong> — Tenure tells you about culture. If most of the team has been here 3+ years, Brandon has built loyalty. If turnover is high, there's a compensation or management issue.</li>
<li><strong>"What does training look like for new hires?"</strong> — Fast-growing companies often skip formal training. If new pickers learn by shadowing for a day and then they're on their own, error rates are high and scale is limited.</li>
<li><strong>"How does the team handle peak? Is it overtime, temps, or weekend shifts?"</strong> — Shows you understand the human side of operations. Kevin's learning to fire people — a COO who also thinks about how to retain and motivate the team stands out.</li>
</ul>

---

## Strategic Observations (Don't Ask — Just Notice)
<!-- id: tour-observe -->

<div class="card card-green">
<h3>Things to Quietly Observe and Bring Up Later</h3>
<ul>
<li><strong>Cleanliness and organization:</strong> 5S principles. Is the floor clean? Are aisles clear? Are staging areas labeled? This tells you whether Brandon runs a tight ship or a chaotic one.</li>
<li><strong>Safety:</strong> Fire extinguishers accessible? Forklift certifications posted? Emergency exits clear? Don't call it out during the tour, but note it for the exercise if relevant.</li>
<li><strong>Space utilization:</strong> How much vertical space is being used? If they have 20-foot ceilings and 8-foot racking, they're using 40% of their cubic capacity. That's a cheap expansion before considering a second location.</li>
<li><strong>Signage and labeling:</strong> Are bin locations labeled? Are zones clearly marked? Good signage = a system. No signage = tribal knowledge that breaks when key people leave.</li>
<li><strong>Work in progress:</strong> How much product is sitting between stations? Long queues between pick and pack = bottleneck. Empty stations = overstaffing or unbalanced workflow.</li>
<li><strong>The vibe:</strong> Are people engaged or going through the motions? Does Brandon introduce you to people by name? Does the team seem to know what they're doing? Culture is visible on the warehouse floor in a way it isn't in an office.</li>
</ul>
</div>

<div class="tip"><strong>After the tour:</strong> Reference specific things you saw during the live exercise. "When I saw the returns area, I noticed..." or "Brandon mentioned peak throughput is X — that's going to be a constraint when body panels launch." This shows Kevin you were paying attention, not just walking and nodding.</div>

---

## The One-Liner Responses
<!-- id: tour-one-liners -->

<p class="muted">Quick responses if Brandon or Kevin asks your opinion during the tour:</p>

<table>
<tr><th>If They Say...</th><th>You Say...</th></tr>
<tr><td>"We're running out of space"</td><td>"How much vertical are you using? And when's the lease up?" (Don't say "you need a 3PL" — that's a later conversation.)</td></tr>
<tr><td>"Returns are killing us"</td><td>"What's the split between defective and non-defective? That changes the playbook completely."</td></tr>
<tr><td>"Q4 was chaos"</td><td>"What was the daily peak? And how early did you start ramping temp labor?" (Shows you know the levers.)</td></tr>
<tr><td>"We're thinking about a second location"</td><td>"Makes sense for transit time reduction. Have you modeled where the customer density is — east coast vs. central?" (Don't oversell 3PL.)</td></tr>
<tr><td>"Fulfil is great but..."</td><td>"What's the biggest gap? Is it WMS functionality, reporting, or integration with channels?" (Shows you know ERPs have limits.)</td></tr>
<tr><td>"Brandon runs a tight ship"</td><td>"I can see that. The question is how we scale what he's built without losing the quality." (Validates Brandon, reframes as growth.)</td></tr>
</table>
