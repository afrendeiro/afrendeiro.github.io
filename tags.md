---
layout: page
title: Tags
header: Posts By Tag
group: navigation
---
{% include JB/setup %}

<h3>All tags:</h3>
<ul class="tags list-inline list-unstyled">
{% assign tags_list = site.tags %}  
{% include JB/tags_list %}
</ul>

<h3>Posts per tag:</h3>
{% for tag in site.tags %} 
{% if tag[0] != "diary" %}
<h4 id="{{ tag[0] }}-ref">{{ tag[0] }}</h4>
<ul>
{% assign pages_list = tag[1] %}  
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
