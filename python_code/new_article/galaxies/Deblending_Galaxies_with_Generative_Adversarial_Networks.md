---
title: "Deblending Galaxies with Generative Adversarial Networks"
date: "2022-11-8"
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

> First author: Shoubaneh Hemmati

 Deep generative models including generative adversarial networks (GANs) are
powerful unsupervised tools in learning the distributions of data sets.
Building a simple GAN architecture in PyTorch and training on the CANDELS data
set, we generate galaxy images with the Hubble Space Telescope resolution
starting from a noise vector. We proceed by modifying the GAN architecture to
improve the Subaru Hyper Suprime-Cam ground-based images by increasing their
resolution to the HST resolution. We use the super resolution GAN on a large
sample of blended galaxies which we create using CANDELS cutouts. In our
simulated blend sample, $\sim 20 \%$ would unrecognizably be blended even in
the HST resolution cutouts. In the HSC-like cutouts this fraction rises to
$\sim 90\%$. With our modified GAN we can lower this value to $\sim 50\%$. We
quantify the blending fraction in the high, low and GAN resolutions over the
whole manifold of angular separation, flux ratios, sizes and redshift
difference between the two blended objects. The two peaks found by the GAN
deblender result in ten times improvement in the photometry measurement of the
blended objects. Modifying the architecture of the GAN, we also train a
Multi-wavelength GAN with seven band optical+NIR HST cutouts. This
multi-wavelength GAN improves the fraction of detected blends by another $\sim
10\%$ compared to the single-band GAN. This is most beneficial to the current
and future precision cosmology experiments (e.g., LSST, SPHEREx, Euclid,
Roman), specifically those relying on weak gravitational lensing, where
blending is a major source of systematic error.

---
[arxiv link](http://arxiv.org/abs/2211.04488v1)

[pdf link](http://arxiv.org/pdf/2211.04488v1)