#
# @lc app=leetcode.cn id=2850 lang=python3
# @lcpr version=30204
#
# [2850] 将石头分散到网格图的最少移动次数
#
# https://leetcode.cn/problems/minimum-moves-to-spread-stones-over-grid/description/
#
# algorithms
# Medium (57.81%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    14.9K
# Total Submissions: 25.8K
# Testcase Example:  '[[1,1,0],[1,1,1],[1,2,1]]'
#
# 给你一个大小为 3 * 3 ，下标从 0 开始的二维整数矩阵 grid ，分别表示每一个格子里石头的数目。网格图中总共恰好有 9
# 个石头，一个格子里可能会有 多个 石头。
# 
# 每一次操作中，你可以将一个石头从它当前所在格子移动到一个至少有一条公共边的相邻格子。
# 
# 请你返回每个格子恰好有一个石头的 最少移动次数 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：grid = [[1,1,0],[1,1,1],[1,2,1]]
# 输出：3
# 解释：让每个格子都有一个石头的一个操作序列为：
# 1 - 将一个石头从格子 (2,1) 移动到 (2,2) 。
# 2 - 将一个石头从格子 (2,2) 移动到 (1,2) 。
# 3 - 将一个石头从格子 (1,2) 移动到 (0,2) 。
# 总共需要 3 次操作让每个格子都有一个石头。
# 让每个格子都有一个石头的最少操作次数为 3 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：grid = [[1,3,0],[1,0,0],[1,0,3]]
# 输出：4
# 解释：让每个格子都有一个石头的一个操作序列为：
# 1 - 将一个石头从格子 (0,1) 移动到 (0,2) 。
# 2 - 将一个石头从格子 (0,1) 移动到 (1,1) 。
# 3 - 将一个石头从格子 (2,2) 移动到 (1,2) 。
# 4 - 将一个石头从格子 (2,2) 移动到 (2,1) 。
# 总共需要 4 次操作让每个格子都有一个石头。
# 让每个格子都有一个石头的最少操作次数为 4 。
# 
# 
# 
# 
# 提示：
# 
# 
# grid.length == grid[i].length == 3
# 0 <= grid[i][j] <= 9
# grid 中元素之和为 9 。
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
# 思路1 枚举全排列
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        high = []
        low = []
        for i,row in enumerate(grid):
            for j,x in enumerate(row):
                if x > 1:
                    high.extend([(i,j)] * (x-1))
                elif x==0:
                    low.append((i,j))
        
        n = len(low)
        ans = inf
        for p in permutations(high):
            cur = sum(abs(x1-x2) + abs(y1-y2) for (x1,y1),(x2,y2) in zip(low, p))
            ans = min(ans, cur)
        return ans



# 思路2 网络流 TODO
# @lc code=end



#
# @lcpr case=start
# [[1,1,0],[1,1,1],[1,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,0],[1,0,0],[1,0,3]]\n
# @lcpr case=end

#

