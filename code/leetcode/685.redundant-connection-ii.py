#
# @lc app=leetcode.cn id=685 lang=python3
# @lcpr version=30204
#
# [685] 冗余连接 II
#
# https://leetcode.cn/problems/redundant-connection-ii/description/
#
# algorithms
# Hard (42.23%)
# Likes:    412
# Dislikes: 0
# Total Accepted:    37.7K
# Total Submissions: 89.1K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 在本问题中，有根树指满足以下条件的 有向
# 图。该树只有一个根节点，所有其他节点都是该根节点的后继。该树除了根节点之外的每一个节点都有且只有一个父节点，而根节点没有父节点。
# 
# 输入一个有向图，该图由一个有着 n 个节点（节点值不重复，从 1 到 n）的树及一条附加的有向边构成。附加的边包含在 1 到 n
# 中的两个不同顶点间，这条附加的边不属于树中已存在的边。
# 
# 结果图是一个以边组成的二维数组 edges 。 每个元素是一对 [ui, vi]，用以表示 有向 图中连接顶点 ui 和顶点 vi 的边，其中 ui 是
# vi 的一个父节点。
# 
# 返回一条能删除的边，使得剩下的图是有 n 个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。
# 
# 
# 
# 示例 1：
# 
# 输入：edges = [[1,2],[1,3],[2,3]]
# 输出：[2,3]
# 
# 
# 示例 2：
# 
# 输入：edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
# 输出：[4,1]
# 
# 
# 
# 
# 提示：
# 
# 
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ui, vi <= n
# 
# 
#


# @lcpr-template-start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
from typing import *
# @lcpr-template-end
# @lc code=start
class UF:
    def __init__(self,n):
        self.pa = list(range(n))
        self.size = [1] * n
        self.cnt = n-1 #连通分量数目

    def find(self,x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self,x,y):
        px,py = self.find(x),self.find(y)
        if px != py:
            self.pa[px] = py
            self.size[py] += self.size[px]
            self.cnt -= 1
            return True
        return False

    def same(self,x,y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self.size[self.find(x)]

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        def valid(x,y):
            uf = UF(n+1)
            for ex,ey in edges:
                if ex!=x or ey !=y:
                    uf.union(ex,ey)
            return uf.cnt == 1

        ind = defaultdict(int)
        for x,y in edges:
            ind[y] += 1
            if ind[y] == 2:
                if valid(x,y):
                    return [x,y]
                else:
                    for ex,ey in edges:
                        if ey==y:
                            return [ex,ey]

        uf = UF(n+1)
        for x,y in edges:
            if not uf.union(x,y):
                return [x,y]
# @lc code=end



#
# @lcpr case=start
# [[1,2],[1,3],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,3],[3,4],[4,1],[1,5]]\n
# @lcpr case=end

#

