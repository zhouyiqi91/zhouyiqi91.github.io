#
# @lc app=leetcode.cn id=3112 lang=python3
# @lcpr version=30204
#
# [3112] 访问消失节点的最少时间
#
# https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/description/
#
# algorithms
# Medium (35.56%)
# Likes:    15
# Dislikes: 0
# Total Accepted:    5.1K
# Total Submissions: 11.5K
# Testcase Example:  '3\n[[0,1,2],[1,2,1],[0,2,4]]\n[1,1,5]'
#
# 给你一个二维数组 edges 表示一个 n 个点的无向图，其中 edges[i] = [ui, vi, lengthi] 表示节点 ui 和节点 vi
# 之间有一条需要 lengthi 单位时间通过的无向边。
# 
# 同时给你一个数组 disappear ，其中 disappear[i] 表示节点 i 从图中消失的时间点，在那一刻及以后，你无法再访问这个节点。
# 
# 注意，图有可能一开始是不连通的，两个节点之间也可能有多条边。
# 
# 请你返回数组 answer ，answer[i] 表示从节点 0 到节点 i 需要的 最少 单位时间。如果从节点 0 出发 无法 到达节点 i ，那么
# answer[i] 为 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]
# 
# 输出：[0,-1,4]
# 
# 解释：
# 
# 我们从节点 0 出发，目的是用最少的时间在其他节点消失之前到达它们。
# 
# 
# 对于节点 0 ，我们不需要任何时间，因为它就是我们的起点。
# 对于节点 1 ，我们需要至少 2 单位时间，通过 edges[0] 到达。但当我们到达的时候，它已经消失了，所以我们无法到达它。
# 对于节点 2 ，我们需要至少 4 单位时间，通过 edges[2] 到达。
# 
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,3,5]
# 
# 输出：[0,2,3]
# 
# 解释：
# 
# 我们从节点 0 出发，目的是用最少的时间在其他节点消失之前到达它们。
# 
# 
# 对于节点 0 ，我们不需要任何时间，因为它就是我们的起点。
# 对于节点 1 ，我们需要至少 2 单位时间，通过 edges[0] 到达。
# 对于节点 2 ，我们需要至少 3 单位时间，通过 edges[0] 和 edges[1] 到达。
# 
# 
# 
# 示例 3：
# 
# 
# 输入：n = 2, edges = [[0,1,1]], disappear = [1,1]
# 
# 输出：[0,-1]
# 
# 解释：
# 
# 当我们到达节点 1 的时候，它恰好消失，所以我们无法到达节点 1 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 5 * 10^4
# 0 <= edges.length <= 10^5
# edges[i] == [ui, vi, lengthi]
# 0 <= ui, vi <= n - 1
# 1 <= lengthi <= 10^5
# disappear.length == n
# 1 <= disappear[i] <= 10^5
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
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = defaultdict(list)
        for x,y,length in edges:
            g[x].append((y,length))
            g[y].append((x,length))
        
        hq = [(0,0)]
        dis = [inf] * n
        dis[0] = 0
        while hq:
            dx, x = heappop(hq)
            if dx > dis[x]: continue
            for y, length in g[x]:
                if (d:= dx+length) < disappear[y] and d < dis[y]:
                    dis[y] = d
                    heappush(hq, (dis[y],y))

        return [x if x != inf else -1 for x in dis]

# @lc code=end



#
# @lcpr case=start
# 3\n[[0,1,2],[1,2,1],[0,2,4]]\n[1,1,5]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1,2],[1,2,1],[0,2,4]]\n[1,3,5]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[0,1,1]]\n[1,1]\n
# @lcpr case=end

#

