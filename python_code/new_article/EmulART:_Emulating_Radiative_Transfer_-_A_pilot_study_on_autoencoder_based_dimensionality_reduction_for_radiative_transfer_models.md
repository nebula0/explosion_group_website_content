---
title: "EmulART: Emulating Radiative Transfer - A pilot study on autoencoder based dimensionality reduction for radiative transfer models"
date: "2022-10-27"
type: article
tags:
  - "arxiv"
  - "most recent update (Sat Oct 29 2022)"
categories:
  - high redshift
  - 2022(year)
  - 10(month)
draft: false
---

> First author: João Rino-Silvestre

 Dust is a major component of the interstellar medium. Through scattering,
absorption and thermal re-emission, it can profoundly alter astrophysical
observations. Models for dust composition and distribution are necessary to
better understand and curb their impact on observations. A new approach for
serial and computationally inexpensive production of such models is here
presented. Traditionally these models are studied with the help of radiative
transfer modelling, a critical tool to understand the impact of dust
attenuation and reddening on the observed properties of galaxies and active
galactic nuclei. Such simulations present, however, an approximately linear
computational cost increase with the desired information resolution. Our new
efficient model generator proposes a denoising variational autoencoder (or
alternatively PCA), for spectral compression, combined with an approximate
Bayesian method for spatial inference, to emulate high information radiative
transfer models from low information models. For a simple spherical dust shell
model with anisotropic illumination, our proposed approach successfully
emulates the reference simulation starting from less than 1% of the
information. Our emulations of the model at different viewing angles present
median residuals below 15% across the spectral dimension, and below 48% across
spatial and spectral dimensions. EmulART infers estimates for ~85% of
information missing from the input, all within a total running time of around
20 minutes, estimated to be 6x faster than the present target high information
resolution simulations, and up to 50x faster when applied to more complicated
simulations.

---
[arxiv link](http://arxiv.org/abs/2210.15400v1)

[pdf link](http://arxiv.org/pdf/2210.15400v1)