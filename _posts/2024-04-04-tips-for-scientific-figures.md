---
layout: post
title: "Tips for scientific figures"
description: "Tips for scientific figures"
category: notebook
tags: [scientific illustration, matplotlib, seaborn, inkscape]
---
{% include JB/setup %}

Sometimes I get asked for tips or guidelines on how to create figures for scientific publications.

I do have a system to do this. It is not perfect, but it fits my workflow and I do improve it over time.

The "dream" of having a full final figure generated as a whole from a piece of code is just not worth it to the type of figures my papers usually have. Therefore only in very rare cases I even attempt to create a full figure or several panels directly from code. Since I have become very familiar with Inkscape, I can very quickly assemble plots into a figure with infinite customization which would be very painful to do in code. Plus building the figures in a graphical interface really helps me 'play' with the pieces of data and make a visual narrative for the paper, which then I translate to text - I am a visual person and every story starts with images for me.

In concept, my approach is quite simple:
1. generate plots individually as data is analyzed using [matplotlib](https://matplotlib.org/)/[seaborn](https://seaborn.pydata.org/);
2. assemble plots into a figure using [Inkscape](https://inkscape.org/);
3. uniformly process all figures into various formats (separate PNG, PDF, joint PDF).


### 1. Making plots (Python, matplotlib, seaborn)

- Try to compartmentalize data processing from visualization (not just the early 'pipeline'-like processing, but also the analytical analysis) - but that does not mean that auxiliary/intermediate plots can't be generated as data is analyzed.
- Each script produces a set of plots into a `results` directory, with subdirectories matching the script or analysis name (more hierarchical if needed, e.g. different datasets).
- Each plot file name should be self explanatory and contain enough information to track down its origin.
- Except for obvious groupings or interrelations, avoid making figures with many subplots.
- Create figures in matplotlib/seaborn always explicitly: `fig, ax = plt.subplots(figsize=(3, 3))`.
- For the most part aim for each subplot to have a square shape with about 3 by 3 inches. If creating a figure with multiple subplots, scale the figure size accordingly: `fig, axes = plt.subplots(4, 2, figsize=(2 * 3, 4 * 3)`.
- Always label the axes, and make use of a single statement to set many properties at once: `ax.set(xlabel="Time", ylabel="Expression (log)", yscale="log")`.
- For plot elements with many objects (e.g. scatter), rasterize that specific single element in order to reduce the size of the figure: `g = sns.clustermap(...); g.ax_heatmap.set(rasterized=True)`. Do not rasterize the whole axes as that will make e.g. text element uneditable.
- Color:
    - Choose consistent colors across a project. This can be achieved for example by importing a config file with preset colors for each factor level.
    - Use categorical colormaps for factors without implicit order. In general do not use more than 8 or 10 different colors.
    - Consider thinking of all factors being highlighted in the paper before starting the project. See colormaps here: [https://matplotlib.org/stable/gallery/color/colormap_reference.html](https://matplotlib.org/stable/gallery/color/colormap_reference.html).
    - Avoid situations where a color is suggestive or is associated with human values such as heteronormative, ageist or racial biases (e.g. gender: blue/pink, age: bright to dark).
    - Use continuous colormaps for continuous variables (magma, viridis), especially if they are fully non-negative. In general, use the brightest color for higher values.
    - Use divergent colormaps (coolwarm, RdBu_r, PuOr_r) only when a central value has meaning (e.g. a Z-score).
- Export figures as SVG format, but explicitly set `dpi=300` to make sure any rasterized elements have good quality. Set `bbox_inches='tight` to make sure the whole content is visible.


### 2. Assemble plots manually into a figure (inkscape)

- Check the journal requirements and limitations for figures and their dimensions. Use A4 by default, not letter.
- Here is a template figure: [https://gist.github.com/afrendeiro/2d9975793629774ad73ea9d18bd7abf3](https://gist.github.com/afrendeiro/2d9975793629774ad73ea9d18bd7abf3).
- Add a plot to the canvas, resize it to an approximate desired size, remove all groupings, remove redundant objects, possibly despine plot (i.e. remove top right, top axes). Make whole plot into a group (or layer).
- Tip: after having several groups, you can still select a single element of a group without 'entering' the group by using Ctrl+click.
- Align elements of plots/panels to each other with the `align` tool in Inkscape (the 'Last selected' option helps).
- Be wary of resize operations that change aspect ratio. Be sure not to create artifacts. Here's some help: [https://github.com/burghoff/Scientific-Inkscape](https://github.com/burghoff/Scientific-Inkscape) (hasn't worked recently for me).
- Use a consistent font family (Arial) for all text elements and only one or two font sizes (12 and 10).
- Tip: You can use the Find/Replace tool with `Object types = 'text'` to find all text objects, or for example find all elements of the same color or linestyle (leave out the "ff" part of a RGBA string when searching properties).
- Add a lowercase letter label to each panel (font 16).
- Add a label to the top of the Figure (i.e. Figure 1).
- Name the figure files consistently 'Figure01.svg', 'Figure02.svg', 'SupplementaryFigure01.svg', 'SupplementaryFigure02.svg', etc.


### 3. Automatic assembly and conversion of file types (bash, inkscape, minify, pdfunite)

- Add all figures to a `svg` directory (itself under `figures` in the project directory).
- Make sure figures are labeled consistently and with zero padded numbering (if needed).
- Use script here: [https://gist.github.com/afrendeiro/a656eca139381eec55da6357e33173ce](https://gist.github.com/afrendeiro/a656eca139381eec55da6357e33173ce).
- Use generated individual PDFs to embed in a manuscript tex file.
- Use generated individual PNGs to embed in a manuscript file like docx.
- Use the joint PDFs to print, share or submit to journal.


## Final thoughts

- Learning the basics of matplotlib and seaborn is essential to make useful plots that display the data in a clear way.
- Learning the basics of inkscape is essential to make figures without too much hassle. There is only a few key hidden tricks (e.g. Ctrl+click) to make the process super easy.
- Ultimately each person has different needs and preferences and this is just what I do. Try out some of the elements and see what works for you.
