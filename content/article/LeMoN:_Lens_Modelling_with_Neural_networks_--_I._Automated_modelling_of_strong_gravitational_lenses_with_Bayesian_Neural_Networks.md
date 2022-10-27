---
title: "LeMoN: Lens Modelling with Neural networks -- I. Automated modelling of strong gravitational lenses with Bayesian Neural Networks"
date: "2022-10-19"
type: article
tags:
  - "arxiv"
  
categories:
  - dwarf galaxy
  - 2022(year)
  - 10(month)
draft: false
---
> First author: Fabrizio Gentile

 The unprecedented number of gravitational lenses expected from new-generation
facilities such as the ESA Euclid telescope and the Vera Rubin Observatory
makes it crucial to rethink our classical approach to lens-modelling. In this
paper, we present LeMoN (Lens Modelling with Neural networks): a new
machine-learning algorithm able to analyse hundreds of thousands of
gravitational lenses in a reasonable amount of time. The algorithm is based on
a Bayesian Neural Network: a new generation of neural networks able to
associate a reliable confidence interval to each predicted parameter. We train
the algorithm to predict the three main parameters of the Singular Isothermal
Ellipsoid model (the Einstein radius and the two components of the ellipticity)
by employing two simulated datasets built to resemble the imaging capabilities
of the Hubble Space Telescope and the forthcoming Euclid satellite. In this
work, we assess the accuracy of the algorithm and the reliability of the
estimated uncertainties by applying the network to several simulated datasets
of 10.000 images each. We obtain accuracies comparable to previous studies
present in the current literature and an average modelling time of just 0.5s
per lens. Finally, we apply the LeMoN algorithm to a pilot dataset of real
lenses observed with HST during the SLACS program, obtaining unbiased estimates
of their SIE parameters. The code is publicly available on GitHub
(https://github.com/fab-gentile/LeMoN).

---
[arxiv link](http://arxiv.org/abs/2210.10793v1)

[pdf link](http://arxiv.org/pdf/2210.10793v1)