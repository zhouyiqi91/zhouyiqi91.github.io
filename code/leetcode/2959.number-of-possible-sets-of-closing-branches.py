#
# @lc app=leetcode.cn id=2959 lang=python3
# @lcpr version=30204
#
# [2959] 关闭分部的可行集合数目
#
# https://leetcode.cn/problems/number-of-possible-sets-of-closing-branches/description/
#
# algorithms
# Hard (59.61%)
# Likes:    16
# Dislikes: 0
# Total Accepted:    5.5K
# Total Submissions: 7.9K
# Testcase Example:  '3\n5\n[[0,1,2],[1,2,10],[0,2,10]]'
#
# 一个公司在全国有 n 个分部，它们之间有的有道路连接。一开始，所有分部通过这些道路两两之间互相可以到达。
# 
# 公司意识到在分部之间旅行花费了太多时间，所以它们决定关闭一些分部（也可能不关闭任何分部），同时保证剩下的分部之间两两互相可以到达且最远距离不超过
# maxDistance 。
# 
# 两个分部之间的 距离 是通过道路长度之和的 最小值 。
# 
# 给你整数 n ，maxDistance 和下标从 0 开始的二维整数数组 roads ，其中 roads[i] = [ui, vi, wi] 表示一条从
# ui 到 vi 长度为 wi的 无向 道路。
# 
# 请你返回关闭分部的可行方案数目，满足每个方案里剩余分部之间的最远距离不超过 maxDistance。
# 
# 注意，关闭一个分部后，与之相连的所有道路不可通行。
# 
# 注意，两个分部之间可能会有多条道路。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：n = 3, maxDistance = 5, roads = [[0,1,2],[1,2,10],[0,2,10]]
# 输出：5
# 解释：可行的关闭分部方案有：
# - 关闭分部集合 [2] ，剩余分部为 [0,1] ，它们之间的距离为 2 。
# - 关闭分部集合 [0,1] ，剩余分部为 [2] 。
# - 关闭分部集合 [1,2] ，剩余分部为 [0] 。
# - 关闭分部集合 [0,2] ，剩余分部为 [1] 。
# - 关闭分部集合 [0,1,2] ，关闭后没有剩余分部。
# 总共有 5 种可行的关闭方案。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：n = 3, maxDistance = 5, roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]
# 输出：7
# 解释：可行的关闭分部方案有：
# - 关闭分部集合 [] ，剩余分部为 [0,1,2] ，它们之间的最远距离为 4 。
# - 关闭分部集合 [0] ，剩余分部为 [1,2] ，它们之间的距离为 2 。
# - 关闭分部集合 [1] ，剩余分部为 [0,2] ，它们之间的距离为 2 。
# - 关闭分部集合 [0,1] ，剩余分部为 [2] 。
# - 关闭分部集合 [1,2] ，剩余分部为 [0] 。
# - 关闭分部集合 [0,2] ，剩余分部为 [1] 。
# - 关闭分部集合 [0,1,2] ，关闭后没有剩余分部。
# 总共有 7 种可行的关闭方案。
# 
# 
# 示例 3：
# 
# 输入：n = 1, maxDistance = 10, roads = []
# 输出：2
# 解释：可行的关闭分部方案有：
# - 关闭分部集合 [] ，剩余分部为 [0] 。
# - 关闭分部集合 [0] ，关闭后没有剩余分部。
# 总共有 2 种可行的关闭方案。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10
# 1 <= maxDistance <= 10^5
# 0 <= roads.length <= 1000
# roads[i].length == 3
# 0 <= ui, vi <= n - 1
# ui != vi
# 1 <= wi <= 1000
# 一开始所有分部之间通过道路互相可以到达。
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

# 容易写错：deepcopy二维矩阵方法；
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        def powerset(n: int):
            for s in range(1<<n):
                yield [mask for mask in range(n) if (1<<mask) & s]

        g0 = [[inf] * n for _ in range(n)]
        for x,y,w in roads:
            g0[x][y] = min(g0[x][y], w)
            g0[y][x] = min(g0[y][x], w)
            
        ans = 0
        for s in powerset(n):
            g = [row.copy() for row in g0]
            for k in s:
                for i in s:
                    for j in s:
                        if (d:=g[i][k] + g[k][j]) < g[i][j]:
                            g[i][j] = d
            ans += all(g[i][j] <= maxDistance for i in s for j in s if i != j) # i==j时距离为默认值inf
        return ans




# @lc code=end



#
# @lcpr case=start
# 3\n5\n[[0,1,2],[1,2,10],[0,2,10]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n5\n[[0,1,20],[0,1,10],[1,2,2],[0,2,2]]\n
# @lcpr case=end

# @lcpr case=start
# 1\n10\n[]\n
# @lcpr case=end

#

