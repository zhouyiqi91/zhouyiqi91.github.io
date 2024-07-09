#
# @lc app=leetcode.cn id=65 lang=python3
# @lcpr version=30204
#
# [65] 有效数字
#
# https://leetcode.cn/problems/valid-number/description/
#
# algorithms
# Hard (27.73%)
# Likes:    381
# Dislikes: 0
# Total Accepted:    73.9K
# Total Submissions: 266.4K
# Testcase Example:  '"0"'
#
# 给定一个字符串 s ，返回 s 是否是一个 有效数字。
# 
# 例如，下面的都是有效数字："2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3",
# "3e+7", "+6e-1", "53.5e93", "-123.456e789"，而接下来的不是："abc", "1a", "1e", "e3",
# "99e2.5", "--6", "-+3", "95a54e53"。
# 
# 一般的，一个 有效数字 可以用以下的规则之一定义：
# 
# 
# 一个 整数 后面跟着一个 可选指数。
# 一个 十进制数 后面跟着一个 可选指数。
# 
# 
# 一个 整数 定义为一个 可选符号 '-' 或 '+' 后面跟着 数字。
# 
# 一个 十进制数 定义为一个 可选符号 '-' 或 '+' 后面跟着下述规则：
# 
# 
# 数字 后跟着一个 小数点 .。
# 数字 后跟着一个 小数点 . 再跟着 数位。
# 一个 小数点 . 后跟着 数位。
# 
# 
# 指数 定义为指数符号 'e' 或 'E'，后面跟着一个 整数。
# 
# 数字 定义为一个或多个数位。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "0"
# 
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "e"
# 
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：s = "."
# 
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 20
# s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。
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
# class Solution:
#     def isNumber(self, s: str) -> bool:
#         try:
#             float(s)
#         except:
#             return False
#         for x in ("inf", "na"):
#             if x in s.lower():
#                 return False
#         return True

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        def isInt(s):
            if not s: return False
            if s[0] in '+-': s = s[1:]
            if not s: return False
            return s.isdigit()
        
        def isDec(s):
            if s.count('.') != 1: return False
            if s[0] in '+-': s = s[1:]
            x,y = s.split('.')
            return (not x and y.isdigit()) or (not y and x.isdigit()) or (x.isdigit() and y.isdigit())

        
        if 'e' in s:
            if s.count('e') != 1: return False
            x,y = s.split('e')
            return (isDec(x) or isInt(x)) and isInt(y)
        else:
            return isInt(s) or isDec(s)

# 官方做法：有限状态自动机
# @lc code=end



#
# @lcpr case=start
# "0"\n
# @lcpr case=end

# @lcpr case=start
# "e"\n
# @lcpr case=end

# @lcpr case=start
# "."\n
# @lcpr case=end

#

