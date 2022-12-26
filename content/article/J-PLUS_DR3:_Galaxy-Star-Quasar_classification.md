---
title: "J-PLUS DR3: Galaxy-Star-Quasar classification"
date: "2022-12-12"
type: article
tags:
  - "arxiv"
  - ""
categories:
  - galaxies
  - 2022(year)
  - 12(month)
draft: false
---

> First author: R. von Marttens

 The Javalambre Photometric Local Universe Survey (J-PLUS) is a 12-band
photometric survey using the 83-cm JAST telescope. Data Release 3 includes 47.4
million sources (29.8 million with $r \le 21$) on 3192 deg$^2$ (2881 deg$^2$
after masking). J-PLUS DR3 only provides star-galaxy classification so that
quasars are not identified from the other sources. Given the size of the
dataset, machine learning methods could provide a valid alternative
classification and a solution to the classification of quasars. Our objective
is to classify J-PLUS DR3 sources into galaxies, stars and quasars,
outperforming the available classifiers in each class. We use an automated
machine learning tool called {\tt TPOT} to find an optimized pipeline to
perform the classification. The supervised machine learning algorithms are
trained on the crossmatch with SDSS DR12, LAMOST DR7 and \textit{Gaia} DR3. We
checked that the training set of about 570 thousand galaxies, one million stars
and 220 thousand quasars is both representative and pure to a good degree. We
considered 37 features: besides the twelve photometric bands with their errors,
six colors, four morphological parameters, galactic extinction with its error
and the PSF relative to the corresponding pointing. After exploring numerous
pipeline possibilities through the TPOT genetic algorithm, we found that
XGBoost provides the best performance: the AUC for galaxies, stars and quasars
is above 0.99 and the average precision is above 0.99 for galaxies and stars
and 0.94 for quasars. XGBoost outperforms the star-galaxy classifiers already
provided in J-PLUS DR3 and also efficiently classifies quasars. We also found
that photometry was very important in the classification of quasars, showing
the relevance of narrow-band photometry.

---
[arxiv link](http://arxiv.org/abs/2212.05868v1)

[pdf link](http://arxiv.org/pdf/2212.05868v1)