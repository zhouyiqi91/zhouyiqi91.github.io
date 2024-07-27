#
# @lc app=leetcode.cn id=2742 lang=python3
# @lcpr version=30204
#
# [2742] 给墙壁刷油漆
#
# https://leetcode.cn/problems/painting-the-walls/description/
#
# algorithms
# Hard (51.72%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    13.6K
# Total Submissions: 26.3K
# Testcase Example:  '[1,2,3,2]\n[1,2,3,2]'
#
# 给你两个长度为 n 下标从 0 开始的整数数组 cost 和 time ，分别表示给 n 堵不同的墙刷油漆需要的开销和时间。你有两名油漆匠：
# 
# 
# 一位需要 付费 的油漆匠，刷第 i 堵墙需要花费 time[i] 单位的时间，开销为 cost[i] 单位的钱。
# 一位 免费 的油漆匠，刷 任意 一堵墙的时间为 1 单位，开销为 0 。但是必须在付费油漆匠 工作 时，免费油漆匠才会工作。
# 
# 
# 请你返回刷完 n 堵墙最少开销为多少。
# 
# 
# 
# 示例 1：
# 
# 输入：cost = [1,2,3,2], time = [1,2,3,2]
# 输出：3
# 解释：下标为 0 和 1 的墙由付费油漆匠来刷，需要 3 单位时间。同时，免费油漆匠刷下标为 2 和 3 的墙，需要 2 单位时间，开销为 0 。总开销为
# 1 + 2 = 3 。
# 
# 
# 示例 2：
# 
# 输入：cost = [2,3,4,2], time = [1,1,1,1]
# 输出：4
# 解释：下标为 0 和 3 的墙由付费油漆匠来刷，需要 2 单位时间。同时，免费油漆匠刷下标为 1 和 2 的墙，需要 2 单位时间，开销为 0 。总开销为
# 2 + 2 = 4 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= cost.length <= 500
# cost.length == time.length
# 1 <= cost[i] <= 10^6
# 1 <= time[i] <= 500
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
# 线性DP
# 剩余免费时间在中间可以为负，只要最后不为负就可以了
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        @cache
        def dp(i, ft):
            if ft > n-i: return 0
            if i==n: 
                if ft < 0: return inf
                return 0
            res = dp(i+1,ft+time[i]) + cost[i]
            res = min(res, dp(i+1,ft-1))
            return res
        ans = dp(0, 0)
        dp.cache_clear()
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3,2]\n[1,2,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4,2]\n[1,1,1,1]\n
# @lcpr case=end

#

