#
# @lc app=leetcode.cn id=214 lang=python3
# @lcpr version=30204
#
# [214] 最短回文串
#
# https://leetcode.cn/problems/shortest-palindrome/description/
#
# algorithms
# Hard (40.40%)
# Likes:    591
# Dislikes: 0
# Total Accepted:    52.5K
# Total Submissions: 130K
# Testcase Example:  '"aacecaaa"'
#
# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "aacecaaa"
# 输出："aaacecaaa"
# 
# 
# 示例 2：
# 
# 输入：s = "abcd"
# 输出："dcbabcd"
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length <= 5 * 10^4
# s 仅由小写英文字母组成
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
# 进制哈希 56ms，不加mod 2000+ms
class Solution1:
    def shortestPalindrome(self, s: str) -> str:
        base = 131
        mod = 10 ** 9 + 7
        offset = ord('a')
        left = right = 0
        mul = 1
        best = 0
        for i,x in enumerate(s):
            x = ord(x) - offset
            left = (left * base + x) % mod
            right = (right + x * mul) % mod
            if left == right:
                best = i
            mul = (mul * base) % mod
        return s[best+1:][::-1] + s

# KMP
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        

# @lc code=end



#
# @lcpr case=start
# "aacecaaa"\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n
# @lcpr case=end

#

