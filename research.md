---
layout: page
title: "Research"
description: ""
group: navigation
weight: 2
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
</style>

I am generally interested in epigenetics in animal development and bioinformatics.

Here are projects I am currently working on or have worked in the past:

# Current projects

## Uncovering the contribution of epigenetics to development and disease

In this project I will try to gain insights into the contribution of epigenetic modulators and their effects during normal development and disease with an unbiased bottom-up approach.

---

# Past projects

## The role of E2F factors and H3K79 methylation in *Oikopleura dioica*'s cell cycle modes

The eukaryotic cell cycle is one of the most studied biological processes. However, variations of the canonical cell cycle have been discovered and found to be more predominant than previously expected. Endoreplication and endocycling - two such variants - produce polyploid cells, conferring advantages in growth and genotoxic stress. Although some of the regulatory principles of these cycles are being discovered, little is known about how cells can transition from a mitotic cell cycle to them.

Recently, it has been proposed that methylation of histone 3 lysine 79 (H3K79me) might have a function distinct from most histone modifications - a timer for a cell’s age -, for methylation of all H3K79 states is performed in a distributive fashion (unlike all other methylated lysines in histones) by Dot1 and no demethylase is known. Functional studies on Dot1 have shown aberrant patterns of replication, linking it directly to a cell’s ability to regulate its cell cycle.

This project aims to study the mechanisms of transition between different cell cycle modes in *Oikopleura dioica* - a marine chordate employing endocycling extensively through its life cycle.

We performed ChIP-seq on two antagonist transcription factors (E2F1 and E2F7) involved in the control of cell cycle progression that have been shown to have differential patterns of regulation in mitotic and endocycling cell cycle modes. We set ourselves to perform an initial functional study of H3K79me in *Oikopleura* though Dot1 inhibition in developmental stages employing different cell cycle modes.

<div class="centerImages">
	<img src={{ site.url }}"/data/figures/oikopleura_lifeCycle.png"
		 alt="<i>Oikopleura dioica</i> employs various types of cell cycle during its life cycle" align="middle" style="height: 200px;"/>

	<img src={{ site.url }}"/data/figures/oikopleura_change_cell-cycle.png"
		 alt="We're interested in the molecular mechanisms leading to the transition between cell cycle modes" align="middle" style="height: 150px;"/>
</div>
<p style="clear: both;"> </p>

---

## Evolution of the eumetazoan regulatory landscape: epigenetics, chromatin modifications and regulatory elements in *Nematostella vectensis*

Bilaterian animals differ from other metazoans in their apparent bilateral symmetry and the development of a third germ layer. Both might have facilitated the evolution of the diverse and complex bilaterian body plans. The first cnidarian genome sequence revealed that despite their morphological simplicity, this sister group to all bilaterians shares a surprisingly complex gene repertoire with vertebrates. This raised the possibility that rather than the gene set itself it might have been the complexity of gene regulation, which differs between cnidarians and bilaterians.

In this project we compared the gene regulatory landscape of a cnidarian and bilaterians. To this end we profiled five epigenetic marks, RNA Polymerase 2 and p300/CBP through ChIP-seq and generated the first genome-wide prediction of chromatin states and gene regulatory elements in a non-bilaterian animal, the cnidarian *Nematostella vectensis*.

We found that the location of chromatin modifications relative to genes and distal enhancers is conserved among eumetazoans. We also show that the inhibition of CpG methylation by the presence of H3K4me3 at CpG islands is not a feature exclusive from mammalian cells, but is also ancestrally conserved. Despite *Nematostella* lacking CTCF (a factor implicated in gene regulation by distal enhancers) we predicted thousands of distal enhancers and tested a portion in vivo, which in a large majority of cases induced expression at least partially reflecting the expression pattern of the neighboring gene.

Taken together our work showed that the genomic landscape of gene regulatory elements and associated genes is highly similar between *Nematostella* and bilaterian model organisms. This suggests that the eumetazoan ancestor already possessed highly complex gene regulation and that the complexity of bilaterian body plans in general did not arise through novel gene regulatory mechanisms. We hypothesize that rather a re-wiring of a few important interactions in gene regulatory networks might have led to the evolution of new body plans and an increase in complexity in bilaterians.

<div class="centerImages">
	<img src={{ site.url }}"/data/figures/nematostella_chipSeq.png"
		 alt="ChIP-seq of histone modifications in the cnidarian <i>Nematostella vectensis</i>" align="middle" style="height: 350px;"/>

	<img src={{ site.url }}"/data/figures/nematostella_hmmStates.png"
		 alt="Chromatin segmentation allows discovery of cis-regulatory elements" align="middle" style="height: 200px;"/>

	<img src={{ site.url }}"/data/figures/nematostella_enhancers.png"
		 alt="Predicted enhancers drive expression in a manner that recapitulates expression of nearby genes" align="middle" style="height: 350px;"/>
</div>

<p style="clear: both;"> </p>

[See full publication here][1].

[See also a poster about this project on Figshare][2].

[1]: http://genome.cshlp.org/content/24/4/639.full
[2]: http://figshare.com/articles/Identification_of_gene_regulatory_elements_in_the_sea_anemone_Nematostella_vectensis/107026
