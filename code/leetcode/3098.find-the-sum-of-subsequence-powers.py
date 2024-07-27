#
# @lc app=leetcode.cn id=3098 lang=python3
# @lcpr version=30204
#
# [3098] 求出所有子序列的能量和
#
# https://leetcode.cn/problems/find-the-sum-of-subsequence-powers/description/
#
# algorithms
# Hard (39.01%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 7.5K
# Testcase Example:  '[1,2,3,4]\n3'
#
# 给你一个长度为 n 的整数数组 nums 和一个 正 整数 k 。
# 
# 一个 子序列 的 能量 定义为子序列中 任意 两个元素的差值绝对值的 最小值 。
# 
# 请你返回 nums 中长度 等于 k 的 所有 子序列的 能量和 。
# 
# 由于答案可能会很大，将答案对 10^9 + 7 取余 后返回。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3,4], k = 3
# 
# 输出：4
# 
# 解释：
# 
# nums 中总共有 4 个长度为 3 的子序列：[1,2,3] ，[1,3,4] ，[1,2,4] 和 [2,3,4] 。能量和为 |2 - 3| +
# |3 - 4| + |2 - 1| + |3 - 4| = 4 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,2], k = 2
# 
# 输出：0
# 
# 解释：
# 
# nums 中唯一一个长度为 2 的子序列是 [2,2] 。能量和为 |2 - 2| = 0 。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [4,3,-1], k = 2
# 
# 输出：10
# 
# 解释：
# 
# nums 总共有 3 个长度为 2 的子序列：[4,3] ，[4,-1] 和 [3,-1] 。能量和为 |4 - 3| + |4 - (-1)| + |3
# - (-1)| = 10 。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= n == nums.length <= 50
# -10^8 <= nums[i] <= 10^8 
# 2 <= k <= n
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

# 计数DP,选或者不选
# 子序列，首先考虑排序
class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        MOD = 10**9+7
        @cache
        def dp(i, last_val, min_diff, length):
            if length == k: return min_diff
            if i==n: return 0
            res = 0
            res += dp(i+1, nums[i], min(min_diff, nums[i]-last_val), length+1)
            res += dp(i+1, last_val, min_diff, length)
            return res % MOD
        ans = dp(0, -inf, inf, 0)
        dp.cache_clear()
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,3,-1]\n2\n
# @lcpr case=end

#

