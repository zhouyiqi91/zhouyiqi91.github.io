一开始accuraSCOPE的3' 和5'的reads都有UMI，所以我设计了https://github.com/singleron-RD/accurascoperna流程来分析。

最近，实验的同事告诉我，他们发现如果5'端设计了UMI，cDNA得率会降低，所以他们放弃了在5'端设计UMI，这使得双端定量转录本无法进行。我决定修改nf-core/rnaseq流程，采用每个细胞/孔类似于bulk，且没有UMI的方式来进行分析。
https://github.com/singleron-RD/rnaseq/blob/main/assets/protocols.json
https://github.com/singleron-RD/rnaseq

如果有更好的想法和分析内容，欢迎与我交流。