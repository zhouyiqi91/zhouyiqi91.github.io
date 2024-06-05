---
layout: post
mathjax: true
description: ""
category: "生信"
tags: ["nextflow"]
---
{% include JB/setup %}

## why nextflow

[Two years with Nextflow](https://labs.epi2me.io/two-years-of-nextflow/#discussion)

## tutorial

- <https://www.nextflow.io/docs/latest/index.html>
- <https://sateeshperi.github.io/nextflow_varcal/nextflow/>

## retry

[maxErrors](https://www.nextflow.io/docs/latest/process.html#maxerrors)

## multiple publishDir

<https://github.com/nextflow-io/nextflow/issues/256>
<https://github.com/nf-core/rnaseq/blob/a10f41afa204538d5dcc89a5910c299d68f94f41/conf/modules.config#L221-L238>

## 多个不同process的输入文件

mix不可以，需要用concat。concat是有序的，[meta,reads,protocol_cmd]
```
ch_input = ch_samplesheet.concat(PROTOCOL_CMD.out.starsolo_cmd)
            .groupTuple()
            .map {
                it -> [it[0], it[1][0], it[1][1].text]
            }
```

## sample sheet多加一列

```
ERROR ~ Invalid method invocation `call` with arguments: [[id:sampleX], /SGRNJ06/randd/USER/zhouyiqi/2024/repo/scsnp_test_data/NPM1/sampleX_001_R1.fq.gz, /SGRNJ06/randd/USER/zhouyiqi/2024/repo/scsnp_test_data/NPM1/sampleX_001_R2.fq.gz] (java.util.ArrayList) on _closure5 type
```

修改
- `schema_input.json`
- 包含`fromSamplesheet`的文件
- 包含`validateInputSamplesheet`的文件

## optional input value
```
FILTER_BAM (
    ch_filter_bam,
    { params.genes ? params.genes : "" },
    { params.panel ? params.panel : "" },
)

def genes_args = genes ? "--genes $genes": ""
def panel_args = panel ? "--panel $panel": ""
```

## multi-tool container / mulled
<https://github.com/BioContainers/multi-package-containers?tab=readme-ov-file>

## schema builder
<https://nf-co.re/pipeline_schema_builder>

