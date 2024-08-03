#
# @lc app=leetcode.cn id=479 lang=python3
# @lcpr version=30204
#
# [479] 最大回文数乘积
#
# https://leetcode.cn/problems/largest-palindrome-product/description/
#
# algorithms
# Hard (62.03%)
# Likes:    143
# Dislikes: 0
# Total Accepted:    24.5K
# Total Submissions: 39.5K
# Testcase Example:  '2'
#
# 给定一个整数 n ，返回 可表示为两个 n 位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 2
# 输出：987
# 解释：99 x 91 = 9009, 9009 % 1337 = 987
# 
# 
# 示例 2：
# 
# 输入：n = 1
# 输出：9
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= n <= 8
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
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9
        m = 10 ** n - 1
        def f(x):
            for y in range(int(sqrt(x)), m+1):
                q, r = divmod(x, y)
                if r==0 and len(str(q)) == n:
                    return True
            return False
        
        x = m
        while True:
            num = int(str(x) + str(x)[::-1])
            if f(num): return num % 1337
            x -= 1

# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

