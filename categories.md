---
layout: page
title: Categories
header: Posts By Category
group: navigation
---
{% include JB/setup %}

<h3>All categories:</h3>
<ul class="tags list-inline list-unstyled">
	{% assign categories_list = site.categories %}
	{% include JB/categories_list %}
</ul>

<h3>Posts per category:</h3>
{% for category in site.categories %}
{% if category[0] != "diary" %}
<h4 id="{{ category[0] }}-ref">{{ category[0] | join: "/" }}</h4>
<ul>
{% assign pages_list = category[1] %}
{% for node in pages_list %}
{% if node.title != null %}
{% if group == null or group == node.group %}
<li>
{{ node.date | date: "%D" }}
<i><a href="{{ BASE_PATH }}{{node.url}}">{{node.title}}</a></i>
</li>
{% endif %}
{% endif %}
{% endfor %}
</ul>
{% endif %}
{% endfor %}

