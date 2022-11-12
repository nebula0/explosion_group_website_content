---
title: "Optimizing machine learning methods to discover strong gravitational lenses in the Deep Lens Survey"
date: "2022-10-31"
type: article
tags:
  - "arxiv"
  - ""
categories:
  - cluster simulation
  - 2022(year)
  - 10(month)
draft: false
---

> First author: Keerthi Vasan G. C.

 Machine learning (ML) models can greatly improve the search for strong
gravitational lenses in imaging surveys by reducing the amount of human
inspection required. In this work, we test the performance of supervised,
semi-supervised, and unsupervised learning algorithms trained with the ResNetV2
neural network architecture on their ability to efficiently find strong
gravitational lenses in the Deep Lens Survey (DLS). We use galaxy images from
the survey, combined with simulated lensed sources, as labeled data in our
training datasets. We find that models using semi-supervised learning along
with data augmentations (transformations applied to an image during training,
e.g., rotation) and Generative Adversarial Network (GAN) generated images yield
the best performance. They offer 5--10 times better precision across all recall
values compared to supervised algorithms. Applying the best performing models
to the full 20 deg$^2$ DLS survey, we find 3 Grade-A lens candidates within the
top 17 image predictions from the model. This increases to 9 Grade-A and 13
Grade-B candidates when $1$\% ($\sim2500$ images) of the model predictions are
visually inspected. This is $\gtrsim10\times$ the sky density of lens
candidates compared to current shallower wide-area surveys (such as the Dark
Energy Survey), indicating a trove of lenses awaiting discovery in upcoming
deeper all-sky surveys. These results suggest that pipelines tasked with
finding strong lens systems can be highly efficient, minimizing human effort.
We additionally report spectroscopic confirmation of the lensing nature of two
Grade-A candidates identified by our model, further validating our methods.

---
[arxiv link](http://arxiv.org/abs/2211.00047v1)

[pdf link](http://arxiv.org/pdf/2211.00047v1)