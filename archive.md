---
layout: page
title : Archive
header : Post Archive
group: navigation
---
{% include JB/setup %}

<h3>Posts by date:</h3>
{% assign posts_collate = site.posts %}
{% include JB/posts_collate %}

<br>

<p align="right"><a href={{site.url}}"/diary.html">Diary entries</a></p>
