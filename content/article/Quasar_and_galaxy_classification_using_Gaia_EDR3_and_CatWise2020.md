---
title: "Quasar and galaxy classification using Gaia EDR3 and CatWise2020"
date: "2022-10-11"
type: article
tags:
  - "arxiv"
categories:
  - dwarf galaxy
  - 2022(year)
  - 10(month)
draft: false
---
> First author: Arvind C. N. Hughes

 In this work, we assess the combined use of Gaia photometry and astrometry
with infrared data from CatWISE in improving the identification of
extragalactic sources compared to the classification obtained using Gaia data.
We evaluate different input feature configurations and prior functions, with
the aim of presenting a classification methodology integrating prior knowledge
stemming from realistic class distributions in the universe. In our work, we
compare different classifiers, namely Gaussian Mixture Models (GMMs), XGBoost
and CatBoost, and classify sources into three classes - star, quasar, and
galaxy, with the target quasar and galaxy class labels obtained from SDSS16 and
the star label from Gaia EDR3. In our approach, we adjust the posterior
probabilities to reflect the intrinsic distribution of extragalactic sources in
the universe via a prior function. We introduce two priors, a global prior
reflecting the overall rarity of quasars and galaxies, and a mixed prior that
incorporates in addition the distribution of the these sources as a function of
Galactic latitude and magnitude. Our best classification performances, in terms
of completeness and purity of the galaxy and quasar classes, are achieved using
the mixed prior for sources at high latitudes and in the magnitude range G =
18.5 to 19.5. We apply our identified best-performing classifier to three
application datasets from Gaia DR3, and find that the global prior is more
conservative in what it considers to be a quasar or a galaxy compared to the
mixed prior. In particular, when applied to the pure quasar and galaxy
candidates samples, we attain a purity of 97% for quasars and 99.9% for
galaxies using the global prior, and purities of 96% and 99% respectively using
the mixed prior. We conclude our work by discussing the importance of applying
adjusted priors portraying realistic class distributions in the universe.

---
[arxiv link](http://arxiv.org/abs/2210.05505v1)

[pdf link](http://arxiv.org/pdf/2210.05505v1)