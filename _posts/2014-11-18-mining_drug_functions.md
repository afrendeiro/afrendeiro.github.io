---
layout: post
title: "Mining drug functions into an ontology"
description: ""
category: research
tags: [chemical biology, chemical screening, data mining, python]
submenu:
  - { anchor: "background", title: "Background" }
  - { anchor: "results", title: "Results" }
  - { anchor: "discussion", title: "Discussion" }
  - { anchor: "methods", title: "Methods" }
  - { anchor: "code", title: "Code" }
---
{% include JB/setup %}
<style>
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

In this short rotation, I mined several databases for known biological functions of chemical compounds and built an ontology which can be used to test enrichment of functional classes in interesting compounds discovered by chemical screening.

#<a href="{{page.url}}#background" name="background">Background</a>
With the exponential rise of information on chemical compounds coming from high-throughput screens there is also increasing demand for integration of available data on the biological role of chemical compounds with biological relevance. By relating chemical compounds with their previously known functions in similar or distinct cellular environments one could be able to better understand underlying modes of action of drugs, or use this information to develop better drugs for new screens.

I implemented a small tool to mine several databases with relevant information on the bioactivity of chemical compounds. This creates a functional ontology of compounds representative of the whole library assayed which can be used to test the enrichment of subsets of relevant compounds (hits) with high-order biological functions of the compounds. I demonstrate the usefulness of the tool by annotating all compounds used in an image-based chemical screen and explore the ontology of the compounds with interesting effects by testing the significant enrichment of functional classes within them.

#<a href="{{page.url}}#results" name="results">Results</a>
As example, all 1448 compounds from a chemical screen were used. Since a particular source of noise in databases stems from unambiguously annotated compounds, we used annotations only from databases which allowed search using *SMILES*.

Having all compounds annotated with their general biological functions, we created an ontology of terms that establishes relations between compounds sharing the same function. This ontology reflects the usage of the compounds - widely used compounds are usually annotated with more functions, while many of the most obscure compounds are often annotated with smaller number of terms (see Figure 1A). Since the specificity of the terms with which a compound is annotated can be widely ranging, most abundant terms are therefore generally less specific, with many drugs having one term that is highly specific to them and therefore unshared (Figure 1B).

<div>
    <img src={{ site.url }}"/data/figures/terms_and_drugs.png"
         align="middle" style="width: 700px;"/>
</div>

<p align="center">Figure 1 - Relationship between compounds and their functional ontology terms. 
    <small>Top panel: Ontology terms per compound; Bottom panel: Compounds per ontology term. </small>
</p>

<p style="clear: both;"> </p>

Using a subset of compounds which showed relevant impact on cellular in the chemical screen, all terms from compounds in this subset were tested for their over-representation in the subset considering the whole library of compounds used in the screen. A list of significantly over-represented terms can be see in  Table 1.
Since the readout for this screen was a measure of viability, it is no surprise that the "antineoplastic agent" has the lowest p-value of the set since most antineoplastic drugs focus on the neutralization of cell viability. Of particular relevance though are the terms "anti-inflammatory drug", "glucocoricoid", "immunosuppressive agent", "anti-inflammatory agent " and others related to steroid drugs. These are the majority of the significant ones, and over-representation of this class indicates that the overall biological effect of inflammatory suppressive drugs is of great interest.

<p align="center">Table 1 - Results from test of enrichment of functional terms.</p>
<table align="center">
  <tr>
    <th>term</th>
    <th>odds_ratio</th>
    <th>p-value</th>
  </tr>
  <tr>
    <td>antineoplastic agent</td>
    <td>3.98</td>
    <td>0.000388</td>
  </tr>
  <tr>
    <td>hydroxamic acid</td>
    <td>20.89</td>
    <td>0.001495</td>
  </tr>
  <tr>
    <td>immunosuppressive agent</td>
    <td>7.22</td>
    <td>0.001685</td>
  </tr>
  <tr>
    <td>11beta-hydroxy steroid</td>
    <td>6.87</td>
    <td>0.002029</td>
  </tr>
  <tr>
    <td>20-oxo steroid</td>
    <td>6.55</td>
    <td>0.002422</td>
  </tr>
  <tr>
    <td>glucocorticoid</td>
    <td>8.72</td>
    <td>0.002736</td>
  </tr>
  <tr>
    <td>anti-inflammatory drug</td>
    <td>6.26</td>
    <td>0.002868</td>
  </tr>
  <tr>
    <td>secondary alcohol</td>
    <td>5.93</td>
    <td>0.008652</td>
  </tr>
  <tr>
    <td>3-oxo-Delta(1),Delta(4)-steroid</td>
    <td>5.63</td>
    <td>0.010105</td>
  </tr>
  <tr>
    <td>antifungal agent</td>
    <td>5.63</td>
    <td>0.010105</td>
  </tr>
  <tr>
    <td>21-hydroxy steroid</td>
    <td>8.31</td>
    <td>0.010449</td>
  </tr>
  <tr>
    <td>anti-inflammatory agent</td>
    <td>7.55</td>
    <td>0.012958</td>
  </tr>
  <tr>
    <td>fluorinated steroid</td>
    <td>7.55</td>
    <td>0.012959</td>
  </tr>
  <tr>
    <td>spiroketal</td>
    <td>13.59</td>
    <td>0.018290</td>
  </tr>
  <tr>
    <td>antiparasitic agent</td>
    <td>5.52</td>
    <td>0.026196</td>
  </tr>
