---
title: "GalCEM I -- An Open-Source Detailed Isotopic Chemical Evolution Code"
date: "2023-01-05"
type: article
tags:
  - "arxiv"
  - "most recent update (Wed Jan 11 2023)"
categories:
  - chemical
  - 2023(year)
  - 1(month)
draft: false
---

> First author: Eda Gjergo

 This is the first of a series of papers that will introduce a user-friendly,
detailed, and modular GALactic Chemical Evolution Model, GalCEM, that tracks
isotope masses as a function of time in a given galaxy. The list of tracked
isotopes automatically adapts to the complete set provided by the input yields.
The present iteration of GalCEM tracks 86 elements broken down in 451 isotopes.
The prescription includes massive stars, low-to-intermediate mass stars, and
Type Ia supernovae as enrichment channels. We have developed a preprocessing
tool that extracts multi-dimensional interpolation curves from the input yield
tables. These interpolation curves improve the computation speeds of the full
convolution integrals, which are computed for each isotope and for each
enrichment channel. We map the integrand quantities onto consistent array grids
in order to perform the numerical integration at each time step. The
differential equation is solved with a fourth-order Runge-Kutta method.
  We constrain our analysis to the evolution of all the light and intermediate
elements from carbon to zinc, and lithium. Our results are consistent up to the
extremely metal poor regime with Galactic abundances. We provide tools to track
the mass rate change of individual isotopes on a typical spiral galaxy with a
final baryonic mass of $5\times 10^{10} M_{\odot}$. Future iterations of the
work will extend to the full periodic table by including the enrichment from
neutron-capture channels as well as spatially-dependent treatments of galaxy
properties. GalCEM is publicly available at https://github.com/egjergo/GalCEM/

---
[arxiv link](http://arxiv.org/abs/2301.02257v1)

[pdf link](http://arxiv.org/pdf/2301.02257v1)