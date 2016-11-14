---
layout: post
title: "Quantile tracks"
description: "Quantile tracks"
category: research
tags: [visualization, python, bash]
---
{% include JB/setup %}


The code we shared on our latest work (see [doi:10.1038/ncomms11938](http://dx.doi.org/10.1038/ncomms11938)) contained all parts necessary to reproduce the figures in the paper, but there was one part that I didn't share. In [Figure 2](http://www.nature.com/articles/ncomms11938/figures/2), you can see percentiles of normalized ATAC-seq signal for the 88 samples used in the study - the code in question produces bigWig files used in this visualization.

The reason why I haven't shared it was because it was a bit challenging and I didn't manage to make it as system-independent as I'd want. Most of the code for the paper is in Python, but for this I used a combination of Python, Bash and GNU programs to handle the amount of signal genome-wide. In addition, I've made extensive use of a HPC cluster with slurm as manager to speed things up.

Since I have now been asked by two persons to share the code, I do it now here.

<br>

This is a brief explanation of the steps:

 - The entry point is "quantile_tracks.py". This is meant to produce two files containing information of the BAM file paths and sizes.

 - The next script is "quantile_tracks.sh", which does the real work. It:
    1. makes windows across the genome (here I chose to have 1bp windows, which was a bit overkill) for each chromosome;

    1. computes the read coverage in each of these windows for each chromosome, for each bam file;

    1. paste together the covereage of all samples per chromosome;

    1. split these in chunks;

    1. compute quantiles across samples for each chunk (uses the `quantilize.py` script);

    1. concatenate back the quantiles of the chunks and,

    1. make a bigWig file for each quantile. Pretty much in each step, a swarm of jobs is launched to the cluster, so if you have a different HPC configuration (which is more than certain) you'll have to adapt that.

If it sounds complicated and unoptimized, it's because it is. I didn't bother optimizing this since I only needed to run it once and I had no resource limitations. I did explore other alternatives, for example using the pyBigWig library to handle everything from with Python, but it seems it is still in early development has a lot of problems. Other solutions failed for other reasons or did not give me as much control as I needed (e.g. to normalize samples by coverage).

Note that you'll need some tools for this like gzip, zcat, split, awk, bedtools, bgzip (from htslib), UCSC tools (for bedGraphToBigWig), which are all quite common though, and a few static files like sizes of chromosomes in your genome assembly. Also depending on the resolution you chose to do this, this might take a lot of disk space (in the order of Tb).

In the end it does produce some nice visualizations, but I'm not sure all this trouble was really worth it - up to you to decide.

<br>

If anyone can make this (the concept, not really my quickly-hacked code) into a nice tool, please feel free!

{% gist f91ac2c554557eb2f1e4fbe8f234e14e %}
