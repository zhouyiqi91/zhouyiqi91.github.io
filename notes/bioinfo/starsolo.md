## [Mapping with STARsolo and BD Rhapsody Enhanced Beads](https://github.com/alexdobin/STAR/issues/1607#top)#1607

## [Help interpreting how STARSolo handles expression of a single read](https://github.com/alexdobin/STAR/issues/2022#top)#2022

## methods

Sequencing reads were processed using singleron-RD/scrna v1.1.0(https://github.com/singleron-RD/scrna), utilising reproducible software environments from the Bioconda (Grüning et al., 2018) and Biocontainers (da Veiga Leprevost et al., 2017) projects. Briefly, STARsolo (v.2.7.11b) were used with default parameters, except that the FDR in the --emptypdrops_CR parameter was changed from the default 0.01 to 0.001.

## featureCounts

Starsolo在人和小鼠样本的表现都是perfect。但是，最近在一个Saccharomyces_cerevisiae样本上的表现却很奇怪。我发现assign到feature的reads偏低：
而使用featureCounts在starsolo输出的同一个BAM上进行定量却可以得到高的多的assign reads


Starsolo performs perfectly on human and mouse samples. However, it performs strangely on a Saccharomyces_cerevisiae sample. I found that the number of reads assigned to features is low:

*.Solo.out/GeneFull_Ex50pAS/Features.stats
```
                                        noUnmapped        1511309
                                       noNoFeature       18090383
                                      MultiFeature        6065952
                       subMultiFeatureMultiGenomic        6015439
                                noTooManyWLmatches              0
                              noMMtoWLwithoutExact              0
                                        yesWLmatch       24094716
                                yessubWLmatchExact       21910936
                       yessubWLmatch_UniqueFeature       24094716
                                   yesCellBarcodes         823115
                                           yesUMIs       23008164
```

However, using featureCounts to quantify the same BAM output by Starsolo can yield much higher assigned reads.
```
Assigned        39880594
Unassigned_Unmapped     0
Unassigned_Read_Type    0
Unassigned_Singleton    0
Unassigned_MappingQuality       0
Unassigned_Chimera      0
Unassigned_FragmentLength       0
Unassigned_Duplicate    0
Unassigned_MultiMapping 15937496
Unassigned_Secondary    0
Unassigned_NonSplit     0
Unassigned_NoFeatures   3967801
Unassigned_Overlapping_Length   0
Unassigned_Ambiguity    551624
```

This is an example of a read that is assigned to YAL038W (XT tag) in featureCounts, but cannot be assigned to the gene in starsolo:
```
E200025550L1C040R03704342097    0       I       73159   255     150M    *       0       0       CCGTATCAACTTCGGTATTGAAAAGGCTAAGGAATTCGGTATCTTGAAGAAGGGTGACACTTACGTTTCCATCCAAGGTTTCAAGGCCGGTGCTGGTCACTCCAACACTTTGCAAGTCTCTACCGTTTAAAAAAAGAATCATGATTGAAT ?@E<DA;D<>DF@B#@AEEA2>E.7D,CDB<<@A>AB>2@EBDACA<DD4FB@BDD,<@DDB?9CADD:AB?ABAA;>FCBA@B99<E<+;;>EE%A@?DEDFAEAAEDFFB;?CDD?FEB=EAFDBDF>>FED95E;EFEEFAEFFBD? NH:i:1  HI:i:1  nM:i:0  AS:i:148        CR:Z:AGACGTTCA_ATGCCTAAG_AGATCTCGT    UR:Z:TCGCTCTCTCGA        GX:Z:-  GN:Z:-  sF:B:i,7,0      CB:Z:AGACGTTCA_ATGCCTAAG_AGATCTCGT      UB:Z:TCGCTCTCTCGA       XS:Z:Assigned   XN:i:1  XT:Z:YAL038W
```

A nearby read can be correctly assigned by both featureCounts and starsolo
```
E200025550L1C029R01701620491    0       I       73142   255     145M5S  *       0       0       ACTGATGATGTTGAAGCCCGTATCAACTTCGGTATTGAAAAGGCTAAGGAATTCGGTATCTTGAAGAAGGGTGACACTTACGTTTCCATCCAAGGTTTCAAGGCCGGTGCTGGTCACTCCAACACTTTGCAAGTCTCTACCGTTTAAAAA FFFFFFFFFFFFFCEFFFFFFFFFFFFFFF@FFFFFFFFFFFEFFFFFFDFFFFCFFFFFFFFFDDFFFFFFFFFFFFFFFFFFFFFFFFFFFFBFFFFFFF@FFFFFFFFFFFFFFFFGFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF NH:i:1  HI:i:1  nM:i:0  AS:i:143        CR:Z:ACACACCAA_CAATGCAAC_CTCTAACAC    UR:Z:TTATGTGCACGG        GX:Z:YAL038W    GN:Z:CDC19      sF:B:i,1,1      CB:Z:ACACACCAA_CAATGCAAC_CTCTAACAC      UB:Z:TTATGTGCACGG       XS:Z:Assigned   XN:i:1 XT:Z:YAL038W
```

Definition of YAL038W in gtf
```
I       sgd     gene    71786   73288   .       +       .       gene_id "YAL038W"; gene_name "CDC19"; gene_source "sgd"; gene_biotype "protein_coding";
I       sgd     transcript      71786   73288   .       +       .       gene_id "YAL038W"; transcript_id "YAL038W_mRNA"; gene_name "CDC19"; gene_source "sgd"; gene_biotype "protein_coding"; transcript_name "CDC19"; transcript_source "sgd"; transcript_biotype "protein_coding";
I       sgd     exon    71786   73288   .       +       .       gene_id "YAL038W"; transcript_id "YAL038W_mRNA"; exon_number "1"; gene_name "CDC19"; gene_source "sgd"; gene_biotype "protein_coding"; transcript_name "CDC19"; transcript_source "sgd"; transcript_biotype "protein_coding"; exon_id "YAL038W_mRNA-E1";
I       sgd     CDS     71786   73285   .       +       0       gene_id "YAL038W"; transcript_id "YAL038W_mRNA"; exon_number "1"; gene_name "CDC19"; gene_source "sgd"; gene_biotype "protein_coding"; transcript_name "CDC19"; transcript_source "sgd"; transcript_biotype "protein_coding"; protein_id "YAL038W";
I       sgd     start_codon     71786   71788   .       +       0       gene_id "YAL038W"; transcript_id "YAL038W_mRNA"; exon_number "1"; gene_name "CDC19"; gene_source "sgd"; gene_biotype "protein_coding"; transcript_name "CDC19"; transcript_source "sgd"; transcript_biotype "protein_coding";
I       sgd     stop_codon      73286   73288   .       +       0       gene_id "YAL038W"; transcript_id "YAL038W_mRNA"; exon_number "1"; gene_name "CDC19"; gene_source "sgd"; gene_biotype "protein_coding"; transcript_name "CDC19"; transcript_source "sgd"; transcript_biotype "protein_coding";
```


