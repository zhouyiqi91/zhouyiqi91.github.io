#
# @lc app=leetcode.cn id=3233 lang=python3
# @lcpr version=30204
#
# [3233] 统计不是特殊数字的数字数量
#
# https://leetcode.cn/problems/find-the-count-of-numbers-which-are-not-special/description/
#
# algorithms
# Medium (29.18%)
# Likes:    4
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 14.6K
# Testcase Example:  '5\n7'
#
# 给你两个 正整数 l 和 r。对于任何数字 x，x 的所有正因数（除了 x 本身）被称为 x 的 真因数。
# 
# 如果一个数字恰好仅有两个 真因数，则称该数字为 特殊数字。例如：
# 
# 
# 数字 4 是 特殊数字，因为它的真因数为 1 和 2。
# 数字 6 不是 特殊数字，因为它的真因数为 1、2 和 3。
# 
# 
# 返回区间 [l, r] 内 不是 特殊数字 的数字数量。
# 
# 
# 
# 示例 1：
# 
# 
# 输入： l = 5, r = 7
# 
# 输出： 3
# 
# 解释：
# 
# 区间 [5, 7] 内不存在特殊数字。
# 
# 
# 示例 2：
# 
# 
# 输入： l = 4, r = 16
# 
# 输出： 11
# 
# 解释：
# 
# 区间 [4, 16] 内的特殊数字为 4 和 9。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= l <= r <= 10^9
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

# 求质数，埃氏筛法 Sieve of Eratosthenes
def primes(n):
    res = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            res.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return res

ps = primes(int(sqrt(10**9))+1)

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def f(n):
            n = int(sqrt(n))
            return bisect_right(ps, n)

        x = f(r) - f(l-1)
        return r-l+1-x
# @lc code=end



#
# @lcpr case=start
# 5\n7\n
# @lcpr case=end

# @lcpr case=start
# 4\n16\n
# @lcpr case=end

#

