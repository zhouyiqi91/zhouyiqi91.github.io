#
# @lc app=leetcode.cn id=1584 lang=python3
# @lcpr version=30204
#
# [1584] 连接所有点的最小费用
#
# https://leetcode.cn/problems/min-cost-to-connect-all-points/description/
#
# algorithms
# Medium (65.64%)
# Likes:    319
# Dislikes: 0
# Total Accepted:    63.4K
# Total Submissions: 96.6K
# Testcase Example:  '[[0,0],[2,2],[3,10],[5,2],[7,0]]'
#
# 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
# 
# 连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示
# val 的绝对值。
# 
# 请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# 输出：20
# 解释：
# 
# 我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
# 注意到任意两个点之间只有唯一一条路径互相到达。
# 
# 
# 示例 2：
# 
# 输入：points = [[3,12],[-2,5],[-4,1]]
# 输出：18
# 
# 
# 示例 3：
# 
# 输入：points = [[0,0],[1,1],[1,0],[-1,1]]
# 输出：4
# 
# 
# 示例 4：
# 
# 输入：points = [[-1000000,-1000000],[1000000,1000000]]
# 输出：4000000
# 
# 
# 示例 5：
# 
# 输入：points = [[0,0]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= points.length <= 1000
# -10^6 <= xi, yi <= 10^6
# 所有点 (xi, yi) 两两不同。
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

# 最小生成树 MST kruskal: 维护最小生成森林；按边权值从小到大排序，端点不连通的边加入最小生成树
class UF:
    def __init__(self,n):
        self.pa = list(range(n))
        #self.size = [1] * n
        self.cnt = n #连通分量数目

    def find(self,x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self,x,y):
        px,py = self.find(x),self.find(y)
        if px != py:
            self.pa[px] = py
            #self.size[py] += self.size[px]
            self.cnt -= 1
            return True
        return False
        
    def same(self,x,y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self.size[self.find(x)]
    

class Solution1:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1,n):
                xi,yi = points[i]
                xj,yj = points[j]
                d = abs(xi-xj)+abs(yi-yj)
                edges.append((d,i,j))

        edges.sort()
        uf = UF(n)
        for d,i,j in edges:
            if uf.union(i,j):
                res += d
                if uf.cnt==1: break
        return res
    
# prim算法 维护最小生成树的一部分
# heap

class Solution2:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        g = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                xi,yi = points[i]
                xj,yj = points[j]
                d = abs(xi-xj)+abs(yi-yj)
                g[i][j] = g[j][i] = d
        
        tree = set()
        hq = [(0,0)]
        ans = 0
        while len(tree) != n:
            w,x = heappop(hq)
            if x in tree: continue
            tree.add(x)
            ans += w
            for y in range(n):
                if y not in tree:
                    heappush(hq, (g[x][y], y))
        return ans

# prim 完全图邻接矩阵写法
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        g = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                xi,yi = points[i]
                xj,yj = points[j]
                d = abs(xi-xj)+abs(yi-yj)
                g[i][j] = g[j][i] = d
        
        tree = set()
        dis = [inf] * n
        dis[0] = 0
        while len(tree) != n:
            x,i = min((x,i) for i,x in enumerate(dis) if i not in tree)
            tree.add(i)
            for j in range(n):
                if j not in tree:
                    dis[j] = min(dis[j], g[i][j])
        return sum(dis)
# @lc code=end



#
# @lcpr case=start
# [[0,0],[2,2],[3,10],[5,2],[7,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,12],[-2,5],[-4,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0],[1,1],[1,0],[-1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[-1000000,-1000000],[1000000,1000000]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0]]\n
# @lcpr case=end

#

