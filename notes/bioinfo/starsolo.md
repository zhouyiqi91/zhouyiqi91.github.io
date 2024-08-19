## [Mapping with STARsolo and BD Rhapsody Enhanced Beads](https://github.com/alexdobin/STAR/issues/1607#top)#1607

## [Help interpreting how STARSolo handles expression of a single read](https://github.com/alexdobin/STAR/issues/2022#top)#2022

## methods

Sequencing reads were processed using singleron-RD/scrna v1.1.0(https://github.com/singleron-RD/scrna), utilising reproducible software environments from the Bioconda (Grüning et al., 2018) and Biocontainers (da Veiga Leprevost et al., 2017) projects. Briefly, STARsolo (v.2.7.11b) were used with default parameters, except that the FDR in the --emptypdrops_CR parameter was changed from the default 0.01 to 0.001.

## featureCounts

```
I       sgd     gene    71786   73288   .       +       .       gene_id "YAL038W"; gene_name "CDC19"; gene_source "sgd"; gene_biotype "protein_coding";
I       sgd     transcript      71786   73288   .       +       .       gene_id "YAL038W"; transcript_id "YAL038W_mRNA"; gene_name "CDC19"; gene_source "sgd"; gene_biotype "protein_coding"; transcript_name "CDC19"; transcript_source "sgd"; transcript_biotype "protein_coding";
I       sgd     exon    71786   73288   .       +       .       gene_id "YAL038W"; transcript_id "YAL038W_mRNA"; exon_number "1"; gene_name "CDC19"; gene_source "sgd"; gene_biotype "protein_coding"; transcript_name "CDC19"; transcript_source "sgd"; transcript_biotype "protein_coding"; exon_id "YAL038W_mRNA-E1";
I       sgd     CDS     71786   73285   .       +       0       gene_id "YAL038W"; transcript_id "YAL038W_mRNA"; exon_number "1"; gene_name "CDC19"; gene_source "sgd"; gene_biotype "protein_coding"; transcript_name "CDC19"; transcript_source "sgd"; transcript_biotype "protein_coding"; protein_id "YAL038W";
I       sgd     start_codon     71786   71788   .       +       0       gene_id "YAL038W"; transcript_id "YAL038W_mRNA"; exon_number "1"; gene_name "CDC19"; gene_source "sgd"; gene_biotype "protein_coding"; transcript_name "CDC19"; transcript_source "sgd"; transcript_biotype "protein_coding";
I       sgd     stop_codon      73286   73288   .       +       0       gene_id "YAL038W"; transcript_id "YAL038W_mRNA"; exon_number "1"; gene_name "CDC19"; gene_source "sgd"; gene_biotype "protein_coding"; transcript_name "CDC19"; transcript_source "sgd"; transcript_biotype "protein_coding";
```