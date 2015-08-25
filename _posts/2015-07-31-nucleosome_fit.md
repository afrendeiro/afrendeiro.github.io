---
layout: post
title: "ATAC-seq library nucleosome fitting"
description: "ATAC-seq library nucleosome fitting"
category: research
tags: [atac-seq, python]
---
{% include JB/setup %}


[This great iPython notebook](https://github.com/dbrg77/ATAC/blob/master/ATAC_seq_read_length_curve_fitting.ipynb) on ATAC-seq nucleosome fitting gave me exactly what I needed for ATAC-seq data analysis.

I've added a few more simple features, adapter the fitting parameters to data produced in our lab and created a single function with it, which I will call during ATAC-seq pipeline runs.

Some metrics will be valuable to assess sample quality as well.

{%gist c37c112a6b4e58eb75b0 %}
