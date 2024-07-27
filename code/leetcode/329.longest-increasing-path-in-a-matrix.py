#
# @lc app=leetcode.cn id=329 lang=python3
# @lcpr version=30204
#
# [329] 矩阵中的最长递增路径
#
# https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (52.24%)
# Likes:    849
# Dislikes: 0
# Total Accepted:    111.3K
# Total Submissions: 212.9K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# 给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。
# 
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。
# 
# 
# 
# 示例 1：
# 
# 输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
# 输出：4 
# 解释：最长递增路径为 [1, 2, 6, 9]。
# 
# 示例 2：
# 
# 输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
# 输出：4 
# 解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
# 
# 
# 示例 3：
# 
# 输入：matrix = [[1]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 2^31 - 1
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

# DFS + DP
DX = [0,0,-1,1]
DY = [1,-1,0,0]
class Solution1:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        @cache
        def dfs(x,y):
            res = 1
            val = matrix[x][y]
            for dx,dy in zip(DX,DY):
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and matrix[nx][ny] > val:
                    res = max(res, dfs(nx,ny) + 1)
            return res
        ans = 1
        for x in range(m):
            for y in range(n):
                ans = max(ans,dfs(x,y))

        dfs.cache_clear()
        return ans
    
# 拓扑排序
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        ind = [[0]*n for _ in range(m)]
        g = defaultdict(list)
        for x in range(m):
            for y in range(n):
                val = matrix[x][y]
                for dx,dy in [(0,1),(1,0)]:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n:
                        nval = matrix[nx][ny]
                        if val > nval:
                            ind[x][y] += 1
                            g[(nx,ny)].append((x,y))
                            g[(x,y)].append((nx,ny))
                        elif val < nval:
                            ind[nx][ny] += 1
                            g[(x,y)].append((nx,ny))

        q = deque([(x,y) for x in range(m) for y in range(n) if ind[x][y]==0])
        ans = 0
        while q:
            size = len(q)
            ans += 1
            for _ in range(size):
                x,y= q.pop()
                for nx,ny in g[(x,y)]:
                    ind[nx][ny] -= 1
                    if ind[nx][ny] == 0:
                        q.appendleft((nx,ny))

        return ans
# @lc code=end



#
# @lcpr case=start
# [[9,9,4],[6,6,8],[2,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,4,5],[3,2,6],[2,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1]]\n
# @lcpr case=end

#

