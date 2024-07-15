<https://bioinformatics.ccr.cancer.gov/docs/getting-started-with-scrna-seq/Seurat_QC_to_Clustering/>

```
ggplot(metadata, aes(x=nFeature_RNA,fill=orig.ident)) +
   geom_density(alpha = 0.2) + 
    theme_classic() +
    scale_x_log10() + 
    geom_vline(xintercept = 350,color="red",linetype="dotted")
```