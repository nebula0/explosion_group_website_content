---
title: "DIGS: Deep Inference of Galaxy Spectra with Neural Posterior Estimation"
date: "2022-11-16"
type: article
tags:
  - "arxiv"
  - ""
categories:
  - galaxies
  - 2022(year)
  - 11(month)
draft: false
---

> First author: Gourav Khullar

 With the advent of billion-galaxy surveys with complex data, the need of the
hour is to efficiently model galaxy spectral energy distributions (SEDs) with
robust uncertainty quantification. The combination of Simulation-Based
inference (SBI) and amortized Neural Posterior Estimation (NPE) has been
successfully used to analyse simulated and real galaxy photometry both
precisely and efficiently. In this work, we utilise this combination and build
on existing literature to analyse simulated noisy galaxy spectra. Here, we
demonstrate a proof-of-concept study of spectra that is a) an efficient
analysis of galaxy SEDs and inference of galaxy parameters with physically
interpretable uncertainties; and b) amortized calculations of posterior
distributions of said galaxy parameters at the modest cost of a few galaxy fits
with MCMC methods. We utilise the SED generator and inference framework
Prospector to generate simulated spectra, and train a dataset of
2$\times$10$^6$ spectra (corresponding to a 5-parameter SED model) with NPE. We
show that SBI -- with its combination of fast and amortized posterior
estimations -- is capable of inferring accurate galaxy stellar masses and
metallicities. Our uncertainty constraints are comparable to or moderately
weaker than traditional inverse-modeling with Bayesian MCMC methods (e.g., 0.17
and 0.26 dex in stellar mass and metallicity for a given galaxy, respectively).
We also find that our inference framework conducts rapid SED inference
(0.9-1.2$\times$10$^5$ galaxy spectra via SBI/SNPE at the cost of 1 MCMC-based
fit). With this work, we set the stage for further work that focuses of SED
fitting of galaxy spectra with SBI, in the era of JWST galaxy survey programs
and the wide-field Roman Space Telescope spectroscopic surveys.

---
[arxiv link](http://arxiv.org/abs/2211.09126v1)

[pdf link](http://arxiv.org/pdf/2211.09126v1)