#
# @lc app=leetcode.cn id=1631 lang=python3
# @lcpr version=30204
#
# [1631] 最小体力消耗路径
#
# https://leetcode.cn/problems/path-with-minimum-effort/description/
#
# algorithms
# Medium (52.80%)
# Likes:    514
# Dislikes: 0
# Total Accepted:    66K
# Total Submissions: 124.9K
# Testcase Example:  '[[1,2,2],[3,8,2],[5,3,5]]'
#
# 你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子
# (row, col) 的高度。一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0
# 开始编号）。你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。
# 
# 一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。
# 
# 请你返回从左上角走到右下角的最小 体力消耗值 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
# 输出：2
# 解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
# 这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
# 输出：1
# 解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。
# 
# 
# 示例 3：
# 
# 输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# 输出：0
# 解释：上图所示路径不需要消耗任何体力。
# 
# 
# 
# 
# 提示：
# 
# 
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 10^6
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

# 思路1 二分答案+DFS
# 更快思路2 排序+并查集
class UF:
    def __init__(self, n):
        self.pa = list(range(n))

    def find(self, x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    def union(self, x, y):
        px,py = self.find(x), self.find(y)
        self.pa[px] = py

    def same(self,x,y):
        return self.find(x)==self.find(y)

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n= len(heights), len(heights[0])
        if m==1 and n==1: return 0
        edges = []
        for i,row in enumerate(heights):
            for j, x in enumerate(row):
                cur = i * n + j
                if j<n-1:
                    edges.append((cur,cur+1,abs(heights[i][j+1] - x)))
                if i<m-1:
                    edges.append((cur,cur+n,abs(heights[i+1][j] -x)))
        edges.sort(key=lambda x:x[2])
        uf = UF(m*n)
        for x,y,w in edges:
            uf.union(x,y)
            if uf.same(0,m*n-1):
                return w
# @lc code=end



#
# @lcpr case=start
# [[1,2,2],[3,8,2],[5,3,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[3,8,4],[5,3,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]\n
# @lcpr case=end

#

