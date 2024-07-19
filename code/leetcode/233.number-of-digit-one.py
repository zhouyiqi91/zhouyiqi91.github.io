#
# @lc app=leetcode.cn id=233 lang=python3
# @lcpr version=30204
#
# [233] 数字 1 的个数
#
# https://leetcode.cn/problems/number-of-digit-one/description/
#
# algorithms
# Hard (49.33%)
# Likes:    582
# Dislikes: 0
# Total Accepted:    65.3K
# Total Submissions: 132.3K
# Testcase Example:  '13'
#
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 13
# 输出：6
# 
# 
# 示例 2：
# 
# 输入：n = 0
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 10^9
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
# 表示构造到从左往右第 i 位，已经出现了 cnt 
# 1个 1，在这种情况下，继续构造最终会得到的 1 的个数
class Solution:
    def countDigitOne(self, n: int) -> int:
        a = str(n)
        length = len(a)
        # index >=i位的1的个数
        @cache
        def dp(i, cnt1, highlimit):
            if i==length: 
                return cnt1
            high = int(a[i]) if highlimit else 9
            res = 0
            for x in range(high+1):
                res += dp(i+1, cnt1 + (x==1), highlimit and x==high)
            return res
        ans = dp(0, 0, True)
        dp.cache_clear()
        return ans


# @lc code=end



#
# @lcpr case=start
# 13\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

#

