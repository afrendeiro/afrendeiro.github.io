---
layout: page
title: Posts
description: "Post tags archive"
header: Latest posts
group: navigation
weight: 3
---
{% include JB/setup %}

<h2>Latest posts:</h2>
{% assign posts_list = site.posts %}
{% include JB/posts_list %}

