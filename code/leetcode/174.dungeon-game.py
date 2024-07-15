#
# @lc app=leetcode.cn id=174 lang=python3
# @lcpr version=30204
#
# [174] 地下城游戏
#
# https://leetcode.cn/problems/dungeon-game/description/
#
# algorithms
# Hard (48.56%)
# Likes:    840
# Dislikes: 0
# Total Accepted:    75.6K
# Total Submissions: 155.7K
# Testcase Example:  '[[-2,-3,3],[-5,-10,1],[10,30,-5]]'
#
# table.dungeon, .dungeon th, .dungeon td {
# ⁠ border:3px solid black;
# }
# 
# ⁠.dungeon th, .dungeon td {
# ⁠   text-align: center;
# ⁠   height: 70px;
# ⁠   width: 70px;
# }
# 
# 恶魔们抓住了公主并将她关在了地下城 dungeon 的 右下角 。地下城是由 m x n 个房间组成的二维网格。我们英勇的骑士最初被安置在 左上角
# 的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
# 
# 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
# 
# 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为
# 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
# 
# 为了尽快解救公主，骑士决定每次只 向右 或 向下 移动一步。
# 
# 返回确保骑士能够拯救到公主所需的最低初始健康点数。
# 
# 注意：任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。
# 
# 
# 
# 示例 1：
# 
# 输入：dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
# 输出：7
# 解释：如果骑士遵循最佳路径：右 -> 右 -> 下 -> 下 ，则骑士的初始健康点数至少为 7 。
# 
# 示例 2：
# 
# 输入：dungeon = [[0]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# m == dungeon.length
# n == dungeon[i].length
# 1 <= m, n <= 200
# -1000 <= dungeon[i][j] <= 1000
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
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n = len(dungeon), len(dungeon[0])
        @cache
        def dp(x,y):
            if x==m-1 and y==n-1:
                pre = 1
            elif x==m-1:
                pre = dp(x,y+1)
            elif y==n-1:
                pre = dp(x+1,y)
            else:
                pre = min(dp(x+1,y),dp(x,y+1))
            return max(pre-dungeon[x][y],1)
        
        ans= dp(0,0)
        dp.cache_clear()
        return ans

# @lc code=end



#
# @lcpr case=start
# [[-2,-3,3],[-5,-10,1],[10,30,-5]]\n
# @lcpr case=end

# @lcpr case=start
# [[0]]\n
# @lcpr case=end

#

