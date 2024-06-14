我这里有之前跑的mean coverage 23.5X的小鼠骨髓和四个1X的CCRF细胞系的测序结果。统计At least 1X genome coverage，小鼠骨髓78%，四个1X的CCRF的在15%-20%

向下downsample统计coverage没问题，向上预测我没有找到好的方法来做。

方博，QIAGEN这里算uniformity数据是一个panel：QIAseq Targeted DNA Human Comprehensive Cancer Panel (DHS-3501Z) covering 275 genes (837 kb)，覆盖度很高. 我们的数据是全基因组，应当是有所不同？

以我们mean read depth 23.5X的小鼠骨髓数据为例，% of bases >= 5% of mean read depth是72.22%，% of bases >= 30% of mean read depth是53.21%