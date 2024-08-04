#
# @lc app=leetcode.cn id=629 lang=python3
# @lcpr version=30204
#
# [629] K 个逆序对数组
#
# https://leetcode.cn/problems/k-inverse-pairs-array/description/
#
# algorithms
# Hard (50.29%)
# Likes:    311
# Dislikes: 0
# Total Accepted:    24.9K
# Total Submissions: 49.4K
# Testcase Example:  '3\n0'
#
# 对于一个整数数组 nums，逆序对是一对满足 0 <= i < j < nums.length 且 nums[i] > nums[j]的整数对 [i,
# j] 。
# 
# 给你两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个 逆序对 的不同的数组的个数。由于答案可能很大，只需要返回对 10^9 +
# 7 取余的结果。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 3, k = 0
# 输出：1
# 解释：
# 只有数组 [1,2,3] 包含了从1到3的整数并且正好拥有 0 个逆序对。
# 
# 
# 示例 2：
# 
# 输入：n = 3, k = 1
# 输出：2
# 解释：
# 数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 1000
# 0 <= k <= 1000
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

# 序列DP 前缀和优化 滚动数组
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp0 = [0] * (k+1)
        dp0[0] = 1
        for i in range(1,n+1):
            pre = list(accumulate(dp0, initial=0))
            dp1 = [0] * (k+1)
            for j in range(k+1):
                dp1[j] = (pre[j+1] - pre[max(0,j-i+1)]) % MOD
            dp0 = dp1
        return dp1[k]
        
# @lc code=end



#
# @lcpr case=start
# 3\n0\n
# @lcpr case=end

# @lcpr case=start
# 3\n1\n
# @lcpr case=end

#

