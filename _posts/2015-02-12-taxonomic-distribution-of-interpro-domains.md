---
layout: post
title: "Taxonomic distribution of interpro domains"
description: ""
category: research
tags: [taxonomy, python, data mining, API]
---
{% include JB/setup %}

I recently faced a problem that seemed trivial to solve at first but (as always) was not: *How to get the taxonomic distribution of proteins with a given interpro domain?*

I start off even without knowing exactly which protein domains to look at (I wanted to look at all that were present in certain proteins). To do this, I query Uniprot through biomart to get all the annotated interpro domains present in a group of proteins. I also get a bunch of other info (other IDs, names) along.

{% highlight python %}
import pandas as pd
from biomart import BiomartServer, BiomartDataset

ids = ["P01106", "P17947"] # some examples

# connect to biomart
server = BiomartServer("http://www.biomart.org/biomart")
uniprot = server.datasets['uniprot']

# query interpro domains for the prots
attributes = ['accession', 'ensembl_id', 'entry_type', 'gene_name', 'name', 'interpro_id']
response = uniprot.search({
    'filters': {'accession': ids},
    'attributes': attributes
})

# put in dataframe
df = pd.DataFrame([line.split("\t") for line in list(response.content.strip().split("\n"))],
                      columns=attributes
                      )
{% endhighlight %}

We now switch to the Interpro database and get the scientific name (and other stuff) of species with proteins containing these interpro domains. Again Biomart is our friend.

{% highlight python %}
domains = df['interpro_id']
attributes = ['entry_id', 'entry_type', 'entry_name', 'taxonomy_scientific_name']

interpro = BiomartDataset("http://www.biomart.org/biomart", name='entry')

for domain in domains:
    # Query taxonomies with domains
    response = interpro.search({
        'filters': {'entry_id': domain},
        'attributes': attributes
    })
    taxons = pd.DataFrame([line.split("\t") for line in list(response.content.strip().split("\n"))],
                          columns=attributes
                          )

    if domain == domains[0]:
        df = taxons
    else:
        df = pd.concat([df, taxons])
{% endhighlight %}

To assess the distribution of these proteins across clades of species, one needs more information about these species. Getting there was the bit not so obvious to me.

[NCBI taxonomy](http://www.ncbi.nlm.nih.gov/taxonomy) has this type of information, but I wasn't familiar with their APIs or services so called [NCBI eutils](http://www.ncbi.nlm.nih.gov/books/NBK25501/). Luckyly there's a Python solution for [accessing NCBI’s Entrez databases thourough BioPython](http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc108).

We define two functions: to get the ID of a taxon based on its name (this actually may fail if species names have appended stuff like "strain") and to get the record (which contains a full lineage description) for that taxon based on its ID.

{% highlight python %}
from Bio import Entrez

def get_tax_id(specie):
    """Get taxon ID for specie."""
    specie = specie.replace(" ", "+").strip()
    search = Entrez.esearch(term=specie, db="taxonomy", retmode="xml")
    record = Entrez.read(search)
    if int(record["Count"]) == 0:
        return None
    if "IdList" in record.keys():
        return record['IdList'][0]


def get_tax_data(taxid):
    """Fetch the record of a taxon ID."""
    search = Entrez.efetch(id=taxid, db="taxonomy", retmode="xml")
    return Entrez.read(search)

Entrez.email = "" # enter your email here

# initialize empty column for taxonomy
df['taxonomy'] = None
for specie in unique(df["taxonomy_scientific_name"]):
    taxid = get_tax_id(specie)
    if taxid is None:
        continue
    data = get_tax_data(taxid)
    if len(data) >= 1:
        if "Lineage" in data[0].keys():
            # add taxonomy to all rows with this specie name
            df['taxonomy'][df['taxonomy_scientific_name'] == specie] = data[0]["Lineage"]
{% endhighlight %}

### Full example:
{% gist edc5af41628c886abe0a %}
