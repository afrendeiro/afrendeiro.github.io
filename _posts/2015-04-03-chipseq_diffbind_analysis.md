---
layout: post
title: "Tools for ChIP-seq differential binding analysis"
description: ""
category: research
tags: [chip-seq, differential binding, tools, software]
---
{% include JB/setup %}

Detection of differential binding events in ChIP-seq data is still a tricky business. For a new collaboration, the whole project is going to depend on it, so I went out there and tried to collect existing tools, work with them and see their pros and cons.

I was looking specifically for tools that work well without replicates or input controls since we already have some data lying around from a pilot in the begging of the project, but they might be useful as well as the data comes along.

In no particular order:

## [diffBind](http://www.bioconductor.org/packages/release/bioc/html/DiffBind.html)
- Robust tutorial.
- Requires a strict table with sample annotation (not necessarily bad though).
- Requires peak files.
- Uses multiple replicates in analysis.
- Always requires input files to perform analysis.
- Close `R` integration provides many useful methods to explore output by plotting.

## [MANorm](http://bcb.dfci.harvard.edu/~gcyuan/MAnorm/MAnorm.htm)
- Requires peak files.
- Does not require input files.
- Terrible code packaging and usage practices.

Commands to install dependencies are outdated. If anyone is also strugling with it, here's what worked for me:

    source("http://bioconductor.org/biocLite.R")
    biocLite("aroma.light")
    install.packages(c("R.oo","R.utils","MASS"))

## [Diffreps](https://github.com/shenlab-sinai/diffreps)
- Installation is not straightforward (dependency hell).
- Requires peak files.
- Does not require input files (but can be used for fold enrichment filtering).
- Some nice tools downstream of differential calling (mostly region annotation).

## [Odin](http://www.regulatory-genomics.org/odin-2/basic-introduction/)
- Can use inputs for analysis.
- Limited description of output.
- Output in "a proprietary BED format" (do I need to say anything?)

## [MACS2](https://github.com/taoliu/MACS/wiki/Call-differential-binding-events)
- Does not require peak files.
- Poor documentation on the diff bind functions
- Very immature code ("prepare a pen to write down the number of non-redundant reads" - seriously?)

## [MultiGPS](mahonylab.org/software/multigps/)

## [PePr](https://github.com/troublezhang/PePr)
- Requires more than one replicate per condition for analysis.
- Does not require peak files.
- Does not require input files.
- Supports several input file formats.

## [ChIPDiff](http://cmb.gis.a-star.edu.sg/ChIPSeq/paperChIPDiff.htm)
- No documentation besides a readme in a zip file.
- Not really packaged.

## [DIME](http://www.stat.osu.edu/~statgen/SOFTWARE/DIME/)
- Poor documentation (only function description in the [R package](http://cran.r-project.org/web/packages/DIME/)).


## [DBChIP](http://pages.cs.wisc.edu/~kliang/DBChIP/)
- Useful tutorial.
- Only recommended for point-source factors.
- Requires peak files.
