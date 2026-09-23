# Handoff — Website Developer

## Suggested title
Scientists Built a DNA Computer That Does Math in a Drop of Water

## Short excerpt
Maynooth University’s Scaffolded DNA Computer settles into the correct answer with heat, salt, and DNA — no continuous electricity — in a *Nature* study that includes 100-bit addition.

## Tags / topic labels
`DNA computing` `molecular computing` `Scaffolded DNA Computer` `SDC` `thermodynamics` `Maynooth University` `Nature` `Damien Woods` `Abeer Eshra` `Tristan Stérin` `nanotechnology` `DNA origami` `equilibrium computation` `energy-efficient computing` `2026`

## Full post body (Markdown — COMPLETE)

# Scientists Built a DNA Computer That Does Math in a Drop of Water

**Subtitle:** Maynooth University’s Scaffolded DNA Computer settles into the correct answer with heat, salt, and DNA — no continuous electricity — in a *Nature* study that includes 100-bit addition.

---

Most computers fight entropy. They burn power to keep bits where you put them, correct errors, and push a calculation through a prescribed sequence of steps. On September 16, 2026, a team at Maynooth University in Ireland published a different bet in *Nature*: build a molecular machine whose **most energetically favoured state is the answer**, then let chemistry relax into it.

They call it the **Scaffolded DNA Computer (SDC)**. Short DNA strands and a longer DNA scaffold go into a tiny drop of salt water. Heat, cool, wait. The molecules compete, bind, and rearrange until the favoured structure forms — and that structure *is* the result. Joint first authors **Tristan Stérin** and **Abeer Eshra**, with **Constantine Glen Evans**, undergraduate researcher **Janet Adio**, and corresponding author **Damien Woods**, demonstrated the idea on **10 programs**, including multiplication by 3, division by 2, 8-bit parity detection, and addition of 25-bit numbers — a **100-bit** computation.

## Why “thermodynamically favoured” matters

Living cells and silicon chips both stay useful by staying *out* of equilibrium. Cells burn fuel. Chips burn watts. Molecular programmers have usually followed the same logic: design kinetic pathways, add molecular “fuel,” time temperature holds carefully, and fight leaks and off-target reactions with redundancy and error correction.

Theory has long said there is another route. If you can engineer an energy landscape so the correct output is the equilibrium configuration, computation becomes a kind of settling — not a forced march. Machine-learning search algorithms already exploit related ideas on conventional hardware, at enormous energy cost. What was missing was a programmable wet medium where that landscape could be built on purpose.

The SDC borrows inspiration from **DNA origami**: a long scaffold that tiles assemble around, driven by a strong thermodynamic preference for the target nanostructure. The Maynooth team’s twist is to make that assembly *compute*. Each scaffold position hosts competing “tiles” (short compute strands). Adjacent tiles must match colour-coded domains. Mismatches cost energy and get replaced. Excess tile concentration over the scaffold pushes every position to fill. Weak enough affinities keep binding reversible, so errors can walk off the chain instead of freezing in place.

Woods told *Live Science* the clever part is competition: molecules jostle to bind the scaffold; the energetically preferred winner encodes the answer. Eshra’s institutional line lands the scale: a small droplet holds **billions, sometimes trillions**, of DNA strands interacting to produce a result.

## What it actually computed

This is not a metaphor for “DNA storage” or a vague wet-lab demo. The paper’s program list is concrete:

- **Multiply-by-3** and **Divide-by-2**
- **8-bit parity** (odd/even number of 1s)
- **Addition**, including 25-bit inputs framed as a 100-bit computation
- Broader runs across **base-3 strings and graphs**

Across the core experiments the team reports **over 700 computations**, with inputs up to 50-bit binary and up to 100 bits of compute. Small instances finish in **under a minute**. *Live Science* and Maynooth’s Tech Xplore release both cite **10 + 3 ≈ 30 seconds**. A harder sum with numbers in the range of about **11 million to 34 million** took up to **14 hours**.

Programming looks almost mundane once the chemistry is designed: different programs and inputs mean different strand sets pulled from the fridge. Readout uses a quenched-fluorescence reporter so output bits light up as 0 or 1 along the scaffold.

Constantine Evans is frank about the vanity metric. Adding 10 and 3 is trivial for a person and instantaneous for silicon. The point is reliability at the molecular scale: a handful of molecule types, no irreversible fuelled steps, and still the right answer — something previous DNA computers have found brutally hard.

## Reusable, not single-use chemistry

Many earlier molecular computers were one-shot reactions. The SDC was built to be **reused**. The *Nature* abstract says algorithms can be reused **dozens of times**; institutional coverage notes up to about **25** calculations in a row, and figure captions describe counter experiments run **24 times** per sample. One plate partially dried out; **1.5 years** later the team added water and re-ran Multiply-by-3 and Parity — getting the data they report.

That longevity matters for the story they are selling: equilibrium computation as a practical experimental style, not a fragile stunt. Simple anneals replace multi-step manual protocols and early experiment termination to dodge leak. No continuous electricity during the compute — only the heat pulse to start the landscape search.

Woods frames the wider motivation bluntly in the Maynooth release: silicon and data centres already eat a huge share of national electricity (he cites **23% of Ireland’s**). Brains and chemistry are reminders that computation need not look like a rack of GPUs. Eshra is equally clear about scope: molecular computers are **not** trying to replace electronic ones. Plausible longer-term niches include biological environments, smart materials, and archival DNA data storage with built-in error-correction flavour — all still speculative relative to the peer-reviewed demo.

## What this is — and what it is not

It is **not** a laptop-killer, a wet ChatGPT, or proof that DNA will run your phone. Fourteen hours for a large sum is glacial next to silicon. Applications inside living cells remain future work. Authors Stérin, Eshra, and Woods are listed as inventors on pending patents covering core principles and fluorescent reporting — a normal academic disclosure, not a product launch.

It **is** peer-reviewed evidence that a programmable DNA system can encode finite-state programs so the thermodynamically favoured configuration is the correct output; that small instances run in under a minute; that the same molecules can be reused dozens of times; and that 100-bit-scale addition is reachable without continuous power or classical kinetic babysitting. Woods calls it blue-sky science. Fair. Blue sky that adds numbers in salt water is still a new colour of computer.

---

## Sources

1. Stérin, T., Eshra, A., Evans, C. G., Adio, J., & Woods, D. (2026). A thermodynamically favoured molecular computer. *Nature*. https://doi.org/10.1038/s41586-026-10996-5
2. Maynooth University (via Tech Xplore). (2026, September 16). DNA computer performs 100-bit calculations using heat, water and salt. https://techxplore.com/news/2026-09-dna-bit-salt.html
3. Hughes-Castleberry, K. (2026, September 19). Scientists build a DNA computer that can perform calculations in a drop of water. *Live Science*. https://www.livescience.com/technology/computing/scientists-build-a-dna-computer-that-can-perform-calculations-in-a-drop-of-water
