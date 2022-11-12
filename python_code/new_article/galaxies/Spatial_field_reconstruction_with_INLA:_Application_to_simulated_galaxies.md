---
title: "Spatial field reconstruction with INLA: Application to simulated galaxies"
date: "2022-11-4"
type: article
tags:
  - "arxiv"
  - "most recent update (Sat Nov 12 2022)"
categories:
  - galaxies
  - 2022(year)
  - 11(month)
draft: false
---

> First author: Majda Smole

 Aims. Monte Carlo Radiative Transfer (MCRT) simulations are a powerful tool
for understanding the role of dust in astrophysical systems and its influence
on observations. However, due to the strong coupling of the radiation field and
medium across the whole computational domain, the problem is non-local and
non-linear and such simulations are computationally expensive in case of
realistic 3D inhomogeneous dust distributions. We explore a novel technique for
post-processing MCRT output to reduce the total computational run time by
enhancing the output of computationally less expensive simulations of
lower-quality.
  Methods. We combine principal component analysis (PCA) and non-negative
matrix factorization (NMF) as dimensionality reduction techniques together with
Gaussian Markov random fields and the Integrated nested Laplace approximation
(INLA), an approximate method for Bayesian inference, to detect and reconstruct
the non-random spatial structure in the images of lower signal-to-noise or with
missing data.
  Results. We test our methodology using synthetic observations of a galaxy
from the SKIRT Auriga project - a suite of high resolution magneto-hydrodynamic
Milky Way-sized galaxies simulated in cosmological environment by 'zoom-in'
technique. With this approach, we are able to reproduce high photon number
reference images $\sim5$ times faster with median residuals below $\sim20\%$.

---
[arxiv link](http://arxiv.org/abs/2211.02602v1)

[pdf link](http://arxiv.org/pdf/2211.02602v1)