---
title: "Scientists Just Watched a Quantum of Sound Jump From One to Zero"
date: 2026-09-20
excerpt: "Stanford physicists recorded the first real-time quantum jump of a phonon in a mechanical resonator — a chip-scale tuning fork that lost its last packet of vibration while a superconducting qubit kept score."
tags: [quantum, physics, phonons, sound, Stanford, Science, quantum-acoustics, superconducting-qubit, quantum-computing, sensing, Safavi-Naeini, 2026]
author: Research
featured: false
---

# Scientists Just Watched a Quantum of Sound Jump From One to Zero

**Subtitle:** Stanford physicists recorded the first real-time quantum jump of a phonon in a mechanical resonator — a chip-scale “tuning fork” that lost its last packet of vibration while a superconducting qubit kept score.

---

Strike a bell and the ringing seems to fade smoothly. Quieter, then quieter still, then gone. Quantum mechanics has insisted for more than a century that this smooth fade is an illusion of scale: vibrational energy comes in discrete packets called **phonons**, and a resonator must lose them one at a time.

On September 17, 2026, a Stanford team led by applied physicist **Amir Safavi-Naeini** reported in *Science* that they had finally caught one of those steps live. In a microscopic mechanical resonator paired with a superconducting qubit, repeated measurements showed the device lingering in its one-phonon state — then abruptly switching to the ground state. Co-first authors **Takuma Makihara** and **Erik Szakiel** helped build the device that made the jump visible.

That is the first real-time observation of individual quantum jumps of sound in a mechanical resonator. Photons did it in 2007. Trapped ions did it in 1986. Sound had been the missing member of the club.

## A phonon is not a tiny bead of noise

A phonon is the quantum description of a coordinated vibration shared by many atoms in a solid — the sound analogue of a photon. Neighboring energy levels of a mechanical mode are separated by *hf*, where *f* is the mode frequency and *h* is Planck’s constant. The allowed energies form a ladder, not a ramp.

“One to zero” does not mean every atom freezes. Quantum mechanics still assigns the ground state an irreducible zero-point motion. The observed jump removed the last *countable* excitation above that floor.

Macroscopic bells hide the staircase because they hold enormous numbers of phonons. Losing them one by one produces steps too small and too fast to notice, the way individual pixels vanish into a continuous-looking photograph from across the room. Ordinary microphones and position sensors also fail the quantum test: average displacement can decline smoothly even when energy occupies discrete levels. Measuring position alone does not label each rung of the ladder.

## The trick: ask the same question hundreds of times

The Stanford device is a microscopic **lithium-niobate** mechanical resonator fabricated with chipmaking techniques, then integrated with a superconducting circuit using an aligned transfer-print process. The coupling is dispersive: each added phonon shifted the qubit’s frequency by about **328 kilohertz**. Microwave pulses turned that shift into a repeated parity check — essentially asking, over and over, whether the mechanical state contained an odd or even number of phonons.

Timing made the experiment possible. Left alone, the mechanical excitation lived about **2.1 milliseconds**. Scaled to an ordinary tuning fork, Stanford notes, that would be hours of ringing. That window was long enough for hundreds of fast quantum measurements during a single ringdown.

Readouts were noisy, so the team heralded the state they wanted to follow. Runs with six consecutive checks indicating one phonon yielded an **85 percent** single-phonon preparation fidelity. The same sequence then continued for **294** checks per trajectory. A public Zenodo archive holds **8,447** selected trajectories plus the Bayesian forward-backward analysis used to estimate the hidden state — unusually inspectable for a result this subtle.

In typical traces, outcomes stayed mostly consistent with the excited state, then abruptly flipped toward the ground state. Waiting times across the ensemble followed the exponential, memoryless pattern expected for spontaneous quantum decay.

## What “real time” and “direct” actually mean

No camera filmed a sound particle vanishing, and nobody heard an audible note snap off. The team inferred the resonator’s energy from a rapid qubit measurement record, resolving whether one vibrational quantum remained or the device had reached ground.

The observation is **direct** in the experimental sense: individual transition histories, not only averages over identically prepared systems. It is **real time** because the sequence located the transition during a single ringdown, with checks much faster than the mechanical lifetime. It is still an inference from a detector — and only approximately nondestructive. Under continuous parity checks, the observed one-phonon lifetime shrank to about **649 microseconds**. Each question carried a small chance of disturbing the excitation being monitored.

That back-action does not erase the result. It defines it more precisely: the detector extracted enough information to distinguish discrete one- and zero-phonon intervals before its own disturbance and natural loss ended the show.

## What this is — and what it is not

It is **not** a working quantum computer, a finished error-correction protocol, or proof that your smartphone will suddenly become a quantum device. It does not photograph phonons. It does not claim the first creation or detection of single phonons — those milestones already existed in quantum acoustics — only the first real-time jump trajectories of mechanical sound.

It **is** peer-reviewed confirmation that a vibration distributed across a solid object can be prepared with one quantum of energy, questioned hundreds of times, and followed to the random instant when that quantum is gone. The averaged ringdown remains smooth. An individual history ends with a step.

Safavi-Naeini framed the enabling claim plainly in Stanford’s release: vibrating objects can exhibit quantum behavior — “the prerequisite for many of the operations needed by quantum computing and sensing.” Makihara emphasized the fabrication fight: making an extremely long-lived vibrating object and integrating it with a qubit “without ruining either subsystem.” Szakiel pointed at the longer arc: fine-tuned control of sound could eventually improve devices that already treat vibration as fundamental technology.

## Why catching the jump matters

In many quantum architectures, a jump is an **error**. You cannot correct an error you cannot see. Repeated nondemolition-style checks are a foundation for any scheme that hopes to protect information encoded in mechanical states. This experiment did not demonstrate correction — 85 percent heralding fidelity and measurement-shortened lifetimes leave hard engineering ahead — but it shows the diagnostic step is possible.

The same platform is also a sensor candidate. Minute forces, accelerations, and added masses shift mechanical motion. Safavi-Naeini’s group, collaborating with Michael Roukes’s team at Caltech, is already exploring related devices to detect and identify proteins inside cells. Chip-scale packing raises the prospect of denser acoustic quantum circuits.

None of that is shipping tomorrow. The immediate result is simpler and stranger:

Sound can jump. We finally watched it do so.

---

## Sources

1. Makihara, T., Szakiel, E., et al.; Safavi-Naeini, A. H. (corresponding). (2026). Quantum jumps of sound. *Science*. https://doi.org/10.1126/science.aeh7535
2. Zaske, S. / Stanford School of Humanities and Sciences. (2026, September 17). Researchers observe first real-time quantum jump in sound. https://humsci.stanford.edu/feature/researchers-observe-first-real-time-quantum-jump-sound
3. EurekAlert! / Stanford University. (2026, September 17). Researchers observe first real-time quantum jump in sound. https://www.eurekalert.org/news-releases/1144153
4. ScienceBlog Lab Report. (2026, September 20). Real-time observation of a mechanical resonator losing its final phonon. https://scienceblog.com/t-quantum-jumps-sound-final-phonon-real-time/
5. Data and Code for “Quantum Jumps of Sound.” Zenodo. https://zenodo.org/records/20944616
