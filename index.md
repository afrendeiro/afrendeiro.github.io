---
layout: page
title : "André Rendeiro"
description: "My personal website"
---
{% include JB/setup %}

<div class="row">
    <div class="col-sm-8 blog-main" typeof="foaf:Person" about="http://andre-rendeiro.com/about" prefix="schema: http://schema.org/Person#">
        <img src="me.jpeg" style="width:210px; height:210px; margin: 0px 10px; float:left" alt="It's me!">
        <p>
            I'm a <span property="schema:jobTitle">PhD student</span> at <a rel="schema:affiliation" href="http://www.cemm.oeaw.ac.at/">CeMM</a> in the lab of <a rel="foaf:knows" href="http://medical-epigenomics.org/">Christoph Bock</a>.
        </p>
        <p>
            I apply computational methods to high-dimentional molecular biology datasets in an attempt to infer high-level patient trajectories through clinical landscapes.
        </p>
        <p>
            This could one day be used to monitor disease progression and risk stratification of patients.
        </p>
        <!--<p>
            Of particular relevance is my group's usage of methods to profile <a href="http://en.wikipedia.org/wiki/Epigenetics">epigenetic</a> states in both development and disease.
        </p> -->
        <p>
            I like to develop computational methodologies driven by a need to solve a new problem.
            I develop and sometimes contribute to open source software.
            <br>
            Check out my <a href="https://github.com/afrendeiro">GitHub profile</a> to see my tools and project contributions.
        </p>
    </div>
    <div class="col-sm-3 col-sm-offset-1 blog-sidebar">
        <dl>
            <dt>Address:</dt>
                <dd>
                    <span property="schema:address" typeof="http://schema.org/PostalAddress" vocab="http://schema.org/PostalAddress/">
                        <span property="streetAddress">
                            <a href="http://www.cemm.oeaw.ac.at/">CeMM Research Center for Molecular Medicine of the Austrian Academy of Sciences </a>
                        </span>, 
                        <a href="https://www.google.at/maps/place/CeMM+-+Forschungszentrum+für+Molekulare+Medizin+GmbH./@48.2194743,16.3496347,18z/">
                            <span property="postalCode">1090</span>
                            <span property="addressLocality">Vienna</span>, 
                            <span property="addressCountry">Austria</span>
                        </a>
                    </span>
                </dd>
            <br>
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
<!--             <dt>ZeroNet ID:</dt>
                <dd>
                    <a href="http://127.0.0.1:43110/Me.ZeroNetwork.bit/?Profile/1RedkCkVaXuVXrqCMpoXQS29bwaqsuFdL/16XR1GVbekHSMMoUZ5pTQWFpq2anbkHgrC/arendeiro@zeroid.bit" title="Email me on ZeroNet">arendeiro@zeroid.bit</a>
                </dd> -->
            <dt>My Keybase identity:</dt>
                <dd>
                    <a href="https://keybase.io/afrendeiro" title="Me on Keybase">keybase.io/afrendeiro</a>
                </dd>
        </dl>
    </div>
</div>
