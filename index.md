---
layout: page
title: Homepage
---
{% include JB/setup %}

### Links
This is a folk of Li Heng's blog now.
[GitHub][github]

### Posts [![](images/feed-icon-14x14.png)](rss.xml)

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>


[github]: https://github.com/zhouyiqi91

