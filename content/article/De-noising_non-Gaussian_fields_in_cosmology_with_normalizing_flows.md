---
title: "De-noising non-Gaussian fields in cosmology with normalizing flows"
date: "2022-11-28"
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

> First author: Adam Rouhiainen

 Fields in cosmology, such as the matter distribution, are observed by
experiments up to experimental noise. The first step in cosmological data
analysis is usually to de-noise the observed field using an analytic or
simulation driven prior. On large enough scales, such fields are Gaussian, and
the de-noising step is known as Wiener filtering. However, on smaller scales
probed by upcoming experiments, a Gaussian prior is substantially sub-optimal
because the true field distribution is very non-Gaussian. Using normalizing
flows, it is possible to learn the non-Gaussian prior from simulations (or from
more high-resolution observations), and use this knowledge to de-noise the data
more effectively. We show that we can train a flow to represent the matter
distribution of the universe, and evaluate how much signal-to-noise can be
gained as a function of the experimental noise under idealized conditions. We
also introduce a patching method to reconstruct fields on arbitrarily large
images by dividing them up into small maps (where we reconstruct non-Gaussian
features), and patching the small posterior maps together on large scales
(where the field is Gaussian).

---
[arxiv link](http://arxiv.org/abs/2211.15161v1)

[pdf link](http://arxiv.org/pdf/2211.15161v1)