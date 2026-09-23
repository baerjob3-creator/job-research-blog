---
title: "They Assembled Gene-Sized DNA Inside Living Human Cells — No Breaks Required, No Cell Division Needed"
date: 2026-09-20
excerpt: "Boston Children’s / Dana-Farber Nature report on prime assembly — CRISPR-programmed dual flaps that install gene-sized DNA without breaks or cell division."
tags: [CRISPR, gene-editing, Nature, Boston-Childrens, Dana-Farber, prime-assembly, genetics, science, 2026]
author: Research
featured: false
---

# They Assembled Gene-Sized DNA Inside Living Human Cells — No Breaks Required, No Cell Division Needed

**Subtitle:** A Boston Children’s / Dana-Farber *Nature* report introduces prime assembly — CRISPR-programmed dual flaps that install DNA up to **12.1 kb**, work in **G1-arrested** cells and primary **T cells / HSPCs**, and can drive **megabase-scale** rearrangements without relying on HDR.

---

Gene therapy’s hardest unfinished sentence is still the same one: *put a large, precise DNA change exactly where you want it — in the cells that matter — without making a mess.* Base editors flip single letters. Prime editors write short patches. Homology-directed repair (HDR) can install bigger payloads, but it mostly works when cells are dividing and usually leans on nuclease-cut DNA. For resting immune cells, blood stem cells, and anything post-mitotic, that combination has been a wall.

On **September 16, 2026**, *Nature* published an open-access answer with a deceptively calm name. **Sébastien Levesque**, **Nozomu Kawashima**, **Gue-Ho Hwang**, and colleagues — senior authors including **Daniel E. Bauer** and **Suneet Agarwal** at Boston Children’s Hospital / Dana-Farber / Harvard / Broad — report **prime assembly (PA)**: CRISPR-targeted dual 3′ flap synthesis that lets human cells assemble and integrate single- or double-stranded DNA donors at a programmed locus (DOI **10.1038/s41586-026-11024-2**). The abstract’s claim is the shareable one: RNA-programmable, site-specific integration of medium-to-large DNA **without** requiring double-stranded DNA donors, **nuclease-driven double-strand breaks**, or **cell-cycle progression**.

This is not another “CRISPR fixed a disease in a patient” clinical vignette. It is a **platform methods** paper — and that is why it matters for Sunday readers who already watched islet transplants and Parkinson’s grafts move through the clinic. The bottleneck PA attacks is the one those therapies still hit when the cargo gets large.

## What prime assembly actually does

Think of classical **Gibson assembly** — the lab trick that stitches overlapping DNA fragments into one molecule in a tube — relocated *inside* a human cell and aimed at a genomic address. Twin prime-editing guide RNAs (pegRNAs) program two 3′ flaps at the target. Donor DNA is designed so its ends overlap those flaps. After annealing, endogenous repair finishes the job: excision of the unedited duplex, fill-in synthesis, ligation. The cell becomes the cloning bench.

That architecture unlocks three headline capabilities in one paper:

- **Kilobase payloads.** Gene-sized donors from **3.1 kb to 12.1 kb** (puromycin resistance + PGK1–eGFP) went into the safe-harbor **AAVS1** locus. Efficiency fell with size, as expected — about **28.1%** eGFP⁺ cells at **9.1 kb**, **7.4%** at **12.1 kb** — but the large cassettes were on-target and enrichable.
- **Multi-fragment assembly.** Under selective pressure at *ATP1A1*, the team assembled **up to four** overlapping ssDNA pieces into one integrated product — Gibson logic, cellular address.
- **Cell-cycle independence.** In K562 cells arrested in **G1** with the CDK4/6 inhibitor **palbociclib**, HDR at AAVS1 collapsed from ~**17%** to undetectable. Prime assembly’s eGFP integration held with little change — the paper’s direct answer to HDR’s S/G2 dependency.

Purity can be tuned. Inhibiting DNA-PK with **AZD7648**, alone or with a Polθ inhibitor (**PolQi1**), raised the precise-to-imprecise PA ratio **4.1-fold** and **8.5-fold**. Genome-wide **Donor-seq** profiles supported high specificity relative to nuclease knock-in strategies.

## Primary cells — where the therapy argument lives

Bench cell lines are rehearsal. The paper’s therapeutic stakes sit in **primary human CD3⁺ T cells** (four healthy donors in cell-cycle assays; three in editing runs) and **CD34⁺ hematopoietic stem and progenitor cells** (three donors).

