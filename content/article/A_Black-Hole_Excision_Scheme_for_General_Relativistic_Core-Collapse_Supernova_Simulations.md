---
title: "A Black-Hole Excision Scheme for General Relativistic Core-Collapse Supernova Simulations"
date: "2022-10-24"
type: article
tags:
  - "arxiv"
  - ""
categories:
  - supernovae
  - 2022(year)
  - 10(month)
draft: false
---

> First author: B. Sykes

 Fallback supernovae and the collapsar scenario for long-gamma ray burst and
hypernovae have received considerable interest as pathways to black-hole
formation and extreme transient events. Consistent simulations of these
scenarios require a general relativistic treatment and need to deal
appropriately with the formation of a singularity. Free evolution schemes for
the Einstein equations can handle the formation of black holes by means of
excision or puncture schemes. However, in constrained schemes, which offer
distinct advantages in long-term numerical stability in stellar collapse
simulations over well above $10^{4}$ light-crossing time scales, the dynamical
treatment of black-hole spacetimes is more challenging. Building on previous
work on excision in conformally flat spacetimes, we here present the
implementation of a black-hole excision scheme for supernova simulations with
the CoCoNuT-FMT neutrino transport code. We describe in detail a choice of
boundary conditions that ensures long-time numerical stability, and also
address upgrades to the hydrodynamics solver that are required to stably evolve
the relativistic accretion flow onto the black hole. The scheme is currently
limited to a spherically symmetric metric, but the hydrodynamics can be treated
multi-dimensionally. For demonstration, we present a spherically symmetric
simulation of black-hole formation in an $85 M_\odot$ star, as well as a
two-dimensional simulation of the fallback explosion of the same progenitor.
These extend past 9s and 0.3s after black-hole formation, respectively.

---
[arxiv link](http://arxiv.org/abs/2210.12939v1)

[pdf link](http://arxiv.org/pdf/2210.12939v1)