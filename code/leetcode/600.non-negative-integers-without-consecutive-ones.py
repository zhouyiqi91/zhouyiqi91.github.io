#
# @lc app=leetcode.cn id=600 lang=python3
# @lcpr version=30204
#
# [600] 不含连续1的非负整数
#
# https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/description/
#
# algorithms
# Hard (50.30%)
# Likes:    356
# Dislikes: 0
# Total Accepted:    28.2K
# Total Submissions: 56K
# Testcase Example:  '5'
#
# 给定一个正整数 n ，请你统计在 [0, n] 范围的非负整数中，有多少个整数的二进制表示中不存在 连续的 1 。
# 
# 
# 
# 示例 1:
# 
# 输入: n = 5
# 输出: 5
# 解释: 
# 下面列出范围在 [0, 5] 的非负整数与其对应的二进制表示：
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# 其中，只有整数 3 违反规则（有两个连续的 1 ），其他 5 个满足规则。
# 
# 示例 2:
# 
# 输入: n = 1
# 输出: 2
# 
# 
# 示例 3:
# 
# 输入: n = 2
# 输出: 3
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= n <= 10^9
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
    def findIntegers(self, n: int) -> int:
        a = bin(n)[2:]
        m = len(a)
        @cache
        def dp(i, highlimit, pre):
            if i==m: return 1
            hi = int(a[i]) if highlimit else 1

            res = 0
            for d in range(hi+1):
                if d==1 and pre==1: continue
                res += dp(i+1, highlimit and d==int(a[i]), d)
            return res
        return dp(0, True, 0)



# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

