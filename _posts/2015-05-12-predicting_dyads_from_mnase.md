---
layout: post
title: "Predicting dyads from MNase-seq data"
description: ""
category: research
tags: [nucleosomes, dyads, MNase-seq]
---
{% include JB/setup %}

<script type="text/javascript"
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<style>
.centerImages {
    line-height:200px;
    text-align:center;
    margin-left: auto;
    margin-right: auto;
    width: 90%;
    vertical-align:middle;
}
.ulpost {list-style-type: none; margin: 0; padding: 0;}
.lipost {display: inline; margin-right: 20px;}
.lipost>a {width: 120px;}
</style>

{% if page.submenu %}
<h3>Contents</h3>
<ul class="ulpost">
{% for item in page.submenu %}
<li class="lipost"><a href="#{{ item.anchor }}">{{ item.title }}</a></li>
{% endfor %}
</ul>
{% endif %}

<br>

I needed the location of nucleosomal dyads in the K562 cell line (ENCODE tier 1 line). Surprisingly, although plenty of MNase-seq data exists, no nucleosome and dyad prediction exists.

### NuMap
I found the [NuMap](http://www-hsc.usc.edu/~valouev/NuMap/NuMap.html) software by Anton Valouev to do exactly what I intended.

Since it is in a somewhat obscure page and this seemed to be the only place where this software was, I have [uploaded it into a Github repository](https://github.com/afrendeiro/NuMap) for the sake of preservation.

Predicting dyads from MNase-seq data with NuMap seemed trivial: I downloaded the [K562 MNase-seq data set](http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhNsome/) (11 replicates ~85Gb!!), combined all replicates and ran NuMap on the data(instructions on the Github README).

From NuMap output there are [dyad positions in bed format](/data/K562_dyads.bed) and you can also produce several metrics to evaluate how good the prediction was.

### Distograms & phasograms

Valouev describes two measurements of the frequencies of distances between MNase-seq reads. The frequency of distances between reads mapping to opposite strands can be used to build a "distogram", which ilustrates the expected nucleosome length (147 bp) - this is consistent across most eukaryotic cells. The frequency of distances between reads mapping to the same strand gives a measurement of the distance between nucleosomes, as they're separated by some linker DNA - (Valouev calls this plot a "phasogram"). This measurement, on the other hand tends to be species and cell-type specific.

<div class="centerImages">
    <img src={{ site.url }}"/data/figures/dist-phasogram.png"
         align="middle"/>
</div>
<p align="center">Valouev, A., Johnson, S. M., Boyd, S. D., Smith, C. L., Fire, A. Z., Sidow, A. (2011). Determinants of nucleosome organization in primary human cells. Nature, 474(7352), 516–520. <a href="http://doi.org/10.1038/nature10002">http://doi.org/10.1038/nature10002</a></p>

#### K562 predictions:

<div class="centerImages">
    <img src={{ site.url }}"/data/figures/mnase-distogram.png"
         align="middle"/>
</div>
<p align="center">The expected 147 bp nucleosome length in K562 cells.</p>


<div class="centerImages">
    <img src={{ site.url }}"/data/figures/mnase-phasogram.png"
         align="middle"/>
</div>
<p align="center">The average distance between dyads in K562 cells seems to be 185 bp.</p>
