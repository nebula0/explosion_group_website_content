---
title: "The Cosmological Simulation Code OpenGadget3 -- Implementation of Meshless Finite Mass"
date: "2023-01-09"
type: article
tags:
  - "arxiv"
  - "most recent update (Wed Jan 11 2023)"
categories:
  - cosmology
  - 2023(year)
  - 1(month)
draft: false
---

> First author: Frederick Groth

 Subsonic turbulence plays a major role in determining properties of the intra
cluster medium (ICM). We introduce a new Meshless Finite Mass (MFM)
implementation in OpenGadget3 and apply it to this specific problem. To this
end, we present a set of test cases to validate our implementation of the MFM
framework in our code. These include but are not limited to: the soundwave and
Kepler disk as smooth situations to probe the stability, a Rayleigh-Taylor and
Kelvin-Helmholtz instability as popular mixing instabilities, a blob test as
more complex example including both mixing and shocks, shock tubes with various
Mach numbers, a Sedov blast wave, different tests including self-gravity such
as gravitational freefall, a hydrostatic sphere, the Zeldovich-pancake, and the
nifty cluster as cosmological application. Advantages over SPH include
increased mixing and a better convergence behavior. We demonstrate that the
MFM-solver is robust, also in a cosmological context. We show evidence that the
solver preforms extraordinarily well when applied to decaying subsonic
turbulence, a problem very difficult to handle for many methods. MFM captures
the expected velocity power spectrum with high accuracy and shows a good
convergence behavior. Using MFM or SPH within OpenGadget3 leads to a comparable
decay in turbulent energy due to numerical dissipation. When studying the
energy decay for different initial turbulent energy fractions, we find that MFM
performs well down to Mach numbers $\mathcal{M}\approx 0.007$. Finally, we show
how important the slope limiter and the energy-entropy switch are to control
the behavior and the evolution of the fluids.

---
[arxiv link](http://arxiv.org/abs/2301.03612v1)

[pdf link](http://arxiv.org/pdf/2301.03612v1)