In HSPCs, using PE7 mRNA plus pegRNAs and ssDNA donors, they measured average PA alleles of **1.5%** at **AAVS1** and **1.3%** at **IL2RG** — modest percentages, high significance: *in cellulo* assembly works in the same cell class that already produced the approved CRISPR medicine exa-cel. In T cells, PA targeted the **TRAC** locus — the industry’s favorite docking site for CAR-T engineering — including under resting (non-activated) culture conditions that keep cells out of the HDR-friendly cycle. Benchmarking in model lines showed PA beating or matching HDR, HITI, MMTI/PITCh, and PASSIGE at several loci; at **TRAC** in Jurkat cells with NHEJ/MMEJ inhibitors, PA reached ~**17.4%** eGFP⁺ versus low single-digit basal rates.

None of those numbers is “cured.” All of them are “the wall moved.”

## Megabases when you need rearrangements

Standard PA is framed as **nickase-class** editing — no obligatory nuclease DSB for integration. For chromosome-scale surgery the team also tested **nuclease prime assembly**. That mode installed a **93 Mb** chromosome-7 arm deletion and a **27 Mb** chromosome-19 arm deletion, a **1 Mb** inversion on chromosome 7 (**40.4%** of clones with the intended inversion vs **12.5%** for SpCas9 NHEJ, which also left junction deletions in every recovered clone), and even an **X–19** translocation. The paper is honest about the trade: DSBs help megabase rearrangements happen, at a purity cost. Keep the two modes mentally separate in any share — kilobase installs without breaks; megabase rearrangements with a nuclease-PA variant.

## What this is not

It is **not** an approved therapy. There is **no in vivo delivery** in this report — electroporation into cultured and primary cells, ex vivo. Efficiencies in HSPCs are still low for many clinical bar heights; large donors cost yield. Nuclease-PA rearrangements reintroduce DSB risk by design. Off-target Donor-seq looked favorable, not empty: TRAC and AAVS1 pegRNA sets showed measurable guide-dependent events that any translation path must map and mitigate. Related 2026 work (including an April *Nature* linear-donor PA paper reaching **~11 kb**, and other donor-annealing strategies) means the field is converging — credit the wave, don’t invent a monopoly.

## Why Sunday readers should care

Every CAR, every multi-exon correction, every gene-sized cassette that today’s editors cannot politely install runs into the same physics: big DNA, quiescent cells, DSB anxiety. Levesque, Kawashima, Hwang, Bauer, Agarwal, and colleagues just published a coherent workaround — **flaps instead of homology-search in S phase**, **assembly instead of blunt knock-in**, **primary blood cells instead of only immortalized lines**. An AllSci summary on **September 18, 2026** framed the same stakes: large payloads without the genotoxicity tax of routine nuclease cuts.

The next experiments write themselves: higher HSPC/T-cell efficiencies, cleaner long-read maps of multi-fragment products, in vivo delivery tests, and head-to-head trials against PASSIGE and twinPE knock-ins in actual therapeutic constructs. None of that is promised by a September methods paper. All of it becomes easier to fund once the field can say, without hedging the sentence to death: **human cells can assemble gene-sized DNA on target without waiting to divide.**

Prime editing taught cells to write short letters. Prime assembly teaches them to paste chapters — and, when needed, to rearrange whole shelves — at an address the RNA specifies.

---

## Sources

1. Levesque, S., Kawashima, N., Hwang, G.-H., Zeng, J., Toskov, V., Barry, T., Mannherz, W., Homfeldt, L., Becerra, B., Schoonenberg, V. A. C., Pinello, L., Agarwal, S. & Bauer, D. E. (2026). Targeted genomic integration and rearrangement using prime assembly. *Nature*. Published 16 September 2026 (open access). https://doi.org/10.1038/s41586-026-11024-2
2. Liu, B., Petti, A., Zhou, X., et al. (2026). Prime assembly with linear DNA donors enables large genomic insertions. *Nature*. Published 29 April 2026. https://doi.org/10.1038/s41586-026-10460-4
3. AllSci Editorial / McTiernan, R. (2026, September 18). Boston Children’s-led team develops prime assembly for large DNA insertions. AllSci News. https://allsci.com/news/research/prime-assembly-boston-childrens-hospital-and/
4. Supplementary information for Levesque et al. (2026), *Nature* DOI 10.1038/s41586-026-11024-2 (megabase deletions/inversion/translocation details; multi-fragment assembly).
