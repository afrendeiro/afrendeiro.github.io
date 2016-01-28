---
layout: post
title: "SNPs from the GWAS catalog as a LOLA region set"
description: "SNPs from the GWAS catalog as a LOLA region set"
category: research
tags: [python, gwas, variation]
---

{% include JB/setup %}

Ever wondered if some genomic regions of interest overlap significantly with known (or own) sets of regions?

[LOLA](http://databio.org/lola/) is an R package that handles that for you. It includes a "core" set of regions from public databases and lets you extend them with your own regions of interest.

I wanted to include the position of every known SNP associated with a trait (specially clinical) in the database, but also preferebly grouped by the broad type of trait. here's what I came up with by using [EBI's GWAS catalog](https://www.ebi.ac.uk/gwas/).

### Creating a bed file with SNPs for each disease group

{% highlight python %}

import os
import pandas as pd
import re

# get GWAS catalog
os.system("wget -O gwas_catalog.tsv http://www.ebi.ac.uk/gwas/api/search/downloads/alternative")  # gwas db dump
os.system("wget http://www.ebi.ac.uk/fgpt/gwas/ontology/GWAS-EFO-Mappings201405.xlsx")  # gwas mapping/ontology

# read in catalog and mappings
df = pd.read_csv("gwas_catalog.tsv", sep="\t")
mapping = pd.read_excel("GWAS-EFO-Mappings201405.xlsx")

# merge both
df2 = pd.merge(df, mapping, on=['PUBMEDID'])

# subset columns
df3 = df2[['CHR_ID', 'CHR_POS', 'PUBMEDID', 'DISEASE/TRAIT', 'PARENT', 'SNPS', 'STRONGEST SNP-RISK ALLELE', 'P-VALUE', 'OR or BETA']]
df3.columns = ['chr', 'pos', 'pubmed_id', 'trait', 'ontology_group', 'snp', 'snp_strongest_allele', 'p_value', 'beta']
df3.to_csv("gwas_catalog.csv", index=False)

# filter on p-value
df4 = df3[df3['p_value'] < 5e-8]

if not os.path.exists("regions"):
    os.makedirs("regions")

# export bed file for each ontology group
regionset_index = pd.DataFrame()
for group in df4['ontology_group'].unique():
    df5 = df4[df4['ontology_group'] == group]
    df5 = df5[['chr', 'pos']]
    df5.columns = ['chr', 'start']
    # drop entries without a position
    df5.dropna(how='any', subset=['chr', 'start'], inplace=True)
    df5['chr'] = ['chr' + str(int(i)) for i in df5['chr']]
    df5['end'] = df5['start'] + 1

    df5['start'] = df5['start'].astype(int)
    df5['end'] = df5['end'].astype(int)

    # write bed file
    group = re.sub(" ", "_", group).lower()
    df5.drop_duplicates().to_csv("regions/gwas_catalog.%s.bed" % group, sep="\t", header=False, index=False)

    # save in regionset index
    regionset_index = regionset_index.append(pd.Series(["Human", "SNPs in gwas catalog - %s" % group, "GWAS catalog", "gwas_catalog.%s.bed" % group]), ignore_index=True)

# save regionset index
regionset_index.columns = ["species", "description", "dataSource", "filename"]
regionset_index.to_csv("index.txt", sep="\t", index=False)

{% endhighlight %}

You will have a file named `index.txt` enumerating the various region sets, which are inside a folder named `regions`.

### Documenting your region sets

Simply create a tab-delimited file in the same folder named `collection.txt` with the following information:

|collector|date|source|description|
|---|---|---|---|
|arendeiro|2016-01-28|customRegionDB/hg38/gwas|GWAS from EBI's GWAS catalog (http://www.ebi.ac.uk/gwas/)|
