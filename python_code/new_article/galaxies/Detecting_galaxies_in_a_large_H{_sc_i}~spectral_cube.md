---
title: "Detecting galaxies in a large H{\\sc i}~spectral cube"
date: "2022-11-3"
type: article
tags:
  - "arxiv"
  - "most recent update (Sat Nov 12 2022)"
categories:
  - galaxies
  - 2022(year)
  - 11(month)
draft: false
---

> First author: Abinash Kumar Shaw

 The upcoming Square Kilometer Array (SKA) is expected to produce humongous
amount of data for undertaking H{\sc i}~science. We have developed an MPI-based
{\sc Python} pipeline to deal with the large data efficiently with the present
computational resources. Our pipeline divides such large H{\sc i}~21-cm
spectral cubes into several small cubelets, and then processes them in parallel
using publicly available H{\sc i}~source finder {\sc SoFiA-$2$}. The pipeline
also takes care of sources at the boundaries of the cubelets and also filters
out false and redundant detections. By comapring with the true source catalog,
we find that the detection efficiency depends on the {\sc SoFiA-$2$} parameters
such as the smoothing kernel size, linking length and threshold values. We find
the optimal kernel size for all flux bins to be between $3$ to $5$ pixels and
$7$ to $15$ pixels, respectively in the spatial and frequency directions.
Comparing the recovered source parameters with the original values, we find
that the output of {\sc SoFiA-$2$} is highly dependent on kernel sizes and a
single choice of kernel is not sufficient for all types of H{\sc i}~galaxies.
We also propose use of alternative methods to {\sc SoFiA-$2$} which can be used
in our pipeline to find sources more robustly.

---
[arxiv link](http://arxiv.org/abs/2211.02041v1)

[pdf link](http://arxiv.org/pdf/2211.02041v1)