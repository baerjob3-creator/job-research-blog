# Handoff — Website Developer

## Suggested title
Zirconia Specks Just Cracked a Solar Trade-Off — 34% Efficiency and a Record 2.014 Volts

## Short excerpt
Soochow University and LONGi’s *Science Bulletin* perovskite–silicon tandem uses a discontinuous ZrO₂ nano-scaffold to hit 34.0% lab efficiency, 33.5% certified steady-state, and a record-class open-circuit voltage of 2.014 V.

## Tags / topic labels
`perovskite` `silicon tandem` `solar cell` `ZrO2` `zirconia` `nano-scaffold` `Soochow University` `LONGi` `Science Bulletin` `photovoltaics` `open-circuit voltage` `interface engineering` `MeO-4PACz` `clean energy` `2026`

## Full post body (Markdown — COMPLETE)

# Zirconia Specks Just Cracked a Solar Trade-Off — 34% Efficiency and a Record 2.014 Volts

**Subtitle:** Soochow University and LONGi build a perovskite–silicon tandem with a discontinuous ZrO₂ nano-scaffold — 34.0% lab efficiency, certified 33.5% steady-state, and an independently verified open-circuit voltage of 2.014 V.

---

Silicon solar cells power most of the world’s rooftops for a reason: they are cheap, durable, and good enough. They are also approaching a **physical ceiling**. A single-junction silicon cell’s practical Auger-limited efficiency sits near **~29.4%**; commercial modules typically live in the mid-20s. To climb higher, engineers stack a second absorber on top — a wide-bandgap **perovskite** that harvests the blue-green photons silicon wastes as heat — and wire the pair into a **two-terminal tandem**. Theory says that architecture can reach the low **40s**. Reality has been stuck on a messier problem: how do you grow a perfect perovskite film on rough silicon without killing the voltage or choking the current?

On the September press cycle culminating in coverage dated **September 18–20, 2026**, a Soochow University–LONGi team answered with something almost rude in its simplicity: **specks**. Discrete monoclinic **zirconia (ZrO₂)** nanoparticles, parked between a transparent conductive oxide and a molecular monolayer, form a nanoscale interfacial scaffold. The paper — *“Nanoscale interfacial scaffold enables perovskite/silicon tandems with 34% efficiency and an open-circuit voltage over 2.01 V”* — appears in *Science Bulletin* (DOI **10.1016/j.scib.2026.09.007**). Science China Press’s EurekAlert release (September 18), *pv magazine*’s technical write-up (September 10), and Interesting Engineering’s same-day September 20 feature put the shareable numbers in one line: **34.0%** lab power conversion efficiency, **33.5%** certified steady-state, and a certified open-circuit voltage of **2.014 V** — among the highest reported for this class of device.

## The trade-off that kept eating voltage

Tandems fail in the dark corners. Textured crystalline silicon is optically excellent and morphologically hostile: perovskite precursors do not want to spread into a dense, void-free film across those pyramids. At the **buried interface** where holes must leave the perovskite through a hole-transport stack, charges get trapped and recombine without making light — **non-radiative recombination**. Past fix attempts often created a second problem. A continuous insulating passivation layer can raise voltage by quieting recombination, then sabotage fill factor by blocking the very carriers you meant to extract.

That is the trade-off: **passivate harder, extract worse**. Sunday science is about the teams that refuse to pick only one side.

## Specks, not a blanket

Led by **Jiang Liu**, **Xiaohong Zhang**, and **Hongbo Mo** at Soochow University’s College of Energy, with **Bo He** at LONGi Central R&D Institute and co–first authors **Huimin Zhang** and **Qingshui Zheng**, the group inserted **discrete** monoclinic ZrO₂ nanoparticles between the cell’s transparent conductive oxide (ITO) and a **MeO-4PACz** self-assembled monolayer (SAM). Not a continuous dielectric sheet. A discontinuous, nanoporous buffer.

The nanoparticles do two jobs at once:

1. **Surface-energy tuning** — helping the liquid perovskite precursor wet and crystallize into denser, larger-grain, void-free films on the textured stack.
2. **Nanoscale localized contacts** — zirconia islands provide **field-effect passivation** that suppresses non-radiative recombination, while the **exposed SAM pathways** keep hole extraction alive.

ZrO₂’s high dielectric constant screens local electrical fluctuations and limits interfacial charge pile-up (and hysteresis). Its wide bandgap (~**5.49 eV**, per the *pv magazine* technical account) means negligible visible-light absorption. X-ray photoelectron spectroscopy supported formation of **Zr–O–P** bonds between zirconia and the monolayer phosphonate chemistry — a **dual-anchoring network** that, together with SAM–oxide bonding, improves molecular attachment and coverage uniformity. Time-resolved photoluminescence told the kinetics story: average carrier lifetime roughly doubled, from **1.46 μs to 2.81 μs**. Conductive AFM and Kelvin probe maps showed more uniform current and surface potential — fewer leaky hotspots.

In plain language: the interface got quieter *and* still conductive where it needed to be.

## The numbers that travel

Under standard illumination, the champion monolithic tandem — crystalline-silicon bottom cell plus inverted **p-i-n** perovskite top cell — posted:

- Power conversion efficiency: **34.0%**
- Open-circuit voltage: **1.997 V** (lab champion)
- Short-circuit current density: **20.36 mA cm⁻²**
- Fill factor: **83.62%**

Independent certification confirmed an open-circuit voltage of **2.014 V** and a steady-state efficiency of **33.5%**. That Voc figure is the record-flavored hook for this device class in the institutional coverage — voltage is often the honest scoreboard for how well an interface has been tamed.

