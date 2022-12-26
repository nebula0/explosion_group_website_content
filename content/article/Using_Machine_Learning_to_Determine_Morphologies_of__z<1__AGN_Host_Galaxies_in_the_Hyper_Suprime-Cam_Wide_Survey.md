---
title: "Using Machine Learning to Determine Morphologies of $z<1$ AGN Host Galaxies in the Hyper Suprime-Cam Wide Survey"
date: "2022-12-20"
type: article
tags:
  - "arxiv"
  - "most recent update (Tue Dec 27 2022)"
categories:
  - galaxies
  - 2022(year)
  - 12(month)
draft: false
---

> First author: Chuan Tian

 We present a machine-learning framework to accurately characterize
morphologies of Active Galactic Nucleus (AGN) host galaxies within $z<1$. We
first use PSFGAN to decouple host galaxy light from the central point source,
then we invoke the Galaxy Morphology Network (GaMorNet) to estimate whether the
host galaxy is disk-dominated, bulge-dominated, or indeterminate. Using optical
images from five bands of the HSC Wide Survey, we build models independently in
three redshift bins: low $(0<z<0.25)$, medium $(0.25<z<0.5)$, and high
$(0.5<z<1.0)$. By first training on a large number of simulated galaxies, then
fine-tuning using far fewer classified real galaxies, our framework predicts
the actual morphology for $\sim$ $60\%-70\%$ host galaxies from test sets, with
a classification precision of $\sim$ $80\%-95\%$, depending on redshift bin.
Specifically, our models achieve disk precision of $96\%/82\%/79\%$ and bulge
precision of $90\%/90\%/80\%$ (for the 3 redshift bins), at thresholds
corresponding to indeterminate fractions of $30\%/43\%/42\%$. The
classification precision of our models has a noticeable dependency on host
galaxy radius and magnitude. No strong dependency is observed on contrast
ratio. Comparing classifications of real AGNs, our models agree well with
traditional 2D fitting with GALFIT. The PSFGAN+GaMorNet framework does not
depend on the choice of fitting functions or galaxy-related input parameters,
runs orders of magnitude faster than GALFIT, and is easily generalizable via
transfer learning, making it an ideal tool for studying AGN host galaxy
morphology in forthcoming large imaging survey.

---
[arxiv link](http://arxiv.org/abs/2212.09984v1)

[pdf link](http://arxiv.org/pdf/2212.09984v1)