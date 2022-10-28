---
title: "Characterization Of Inpaint Residuals In Interferometric Measurements of the Epoch Of Reionization"
date: "2022-10-26"
type: article
tags:
  - "arxiv"
  - "most recent update (Sat Oct 29 2022)"
categories:
  - high redshift
  - 2022(year)
  - 10(month)
draft: false
---

> First author: Michael Pagano

 Radio Frequency Interference (RFI) is one of the systematic challenges
preventing 21cm interferometric instruments from detecting the Epoch of
Reionization. To mitigate the effects of RFI on data analysis pipelines,
numerous inpaint techniques have been developed to restore RFI corrupted data.
We examine the qualitative and quantitative errors introduced into the
visibilities and power spectrum due to inpainting. We perform our analysis on
simulated data as well as real data from the Hydrogen Epoch of Reionization
Array (HERA) Phase 1 upper limits. We also introduce a convolutional neural
network that capable of inpainting RFI corrupted data in interferometric
instruments. We train our network on simulated data and show that our network
is capable at inpainting real data without requiring to be retrained. We find
that techniques that incorporate high wavenumbers in delay space in their
modeling are best suited for inpainting over narrowband RFI. We also show that
with our fiducial parameters Discrete Prolate Spheroidal Sequences (DPSS) and
CLEAN provide the best performance for intermittent ``narrowband'' RFI while
Gaussian Progress Regression (GPR) and Least Squares Spectral Analysis (LSSA)
provide the best performance for larger RFI gaps. However we caution that these
qualitative conclusions are sensitive to the chosen hyperparameters of each
inpainting technique. We find these results to be consistent in both simulated
and real visibilities. We show that all inpainting techniques reliably
reproduce foreground dominated modes in the power spectrum. Since the
inpainting techniques should not be capable of reproducing noise realizations,
we find that the largest errors occur in the noise dominated delay modes. We
show that in the future, as the noise level of the data comes down, CLEAN and
DPSS are most capable of reproducing the fine frequency structure in the
visibilities of HERA data.

---
[arxiv link](http://arxiv.org/abs/2210.14927v1)

[pdf link](http://arxiv.org/pdf/2210.14927v1)