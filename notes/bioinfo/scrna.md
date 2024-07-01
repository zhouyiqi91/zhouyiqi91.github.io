## GEXSCOPE-V3
/SGRNJ07/Standard_Analysis/DATA05/limsdownload/24_06/2024_06_04/RD21010601/SN216243_1_0531/2024-06-04-6/R240531029_combined_R1.fastq.gz
/SGRNJ07/Standard_Analysis/DATA05/limsdownload/24_06/2024_06_04/RD21010601/SN216246_1_0531/2024-06-04-7/R240531030_combined_R1.fastq.gz


celescope v1和v2的cell calling算法基本是一样的，除了EmptyDrops_CR的FDR参数，v1是默认的0.01,v2是0.001
但是v2定量使用了starsolo的定量算法代替了featureCounts, 在包含intron时的表现更好。
CHANGELOG在这里：
https://github.com/singleron-RD/CeleScope/blob/master/doc/CHANGELOG.md

至于分析数据，可以给一些常见的分析需求吗？

|sample|knee filtering|emptydrops|
|--|--|--|
|pbmc1|17255|23793|
|pbmc2|15845|21428|

