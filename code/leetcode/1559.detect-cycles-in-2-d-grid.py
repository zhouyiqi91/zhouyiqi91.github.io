#
# @lc app=leetcode.cn id=1559 lang=python3
# @lcpr version=30204
#
# [1559] 二维网格图中探测环
#
# https://leetcode.cn/problems/detect-cycles-in-2d-grid/description/
#
# algorithms
# Medium (42.40%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    8.9K
# Total Submissions: 20.9K
# Testcase Example:  '[["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]'
#
# 给你一个二维字符网格数组 grid ，大小为 m x n ，你需要检查 grid 中是否存在 相同值 形成的环。
# 
# 一个环是一条开始和结束于同一个格子的长度 大于等于 4
# 的路径。对于一个给定的格子，你可以移动到它上、下、左、右四个方向相邻的格子之一，可以移动的前提是这两个格子有 相同的值 。
# 
# 同时，你也不能回到上一次移动时所在的格子。比方说，环  (1, 1) -> (1, 2) -> (1, 1) 是不合法的，因为从 (1, 2) 移动到
# (1, 1) 回到了上一次移动时的格子。
# 
# 如果 grid 中有相同值形成的环，请你返回 true ，否则返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：grid =
# [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# 输出：true
# 解释：如下图所示，有 2 个用不同颜色标出来的环：
# 
# 
# 
# 示例 2：
# 
# 
# 
# 输入：grid =
# [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# 输出：true
# 解释：如下图所示，只有高亮所示的一个合法环：
# 
# 
# 
# 示例 3：
# 
# 
# 
# 输入：grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m <= 500
# 1 <= n <= 500
# grid 只包含小写英文字母。
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

# 图中寻找环
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m,n = len(grid), len(grid[0])
        vis = [[False] *n for _ in range(m)]

        dxs = [0,0,1,-1]
        dys = [-1,1,0,0]
        def edges(x,y,fa):
            vis[x][y] = True
            for dx,dy in zip(dxs,dys):
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and (nx,ny) != fa and grid[nx][ny] == grid[x][y]:
                    yield nx,ny

        def dfs(x, y, fa):
            vis[x][y] = True
            for nx,ny in edges(x,y, fa):
                if vis[nx][ny]: 
                    return True
                if dfs(nx,ny,(x,y)):
                    return True
            return False
        for x in range(m):
            for y in range(n):
                if not vis[x][y]:
                    if dfs(x,y,(-1,-1)):
                        return True
        return False
                    



# @lc code=end



#
# @lcpr case=start
# [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]\n
# @lcpr case=end

# @lcpr case=start
# [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b","b"],["b","z","b"],["b","b","a"]]\n
# @lcpr case=end

#

