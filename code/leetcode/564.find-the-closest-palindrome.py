#
# @lc app=leetcode.cn id=564 lang=python3
# @lcpr version=30204
#
# [564] 寻找最近的回文数
#
# https://leetcode.cn/problems/find-the-closest-palindrome/description/
#
# algorithms
# Hard (30.42%)
# Likes:    285
# Dislikes: 0
# Total Accepted:    26K
# Total Submissions: 85.6K
# Testcase Example:  '"123"'
#
# 给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。
# 
# “最近的”定义为两个整数差的绝对值最小。
# 
# 
# 
# 示例 1:
# 
# 输入: n = "123"
# 输出: "121"
# 
# 
# 示例 2:
# 
# 输入: n = "1"
# 输出: "0"
# 解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= n.length <= 18
# n 只由数字组成
# n 不含前导 0
# n 代表在 [1, 10^18 - 1] 范围内的整数
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
class Solution_wrong:
    def nearestPalindromic(self, n: str) -> str:
        n = list(n)
        length = len(n)
        i = 0
        j = length - 1
        cnt = 0
        while i < j:
            if n[i] != n[j]:
                n[j] = n[i]
                cnt += 1
            i += 1
            j -= 1
        if cnt == 0:
            tmp = str(int(n[i]) - 1) if n[i] != '0' else '1'
            if i==j:
                n[i] = tmp
            else:
                n[i] = n[j] = tmp
        return "".join(n)

# adhoc 枚举前一半,+1,-1,以及进退位的100...001和99..99
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        cands = [pow(10,m)+1,pow(10,(m-1))-1]
        pre = int(n[:(m+1)//2])
        for x in range(pre-1,pre+2):
            if m % 2 == 0:
                cur = str(x) + str(x)[::-1]
            else:
                y = str(x)[:-1]
                cur = y + str(x)[-1] + y[::-1]
            cands.append(int(cur))

        n = int(n)
        #print(cands)
        ans = min((abs(c-n),c) for c in cands if c != n)[1]
        return str(ans)

# @lc code=end



#
# @lcpr case=start
# "123"\n
# @lcpr case=end

# @lcpr case=start
# "1"\n
# @lcpr case=end

#

