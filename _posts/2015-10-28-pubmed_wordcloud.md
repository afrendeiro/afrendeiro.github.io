---
layout: post
title: "Pubmed wordcloud"
description: "Wordcloud with search results from Pubmed"
category: research
tags: [python, pubmed, graphics]
---
{% include JB/setup %}

A friend asked me recently to make a wordcloud with publications that arise when searching Pubmed for a particular term.

My implementation uses NCBI's `eutils` to search for the term and retrieve pubmed ids, which I in a second step query NCBI with. I chose to use the publication titles to cound word frequencies and build the wordcloud after removing common words (*e.g.* articles).

{% gist 6ec23ce2d0317a160e8f %}

Since there are a few free online tools to actually draw the tool (*e.g.* wordle.net) I didn't bother implementing that, but I did searched and there are a few interesting Python modules to do that as well ([amueller/word_cloud](https://github.com/amueller/word_cloud) seemed quite feature-complete, for example).


### LCMV wordcloud
(Some common words removed on request (virus, etc...))

![lcmv wordcloud](/data/figures/lcmv_cloud.svg)
