# 换根dp

换根时，改变的是两个节点的父子关系，其他节点的父子关系没有改变。

## [834\. 树中距离之和](https://leetcode.cn/problems/sum-of-distances-in-tree/)

## [310.最小高度树](https://leetcode.cn/problems/minimum-height-trees/description/)
换根的同时，维护父节点的子树的最大和次大高度。
叶子节点的子树最大高度是-1，因为没有子树。只有一个叶子节点的节点的子树最大高度是0。
用dfs1,dfs2命名两次dfs不容易搞错。

