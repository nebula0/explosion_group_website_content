---
title: "Morphological Parameters and Associated Uncertainties for 8 Million Galaxies in the Hyper Suprime-Cam Wide Survey"
date: "2022-11-30"
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

> First author: Aritra Ghosh

 We use the Galaxy Morphology Posterior Estimation Network (GaMPEN) to
estimate morphological parameters and associated uncertainties for $\sim 8$
million galaxies in the Hyper Suprime-Cam (HSC) Wide survey with $z \leq 0.75$
and $m \leq 23$. GaMPEN is a machine learning framework that estimates Bayesian
posteriors for a galaxy's bulge-to-total light ratio ($L_B/L_T$), effective
radius ($R_e$), and flux ($F$). By first training on simulations of galaxies
and then applying transfer learning using real data, we trained GaMPEN with
$<1\%$ of our dataset. This two-step process will be critical for applying
machine learning algorithms to future large imaging surveys, such as the
Rubin-Legacy Survey of Space and Time (LSST), the Nancy Grace Roman Space
Telescope (NGRST), and Euclid. By comparing our results to those obtained using
light-profile fitting, we demonstrate that GaMPEN's predicted posterior
distributions are well-calibrated ($\lesssim 5\%$ deviation) and accurate. This
represents a significant improvement over light profile fitting algorithms
which underestimate uncertainties by as much as $\sim60\%$. For an overlapping
sub-sample, we also compare the derived morphological parameters with values in
two external catalogs and find that the results agree within the limits of
uncertainties predicted by GaMPEN. This step also permits us to define an
empirical relationship between the S\'ersic index and $L_B/L_T$ that can be
used to convert between these two parameters. The catalog presented here
represents a significant improvement in size ($\sim10 \times $), depth ($\sim4$
magnitudes), and uncertainty quantification over previous state-of-the-art
bulge+disk decomposition catalogs. With this work, we also release GaMPEN's
source code and trained models, which can be adapted to other datasets.

---
[arxiv link](http://arxiv.org/abs/2212.00051v1)

[pdf link](http://arxiv.org/pdf/2212.00051v1)