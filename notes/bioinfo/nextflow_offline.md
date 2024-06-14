1. nextflow
解压后有nextflow binary和隐藏目录.nextflow
```
tar -zcvf nextflow_offline.tar.gz
$ ls -a nextflow_offline
.  ..  nextflow  .nextflow
```
将.nextflow目录移动到`$HOME`；
nextflow binary加入`$PATH`, 方便调用

2. 安装依赖软件
   
|Software|	Version|
|--|--|
|pyfastx|	2.1.0|
|star|	2.7.11b0|