Durability is not an afterthought. Encapsulated zirconia-modified devices under continuous **1-sun** illumination at maximum power point and room temperature retained **84%** of initial efficiency after **2,000 hours**. A control without the interfacial strategy, *pv magazine* notes, had already fallen to **70%** by **1,000 hours**. That is not a 25-year rooftop warranty. It is evidence that the same nano-scaffold that raises Voc also helps the stack survive continuous operation — the metric that separates press-cycle cells from products.

## What this is — and what it is not

It is **not** the absolute world-record tandem efficiency. LONGi separately holds a **35.5%** crystalline silicon–perovskite two-terminal record certified by ESTI (July 2026 conference disclosure), with earlier milestones logged in the Solar Cell Efficiency Tables. Tonight’s story is a **mechanism**: a dual-anchored ZrO₂ nano-scaffold that solves a specific buried-interface trade-off while delivering mid-30s efficiency, record-class voltage, and improved operational stability.

It is **not** a commercial rooftop panel shipping tomorrow. Lab cells, even certified ones, still face scale-up: large-area uniformity, lead management in perovskites, outdoor thermal cycling, damp heat, and bankable module warranties. LONGi’s own public pipeline talk — mass-production generation, next generation in development, another in reserve — is the industrial translation of that caveat.

What it **is**: a peer-reviewed demonstration, from a university–manufacturer collaboration already deep in the tandem race, that **patterned insulating contacts** can raise film quality and suppress recombination **without** forming a continuous transport-blocking blanket. Primary paper: Zhang, Zheng, Mo, He, Liu, Zhang, et al., *Science Bulletin* (2026). Public anchors: Science China Press / EurekAlert (September 18), *pv magazine* (September 10), Interesting Engineering (September 20).

## Why the voltage matters more than the round number

Efficiency headlines compress a stack of physics into one percentage. Open-circuit voltage is closer to a confession about interface quality. Hitting **>2.01 V** certified on a perovskite/silicon tandem means the top and bottom junctions are contributing with unusually little recombination tax at the joint that used to eat both. That is why the EurekAlert framing leads with voltage alongside the 34% lab figure — and why engineers will care about the zirconia recipe even if tomorrow’s absolute efficiency crown sits a point higher somewhere else.

The broader arc is industrial. Silicon alone is asymptotically approaching its Auger wall. Tandems are how photovoltaics keep compounding after that wall. Every credible interfacial fix — especially one built from earth-abundant oxide nanoparticles and a commercially familiar SAM chemistry — is a brick in the path from champion cells to factory lines.

## Why tonight’s shareable fact sticks

Clean energy does not only advance by inventing new fuels. Sometimes it advances by **refusing a false choice** at a buried interface. Specks of zirconia. Dual anchoring. A perovskite film that grows cleaner. Carriers that live twice as long. **34%** in the lab. **33.5%** certified steady-state. **2.014 V**. **84%** left after **2,000** hours of continuous sun.

Not an artificial leaf making hydrogen from seawater. Not a claim that rooftops hit 34% next quarter. A materials-science Sunday: the nano-scaffold that lets a tandem keep its voltage *and* its current — published in *Science Bulletin*, amplified across the PV press this month, and still fresh for tonight’s volume.

---

## Sources

1. Zhang, H., Zheng, Q., Mo, H., et al. (2026). Nanoscale interfacial scaffold enables perovskite/silicon tandems with 34% efficiency and an open-circuit voltage over 2.01 V. *Science Bulletin*. https://doi.org/10.1016/j.scib.2026.09.007
2. Science China Press / EurekAlert! (2026, September 18). Nano-scaffold breakthrough pushes perovskite/silicon tandem solar cells to 34% efficiency with record voltage of 2.014v. https://www.eurekalert.org/news-releases/1144549
3. Bellini, E. / *pv magazine*. (2026, September 10). Longi, Soochow University unveil 34.0% perovskite-silicon tandem solar cell based on dual-anchored interfacial design. https://www.pv-magazine.com/2026/09/10/longi-soochow-university-unveil-34-0-perovskite-silicon-tandem-solar-cell-based-on-dual-anchored-interfacial-design/
4. Tripathi, A. / Interesting Engineering. (2026, September 20). ‘Breakthrough’ perovskite-silicon tandem solar cell hits 34% efficiency, record-level voltage. https://interestingengineering.com/energy/perovskite-silicon-tandem-solar-cell
5. LONGi (2026, July). LONGi sets a 35.5 percent world record for crystalline silicon-perovskite tandem solar cell efficiency. https://eu.longi.com/press/longi-sets-a-35-5-percent-world-record-for-crystalline-silicon-perovskite-tandem-solar-cell-efficiency


## Notes for Website Developer

- Suggested slug: `2026-09-20-zirconia-perovskite-silicon-tandem-34-percent`
- Date: `2026-09-20`
- Featured: yes (tonight’s volume post) unless another post-0N in the same batch wins the slot
- Image preference: Science Bulletin / EurekAlert schematic of ZrO₂ nanoparticles at the ITO/SAM buried interface; optional certified J–V curves (33.5% / 2.014 V) and 2,000 h MPPT retention panel; avoid “miracle free-energy” stock imagery
- Differentiation: not artificial-leaf seawater H₂ (post-07); this is photovoltaic tandem interface engineering / electricity, not photochemical fuel
- Tone caveat: do not claim this paper is the 35.5% absolute world record, that modules ship at 34%, or that 2,000 h MPPT equals a rooftop warranty; keep lab vs certified vs commercial distinctions visible
