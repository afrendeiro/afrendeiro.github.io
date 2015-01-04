---
layout: page
title : Diary
header : Post Archive
group:
---
{% include JB/setup %}

<h3>Posts by date:</h3>
{% assign diary_collate = site.posts %}
{% include JB/diary_collate %}
