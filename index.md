---
layout: page
title : "André Rendeiro"
description: "My personal website"
---
{% include JB/setup %}

<div class="row">
    <div class="col-sm-4">
        <img src="me.jpeg" style="width:70%;" alt="It's me!">
        <dl>
            <br>
            <dt><span property="foaf:firstName">André</span> <span property="foaf:familyName">Figueiredo Rendeiro</span></dt>
            <dd>Postdoctoral Associate</dd>
            <dd>Institute for Computational Biomedicine</dd>
            <dd>Englander Institute for Precision Medicine</dd>
            <dd>Weill Cornell Medicine</dd>
            <br>
            <!--<dt>Address:</dt>
                <dd>
                    <span property="schema:address" typeof="http://schema.org/PostalAddress" vocab="http://schema.org/PostalAddress/">
                        <a href="https://goo.gl/maps/E1cvcQCrLWKNQBct5">
                            <span property="streetAddress">Weill Cornell Medicine<br>Greenberg Center<br>1305 York Ave</span>,<br>
                            <span property="postalCode">10021</span>
                            <span property="addressLocality">New York</span>, 
                            <span property="addressCountry">USA</span>
                        </a>
                    </span>
                </dd>
            <br>
            -->
            <dt>Orcid ID:</dt>
                <dd>
                    <a property="http://purl.org/spar/datacite/orcid" href="https://orcid.org/0000-0001-9362-5373" onclick="recordOutboundLink(this, 'Link', '| + input + |'); return false;">0000-0001-9362-5373</a>
                </dd>
            <dt>Google Scholar:</dt>
                <dd>
                    <a href="https://scholar.google.at/citations?user=lj17pqEAAAAJ&hl=en">André Figueiredo Rendeiro</a>
                </dd>
            <br>
            <dt>Public Key:</dt>
                <dd>
                    <a href="http://andre-rendeiro.com/data/documents/public_key.pgp" title="Use this to send me encrypted email">PGP public key</a>
                </dd>
            <!-- <dt>ZeroNet ID:</dt>
                <dd>
                    <a href="http://127.0.0.1:43110/Me.ZeroNetwork.bit/?Profile/1RedkCkVaXuVXrqCMpoXQS29bwaqsuFdL/16XR1GVbekHSMMoUZ5pTQWFpq2anbkHgrC/arendeiro@zeroid.bit" title="Email me on ZeroNet">arendeiro@zeroid.bit</a>
                </dd>
            <dt>My Keybase identity:</dt>
                <dd>
                    <a href="https://keybase.io/afrendeiro" title="Me on Keybase">keybase.io/afrendeiro</a>
                </dd>
                 -->
        </dl>
        <h4>Curriculum Vitae</h4>
        <a href="https://raw.githubusercontent.com/afrendeiro/cv/master/cv.pdf">Download my CV in PDF format</a>
    </div>
    <div class="col-sm-8" typeof="foaf:Person" about="http://andre-rendeiro.com/about" prefix="schema: http://schema.org/Person#">
        <!--<img src="me.jpeg" style="width:210px; height:210px; margin: 0px 10px; float:left" alt="It's me!">-->
        <p>
            I am a <span property="schema:jobTitle">Postdoctoral Associate</span> in Computational Biomedicine at the 
            <a rel="schema:affiliation" href="https://icb.med.cornell.edu/">Institute for Computational Biomedicine of Weill Cornell Medical College</a>
            and the 
            <a rel="schema:affiliation" href="https://eipm.weill.cornell.edu/">Englander Institute for Precision Medicine</a> 
            in the lab of <a rel="foaf:member" href="https://elementolab.weill.cornell.edu/">Olivier Elemento</a>.
        </p>
        <p>
            I am currently developing computational methodologies to understand the spatial organization of tissue and the interplay between cancer cells, immune system and structural cell types, and how that can be applied for the development of novel therapeutical options or disease management.
            I develop and sometimes contribute to open source software. Check out my <a href="https://github.com/afrendeiro">GitHub profile</a> to see my tools and project contributions.
        </p>
        <p>
            I did my PhD at the <a href="https://cemm.at">CeMM - Research Center for Molecular Medicine of the Austrian Academy of Sciences</a> in the lab of Christoph Bock where I applied computational methods to high-dimentional molecular biology datasets of primary patient data in an effort to produce novel ways to monitor disease progression, predict risk and stratify patients and develop novel therapeutical avenues.
        </p>
    </div>
    <div class="col-sm-8 blog-main" id="research">
        <h4>Research highlights</h4>
        <h5>Spatial and temporally resolved COVID-19 pathology and immunology:</h5>
        <ol>
            <li>
                <a rel="datacite:doi" href="http://dx.doi.org/10.1101/2020.10.26.20219584" onclick="recordOutboundLink(this, 'DOI', '10.1101/2020.10.26.20219584'); return false;">Rendeiro*, Ravichandran*, <i>et al</i>, MedRxiv, 2020</a>
            </li>
            <li>
                <a rel="datacite:doi" href="http://dx.doi.org/10.26508/lsa.202000955" onclick="recordOutboundLink(this, 'DOI', '10.26508/lsa.202000955'); return false;">Rendeiro <i>et al</i>, Life Science Alliance, 2020</a>
            </li>
        </ol>
        <h5>Epigenetics for personalized medicine in cancer:</h5>
        <ol>
            <li>
                <a rel="datacite:doi" href="http://dx.doi.org/10.1038/s41467-019-14081-6" onclick="recordOutboundLink(this, 'DOI', '10.1038/s41467-019-14081-6'); return false;">Rendeiro*, Krausgruber*, <i>et al</i>, Nature Communications, 2020</a>
            </li>
            <li>
                <a rel="datacite:doi" href="http://dx.doi.org/10.1038/s41589-018-0205-2" onclick="recordOutboundLink(this, 'DOI', '10.1038/s41589-018-0205-2'); return false;">Schmidl*, Vladimer*, Rendeiro*, Schnabl*, <i>et al</i>, Nature Chemical Biology, 2019</a>
            </li>
            <li>
                <a rel="datacite:doi" href="http://dx.doi.org/10.1038/ncomms11938" onclick="recordOutboundLink(this, 'DOI', '10.1038/ncomms11938'); return false;">Rendeiro*, Schmidl*, Strefford*, <i>et al</i>, Nature Communications, 2016</a>
            </li>
        </ol>
        <h5>Technology development:</h5>
        <ol>
            <li>
                scifi-RNA-seq: <a rel="datacite:doi" href="http://dx.doi.org/10.1101/2019.12.17.879304" onclick="recordOutboundLink(this, 'DOI', '10.1101/2019.12.17.879304'); return false;">Datlinger<sup>*</sup>, Rendeiro<sup>*</sup>, <i>et al</i>, bioRxiv, 2019</a>
            </li>
            <li>
                ChIP-STARR-seq: <a rel="datacite:doi" href="http://dx.doi.org/http://dx.doi.org/10.1016/j.stem.2018.06.014" onclick="recordOutboundLink(this, 'DOI', 'http://dx.doi.org/10.1016/j.stem.2018.06.014'); return false;">Barakat<sup>*</sup>, Halbritter<sup>*</sup>, <i>et al</i>, Cell Stem Cell, 2018</a>
            </li>
            <li>
                CROP-seq: <a rel="datacite:doi" href="http://dx.doi.org/10.1038/nmeth.4177" onclick="recordOutboundLink(this, 'DOI', '10.1038/nmeth.4177'); return false;">Datlinger, <i>et al</i>, Nature Methods, 2017</a>
            </li>
            <li>
                ChIPmentation: <a rel="datacite:doi" href="http://dx.doi.org/10.1038/nmeth.3542" onclick="recordOutboundLink(this, 'DOI', '10.1038/nmeth.3542'); return false;">Schmidl<sup>*</sup>, Rendeiro<sup>*</sup>, <i>et al</i>, Nature Methods, 2015</a>
            </li>
        </ol>
        <h4>Support</h4>
        <p>I am supported by a National Cancer Institute T32 grant for Molecular and Translational Oncology Research (T32CA203702) awarded to Weill Cornell Medical College.</p>
    </div>
