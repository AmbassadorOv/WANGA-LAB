---
layout: default
title: Research Index
---

# Copernicus Research Index

The archive currently defines 100 initial article nodes. Each node is a versioned Markdown document and can later expand into subarticles, evidence records, datasets, and verified references.

{% for post in site.posts %}- [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}