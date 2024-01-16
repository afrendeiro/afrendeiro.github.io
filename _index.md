---
layout: page
title : "André Rendeiro"
description: "My personal website"
---
{% include JB/setup %}

<a rel="me" href="https://sciencemastodon.com/@afrendeiro"></a>

<div class="row">
    <div class="col-sm-3 center-block text-center brd">  <!--  custom-col-width -->
        <img src="me.jpg" class="my_image" alt="It's me, André!">
        <dl>
            <dt>
                <span property="foaf:firstName">André</span>
                <span property="foaf:middleName">Figueiredo</span>
                <span property="foaf:familyName">Rendeiro</span>
            </dt>
            <dd>Principal Investigator</dd>
            <dd>CeMM - Research Center</dd><dd>for Molecular Medicine,</dd>
            <dd>Austrian Academy of Sciences</dd>
            <br>
            <dt>Address:</dt>
            <dd>
                <span
                    property="schema:address"
                    typeof="https://schema.org/PostalAddress"
                    vocab="https://schema.org/PostalAddress/">
                    <a href="https://goo.gl/maps/qa1K9PSu8xSp7z3M6">
                        <span property="streetAddress">Lazarettgasse 14, AKH BT 25.3</span>,<br>
                        <span property="postalCode">1090</span>
                        <span property="addressLocality">Vienna</span>, 
                        <span property="addressCountry">Austria</span>
                    </a>
                </span>
            </dd>
            <dt>Orcid ID:</dt>
            <dd>
                <a
                    property="https://purl.org/spar/datacite/orcid"
                    href="https://orcid.org/0000-0001-9362-5373">
                    0000-0001-9362-5373
                </a>
            </dd>
            <dt>Google Scholar:</dt>
            <dd>
                <a
                    href="https://scholar.google.at/citations?user=lj17pqEAAAAJ&hl=en">
                    André Figueiredo Rendeiro
                </a>
            </dd>
            <!-- <dt>Public Key:</dt>
            <dd>
                <a
                    href="https://andre-rendeiro.com/data/documents/public_key.pgp"
                    title="Use this to send me encrypted email">
                    PGP public key
                </a>
            </dd> -->
            <!-- <dt>ZeroNet ID:</dt>
                <dd>
                    <a href="http://127.0.0.1:43110/Me.ZeroNetwork.bit/?Profile/1RedkCkVaXuVXrqCMpoXQS29bwaqsuFdL/16XR1GVbekHSMMoUZ5pTQWFpq2anbkHgrC/arendeiro@zeroid.bit" title="Email me on ZeroNet">arendeiro@zeroid.bit</a>
                </dd>
            <dt>My Keybase identity:</dt>
                <dd>
                    <a href="https://keybase.io/afrendeiro" title="Me on Keybase">keybase.io/afrendeiro</a>
                </dd>
                 -->
            <dt>Curriculum Vitae:</dt>
            <dd>
                <a href="{{ site.author.cv }}" download="Rendeiro_AF_CV.pdf">Download my CV in PDF format</a>
            </dd>
        </dl>
    </div>
    <div class="col-sm-8" typeof="foaf:Person" about="https://andre-rendeiro.com/about" prefix="schema: https://schema.org/Person#">
        <p>
            I am a <span property="schema:jobTitle">Principal Investigator</span> at <a rel="schema:affiliation" href="https://cemm.at/research/groups/andre-rendeiro-group">CeMM </a>- the <a rel="schema:affiliation" href="https://cemm.at/research/groups/andre-rendeiro-group">Research Center for Molecular Medicine</a> of the <a rel="schema:memberOf" href="https://www.oeaw.ac.at/en/">Austrian Academy of Sciences</a> leading a research group on computational and molecular methods to study human aging and pathology.
        </p>
        <p>
            My group develops computational methods for the analysis of spatial data (spatial transcriptomics, highly multiplexed imaging), and its integration with various modalities of molecular and    clinical data of individuals along their lifespan.
            I am particularly interested in the organization of cells at the micro-anatomical level and understanding how this changes during the lifespan of individuals and at the onset of disease.
        </p>
        <p>
            For my postdoctoral research, I was at the
            <a href="https://icb.med.cornell.edu/">Institute for Computational Biomedicine of Weill Cornell Medical College</a>
            and the <a href="https://eipm.weill.cornell.edu/">Englander Institute for Precision Medicine</a> 
            in the lab of <a href="https://elementolab.weill.cornell.edu/">Olivier Elemento</a>.
            There, I developed computational methods to understand the spatial organization of tissue, and employed them to infectious disease and cancer.
        </p>
        <p>
            During my PhD at <a href="https://cemm.at">CeMM</a> in the lab of <a href="https://www.bocklab.org/">Christoph Bock</a>, I applied computational methods to high-dimensional datasets of patient data to produce novel ways to monitor disease progression, stratify patients and develop novel therapeutic options. I also developed several methods for the epigenomic or single-cell profiling of human cells.
        </p>
        <!-- <p>
            I develop and sometimes contribute to open source software. Check out my <a href="https://github.com/afrendeiro">GitHub profile</a> to see my tools and project contributions.
        </p> -->
    </div>
    <div class="col-sm-8 blog-main" id="research">
        <h4>Research highlights</h4>
        <div class="col-sm-12">
            <!-- <div class="col-sm-6 col-shorter">
                <h5>Microanatomical basis of human aging:</h5>
                <ol>
                    <li>
                        <a rel="datacite:doi" href="https://dx.doi.org/">
                        X, <i>et al</i>, BioRxiv, 2024</a>
                    </li>
                </ol>
            </div> -->
            <div class="col-sm-6 col-shorter">
                <h5>Spatially resolved biology and tissue architecture:</h5>
                <ol>
                    <!-- <li>
                        <a rel="datacite:doi" href="https://dx.doi.org/">
                        X, <i>et al</i>, BioRxiv, 2024</a>
                    </li> -->
                    <li>
                        <a rel="datacite:doi" href="https://dx.doi.org/10.1038/s41592-022-01657-2">
                        Kim, <i>et al</i>, Nature Methods, 2022</a>
                    </li>
                </ol>
            </div>
        </div>
        <div class="col-sm-12">
            <div class="col-sm-4 col-shorter">
                <h5>Spatial and temporally resolved COVID-19 pathology and immunology:</h5>
                <ol>
                    <li>
                        <a rel="datacite:doi" href="https://dx.doi.org/10.1101/2022.11.28.22282811">
                        Rendeiro*, Ravichandran*, <i>et al</i>, medRxiv, 2022</a>
                    </li>
                    <li>
                        <a rel="datacite:doi" href="https://dx.doi.org/10.1038/s41586-021-03475-6">
                        Rendeiro*, Ravichandran*, <i>et al</i>, Nature, 2021</a>
                    </li>
                    <li>
                        <a rel="datacite:doi" href="https://dx.doi.org/10.1038/s41586-021-03569-1">
                        Melms*, [...], Rendeiro*, [...] <i>et al</i>, Nature, 2021</a>
                    </li>
                    <li>
                        <a rel="datacite:doi" href="https://dx.doi.org/10.3389/fimmu.2021.809937">
                        Rendeiro <i>et al</i>, Frontiers in Immunology, 2021</a>
                    </li>
                    <li>
                        <a rel="datacite:doi" href="https://dx.doi.org/10.26508/lsa.202000955">
                        Rendeiro <i>et al</i>, Life Science Alliance, 2020</a>
                    </li>
                </ol>
            </div>
            <div class="col-sm-4 col-shorter">
                <h5>Novel molecular techniques:</h5>
                <ol>
                    <li>
                        scifi-RNA-seq: <a rel="datacite:doi" href="https://dx.doi.org/10.1038/s41592-021-01153-z">
                        Datlinger<sup>*</sup>, Rendeiro<sup>*</sup>, <i>et al</i>, Nature Methods, 2021</a>
                    </li>
                    <li>
                        ChIP-STARR-seq: <a rel="datacite:doi" href="https://dx.doi.org/10.1016/j.stem.2018.06.014">
                        Barakat<sup>*</sup>, Halbritter<sup>*</sup>, <i>et al</i>, Cell Stem Cell, 2018</a>
                    </li>
                    <li>
                        CROP-seq: <a rel="datacite:doi" href="https://dx.doi.org/10.1038/nmeth.4177">
                        Datlinger, <i>et al</i>, Nature Methods, 2017</a>
                    </li>
                    <li>
                        ChIPmentation: <a rel="datacite:doi" href="https://dx.doi.org/10.1038/nmeth.3542">
                        Schmidl<sup>*</sup>, Rendeiro<sup>*</sup>, <i>et al</i>, Nature Methods, 2015</a>
                    </li>
                </ol>
            </div>
            <div class="col-sm-4 col-shorter">
                <h5>Precision medicine in cancer:</h5>
                <ol>
                    <li>
                        <a rel="datacite:doi" href="https://dx.doi.org/10.1038/s41467-019-14081-6">
                        Rendeiro*, Krausgruber*, <i>et al</i>, Nature Communications, 2020</a>
                    </li>
                    <li>
                        <a rel="datacite:doi" href="https://dx.doi.org/10.1038/s41589-018-0205-2">
                        Schmidl*, Vladimer*, Rendeiro*, Schnabl*, <i>et al</i>, Nature Chemical Biology, 2019</a>
                    </li>
                    <li>
                        <a rel="datacite:doi" href="https://dx.doi.org/10.1038/ncomms11938">
                        Rendeiro*, Schmidl*, Strefford*, <i>et al</i>, Nature Communications, 2016</a>
                    </li>
                </ol>
            </div>
        </div>
    </div>
</div>

<hr>

<div class="row blog-main" prefix="datacite: https://purl.org/spar/datacite/" id="publications">
    <h3>Publications and associated resources</h3>
	<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
    <script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>
    <small><sup>*</sup> equal first-author contributions; <sup>Ω</sup> joint corresponding authors</small><br>
    <div class="col-sm-12">
        <h4>Preprints</h4>
        <small>(does not include preprints later published as journal articles)</small>
        <ol reversed="">
{{preprints_go_here}}
        </ol>
    </div>
    <div class="col-sm-12">
        <h4>All peer reviewed publications</h4>
        <ol reversed="">
{{publications_go_here}}
        </ol>
    </div>
    <br>
    <div class="col-sm-12" style="margin-bottom: 30px;">
        <p>Last updated on {{current_date}}.</p>
    </div>
    <br>
</div>
