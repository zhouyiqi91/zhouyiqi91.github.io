#
# @lc app=leetcode.cn id=115 lang=python3
# @lcpr version=30204
#
# [115] 不同的子序列
#
# https://leetcode.cn/problems/distinct-subsequences/description/
#
# algorithms
# Hard (52.09%)
# Likes:    1243
# Dislikes: 0
# Total Accepted:    184.5K
# Total Submissions: 353.8K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# 给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数，结果需要对 10^9 + 7 取模。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# rabbbit
# rabbbit
# rabbbit
# 
# 示例 2：
# 
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length, t.length <= 1000
# s 和 t 由英文字母组成
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
# 动态规划 + 剪枝
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dp(i,j):
            if j==-1: return 1
            if i==-1: return 0
            if j > i: return 0 # 剪枝，速度快10倍
            res = 0
            if s[i] == t[j]:
                res += dp(i-1,j-1)
            res += dp(i-1,j)
            return res
        
        ans = dp(len(s)-1,len(t)-1)
        dp.cache_clear()
        MOD = 10 ** 9 + 7
        return ans % MOD
# @lc code=end



#
# @lcpr case=start
# "rabbbit"\n"rabbit"\n
# @lcpr case=end

# @lcpr case=start
# "babgbag"\n"bag"\n
# @lcpr case=end

#

