---
title: "Enabling the discovery of fast transients: A kilonova science module for the Fink broker"
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

> First author: B. Biswas

 We describe the fast transient classification algorithm in the center of the
kilonova (KN) science module currently implemented in the Fink broker and
report classification results based on simulated catalogs and real data from
the ZTF alert stream. We used noiseless, homogeneously sampled simulations to
construct a basis of principal components (PCs). All light curves from a more
realistic ZTF simulation were written as a linear combination of this basis.
The corresponding coefficients were used as features in training a random
forest classifier. The same method was applied to long (>30 days) and medium
(<30 days) light curves. The latter aimed to simulate the data situation found
within the ZTF alert stream. Classification based on long light curves achieved
73.87% precision and 82.19% recall. Medium baseline analysis resulted in 69.30%
precision and 69.74% recall, thus confirming the robustness of precision
results when limited to 30 days of observations. In both cases, dwarf flares
and point Type Ia supernovae were the most frequent contaminants. The final
trained model was integrated into the Fink broker and has been distributing
fast transients, tagged as \texttt{KN\_candidates}, to the astronomical
community, especially through the GRANDMA collaboration. We showed that
features specifically designed to grasp different light curve behaviors provide
enough information to separate fast (KN-like) from slow (non-KN-like) evolving
events. This module represents one crucial link in an intricate chain of
infrastructure elements for multi-messenger astronomy which is currently being
put in place by the Fink broker team in preparation for the arrival of data
from the Vera Rubin Observatory Legacy Survey of Space and Time.

---
[arxiv link](http://arxiv.org/abs/2210.17433v1)

[pdf link](http://arxiv.org/pdf/2210.17433v1)