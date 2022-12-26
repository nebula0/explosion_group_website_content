---
title: "The N5K Challenge: Non-Limber Integration for LSST Cosmology"
date: "2022-12-8"
type: article
tags:
  - "arxiv"
  - ""
categories:
  - cosmology
  - 2022(year)
  - 12(month)
draft: false
---

> First author: C. D. Leonard

 The rapidly increasing statistical power of cosmological imaging surveys
requires us to reassess the regime of validity for various approximations that
accelerate the calculation of relevant theoretical predictions. In this paper,
we present the results of the 'N5K non-Limber integration challenge', the goal
of which was to quantify the performance of different approaches to calculating
the angular power spectrum of galaxy number counts and cosmic shear data
without invoking the so-called 'Limber approximation', in the context of the
Rubin Observatory Legacy Survey of Space and Time (LSST). We quantify the
performance, in terms of accuracy and speed, of three non-Limber
implementations: ${\tt FKEM (CosmoLike)}$, ${\tt Levin}$, and ${\tt matter}$,
themselves based on different integration schemes and approximations. We find
that in the challenge's fiducial 3x2pt LSST Year 10 scenario, ${\tt FKEM
(CosmoLike)}$ produces the fastest run time within the required accuracy by a
considerable margin, positioning it favourably for use in Bayesian parameter
inference. This method, however, requires further development and testing to
extend its use to certain analysis scenarios, particularly those involving a
scale-dependent growth rate. For this and other reasons discussed herein,
alternative approaches such as ${\tt matter}$ and ${\tt Levin}$ may be
necessary for a full exploration of parameter space. We also find that the
usual first-order Limber approximation is insufficiently accurate for LSST Year
10 3x2pt analysis on $\ell=200-1000$, whereas invoking the second-order Limber
approximation on these scales (with a full non-Limber method at smaller $\ell$)
does suffice.

---
[arxiv link](http://arxiv.org/abs/2212.04291v1)

[pdf link](http://arxiv.org/pdf/2212.04291v1)