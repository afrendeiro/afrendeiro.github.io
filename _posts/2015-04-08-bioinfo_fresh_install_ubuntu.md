---
layout: post
title: "Bioinformatics software install from fresh Ubuntu image on AWS EC2"
description: ""
category: research
tags: [software, aws, ubuntu]
---
{% include JB/setup %}

I've recently started using Amazon's web services (AWS) for cloud computing (EC2 service). It takes a bit until you grasp the concepts and get familiar with the services offered. I won't write more on this since I found an [**excelent guide** to AWS and EC2](https://github.com/griffithlab/rnaseq_tutorial/wiki/Intro-to-AWS-Cloud-Computing), which I recommend going through if you're new to cloud computing in general or AWS'.

After you start your virtual machine (VM) instances you'll want to start working as fast as possible but you'll need the software you're used to for that. Fortunately you only have to install all of that once. After you've installed all you can save an image of the instance's boot disk and reuse it as many times as you want when you create new VM instances

Here's a guide to install common bioinformatics software in a fresh Ubuntu 14.04 LTS image on an AWS EC2 instance.

### Software
This will get updated, so [refer to the gist's versions](https://gist.github.com/afrendeiro/a3718d50cdb370a83f88/revisions) to see changes.

{% gist a3718d50cdb370a83f88 %}

### Static files used in bioinformatics (genomes, indexes, annotations)

{% gist 2ba0d2bb3a5710c51c0f %}
