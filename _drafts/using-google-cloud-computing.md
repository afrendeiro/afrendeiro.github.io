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

Mounting new disks in instances:

    df -h  # see mounted volumes
    sudo mkdir /projects
    sudo chown user:user /projects
    sudo /usr/share/google/safe_format_and_mount -m "mkfs.ext4 -F" /dev/sdb /projects

Set to mount at startup - add:

    /dev/sdaX /media/mydata ext4 defaults 0 0

to /etc/fstab

# Images
Pretty much similar to AWS EC2

# Tools
    
`gcloud` : manage services, instances, configurations, permissions
`gsutil` : manage cloud storage (upload, download to and from local)

# Uploading to gcs
Upload in parallel to Google cloud storage:

    pip install crc...
    configure .boto

    # with Rsync
    gsutil -m rsync -r . gs://storage-cm/data/

    # selectively using grep
    ls /localdir/data/mapped | grep .dups.bam | \  # grep samples
    grep -v _string_ | \  # exclude some samples based on some string
    gsutil -m cp -I gs://storagedir/data/mapped/  # upload

Auto-resumable uploads, pretty fast.

Uploaded ~250 bam files (1-5 Gb each) overnight!
