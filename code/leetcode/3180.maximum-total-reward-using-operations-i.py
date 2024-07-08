#
# @lc app=leetcode.cn id=3180 lang=python3
# @lcpr version=30204
#
# [3180] 执行操作可获得的最大总奖励 I
#
# https://leetcode.cn/problems/maximum-total-reward-using-operations-i/description/
#
# algorithms
# Medium (32.60%)
# Likes:    8
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 11.5K
# Testcase Example:  '[1,1,3,3]'
#
# 给你一个整数数组 rewardValues，长度为 n，代表奖励的值。
# 
# 最初，你的总奖励 x 为 0，所有下标都是 未标记 的。你可以执行以下操作 任意次 ：
# 
# 
# 从区间 [0, n - 1] 中选择一个 未标记 的下标 i。
# 如果 rewardValues[i] 大于 你当前的总奖励 x，则将 rewardValues[i] 加到 x 上（即 x = x +
# rewardValues[i]），并 标记 下标 i。
# 
# 
# 以整数形式返回执行最优操作能够获得的 最大 总奖励。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：rewardValues = [1,1,3,3]
# 
# 输出：4
# 
# 解释：
# 
# 依次标记下标 0 和 2，总奖励为 4，这是可获得的最大值。
# 
# 
# 示例 2：
# 
# 
# 输入：rewardValues = [1,6,4,3,2]
# 
# 输出：11
# 
# 解释：
# 
# 依次标记下标 0、2 和 1。总奖励为 11，这是可获得的最大值。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= rewardValues.length <= 2000
# 1 <= rewardValues[i] <= 2000
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
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = list(set(rewardValues))
        rewardValues.sort()
        f = 1
        for v in rewardValues:
            mask = ((1<<v) - 1) & f
            f |= mask << v
        return f.bit_length() - 1
# @lc code=end



#
# @lcpr case=start
# [1,1,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,6,4,3,2]\n
# @lcpr case=end

#

