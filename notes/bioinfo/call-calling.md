BD也有两个cell-calling算法: basic和refine
basic 类似于knee filtering，refine类似于emptydrops_CR；
这篇比较的文章用的BD的分析版本是2.0，刚好把default的算法从refine改成了basic


https://support.bioconductor.org/p/9145822/

我很满意我已经找到了“细胞过多”问题的根本原因， C120_batch13_1 并通过在运行 emptyDrops() 前过滤掉线粒体、核糖体蛋白、TCR 和 BCR 基因来获得补救措施


|sample cell-calling|cell number|
|--|--|
pbmc1 knee|17255
pbmc1 emptydrops UMI min 500|23793
pbmc1 0.1 subsample knee|17427
pbmc1 0.1 subsample emptydrops UMI min 500|17868
pbmc1 0.1 subsample emptydrops UMI min 200|18924
