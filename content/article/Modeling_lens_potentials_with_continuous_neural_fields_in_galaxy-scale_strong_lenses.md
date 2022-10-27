---
title: "Modeling lens potentials with continuous neural fields in galaxy-scale strong lenses"
date: "2022-10-17"
type: article
tags:
  - "arxiv"
  
categories:
  - blackhole physics
  - 2022(year)
  - 10(month)
draft: false
---
> First author: Luca Biggio

 Strong gravitational lensing is a unique observational tool for studying the
dark and luminous mass distribution both within and between galaxies. Given the
presence of substructures, current strong lensing observations demand more
complex mass models than smooth analytical profiles, such as power-law
ellipsoids. In this work, we introduce a continuous neural field to predict the
lensing potential at any position throughout the image plane, allowing for a
nearly model-independent description of the lensing mass. We apply our method
on simulated Hubble Space Telescope imaging data containing different types of
perturbations to a smooth mass distribution: a localized dark subhalo, a
population of subhalos, and an external shear perturbation. Assuming knowledge
of the source surface brightness, we use the continuous neural field to model
either the perturbations alone or the full lensing potential. In both cases,
the resulting model is able to fit the imaging data, and we are able to
accurately recover the properties of both the smooth potential and of the
perturbations. Unlike many other deep learning methods, ours explicitly retains
lensing physics (i.e., the lens equation) and introduces high flexibility in
the model only where required, namely, in the lens potential. Moreover, the
neural network does not require pre-training on large sets of labelled data and
predicts the potential from the single observed lensing image. Our model is
implemented in the fully differentiable lens modeling code Herculens.

---
[arxiv link](http://arxiv.org/abs/2210.09169v1)

[pdf link](http://arxiv.org/pdf/2210.09169v1)