---
layout: post
mathjax: true
title: ""
description: ""
category: "生信"
tags: ["debug"]
---
{% include JB/setup %}

## pysam `bgzf.c:38:10: fatal error: zlib.h: No such file or directory`

还是同样的报错：`sudo yum install zlib-devel`
<https://stackoverflow.com/questions/36372756/missing-libz-library-on-redhat-install>

解决：`mamba install -y bioconda::pysam`