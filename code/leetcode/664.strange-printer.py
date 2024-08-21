#
# @lc app=leetcode.cn id=664 lang=python3
# @lcpr version=30204
#
# [664] 奇怪的打印机
#
# https://leetcode.cn/problems/strange-printer/description/
#
# algorithms
# Hard (65.32%)
# Likes:    343
# Dislikes: 0
# Total Accepted:    30K
# Total Submissions: 45.9K
# Testcase Example:  '"aaabbb"'
#
# 有台奇怪的打印机有以下两个特殊要求：
# 
# 
# 打印机每次只能打印由 同一个字符 组成的序列。
# 每次可以在从起始到结束的任意位置打印新字符，并且会覆盖掉原来已有的字符。
# 
# 
# 给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。
# 
# 
# 示例 1：
# 
# 输入：s = "aaabbb"
# 输出：2
# 解释：首先打印 "aaa" 然后打印 "bbb"。
# 
# 
# 示例 2：
# 
# 输入：s = "aba"
# 输出：2
# 解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 100
# s 由小写英文字母组成
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
    def strangePrinter(self, s: str) -> int:
        s = [g[0] for g in groupby(s)]
        @cache
        def dp(i,j):
            if i==j: return 1
            if s[i] == s[j]: return dp(i,j-1)
            return min( dp(i,k) + dp(k+1,j) for k in range(i,j) )
        return dp(0, len(s)-1)

# @lc code=end



#
# @lcpr case=start
# "aaabbb"\n
# @lcpr case=end

# @lcpr case=start
# "aba"\n
# @lcpr case=end

#

