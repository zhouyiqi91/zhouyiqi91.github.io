---
layout: post
mathjax: true
description: ""
category: "生信"
tags: ["软件"]

---
{% include JB/setup %}

一个NPM1基因W288位置[4bp的插入突变](https://bioinfo.uth.edu/TSGene/gene_mutation.cgi?gene=4869)无法检出。

```
bcftools mpileup \
 -f /SGRNJ06/randd/public/genome/rna/celescope_v2/hs/Homo_sapiens.GRCh38.dna.primary_assembly.fa \
 --threads 10 \
 --annotate DP,AD -d 100000000 \
 -o .//BL22680_FJ/07.variant_calling/BL22680_FJ_raw.bcf \
 .//BL22680_FJ/07.variant_calling/BL22680_FJ_splitN.bam

bcftools call -mv -Ov -o .//BL22680_FJ/07.variant_calling/BL22680_FJ_raw.vcf .//BL22680_FJ/07.variant_calling/BL22680_FJ_raw.bcf

bcftools norm -m- -f /SGRNJ06/randd/public/genome/rna/celescope_v2/hs/Homo_sapiens.GRCh38.dna.primary_assembly.fa .//BL22680_FJ/07.variant_calling/BL22680_FJ_raw.vcf | bcftools norm -d both -o .//BL22680_FJ/07.variant_calling/BL22680_FJ_norm.vcf
```
但是将BAM downsample到1/20却可以检出。

- https://samtools.github.io/bcftools/bcftools.html#mpileup
- [bcftools call ignores deletion with high coverage](https://github.com/samtools/bcftools/issues/1459)
- [samtools mpileup gives inconsistent results with different depth limits](https://github.com/samtools/samtools/issues/619)
- [bcftools norm](https://github.com/samtools/bcftools/issues/1114)