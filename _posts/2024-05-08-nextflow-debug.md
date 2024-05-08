---
layout: post
mathjax: true
title: "nextflow使用中的问题记录"
description: ""
category: "生信"
tags: ["nextflow"]
---
{% include JB/setup %}

## xopen: no content

wf-single-cell报错
```
Caused by:
  Process `pipeline:process_bams:combine_bams_and_tags (1)` terminated with an error exit status (255)

Command executed:

  samtools merge -@ 3 --write-index -o "20221013-NPL4536-P4-PAM81839-sup.tagged.sorted.bam##idx##20221013-NPL4536-P4-PAM81839-sup.tagged.sorted.bam.bai" bams/*.bam

  mkdir chr_tags
  # merge the tags TSVs, keep header from first
  csvtk concat -tT tags/*         | csvtk split -tl -f chr -o chr_tags/
  # Strip appended source filename ("stdin-"") from the split TSVs
  for file in chr_tags/*; do mv "${file}" "${file//stdin-//}"; done

Command exit status:
  255

Command output:
  (empty)

Command error:
  [ERRO] xopen: no content
```

[csvtk](https://github.com/shenwei356/csvtk)运行这个数据时需要>50G RAM, 但只给了8G: <https://github.com/singleron-RD/wf-single-cell/commit/f59c3df733e845970f4d3bfa4583a97328516325>

去掉RAM限制就可以了。