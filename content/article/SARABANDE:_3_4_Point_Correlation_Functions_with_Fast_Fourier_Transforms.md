---
title: "SARABANDE: 3/4 Point Correlation Functions with Fast Fourier Transforms"
date: "2022-10-18"
type: article
tags:
  - "arxiv"
  
categories:
  - intergalactic medium
  - 2022(year)
  - 10(month)
draft: false
---
> First author: James Sunseri

 We present a new $\texttt{python}$ package SARABANDE for measuring 3 & 4
Point Correlation Functions (3/4 PCFs) in $\mathcal{O}(N_{\rm g} \log N_{\rm
g})$ time using Fast Fourier Transforms (FFTs), with $N_{\rm g}$ the number of
grid points used for the FFT. SARABANDE can measure both projected and full 3
and 4 PCFs on gridded 2D and 3D datasets. The general technique is to generate
suitable angular basis functions on an underlying grid, radially bin these to
create kernels, and convolve these kernels with the original gridded data to
obtain expansion coefficients about every point simultaneously. These
coefficients are then combined to give us the 3/4 PCF as expanded in our basis.
We apply SARABANDE to simulations of the Interstellar Medium (ISM) to show the
results and scaling of calculating both the full and projected 3/4 PCFs.

---
[arxiv link](http://arxiv.org/abs/2210.10206v1)

[pdf link](http://arxiv.org/pdf/2210.10206v1)