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

## use pip install inside docker
```
def is_docker = workflow.profile.tokenize(',').intersect(['docker', 'singularity']).size() >= 1
def pip_mirror = params.pip_mirror ? "-i ${params.pip_mirror}" : ''
def pip_install = is_docker ? "pip install --timeout 100 $pip_mirror snapatac2==2.5.3 --user" : ''
```

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


## docker DEPRECATION NOTICE

```
Command error:
  Unable to find image 'quay.io/biocontainers/bwa:0.7.17--hed695b0_7' locally
  0.7.17--hed695b0_7: Pulling from biocontainers/bwa
  docker: [DEPRECATION NOTICE] Docker Image Format v1 and Docker Image manifest version 2, schema 1 support is disabled by default and will be removed in an upcoming release. Suggest the author of quay.io/biocontainers/bwa:0.7.17--hed695b0_7 to upgrade the image to the OCI Format or Docker Image manifest v2, schema 2. More information at https://docs.docker.com/go/deprecated-image-specs/.
  See 'docker run --help'.
```

解决：使用0.7.17--he4a0461_11


## docker: failed to register layer: lsetxattr user.overlay.impure /etc: operation not supported.

在pull quay.io/singleron-rd/multiqc_sgr:1.21.3时报错。docker 26.0.1升级到26.1.2无法解决。

[https://github.com/MultiQC/MultiQC/issues/2283](Pulling latest version of MultiQC image on GitPod fails)

##  .command.sh: line 3: multiqc: command not found

解决：conda环境没有正确安装。移除错误的conda环境。

## `there may be a syntax error in the body`

<https://training.nextflow.io/troubleshoot/04_exercise/>

可能原因：少加双引号，逗号,括号

path没有加括号
```
- cause: Unexpected input: '{' @ line 146, column 18.
   process STARSOLO {

tuple val(meta), path "*.Solo.out/GeneFull_Ex50pAS/Summary.csv" , emit: summary
```

## 跳过某个process，例如freebayes

有一个input channel为空，例如
```
    FREEBAYES (
        ch_bam,
        [ [], params.fasta ], 
        SAMTOOLS_FAIDX.out.fai,
        ch_bam.map { it -> [[id:'fake'],[]] },
        ch_bam.map { it -> [[id:'fake'],[]] },
        ch_bam.map { it -> [[id:'fake'],[]] },
    )
```
如果把第二个参数换成`SAMTOOLS_FAIDX.out.fa`,由于`SAMTOOLS_FAIDX.out.fa`是optional output，为空，所以会跳过FREEBAYES

## docker ENV

home目录不可写
```
containerOptions '--env HOME=/tmp'
```

## numba with docker 
```
RuntimeError: cannot cache function 'rdist': no locator available for file '/usr/local/lib/python3.9/site-packages/umap/layouts.py'
```

<https://github.com/numba/numba/issues/4032>
<https://github.com/numba/numba/issues/4908>

## name collision 同一个样本有不同目录下同名的fastq

<https://stackoverflow.com/questions/73660749/nextflow-name-collision>

`tuple val(meta), path(reads, stageAs: "?/*")`


```
├── 1
│   └── R240115003_R1.fastq.gz -> /SGRNJ07/Standard_Analysis/DATA05/limsdownload/24_01/2024_01_18/RD22110301/A0111_6_PBMC_02lysis_WX_D02SDS_T7_EDTA5030/2024-01-18-54/R240115003_R1.fastq.gz
├── 2
│   └── R240115003_R2.fastq.gz -> /SGRNJ07/Standard_Analysis/DATA05/limsdownload/24_01/2024_01_18/RD22110301/A0111_6_PBMC_02lysis_WX_D02SDS_T7_EDTA5030/2024-01-18-54/R240115003_R2.fastq.gz
├── 3
│   └── R240115003_R3.fastq.gz -> /SGRNJ07/Standard_Analysis/DATA05/limsdownload/24_01/2024_01_18/RD22110301/A0111_6_PBMC_02lysis_WX_D02SDS_T7_EDTA5030/2024-01-18-54/R240115003_R3.fastq.gz
├── 4
│   └── R240115003_R1.fastq.gz -> /SGRNJ07/Standard_Analysis/DATA05/limsdownload/24_02/2024_02_06/RD22110301/A0111_6_PBMC_02lysis_WX_D02SDS_T7_EDTA5030/2024-02-06-1/R240115003_R1.fastq.gz
├── 5
│   └── R240115003_R2.fastq.gz -> /SGRNJ07/Standard_Analysis/DATA05/limsdownload/24_02/2024_02_06/RD22110301/A0111_6_PBMC_02lysis_WX_D02SDS_T7_EDTA5030/2024-02-06-1/R240115003_R2.fastq.gz
├── 6
│   └── R240115003_R3.fastq.gz -> /SGRNJ07/Standard_Analysis/DATA05/limsdownload/24_02/2024_02_06/RD22110301/A0111_6_PBMC_02lysis_WX_D02SDS_T7_EDTA5030/2024-02-06-1/R240115003_R3.fastq.gz

```
