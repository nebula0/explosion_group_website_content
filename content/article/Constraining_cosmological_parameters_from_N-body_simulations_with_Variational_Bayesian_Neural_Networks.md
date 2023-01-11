---
title: "Constraining cosmological parameters from N-body simulations with Variational Bayesian Neural Networks"
date: "2023-01-09"
type: article
tags:
  - "arxiv"
  - "most recent update (Wed Jan 11 2023)"
categories:
  - cosmology
  - 2023(year)
  - 1(month)
draft: false
---

> First author: Héctor J. Hortúa

 Methods based on Deep Learning have recently been applied on astrophysical
parameter recovery thanks to their ability to capture information from complex
data. One of these methods is the approximate Bayesian Neural Networks (BNNs)
which have demonstrated to yield consistent posterior distribution into the
parameter space, helpful for uncertainty quantification. However, as any modern
neural networks, they tend to produce overly confident uncertainty estimates
and can introduce bias when BNNs are applied to data. In this work, we
implement multiplicative normalizing flows (MNFs), a family of approximate
posteriors for the parameters of BNNs with the purpose of enhancing the
flexibility of the variational posterior distribution, to extract $\Omega_m$,
$h$, and $\sigma_8$ from the QUIJOTE simulations. We have compared this method
with respect to the standard BNNs, and the flipout estimator. We found that
MNFs combined with BNNs outperform the other models obtaining predictive
performance with almost one order of magnitude larger that standard BNNs,
$\sigma_8$ extracted with high accuracy ($r^2=0.99$), and precise uncertainty
estimates. The latter implies that MNFs provide more realistic predictive
distribution closer to the true posterior mitigating the bias introduced by the
variational approximation and allowing to work with well-calibrated networks.

---
[arxiv link](http://arxiv.org/abs/2301.03991v1)

[pdf link](http://arxiv.org/pdf/2301.03991v1)