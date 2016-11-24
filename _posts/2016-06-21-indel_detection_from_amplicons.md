---
layout: post
title: "Indel Detection From Amplicons"
description: ""
category: research
tags: [python, ngs]
---
{% include JB/setup %}

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

There is plenty of good software out there for indel detection, but obviously I had to get some data which didn't fit any of them (AFAIK).
In my case I had some amplicon libraries of targeted loci with CRISPR (two cell lines, three guide RNAs each) from a MiSeq run.
What was particular about these was that the amplicon library was digested after amplification to provide more fragments and increase the likehood that the reads would overlap the indel event, so in practice my reads didn't start and end with the ends of the amplicon sequence - so **I quickly hacked something together for this effect** (**sharing for preservation, use at own risk**).

[All code and outputs can be seen here](https://github.com/afrendeiro/amplicon_indel_detection).

<br>

My first approch was to simply trim the reads of any primers/adapters, map them to the amplicons and count indels based on the CIGAR string of the reads.

The second one (at the request of a colleage) was to observe the distance between the extremeties of the amplicon in the reads without alignment.

<br>

Here's how it looks like for the first method:

<img src="https://rawgithub.com/afrendeiro/amplicon_indel_detection/master/results/editing_efficiency.indels.svg" width="90%">

<div class="centerImages">
    <img src="https://rawgithub.com/afrendeiro/amplicon_indel_detection/master/results/editing_efficiency.indels_percentage.svg"
         align="middle" style="width: 40%;"/>
</div>

<br>

And the same with the "grep method":

<img src="https://rawgithub.com/afrendeiro/amplicon_indel_detection/master/results/editing_efficiency.read_sizes.svg" width="90%">

<div class="centerImages">
    <img src="https://rawgithub.com/afrendeiro/amplicon_indel_detection/master/results/editing_efficiency.sizes_percentage.svg"
         align="middle" style="width: 40%;"/>
</div>

Although the methods differ in the sensitivity, both show very similar estimates of indel percentages.
Unfortunately for these experiments the editing efficiency was not very high due to a problem in the lab, but it is since solved.

<br>

The only thing missing is the rate of in frame indels because I'd need to look up the coordinate of the transcript in relation to the amplicon, since I aligned the reads to the "amplicon library" rather than to the genome, but that was too much work considering that people generally simply consider every indel multiple of 3 to be in frame.
