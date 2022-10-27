---
title: "Identifying Tidal Disruption Events with an Expansion of the FLEET Machine Learning Algorithm"
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
> First author: Sebastian Gomez

 We present an expansion of FLEET, a machine learning algorithm optimized to
select transients that are most likely to be tidal disruption events (TDEs).
FLEET is based on a random forest algorithm trained on the light curves and
host galaxy information of 4,779 spectroscopically classified transients. For
transients with a probability of being a TDE, \ptde$>0.5$, we can successfully
recover TDEs with a $\approx40$\% completeness and a $\approx30$\% purity when
using the first 20 days of photometry, or a similar completeness and
$\approx50$\% purity when including 40 days of photometry. We find that the
most relevant features for differentiating TDEs from other transients are the
normalized host separation, and the light curve $(g-r)$ color during peak.
Additionally, we use FLEET to produce a list of the 39 most likely TDE
candidates discovered by the Zwicky Transient Facility that remain currently
unclassified. We explore the use of FLEET for the Legacy Survey of Space and
Time on the Vera C. Rubin Observatory (\textit{Rubin}) and the \textit{Nancy
Grace Roman Space Telescope} (\textit{Roman}). We simulate the \textit{Rubin}
and \textit{Roman} survey strategies and estimate that $\sim 10^4$ TDEs could
be discovered every year by \textit{Rubin}, and $\sim200$ TDEs per year by
\textit{Roman}. Finally, we run FLEET on the TDEs in our \textit{Rubin} survey
simulation and find that we can recover $\sim 30$\% of those at a redshift $z
<0.5$ with \ptde$>0.5$. This translates to $\sim3,000$ TDEs per year that FLEET
could uncover from \textit{Rubin}. FLEET is provided as a open source package
on GitHub https://github.com/gmzsebastian/FLEET

---
[arxiv link](http://arxiv.org/abs/2210.10810v1)

[pdf link](http://arxiv.org/pdf/2210.10810v1)