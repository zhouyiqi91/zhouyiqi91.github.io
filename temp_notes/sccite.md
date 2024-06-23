我正在用nextflow重写celescope中的citeseq流程，使得流程更user friendly，并产生更为详细的文档。预计明天可以完成。

I'm rewriting the citeseq pipeline in celescope using nextflow to make the pipeline more user friendly and generate more detailed documentation. Expected to be finished tomorrow.

抗体染色实验中的蛋白质聚集体可能导致少数cell barcode的 UMI 计数显著升高。为了解决这个问题，tag_barcode步骤进行了过滤：

将任何antibody UMI计数超过max(10000, total antibody UMI * 0.01)的UMI计数去除


Protein aggregates in antibody staining experiments may cause a significant increase in the UMI counts of a few cell barcodes. To address this issue, the tag_barcode step performs the following filtering:

Remove any antibody counts that exceed max(10000, total antibody UMI * 0.01)