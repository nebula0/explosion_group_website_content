---
title: "Data-driven photometric redshift estimation from type Ia supernovae light curves"
date: "2022-12-30"
type: article
tags:
  - "arxiv"
  - ""
categories:
  - supernovae
  - 2022(year)
  - 12(month)
draft: false
---

> First author: Felipe M F de Oliveira

 Redshift measurement has always been a constant need in modern astronomy and
cosmology. And as new surveys have been providing an immense amount of data on
astronomical objects, the need to process such data automatically proves to be
increasingly necessary. In this article, we use simulated data from the Dark
Energy Survey, and from a pipeline originally created to classify supernovae,
we developed a linear regression algorithm optimized through novel automated
machine learning (AutoML) frameworks achieving an error score better than
ordinary data pre-processing methods when compared with other modern algorithms
(such as XGBOOST). Numerically, the photometric prediction RMSE of type Ia
supernovae events was reduced from 0.16 to 0.09 and the RMSE of all supernovae
types decreased from 0.20 to 0.14. Our pipeline consists of four steps: through
spectroscopic data points we interpolate the light curve using Gaussian process
fitting algorithm, then using a wavelet transform we extract the most important
features of such curves; in sequence we reduce the dimensionality of such
features through principal component analysis, and in the end we applied super
learning techniques (stacked ensemble methods) through an AutoML framework
dedicated to optimize the parameters of several different machine learning
models, better resolving the problem. As a final check, we obtained probability
distribution functions (PDFs) using Gaussian kernel density estimations through
the predictions of more than 50 models trained and optimized by AutoML. Those
PDFs were calculated to replicate the original curves that used SALT2 model, a
model used for the simulation of the raw data itself.

---
[arxiv link](http://arxiv.org/abs/2212.14668v1)

[pdf link](http://arxiv.org/pdf/2212.14668v1)