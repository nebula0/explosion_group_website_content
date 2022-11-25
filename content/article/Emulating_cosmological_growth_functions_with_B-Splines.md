---
title: "Emulating cosmological growth functions with B-Splines"
date: "2022-11-12"
type: article
tags:
  - "arxiv"
  - ""
categories:
  - cosmology
  - 2022(year)
  - 11(month)
draft: false
---

> First author: Ngai Pok Kwan

 In the light of GPU accelerations, sequential operations such as solving
ordinary differential equations can be bottlenecks for gradient evaluations and
hinder potential speed gains. In this work, we focus on growth functions and
their time derivatives in cosmological particle mesh simulations and show that
these are the majority time cost when using gradient based inference
algorithms. We propose to construct novel conditional B-spline emulators which
directly learn an interpolating function for the growth factor as a function of
time, conditioned on the cosmology. We demonstrate that these emulators are
sufficiently accurate to not bias our results for cosmological inference and
can lead to over an order of magnitude gains in time, especially for small to
intermediate size simulations.

---
[arxiv link](http://arxiv.org/abs/2211.06564v1)

[pdf link](http://arxiv.org/pdf/2211.06564v1)