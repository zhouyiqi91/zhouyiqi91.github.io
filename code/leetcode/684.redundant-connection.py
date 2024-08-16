#
# @lc app=leetcode.cn id=684 lang=python3
# @lcpr version=30204
#
# [684] 冗余连接
#
# https://leetcode.cn/problems/redundant-connection/description/
#
# algorithms
# Medium (68.03%)
# Likes:    641
# Dislikes: 0
# Total Accepted:    119.9K
# Total Submissions: 176.2K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 树可以看成是一个连通且 无环 的 无向 图。
# 
# 给定往一棵 n 个节点 (节点值 1～n) 的树中添加一条边后的图。添加的边的两个顶点包含在 1 到 n
# 中间，且这条附加的边不属于树中已存在的边。图的信息记录于长度为 n 的二维数组 edges ，edges[i] = [ai, bi] 表示图中在 ai 和
# bi 之间存在一条边。
# 
# 请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。如果有多个答案，则返回数组 edges 中最后出现的那个。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入: edges = [[1,2], [1,3], [2,3]]
# 输出: [2,3]
# 
# 
# 示例 2：
# 
# 
# 
# 输入: edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
# 输出: [1,4]
# 
# 
# 
# 
# 提示:
# 
# 
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# edges 中无重复元素
# 给定的图是连通的 
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

# 可以用tarjan求出所有割边，不在割边集合中的边说明在环中，可以去掉，比较低效
class Solution1:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        n = len(g)

        cut_edges = set()
        self.time = 0
        time = [0] * (n+1)
        low = [0] * (n+1)
        def dfs(x, fa):
            self.time += 1
            time[x] = low[x] = self.time
            for y in g[x]:
                if not time[y]:
                    dfs(y,x)
                    low[x] = min(low[x], low[y])
                    if time[x] < low[y]:
                        tx,ty = x,y
                        if tx > ty: tx,ty = ty,tx
                        cut_edges.add((tx,ty))
                elif y != fa:
                    low[x] = min(low[x], time[y]) 
        dfs(1,-1)
        #print(cut_edges)
        for x,y in edges[::-1]:
            if (x,y) not in cut_edges:
                return [x,y]
        
# 高效做法 并查集
class UF:
    def __init__(self,n):
        self.pa = list(range(n))
        self.size = [1] * n
        self.cnt = n #连通分量数目

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

    def same(self,x,y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self.size[self.find(x)]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UF(n)
        for x,y in edges:
            tx,ty = x-1,y-1
            if uf.same(tx,ty):
                return [x,y]
            uf.union(tx,ty)


# @lc code=end



#
# @lcpr case=start
# [[1,2], [1,3], [2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2], [2,3], [3,4], [1,4], [1,5]]\n
# @lcpr case=end

#

