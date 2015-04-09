---
layout: post
title: "Using Google cloud computing"
description: ""
category: research
tags: [gce, gcs]
---
{% include JB/setup %}



Unrestricted choice of zones.


# Instances
Google's "free tier" is better than Amazons's on the choice of machines

# Images
Pretty much similar to AWS EC2

# Tools
    
`gcloud` : manage services, instances, configurations, permissions
`gsutil` : manage cloud storage (upload, download to and from local)

# Uploading to gcs
Upload in parallel to Google cloud storage:

    ls /localdir/data/mapped | grep .dups.bam | \  # grep samples
    grep -v _string_ | \  # exclude some samples based on some string
    gsutil -m cp -I gs://storagedir/data/mapped/  # upload

Auto-resumable uploads, pretty fast.

Uploaded ~250 bam files (1-5 Gb each) overnight!
