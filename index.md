---
layout: page
title : "André Rendeiro"
description: "My personal website"
---
{% include JB/setup %}

<a rel="me" href="https://sciencemastodon.com/@afrendeiro"></a>

<div class="row">
    <div class="col-sm-3 text-center">  <!--  custom-col-width -->
        <img src="me.jpg" alt="It's me, André!" class="img-fluid mx-auto d-block">
        <dl>
            <dt>
                <span property="foaf:firstName">André</span>
                <span property="foaf:middleName">Figueiredo</span>
                <span property="foaf:familyName">Rendeiro</span>
            </dt>
            <dd>Principal Investigator, CeMM</dd>
            <dd>Research Group Leader, LBI-NetMed</dd>
        </dl>
    </div>
    <div class="col-sm-8" typeof="foaf:Person" about="https://andre-rendeiro.com/about" prefix="schema: https://schema.org/Person#">
        <div class="alert alert-primary py-2" role="alert">
            Visit the <a href="https://rendeiro.group" class="alert-link"><strong>lab website</strong></a> for the team, research highlights, publications and open positions.
        </div>
        <p>
            I am a <span property="schema:jobTitle">Principal Investigator</span> at <a rel="schema:affiliation" href="https://cemm.at/research/groups/andre-rendeiro-group">CeMM </a>- the <a rel="schema:affiliation" href="https://cemm.at/research/groups/andre-rendeiro-group">Research Center for Molecular Medicine</a> of the <a rel="schema:memberOf" href="https://www.oeaw.ac.at/en/">Austrian Academy of Sciences</a> and a <span property="schema:jobTitle">Research Group Leader</span> at the <a rel="schema:affiliation" href="https://netmed.lbg.ac.at/">Ludwig Boltzmann Institute for Network Medicine at the University of Vienna</a>, leading a research group on computational and molecular methods to study human aging and pathology.
        </p>
        <p>
            <a href="https://rendeiro.group">My group</a> develops computational methods for the analysis of spatial data (spatial transcriptomics, highly multiplexed imaging), and its integration with various modalities of molecular and clinical data of individuals along their lifespan.
            I am particularly interested in the organization of cells at the micro-anatomical level and understanding how this changes during the lifespan of individuals and at the onset of disease.
        </p>
        <p>
            My postdoctoral research was at the
            <a href="https://icb.med.cornell.edu/">Institute for Computational Biomedicine of Weill Cornell Medical College</a>
            and the <a href="https://eipm.weill.cornell.edu/">Englander Institute for Precision Medicine</a>
            in the lab of <a href="https://elementolab.weill.cornell.edu/">Olivier Elemento</a>, and my PhD at <a href="https://cemm.at">CeMM</a> in the lab of <a href="https://www.bocklab.org/">Christoph Bock</a>, where I developed computational methods to study the spatial organization of tissue and to analyze high-dimensional patient data for disease monitoring and therapy.
        </p>
        <div class="blog-main" id="research">
        <h4>Research highlights</h4>
        <ul>
            <li>
                <a rel="datacite:doi" href="https://dx.doi.org/10.1038/s41591-026-04566-5">
                Abila, Buljan, Zheng, <i>et al</i>, Nature Medicine, 2026</a>
            </li>
            <li>
                <a rel="datacite:doi" href="http://dx.doi.org/10.1038/s41592-026-03044-7">
                Zheng, <i>et al</i>, Nature Methods, 2026</a>
            </li>
            <li>
                <a rel="datacite:doi" href="http://dx.doi.org/10.1101/2025.10.13.682110">
                Buljan, <i>et al</i>, BioRxiv, 2025</a>
            </li>
            <li>
                <a rel="datacite:doi" href="https://dx.doi.org/10.1038/s41592-022-01657-2">
                Kim, <i>et al</i>, Nature Methods, 2022</a>
            </li>
        </ul>
        </div>
</div>
</div>

<hr>

{% include publications.html %}
