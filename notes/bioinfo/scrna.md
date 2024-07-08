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

|sample|knee filtering|emptydrops|
|--|--|--|
|pbmc1|17255|23793|

|sample-cellcalling|cell number|
|--|--|
pbmc1 knee|17255
pbmc1 emptydrops UMI min 500|23793
pbmc1 0.1 subsample knee|17427
pbmc1 0.1 subsample emptydrops UMI min 500|17868
pbmc1 0.1 subsample emptydrops UMI min 200|18924

We have a good data of mouse bone marrow. Attached is the QC report.
fastq R1 and R2, ~16GB each. The download link will expire in 10 days.

https://singleronbio-opendata.oss-cn-hangzhou.aliyuncs.com/web-data/RNA/Mouse_marrow_1/fastq/R220218069_R1.fastq.gz?OSSAccessKeyId=LTAI5t5fUiqw2ZzNrH8kvKcm&Expires=1721035464&Signature=JaN1cwTVx%2F8NIxTPPomZGYpN9Y8%3D
https://singleronbio-opendata.oss-cn-hangzhou.aliyuncs.com/web-data/RNA/Mouse_marrow_1/fastq/R220218069_R2.fastq.gz?OSSAccessKeyId=LTAI5t5fUiqw2ZzNrH8kvKcm&Expires=1721035529&Signature=gm2l02ZF5zTwQYlYW2TnMtwMwJ0%3D


另外，我下载了Genentech预印本中的数据进行了分析。附件是两种不同cell-calling算法的结果。
这里有两种算法的简要描述：
https://github.com/alexdobin/STAR/blob/master/docs/STARsolo.md#cell-filtering-calling

看起来结果并不是特别差。

预印本中提到的一个问题：
The results for Singleron were particularly concerning given the linear correlation (mean Pearson r = 0.998) between observed cell count yield and sequencing depth across the downsampling range.

使用emptydrops算法时，因为算法的特性，细胞数确实会随着测序深度提高而提高。使用knee filtering，则细胞数会稳定不变。(knee_0.1是pbmc1 subsample 10% reads的结果)

希望这有用。