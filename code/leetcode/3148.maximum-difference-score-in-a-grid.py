#
# @lc app=leetcode.cn id=3148 lang=python3
# @lcpr version=30204
#
# [3148] 矩阵中的最大得分
#
# https://leetcode.cn/problems/maximum-difference-score-in-a-grid/description/
#
# algorithms
# Medium (50.74%)
# Likes:    27
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 14K
# Testcase Example:  '[[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]'
#
# 给你一个由 正整数 组成、大小为 m x n 的矩阵 grid。你可以从矩阵中的任一单元格移动到另一个位于正下方或正右侧的任意单元格（不必相邻）。从值为
# c1 的单元格移动到值为 c2 的单元格的得分为 c2 - c1 。
# 
# 你可以从 任一 单元格开始，并且必须至少移动一次。
# 
# 返回你能得到的 最大 总得分。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]
# 
# 输出：9
# 
# 解释：从单元格 (0, 1) 开始，并执行以下移动：
# - 从单元格 (0, 1) 移动到 (2, 1)，得分为 7 - 5 = 2 。
# - 从单元格 (2, 1) 移动到 (2, 2)，得分为 14 - 7 = 7 。
# 总得分为 2 + 7 = 9 。
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：grid = [[4,3,2],[3,2,1]]
# 
# 输出：-1
# 
# 解释：从单元格 (0, 0) 开始，执行一次移动：从 (0, 0) 到 (0, 1) 。得分为 3 - 4 = -1 。
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 10^5
# 1 <= grid[i][j] <= 10^5
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

# 思路：路径的中间值都会被消去，实际上对于每一个终点，找左上矩阵中的最小值
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        rowmin = [inf] * m
        colmin = [inf] * n
        ans = -inf
        for i, row in enumerate(grid):
            for j,x in enumerate(row):
                m = min(rowmin[i], colmin[j])
                ans = max(ans, x - m)
                rowmin[i] = colmin[j] = min(m, x)
        return ans
    
# @lc code=end



#
# @lcpr case=start
# [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,3,2],[3,2,1]]\n
# @lcpr case=end

#

