---
layout: post
title: "Human receptor-ligand interaction repertoire"
description: "Human receptor-ligand interaction repertoire and its expression in primary cells"
category: research
tags: [programming, python]
---
{% include JB/setup %}


Available as a [Jupyter notebook here](https://github.com/afrendeiro/afrendeiro.github.io/blob/master/data/notebooks/human_ligand_receptor_expression/receptor-ligand-expression.ipynb)


## Receptor-ligand interactions in human primary cells

Ramilowski et al (10.1038/ncomms8866) have a very nice resource on receptor-ligand interactions in human primary cells.
Let's explore...


```python
%pylab inline

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_style("white")
plt.rcParams['svg.fonttype'] = 'none'
```

    Populating the interactive namespace from numpy and matplotlib



```python
# Read in the supplementary material
df = pd.read_excel(
    "https://images.nature.com/original/nature-assets/ncomms/2015/150722/ncomms8866/extref/ncomms8866-s3.xlsx", 1)
df.head()
```

<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pair.Name</th>
      <th>Ligand.ApprovedSymbol</th>
      <th>Ligand.Name</th>
      <th>Receptor.ApprovedSymbol</th>
      <th>Receptor.Name</th>
      <th>DLRP</th>
      <th>HPMR</th>
      <th>IUPHAR</th>
      <th>HPRD</th>
      <th>STRING.binding</th>
      <th>STRING.experiment</th>
      <th>HPMR.Ligand</th>
      <th>HPMR.Receptor</th>
      <th>PMID.Manual</th>
      <th>Pair.Source</th>
      <th>Pair.Evidence</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A2M_LRP1</td>
      <td>A2M</td>
      <td>alpha-2-macroglobulin</td>
      <td>LRP1</td>
      <td>low density lipoprotein receptor-related prote...</td>
      <td>NaN</td>
      <td>HPMR</td>
      <td>NaN</td>
      <td>HPRD</td>
      <td>STRING.binding</td>
      <td>STRING.experiment</td>
      <td>A2M</td>
      <td>LRP1</td>
      <td>NaN</td>
      <td>known</td>
      <td>literature supported</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AANAT_MTNR1A</td>
      <td>AANAT</td>
      <td>aralkylamine N-acetyltransferase</td>
      <td>MTNR1A</td>
      <td>melatonin receptor 1A</td>
      <td>NaN</td>
      <td>HPMR</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>AANAT</td>
      <td>MTNR1A</td>
      <td>NaN</td>
      <td>known</td>
      <td>literature supported</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AANAT_MTNR1B</td>
      <td>AANAT</td>
      <td>aralkylamine N-acetyltransferase</td>
      <td>MTNR1B</td>
      <td>melatonin receptor 1B</td>
      <td>NaN</td>
      <td>HPMR</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>AANAT</td>
      <td>MTNR1B</td>
      <td>NaN</td>
      <td>known</td>
      <td>literature supported</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ACE_AGTR2</td>
      <td>ACE</td>
      <td>angiotensin I converting enzyme</td>
      <td>AGTR2</td>
      <td>angiotensin II receptor, type 2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>HPRD</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>ACE</td>
      <td>AGTR2</td>
      <td>NaN</td>
      <td>novel</td>
      <td>literature supported</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ACE_BDKRB2</td>
      <td>ACE</td>
      <td>angiotensin I converting enzyme</td>
      <td>BDKRB2</td>
      <td>bradykinin receptor B2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>HPRD</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>ACE</td>
      <td>BDKRB2</td>
      <td>NaN</td>
      <td>novel</td>
      <td>literature supported</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Let's explore the existing known interactions

# filter out interactions labeled as "EXCLUDED"
df = df.loc[
    ~df['Pair.Evidence'].str.contains("EXCLUDED"),
    ['Pair.Name', 'Ligand.ApprovedSymbol', 'Receptor.ApprovedSymbol']]
df.columns = ['pair', 'ligand', 'receptor']
df['interaction'] = 1
```


```python
# Let's make a pivot table of receptor vs ligands
df_pivot = pd.pivot_table(data=df, index="ligand", columns='receptor', aggfunc=sum, fill_value=0)

# Heatmap
g = sns.clustermap(
    df_pivot, xticklabels=False, yticklabels=False, metric="jaccard",
    rasterized=True, cbar_kws={"label": "Jaccard distance"})
g.ax_row_dendrogram.set_visible(False)
g.ax_col_dendrogram.set_visible(False)
g.ax_heatmap.set_xlabel("receptor")
g.savefig(os.path.join("human_receptor_ligand.interaction_map.clustermap.svg"), bbox_inches="tight", dpi=300)
```

    /home/afr/.local/lib/python3.5/site-packages/matplotlib/cbook.py:136: MatplotlibDeprecationWarning: The axisbg attribute was deprecated in version 2.0. Use facecolor instead.
      warnings.warn(message, mplDeprecation, stacklevel=1)



![png](/data/notebooks/human_ligand_receptor_expression/output_4_1.png)



```python
# Let's now play with the expression of these genes in tissues
df = pd.read_excel(
    "https://images.nature.com/original/nature-assets/ncomms/2015/150722/ncomms8866/extref/ncomms8866-s5.xlsx",
    1, index_col=[0, 1, 2])
df.head()

# remove not expressed genes in any tissue
df = df[~(df.sum(1) == 0)]
```


```python
# Let's correlate tissues in the expression of these genes
w, h = df.shape[1] * 0.12, df.shape[1] * 0.12
g = sns.clustermap(
    df.corr(), xticklabels=False, figsize=(w, h), cbar_kws={"label": "Pearson correlation"})
g.ax_heatmap.set_yticklabels(g.ax_heatmap.get_yticklabels(), rotation=0, fontsize="xx-small", rasterized=True)
g.ax_row_dendrogram.set_rasterized(True)
g.ax_col_dendrogram.set_rasterized(True)
g.savefig(
    os.path.join("human_receptor_ligand.expression.tissue_correlation.clustermap.svg"),
    bbox_inches="tight", dpi=300)
```

    /home/afr/.local/lib/python3.5/site-packages/matplotlib/cbook.py:136: MatplotlibDeprecationWarning: The axisbg attribute was deprecated in version 2.0. Use facecolor instead.
      warnings.warn(message, mplDeprecation, stacklevel=1)



![png](/data/notebooks/human_ligand_receptor_expression/output_6_1.png)



```python
# Let's visualize the expression ligand and receptors in the different tissues
df2 = np.log2(1 + df.drop("F5.PrimaryCells.Expression_Max", axis=1).dropna())

w, h = df2.shape[1] * 0.12, df2.shape[0] * 0.01
g = sns.clustermap(df2.T, metric="correlation", z_score=1, vmin=-3, vmax=3,
                   figsize=(h, w), cbar_kws={"label": "log(expression) Z-score"}, xticklabels=False, rasterized=True)
g.ax_heatmap.set_yticklabels(g.ax_heatmap.get_yticklabels(), rotation=0, fontsize="x-small")
g.ax_row_dendrogram.set_rasterized(True)
g.ax_col_dendrogram.set_rasterized(True)
g.ax_heatmap.set_xlabel("Gene (ligands, receptors)")
g.savefig(os.path.join("human_receptor_ligand.expression.clustermap.svg"), bbox_inches="tight", dpi=300)
```

    /home/afr/.local/lib/python3.5/site-packages/matplotlib/cbook.py:136: MatplotlibDeprecationWarning: The axisbg attribute was deprecated in version 2.0. Use facecolor instead.
      warnings.warn(message, mplDeprecation, stacklevel=1)



![png](/data/notebooks/human_ligand_receptor_expression/output_7_1.png)