</table>

<p style="clear: both;"> </p>

#<a href="{{page.url}}#discussion" name="discussion">Discussion</a>
Further development could focus on the optimization of the data mining process, where more sources could be integrated, and more information could be extracted. A critical improvement would be a better integration of information from the several sources used, merging them on common terms, which could reduce the amount of any contradicting annotation. Implementing user-oriented annotation would also be of interest, since users could select sources to annotate compounds focused on a particular interest. Adding support for alternative testing options, such as the hypergeometric test would also be something to develop further.

#<a href="{{page.url}}#methods" name="methods">Methods</a>

##<a name="database mining">Database mining</a>
Sources for the annotation of chemical compounds were diverse databases with relevance to Chemical Biology or specialized on their use in a biological context. Matches to most databases were performed by a simplified molecular-input line-entry system (*SMILES*) - a one-line notation commonly used to describe the structure of a chemical compound. This system has the advantage of while still being human-readable, it provides an unequivocal description of a given chemical compound (one *SMILES* - one compound), but the reverse relationship can be redundant (one compound - many *SMILES*). This property makes database searches by *SMILES* suboptimal if the same compound is described with different *SMILES* in various entries.

[ChemSpider](www.chemspider.com/), maintained by the Royal Society of Chemistry contains chemical structures of over 32 million compounds and provides text search with an API. Matches to database were performed based on *SMILES*. 

ChEMBL is the EMBL-EBI database for bioactive small molecules. It contains information on structural and chemical properties as well as on 'bioactivities' attributed to compounds. To circumvent the redundancy of the database, reduce the rates of misannotation of compounds and get an annotation as complete as possible, we developed a very simple algorithm to match a *SMILES* query to its ChEMBL entry if more than one match was retrieved: for each of several selected properties, results were compared with the query and differing results were discarded until only one result remained. This proceeded from more broad to specific characteristics in this order: molecular formula, molecular weight, *SMILES*, ChEMBL known drug. If after all iterations more than one result remained, the one on the top of the results was selected. For each selected compound bioactivities were also extracted if compound was marked as active in that particular assay. This information comes from assays in which the compound was used and include the status of activity (active/inactive) the target (ChEMBL id and name were extracted) and the organism in which the assay was performed.

Chemical Entities of Biological Interest (ChEBI) is another EMBL-EBI database for chemical compounds which focuses on the ontology of these molecular entities. It is therefore extremely useful for the purpose of this project. Queries to the database are made by *SMILES* and a positive match requires at least 70\% identity. Extracted information consists of a ChEBI id, compound name and functional terms associated with the compound in the ontology. For the purpose of annotation, the ChEBI ontology tree was flattened and the compound was annotated with all parent terms.

The Kyoto encyclopedia of Genes and Genomes (KEGG) also houses a database focusing on compounds with biological relevance (KEGG DRUG). While the information for approved compounds is comprehensive, including chemical structures, associated targets, metabolizing enzymes and interaction network information, search is only possible through the name of the compound, which is highly error-prone.

Since ultimately the goal of chemical screening is to identify molecules which can be used in human treatments, it is useful to connect this compound to previously executed clinical trials. The [http://clinicaltrials.gov](http://clinicaltrials.gov) database is a repository maintained by the U.S. National Institutes of Health containing worldwide clinical trial data. Search is only possible by compound name. Only completed studies employing the compounds were inspected and the study title, url and outcome were extracted.

#### <a name="implementation">Implementation</a>
Python is the sole language used for the implementation. Two separate scripts were composed to allow independence between the compound annotation step ```drugAnnotation.py``` and the testing for enriched ontology terms in a subset of the compounds (```drugEnrichment.py```). This also provides some modularization, allowing these scripts to be used in other contexts than originally conceived.

The APIs of the databases mentioned in the previous section were accessed using the Python *bioservices* package (ChEMBL, ChEBI and KEGG), while the *chemspipy* package was used for ChemSpider. Since ```clinicaltrials.org``` does not offer an API, queries were done by requesting results in XML. The python *urllib2* and *BeautifulSoup* packages were used to manage connections and extract content.

By default, database searches by name will not be performed, but the user can supply a flag which overides the default behaviour and allows annotation of compounds from databases such as KEGG and ```clinicaltrials.org```.

*Numpy* and *Pandas* packages were used throughout to easily provide implementation of data frames in Python and handle numeric data. This approach was very convenient due to the input data being on a spreadsheet format. Output data was kept in a comma-separated value (CSV) format, which is easily loaded into most GUI spreadsheet editors.      

The script testing over-representation requires ontology annotation of the whole universe of compounds assayed (the output from ```drugAnnotation.py```) and a list of compounds of interest which is a subset of the universe. The two are merged based on *SMILES*, and the Fischer's Exact Test (implemented in the *Scipy* package) is used to test each ontology term in the list of compounds of interest for over- or under-representation. The full list of tested term along with the number of compounds in each term, odds-ratio and p-value is outputted to allow the user overview over the whole data and control over the significance threshold.

# <a href="{{page.url}}#code" name="code">Code</a>
Code is licensed under the GNU General Public Licence (Version 3) and freely available at github: [https://github.com/afrendeiro/drugAnnotation](https://github.com/afrendeiro/drugAnnotation).
