---
title: "Autoencoding Galaxy Spectra I: Architecture"
date: "2022-11-15"
type: article
tags:
  - "arxiv"
  - "most recent update (Sat Nov 19 2022)"
categories:
  - galaxies
  - 2022(year)
  - 11(month)
draft: false
---

> First author: Peter Melchior

 We introduce the neural network architecture SPENDER as a core differentiable
building block for analyzing, representing, and creating galaxy spectra. It
combines a convolutional encoder, which pays attention to up to 256 spectral
features and compresses them into a low-dimensional latent space, with a
decoder that generates a restframe representation, whose spectral range and
resolution exceeds that of the observing instrument. The decoder is followed by
explicit redshift, resampling, and convolution transformations to match the
observations. The architecture takes galaxy spectra at arbitrary redshifts and
is robust to glitches like residuals of the skyline subtraction, so that
spectra from a large survey can be ingested directly without additional
preprocessing. We demonstrate the performance of SPENDER by training on the
entire spectroscopic galaxy sample of SDSS-II; show its ability to create
highly accurate reconstructions with substantially reduced noise; perform
deconvolution and oversampling for a super-resolution model that resolves the
[OII] doublet; introduce a novel method to interpret attention weights as
proxies for important spectral features; and infer the main degrees of freedom
represented in the latent space. We conclude with a discussion of future
improvements and applications.

---
[arxiv link](http://arxiv.org/abs/2211.07890v1)

[pdf link](http://arxiv.org/pdf/2211.07890v1)