</div>

<hr>

<div class="row blog-main" prefix="datacite: http://purl.org/spar/datacite/" id="publications">
    <h3>Publications and associated resources</h3>
	<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
    <small><sup>*</sup> equal contributions</small><br>
    <div class="col-sm-6">
        <h4>All peer reviewed publications</h4>
        <ol reversed="">
            <li>
                <p>Sandra Schick, Sarah Grosche, Katharina Eva Kohl, Danica Drpic, Martin G. Jaeger, Nara C. Marella, Hana Imrichova, Jung-Ming G. Lin, Gerald Hofstätter, Michael Schuster, <u>André F. Rendeiro</u>, Anna Koren, Mark Petronczki, Christoph Bock, André C. Müller, Georg E. Winter & Stefan Kubicek.
            	<br><strong>Acute BAF perturbation causes immediate changes in chromatin accessibility</strong>.
                <br>Nature Genetics (2021). <a rel="datacite:doi" href="https://doi.org/10.1038/s41588-021-00777-3" onclick="recordOutboundLink(this, 'DOI', '10.1038/s41588-021-00777-3'); return false;">doi:10.1038/s41588-021-00777-3</a>
                <br>
                <a href="https://github.com/Kubicek-Lab-at-CeMM/BAF-kinetics"><button type="button" class="btn btn-default btn-sm"> <span class="fab fa-github" style="font-size: 1.4em;" aria-hidden="true"></span> Code </button></a>
                <span data-badge-type="2" data-doi="10.1038/s41588-021-00777-3" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    <u>André F. Rendeiro</u>, Joseph Casano, Charles Kyriakos Vorkas, Harjot Singh, Ayana Morales, Robert A DeSimone, Grant B Ellsworth, Rosemary Soave, Shashi N Kapadia, Kohta Saito, Christopher D Brown, JingMei Hsu, Christopher Kyriakides, Steven Chui, Luca Cappelli, Maria Teresa Cacciapuoti, Wayne Tam, Lorenzo Galluzzi, Paul D Simonson, Olivier Elemento, Mirella Salvatore, Giorgio Inghirami.
                    <br><strong>Profiling of immune dysfunction in COVID-19 patients allows early prediction of disease progression</strong>.
                    <br>Life Science Alliance (2020). <a rel="datacite:doi" href="https://doi.org/10.26508/lsa.202000955" onclick="recordOutboundLink(this, 'DOI', '10.26508/lsa.202000955'); return false;">doi:10.26508/lsa.202000955</a>
                    <br>
                    <a href="https://www.life-science-alliance.org/content/lsa/4/2/e202000955.full.pdf"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-file" aria-hidden="true"></span> PDF </button></a>
                    <a href="https://dx.doi.org/10.1101/2020.09.08.20189092"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-file" aria-hidden="true"></span> Preprint </button></a>
                    <a href="https://github.com/ElementoLab/covid-flowcyto"><button type="button" class="btn btn-default btn-sm"> <span class="fab fa-github" style="font-size: 1.4em;" aria-hidden="true"></span> Code </button></a>
                    <span data-badge-type="2" data-doi="10.26508/lsa.202000955" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Alexander Swoboda, Robert Soukup, Oliver Eckel, Katharina Kinslechner, Bettina Wingelhofer, David Schörghofer, Christina Sternberg, Ha T T Pham, Maria Vallianou, Jaqueline Horvath, Dagmar Stoiber, Lukas Kenner, Lionel Larue, Valeria Poli, Friedrich Beermann, Takashi Yokota, Stefan Kubicek, Thomas Krausgruber, <u>André F Rendeiro</u>, Christoph Bock, Rainer Zenz, Boris Kovacic, Fritz Aberger, Markus Hengstschläger, Peter Petzelbauer, Mario Mikula, Richard Moriggl.
                    <br><strong>STAT3 promotes melanoma metastasis by CEBP-induced repression of the MITF pathway</strong>.
                    <br>Oncogene (2020). <a rel="datacite:doi" href="http://dx.doi.org/10.1038/s41388-020-01584-6" onclick="recordOutboundLink(this, 'DOI', '10.1038/s41388-020-01584-6'); return false;">doi:10.1038/s41388-020-01584-6</a>
                    <br>
                    <a href="https://dx.doi.org/10.1101/422832"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-file" aria-hidden="true"></span> Preprint </button></a>
                    <span data-badge-type="2" data-doi="10.1101/422832" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Thomas Krausgruber, Nikolaus Fortelny, Victoria Fife-Gernedl, Martin Senekowitsch, Linda C. Schuster, Alexander Lercher, Amelie Nemc, Christian Schmidl, <u>André F. Rendeiro</u>, Andreas Bergthaler, Christoph Bock.
                    <br><strong>Structural cells are key regulators of organ-specific immune responses</strong>.
                    <br>Nature (2020). <a rel="datacite:doi" href="http://dx.doi.org/10.1038/s41586-020-2424-4" onclick="recordOutboundLink(this, 'DOI', '10.1038/s41586-020-2424-4'); return false;">doi:10.1038/s41586-020-2424-4</a>
                    <br>
                    <a href="http://structural-immunity-paper.medical-epigenomics.org/"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-file" aria-hidden="true"></span> PDF </button></a>
                    <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE134663"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" aria-hidden="true"></span> Data </button></a>
                    <a href="https://github.com/epigen/StructuralImmunity"><button type="button" class="btn btn-default btn-sm"> <span class="fab fa-github" style="font-size: 1.4em;" aria-hidden="true"></span> Code </button></a>
                    <span data-badge-type="2" data-doi="10.1038/s41586-020-2424-4" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Rainer Hubmann, Susanne Schnabl, Mohammad Araghi, Christian Schmidl, <u>André F. Rendeiro</u>, Martin Hilgarth, Dita Demirtas, Farghaly Ali,Philipp B. Staber, Peter Valent, Christoph Zielinski, Ulrich Jäger, Medhat Shehata.
                    <br><strong>Targeting Nuclear NOTCH2 by Gliotoxin Recovers a Tumor-Suppressor NOTCH3 Activity in CLL</strong>.
                    <br>Cells (2020). <a rel="datacite:doi" href="http://dx.doi.org/10.3390/cells9061484" onclick="recordOutboundLink(this, 'DOI', '10.3390/cells9061484'); return false;">doi:10.3390/cells9061484</a>
                    <br>
                    <span data-badge-type="2" data-doi="10.3390/cells9061484" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Elizabeth C Rosser, Christopher J.M. Piper, Diana E Matei ,Paul A. Blair, <u>André F. Rendeiro</u>, Michael Orford, Dagmar G. Alber, Thomas Krausgruber, Diego Catalan, Nigel Klein, Jessica J. Manson, Ignat Drozdov, Christoph Bock, Lucy R Wedderburn, Simon Eaton, Claudia Mauri.
                    <br><strong>Microbiota-Derived Metabolites Suppress Arthritis by Amplifying Aryl-Hydrocarbon Receptor Activation in Regulatory B Cells</strong>.
                    <br>Cell Metabolism (2020). <a rel="datacite:doi" href="http://dx.doi.org/10.1016/j.cmet.2020.03.003" onclick="recordOutboundLink(this, 'DOI', '10.1016/j.cmet.2020.03.003'); return false;">doi:10.1016/j.cmet.2020.03.003</a>
                    <br>
                    <a href="https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-7345/"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" aria-hidden="true"></span> Data </button></a>
                    <a href="https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-7525/"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" aria-hidden="true"></span> Data </button></a>
                    <span data-badge-type="2" data-doi="10.1016/j.cmet.2020.03.003" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    <u>André F. Rendeiro*</u>, Thomas Krausgruber*, Nikolaus Fortelny, Fangwen Zhao, ThomasPenz, Matthias Farlik, Linda C. Schuster, Amelie Nemc, Szabolcs Tasnády, MariennRéti, Zoltán Mátrai, Donat Alpar, Csaba Bödör, Christian Schmidl, Christoph Bock.
                    <br><strong>Chromatin mapping and single-cell immune profiling define the temporal dynamics of ibrutinib drug response in CLL</strong>.
                    <br>Nature Communications (2020). <a rel="datacite:doi" href="http://dx.doi.org/10.1038/s41467-019-14081-6" onclick="recordOutboundLink(this, 'DOI', '10.1038/s41467-019-14081-6'); return false;">doi:10.1038/s41467-019-14081-6</a>
                    <br>
                    <a href="https://dx.doi.org/10.1038/s41467-019-14081-6"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-file" aria-hidden="true"></span> Preprint </button></a>
                    <a href="http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE111015"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" aria-hidden="true"></span> Data </button></a>
                    <a href="https://github.com/epigen/cll-time_course"><button type="button" class="btn btn-default btn-sm"> <span class="fab fa-github" style="font-size: 1.4em;" aria-hidden="true"></span> Code </button></a>
                    <span data-badge-type="2" data-doi="10.1038/s41467-019-14081-6" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Christopher JM Piper, Elizabeth C Rosser, Kristine Oleinika, Kiran Nistala, Thomas Krausgruber, <u>André F. Rendeiro</u>, Aggelos Banos, Ignat Drozdov, Matteo Villa, Scott Thomson, Georgina Xanthou, Christoph Bock, Brigitta Stockinger, Claudia Mauri.
                    <br><strong>Aryl Hydrocarbon Receptor Contributes to the Transcriptional Program of IL-10-Producing Regulatory B Cells</strong>.
                    <br>Cell Reports. (2019) <a rel="datacite:doi" href="http://dx.doi.org/10.1016/j.celrep.2019.10.018" onclick="recordOutboundLink(this, 'DOI', '10.1016/j.celrep.2019.10.018'); return false;">doi:10.1016/j.celrep.2019.10.018</a>
                    <br>
                    <a href="https://www.ebi.ac.uk/arrayexpress/search.html?query=Aryl+hydrocarbon+receptor+governs+a+transcriptional+programme+that+determines+regulatory+B+cell+differentiation+and+function"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" aria-hidden="true"></span> Data </button></a>
                    <span data-badge-type="2" data-doi="10.1016/j.celrep.2019.10.018" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Florian Puhm, Taras Afonyushkin, Ulrike Resch, Georg Obermayer, Manfred Rohde, Thomas Penz, Michael Schuster, Gabriel Wagner, <u>André F. Rendeiro</u>, Imene Melki, Christoph Kaun, Johann Wojta, Christoph Bock, Bernd Jilma, Nigel Mackman, Eric Boilard, Christoph J Binder.
                    <br><strong>Mitochondria are a subset of extracellular vesicles released by activated monocytes and induce type I IFN and TNF responses in endothelial cells</strong>.
                    <br>Circulation Research. (2019) <a rel="datacite:doi" href="http://dx.doi.org/10.1161/CIRCRESAHA.118.314601" onclick="recordOutboundLink(this, 'DOI', '10.1161/CIRCRESAHA.118.314601'); return false;">doi:10.1161/CIRCRESAHA.118.314601</a>
                    <br>
                    <span data-badge-type="2" data-doi="10.1161/CIRCRESAHA.118.314601" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Sandra Schick, <u>André F. Rendeiro</u>, Kathrin Runggatscher, Anna Ringler, Bernd Boidol, Melanie Hinkel, Peter Májek, Loan Vulliard, Thomas Penz, Katja Parapatics, Christian Schmidl, Jörg Menche, Guido Boehmelt, Mark Petronczki, André C. Müller, Christoph Bock, Stefan Kubicek.
                    <br><strong>Systematic characterization of BAF mutations provides insights into intracomplex synthetic lethalities in human cancers</strong>.
                    <br>Nature Genetics (2019). <a rel="datacite:doi" href="http://dx.doi.org/10.1038/s41588-019-0477-9" onclick="recordOutboundLink(this, 'DOI', '10.1038/s41588-019-0477-9'); return false;">doi:10.1038/s41588-019-0477-9</a>
                    <br>
                    <a href="http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE108390"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" aria-hidden="true"></span> Data </button></a>
                    <a href="https://github.com/epigen/baf-complex"><button type="button" class="btn btn-default btn-sm"> <span class="fab fa-github" style="font-size: 1.4em;" aria-hidden="true"></span> Code </button></a>
                    <span data-badge-type="2" data-doi="10.1038/s41588-019-0477-9" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Sara Sdelci, <u>André F. Rendeiro</u>, Philipp Rathert, Wanhui You, Jung-Ming G. Lin, Anna Ringler, Gerald Hofstätter, Herwig P. Moll, Bettina Gürtl, Matthias Farlik, Sandra Schick, Freya Klepsch, Matthew Oldach, Pisanu Buphamalai, Fiorella Schischlik, Peter Májek, Katja Parapatics, Christian Schmidl, Michael Schuster, Thomas Penz, Dennis L. Buckley, Otto Hudecz, Richard Imre, Shuang-Yan Wang, Hans Michael Maric, Robert Kralovics, Keiryn L. Bennett, Andre C. Müller, Karl Mechtler, Jörg Menche, James E. Bradner, Georg E. Winter, Kristaps Klavins, Emilio Casanova, Christoph Bock, Johannes Zuber & Stefan Kubicek.
                    <br><strong>MTHFD1 interaction with BRD4 links folate metabolism to transcriptional regulation</strong>.
                    <br>Nature Genetics (2019). <a rel="datacite:doi" href="http://dx.doi.org/10.1038/s41588-019-0413-z" onclick="recordOutboundLink(this, 'DOI', '10.1038/s41588-019-0413-z'); return false;">doi:10.1038/s41588-019-0413-z</a>
                    <br>
                    <a href="http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE105786"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" aria-hidden="true"></span> Data </button></a>
                    <a href="https://github.com/epigen/mthfd1"><button type="button" class="btn btn-default btn-sm"> <span class="fab fa-github" style="font-size: 1.4em;" aria-hidden="true"></span> Code </button></a>
                    <span data-badge-type="2" data-doi="10.1038/s41588-019-0413-z" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Christian Schmidl*, Gregory I Vladimer*, <u>André F. Rendeiro*</u>, Susanne Schnabl*,Thomas Krausgruber, Christina Taubert, Nikolaus Krall, Tea Pemovska, MohammadAraghi, Berend Snijder, Rainer Hubmann, Anna Ringler, Kathrin Runggatscher,Dita Demirtas, Oscar Lopez de la Fuente, Martin Hilgarth, Cathrin Skrabs, Edit Porpaczy, Michaela Gruber, Gregor Hoermann, Stefan Kubicek, Philipp B Staber, Medhat Shehata, Giulio Superti-Furga, Ulrich Jäger, Christoph Bock.
                    <br><strong>Combined chemosensitivity and chromatin profiling prioritizes drug combinations in CLL</strong>.
                    <br>Nature Chemical Biology (2019). <a rel="datacite:doi" href="http://dx.doi.org/10.1038/s41589-018-0205-2" onclick="recordOutboundLink(this, 'DOI', '10.1038/s41589-018-0205-2'); return false;">doi:10.1038/s41589-018-0205-2</a>
                    <br>
                    <a href="https://www.nature.com/articles/s41589-018-0205-2.epdf?author_access_token=bhLY62eOUKzMxIek0Lrur9RgN0jAjWel9jnR3ZoTv0OorJZAyhsTHb_lKvE8iHB4D-HCNtQW3iuHJ6rd4yyhVuqSRybOkvDAylqw3Y4ls_TSAbSvsrbyBKCASfcuMe_LYEtnAVhV2dzkOxsLOLffEA%3D%3D"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-file" aria-hidden="true"></span> PDF </button></a>
                    <a href="http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100672"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" aria-hidden="true"></span> Data </button></a>
                    <a href="https://github.com/epigen/cll-ibrutinib"><button type="button" class="btn btn-default btn-sm"> <span class="fab fa-github" style="font-size: 1.4em;" aria-hidden="true"></span> Code </button></a>
                    <span data-badge-type="2" data-doi="10.1038/s41589-018-0205-2" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Tahsin Stefan Barakat*, Florian Halbritter*, Man Zhang, <u>André F. Rendeiro</u>, Christoph Bock, Ian Chambers.
                    <br><strong>Functional dissection of the enhancer repertoire in human embryonic stem cells</strong>.
                    <br>Cell Stem Cell. (2018) <a rel="datacite:doi" href="http://dx.doi.org/10.1016/j.stem.2018.06.014" onclick="recordOutboundLink(this, 'DOI', '10.1016/j.stem.2018.06.014'); return false;">doi:10.1016/j.stem.2018.06.014</a>
                    <br>
                    <a href="http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE99631"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" aria-hidden="true"></span> Data </button></a>
                    <span data-badge-type="2" data-doi="10.1016/j.stem.2018.06.014" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Paul Datlinger, <u>André F Rendeiro*</u>, Christian Schmidl*, Thomas Krausgruber, Peter Traxler, Johanna Klughammer, Linda C Schuster, Amelie Kuchler, Donat Alpar, Christoph Bock.
                    <br><strong>Pooled CRISPR screening with single-cell transcriptome readout</strong>.
                    <br>Nature Methods. (2017) <a rel="datacite:doi" href="http://dx.doi.org/10.1038/nmeth.4177" onclick="recordOutboundLink(this, 'DOI', '10.1038/nmeth.4177'); return false;">doi:10.1038/nmeth.4177</a>
                    <br>
                    <a href="http://rdcu.be/oDFf"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-file" aria-hidden="true"></span> PDF </button></a>
                    <a href="http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE81274"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" aria-hidden="true"></span> Data </button></a>
                    <a href="https://github.com/epigen/crop-seq"><button type="button" class="btn btn-default btn-sm"> <span class="fab fa-github" style="font-size: 1.4em;" aria-hidden="true"></span> Code </button></a>
                    <span data-badge-type="2" data-doi="10.1038/nmeth.4177" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Roman A Romanov, Amit Zeisel, Joanne Bakker, Fatima Girach, Arash Hellysaz, Raju Tomer, Alán Alpár, Jan Mulder, Frédéric Clotman, Erik Keimpema,  Brian Hsueh, Ailey K Crow, Henrik Martens, Christian Schwindling,  Daniela Calvigioni, Jaideep S Bains, Zoltán Máté, Gábor Szabó, Yuchio Yanagawa, Ming-Dong Zhang, <u>Andre Rendeiro</u>, Matthias Farlik, Mathias Uhlén, Peer Wulff,  Christoph Bock, Christian Broberger, Karl Deisseroth, Tomas Hökfelt,  Sten Linnarsson, Tamas L Horvath & Tibor Harkany.
                    <br><strong>Molecular interrogation of hypothalamic organization reveals distinct dopamine neuronal subtypes</strong>.
                    <br>Nature Neuroscience (2017). <a rel="datacite:doi" href="http://dx.doi.org/10.1038/nn.4462" onclick="recordOutboundLink(this, 'DOI', '10.1038/nn.4462'); return false;">doi:10.1038/nn.4462</a>
                    <br>                    
                    <a href="http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE74672"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" aria-hidden="true"></span> Data </button></a>
                    <span data-badge-type="2" data-doi="10.1038/nn.4462" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Clara Jana-Lui Busch, Tim Hendrikx, David Weismann, Sven Jäckel, Sofie M. A. Walenbergh, <u>André F. Rendeiro</u>, Juliane Weißer, Florian Puhm, Anastasiya Hladik, Laura Göderle, Nikolina Papac-Milicevic, Gerald Haas, Vincent Millischer, Saravanan Subramaniam, Sylvia Knapp, Keiryn L. Bennett, Christoph Bock, Christoph Reinhardt, Ronit Shiri-Sverdlov, Christoph J. Binder.
                    <br><strong>Malondialdehyde epitopes are sterile mediators of hepatic inflammation in hypercholesterolemic mice</strong>.
                    <br>Hepatology (2017). <a rel="datacite:doi" href="http://dx.doi.org/10.1002/hep.28970" onclick="recordOutboundLink(this, 'DOI', '10.1002/hep.28970'); return false;">doi:10.1002/hep.28970</a>
                    <br>
                    <span data-badge-type="2" data-doi="10.1002/hep.28970" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    <u>André F Rendeiro*</u>, Christian Schmidl*, Jonathan C. Strefford*,  Renata Walewska, Zadie Davis, Matthias Farlik,   David Oscier, Christoph Bock.
                    <br><strong>Chromatin accessibility maps of chronic lymphocytic leukaemia identify subtype-specific epigenome signatures and transcription regulatory networks</strong>.
                    <br>Nature Communications (2016). <a rel="datacite:doi" href="http://dx.doi.org/10.1038/ncomms11938" onclick="recordOutboundLink(this, 'DOI', '10.1038/ncomms11938'); return false;">doi:10.1038/ncomms11938</a>
                    <br>
                    <a href="http://www.nature.com/ncomms/2016/160627/ncomms11938/pdf/ncomms11938.pdf"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-file" aria-hidden="true"></span> PDF </button></a>
                    <a href="https://ega-archive.org/studies/EGAS00001001821"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" aria-hidden="true"></span> Raw data</button></a>
                    <a href="http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE81274"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" aria-hidden="true"></span> Processed data</button></a>
                    <a href="https://github.com/epigen/cll-chromatin"><button type="button" class="btn btn-default btn-sm"> <span class="fab fa-github" style="font-size: 1.4em;" aria-hidden="true"></span> Code </button></a>
                    <span data-badge-type="2" data-doi="10.1038/ncomms11938" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Christian Schmidl*, <u>André F Rendeiro*</u>, Nathan C Sheffield, Christoph Bock.
                    <br><strong>ChIPmentation: fast, robust, low-input ChIP-seq for histones and transcription factors</strong>.
                    <br>Nature Methods (2015). <a rel="datacite:doi" href="http://dx.doi.org/10.1038/nmeth.3542" onclick="recordOutboundLink(this, 'DOI', '10.1038/nmeth.3542'); return false;">doi:10.1038/nmeth.3542</a>
                    <br>
                    <a href="http://www.cemm.oeaw.ac.at/fileadmin/img/Research/research/Schmidl_et_al_Nature_Methods_2015.pdf"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-file" aria-hidden="true"></span> PDF </button></a>
                    <a href="http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE70482"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" aria-hidden="true"></span> Data </button></a>
                    <a href="https://github.com/epigen/chipmentation"><button type="button" class="btn btn-default btn-sm"> <span class="fab fa-github" style="font-size: 1.4em;" aria-hidden="true"></span> Code </button></a>
                    <span data-badge-type="2" data-doi="10.1038/nmeth.3542" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Michaela Schwaiger, Anna Schönauer, <u>André F Rendeiro</u>, Carina Pribitzer, Alexandra Schauer, Anna F Gilles, Johannes B Schinko, Eduard Renfer, David Fredman, Ulrich Technau.
                    <br><strong>Evolutionary conservation of the eumetazoan gene regulatory landscape</strong>.
                    <br>Genome Research (2014). <a rel="datacite:doi" href="http://dx.doi.org/10.1101/gr.162529.113" onclick="recordOutboundLink(this, 'DOI', '10.1101/gr.162529.113'); return false;">doi:10.1101/gr.162529.113</a>
                    <br>
                    <a href="http://genome.cshlp.org/content/24/4/639.full.pdf"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-file" aria-hidden="true"></span> PDF </button></a>
                    <a href="http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE46488"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" aria-hidden="true"></span> Data </button></a>
                    <span data-badge-type="2" data-doi="10.1101/gr.162529.113" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
        </ol>
    </div>
    <div class="col-sm-6">
        <h4>Preprints</h4>
        <ol reversed="">
            <li>
                <p>
                    <u>André F. Rendeiro*</u>, Hiranmayi Ravichandran*, Yaron Bram, Steven Salvatore, Alain Borczuk, Olivier Elemento, Robert E. Schwartz.
                    <br><strong>The spatio-temporal landscape of lung pathology in SARS-CoV-2 infection</strong>.
                    <br>medRxiv (2020). <a rel="datacite:doi" href="http://dx.doi.org/10.1101/2020.10.26.20219584" onclick="recordOutboundLink(this, 'DOI', '10.1101/2020.10.26.20219584'); return false;">doi:10.1101/2020.10.26.20219584</a>
                    <br>
                    <a href="https://dx.doi.org/10.1101/2020.10.26.20219584"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-file" aria-hidden="true"></span> Preprint </button></a>
                    <a href="https://doi.org/10.5281/zenodo.4110560"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" style="font-size: 1.4em;" aria-hidden="true"></span> Raw data </button></a>
                    <a href="https://doi.org/10.5281/zenodo.4139443"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-hdd" style="font-size: 1.4em;" aria-hidden="true"></span> Processed data </button></a>
                    <a href="https://github.com/ElementoLab/covid-imc"><button type="button" class="btn btn-default btn-sm"> <span class="fab fa-github" style="font-size: 1.4em;" aria-hidden="true"></span> Code </button></a>
                    <span data-badge-type="2" data-doi="10.1101/2020.10.26.20219584" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
        	<li>
                <p>
                    Nathan C. Sheffield, Michał Stolarczyk, Vincent P. Reuter, <u>André F. Rendeiro</u>.
                    <br><strong>Linking big biomedical datasets to modular analysis with Portable Encapsulated Projects</strong>.
                    <br>bioRxiv (2020). <a rel="datacite:doi" href="http://dx.doi.org/10.1101/2020.10.08.331322" onclick="recordOutboundLink(this, 'DOI', '10.1101/2020.10.08.331322'); return false;">doi:10.1101/2020.10.08.331322</a>
                    <br>
                    <a href="https://dx.doi.org/10.1101/2020.10.08.331322"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-file" aria-hidden="true"></span> Preprint </button></a>
                    <a href="https://github.com/pepkit/peppy"><button type="button" class="btn btn-default btn-sm"> <span class="fab fa-github" style="font-size: 1.4em;" aria-hidden="true"></span> Code </button></a>
                    <span data-badge-type="2" data-doi="10.1101/2020.10.08.331322" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    Paul Datlinger*, <u>André F. Rendeiro*</u>, Thorina Boenke, Thomas Krausgruber, Daniele Barreca, Christoph Bock.
                    <br><strong>Ultra-high throughput single-cell RNA sequencing by combinatorial fluidic indexing</strong>.
                    <br>bioRxiv (2019). <a rel="datacite:doi" href="http://dx.doi.org/10.1101/2019.12.17.879304" onclick="recordOutboundLink(this, 'DOI', '10.1101/2019.12.17.879304'); return false;">doi:10.1101/2019.12.17.879304</a>
                    <br>
                    <a href="https://dx.doi.org/10.1101/2019.12.17.879304"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-file" aria-hidden="true"></span> Preprint </button></a>
                    <a href="/2019/12/13/chromium_modeling"><button type="button" class="btn btn-default btn-sm"> <span class="fab book-open" style="font-size: 1.4em;" aria-hidden="true"></span> Notebook</button></a>
                    <span data-badge-type="2" data-doi="10.1101/2019.12.17.879304" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
            <li>
                <p>
                    <u>André F Rendeiro</u>, Pavla Navratilova, Eric Thompson.
                    <br><strong>Chromatin preparation for ChIP-seq in Oikopleura dioica</strong>.
                    <br>Figshare (2014). <a rel="datacite:doi" href="http://dx.doi.org/10.6084/m9.figshare.884562" onclick="recordOutboundLink(this, 'DOI', '10.6084/m9.figshare.884562'); return false;">doi:10.6084/m9.figshare.884562</a>
                    <br>
                    <a href="http://files.figshare.com/1360952/ChIP_chromprep_Oikopleura.pdf"><button type="button" class="btn btn-default btn-sm"> <span class="glyphicon glyphicon-file" aria-hidden="true"></span> PDF </button></a>
                    <span data-badge-type="2" data-doi="10.6084/m9.figshare.884562" data-hide-no-mentions="true" class="altmetric-embed"></span>
                </p>
            </li>
        </ol>
    </div>
    <br>
</div>

