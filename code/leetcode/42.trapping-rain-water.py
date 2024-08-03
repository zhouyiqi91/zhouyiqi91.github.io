#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30204
#
# [42] 接雨水
#
# https://leetcode.cn/problems/trapping-rain-water/description/
#
# algorithms
# Hard (63.74%)
# Likes:    5234
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 1.6M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
# 
# 
# 示例 2：
# 
# 输入：height = [4,2,0,3,2,5]
# 输出：9
# 
# 
# 
# 
# 提示：
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
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
    def trap(self, height: List[int]) -> int:
        rmax = 0
        n = len(height)
        right = [0] * n
        for i in range(n-1,-1,-1):
            right[i] = rmax
            rmax = max(rmax, height[i])

        lmax = 0
        ans = 0
        for i,x in enumerate(height):
            cur = min(lmax, right[i]) - x
            if cur > 0: ans += cur
            lmax = max(lmax,x)
        return ans

# @lc code=end



#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#

