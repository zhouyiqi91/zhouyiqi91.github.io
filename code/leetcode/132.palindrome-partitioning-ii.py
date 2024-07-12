#
# @lc app=leetcode.cn id=132 lang=python3
# @lcpr version=30204
#
# [132] 分割回文串 II
#
# https://leetcode.cn/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (49.82%)
# Likes:    748
# Dislikes: 0
# Total Accepted:    89.9K
# Total Submissions: 180.4K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。
# 
# 返回符合要求的 最少分割次数 。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
# 
# 
# 示例 2：
# 
# 输入：s = "a"
# 输出：0
# 
# 
# 示例 3：
# 
# 输入：s = "ab"
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 2000
# s 仅由小写英文字母组成
# 
# 
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
    def minCut(self, s: str) -> int:
        @cache
        def p(i,j):
            if i>=j: return True
            return s[i]==s[j] and p(i+1,j-1)
        
        n = len(s)
        @cache
        def dp(i):
            if p(0,i): return 0
            res = inf
            for cut in range(i+1):
                if p(cut,i):
                    res = min(res, 1 + dp(cut-1))
            return res
        
        ans = dp(n-1)
        dp.cache_clear()
        p.cache_clear()
        return ans
        


# @lc code=end



#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n
# @lcpr case=end

#

