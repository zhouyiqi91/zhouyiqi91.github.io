#
# @lc app=leetcode.cn id=96 lang=python3
# @lcpr version=30204
#
# [96] 不同的二叉搜索树
#
# https://leetcode.cn/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (71.19%)
# Likes:    2528
# Dislikes: 0
# Total Accepted:    458.9K
# Total Submissions: 644.5K
# Testcase Example:  '3'
#
# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 3
# 输出：5
# 
# 
# 示例 2：
# 
# 输入：n = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 19
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

# 卡特兰数

dp = [0] * 20
dp[0] = 1
for i in range(1, 20):
    dp[i] = dp[i-1] * 2*(2*i-1)//(i+1)

"""
for i in range(1, 20):
    for left in range(i):
        right = i-left-1
        dp[i] += dp[left] * dp[right]
"""

class Solution:
    def numTrees(self, n: int) -> int:
        return dp[n]
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

