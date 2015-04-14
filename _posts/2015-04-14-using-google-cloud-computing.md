---
layout: post
title: "Using Google cloud computing"
description: ""
category: research
tags: [gce, gcs]
---
{% include JB/setup %}


I recently started using cloud computing services.

Amazon seems to be the preferred provider of cloud services and they do rightly so: their breath of services and their customization is currently unparalleled. Although I had experimented with some Amazon Web Services (AWS) before (*e.g.* S3 storage), I had never used it for computing.

Unfortunately, Amazon has quite restrictive limits for new users (while you can't get out of the Free Tier):

- limit of two usage zones (this wouldn't be a problem, weren't it for:)
- all possible zones to choose from are in the US
- really weak VMs available

I contacted service to change my zones and have my permissions raised and start real work, willing to pay the costs, but the issue took 3 days to be responded with basically "though luck" as reply and [this seems like a general pattern](https://forums.aws.amazon.com/thread.jspa?threadID=175448).

So I figured other providers might give better conditions to starting users due to their smaller market share. So it was with [Google Cloud Compute](https://cloud.google.com/compute/).

Features:

- credit of 300$ to spend over 60 days - *very* attractive;
- unrestricted choice of zones;
- more choice of VMs for starting users;
- simpler interface (also less features);
- competitive prices per hour and Gb storage compared with AWS.

Computing and storage aren't as separated as in AWS. The computing service is called Google Cloud Engine - similar to AWS' EC2. Long-term storage is called Google Storage and is equivalent to AWS' S3. Disks can be mounted on instances in a way equivalent to AWS' EBS storage.

Following is a series of notes on how to interface with GCE and GCS, written mostly for the future me.

## Instances

#### Mounting new disks in instances:

    df -h  # see mounted volumes
    sudo mkdir /projects
    sudo chown user:user /projects
    sudo /usr/share/google/safe_format_and_mount -m "mkfs.ext4 -F" /dev/sdb /projects

Set to mount at startup - add:

    /dev/sdaX /media/mydata ext4 defaults 0 0

to /etc/fstab

#### Sftp
You can give an external IP to your instances and transfer files easily.

You can use Filezilla by adding your instance key (`Edit -> Preferences -> SFTP -> Add key...`) and using `sftp://<user>@<externalIP>`.

## Images
Pretty much similar to AWS EC2: create a new instance, [install all your software](http://andre-rendeiro.me/2015/04/08/bioinfo_fresh_install_ubuntu/) and save an image of the instance. Next time start a new instance with this image and *voilá* all your software is there.

Unfortunately, I haven't found a way of sharing images :disappointed:.

## Tools

+ `gcloud` : manage services, instances, configurations, permissions
+ `gsutil` : manage cloud storage (upload, download to and from local)

### Uploading to gcs
Upload in parallel to Google cloud storage:

    pip install crc...
    configure .boto

    # with Rsync
    gsutil -m rsync -r . gs://storage/data/

    # selectively using grep
    ls /localdir/data/mapped | grep .dups.bam | \  # grep samples
    grep -v _string_ | \  # exclude some samples based on some string
    gsutil -m cp -I gs://storagedir/data/mapped/  # upload


#### Change permissions
*e.g.* upload bigwig tracks and hub, make them publicly accessible

    gsutil -m rsync data/bigWig gs://storage/bigWig/
    gsutil cp trackHub_hg19.txt gs://storage/bigWig/
    gsutil -m acl ch -g All:R gs://storage/bigWig/*

Auto-resumable uploads, pretty fast.

Uploaded ~250 bam files (1-5 Gb each) overnight!
