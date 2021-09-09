---
layout: page
title : "André Rendeiro"
description: "My personal website"
---
{% include JB/setup %}

<div class="row">
    <div class="col-sm-3 center-block text-center brd custom-col-width">
        <img src="me.jpg" class="my_image" alt="It's me, André!">
        <dl>
            <br>
            <dt>
                <span property="foaf:firstName">André</span>
                <span property="foaf:middleName">Figueiredo</span>
                <span property="foaf:familyName">Rendeiro</span>
            </dt>
            <dd>Postdoctoral Associate</dd>
            <dd>Institute for Computational Biomedicine</dd>
            <dd>Englander Institute for Precision Medicine</dd>
            <dd>Weill Cornell Medicine</dd>
            <br>
            <dt>Address:</dt>
                <dd>
                    <span
                        property="schema:address"
                        typeof="http://schema.org/PostalAddress"
                        vocab="http://schema.org/PostalAddress/">
                        <a href="https://goo.gl/maps/E1cvcQCrLWKNQBct5">
                            <span property="streetAddress">Weill Cornell Medicine<br>Greenberg Center<br>1305 York Ave</span>,<br>
                            <span property="postalCode">10021</span>
                            <span property="addressLocality">New York</span>, 
                            <span property="addressCountry">USA</span>
                        </a>
                    </span>
                </dd>
            <br>
            <dt>Orcid ID:</dt>
                <dd>
                    <a
                        property="http://purl.org/spar/datacite/orcid"
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
            <br>
            <dt>Public Key:</dt>
                <dd>
                    <a
                        href="http://andre-rendeiro.com/data/documents/public_key.pgp"
                        title="Use this to send me encrypted email">
                        PGP public key
                    </a>
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
            <br>
            <dt>Curriculum Vitae:</dt>
                <dd>
                    <a href="{{ site.author.cv }}" download="Rendeiro_AF_CV.pdf">Download my CV in PDF format</a>
                </dd>
            </dl>
    </div>
    <br>
    <div class="col-sm-8" typeof="foaf:Person" about="http://andre-rendeiro.com/about" prefix="schema: http://schema.org/Person#">
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
                <a rel="datacite:doi" href="http://dx.doi.org/10.1101/2021.09.05.21263141">
                Rendeiro <i>et al</i>, MedRxiv, 2021</a>
            </li>
            <li>
                <a rel="datacite:doi" href="http://dx.doi.org/10.1038/s41586-021-03475-6">
                Rendeiro*, Ravichandran*, <i>et al</i>, Nature, 2021</a>
            </li>
            <li>
                <a rel="datacite:doi" href="http://dx.doi.org/10.1038/s41586-021-03569-1">
                Melms*, [...], Rendeiro*, [...] <i>et al</i>, Nature, 2021</a>
            </li>
            <li>
                <a rel="datacite:doi" href="http://dx.doi.org/10.26508/lsa.202000955">
                Rendeiro <i>et al</i>, Life Science Alliance, 2020</a>
            </li>
        </ol>
        <h5>Epigenetics for personalized medicine in cancer:</h5>
        <ol>
            <li>
                <a rel="datacite:doi" href="http://dx.doi.org/10.1038/s41467-019-14081-6">
                Rendeiro*, Krausgruber*, <i>et al</i>, Nature Communications, 2020</a>
            </li>
            <li>
                <a rel="datacite:doi" href="http://dx.doi.org/10.1038/s41589-018-0205-2">
                Schmidl*, Vladimer*, Rendeiro*, Schnabl*, <i>et al</i>, Nature Chemical Biology, 2019</a>
            </li>
            <li>
                <a rel="datacite:doi" href="http://dx.doi.org/10.1038/ncomms11938">
                Rendeiro*, Schmidl*, Strefford*, <i>et al</i>, Nature Communications, 2016</a>
            </li>
        </ol>
        <h5>Technology development:</h5>
        <ol>
            <li>
                scifi-RNA-seq: <a rel="datacite:doi" href="http://dx.doi.org/10.1038/s41592-021-01153-z">
                Datlinger<sup>*</sup>, Rendeiro<sup>*</sup>, <i>et al</i>, Nature Methods, 2021</a>
            </li>
            <li>
                ChIP-STARR-seq: <a rel="datacite:doi" href="http://dx.doi.org/http://dx.doi.org/10.1016/j.stem.2018.06.014">
                Barakat<sup>*</sup>, Halbritter<sup>*</sup>, <i>et al</i>, Cell Stem Cell, 2018</a>
            </li>
            <li>
                CROP-seq: <a rel="datacite:doi" href="http://dx.doi.org/10.1038/nmeth.4177">
                Datlinger, <i>et al</i>, Nature Methods, 2017</a>
            </li>
            <li>
                ChIPmentation: <a rel="datacite:doi" href="http://dx.doi.org/10.1038/nmeth.3542">
                Schmidl<sup>*</sup>, Rendeiro<sup>*</sup>, <i>et al</i>, Nature Methods, 2015</a>
            </li>
        </ol>
        <h4>Support</h4>
        <p>I am the recipient of a National Cancer Institute T32 grant for Molecular and
           Translational Oncology Research (T32CA203702) awarded to Weill Cornell Medical College.</p>
    </div>
</div>

<hr>

<div class="row blog-main" prefix="datacite: http://purl.org/spar/datacite/" id="publications">
    <h3>Publications and associated resources</h3>
	<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
    <script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>
    <small><sup>*</sup> equal contributions</small><br>
    <div class="col-sm-12">
        <h4>All peer reviewed publications</h4>
        <ol reversed="">
{{publications_go_here}}
        </ol>
    </div>
    <div class="col-sm-12">
        <h4>Preprints</h4>
        <small>(does not include preprints later published as journal articles)</small>
        <ol reversed="">
{{preprints_go_here}}
        </ol>
    </div>
    <br>
</div>

Updated on {{current_date}}.
