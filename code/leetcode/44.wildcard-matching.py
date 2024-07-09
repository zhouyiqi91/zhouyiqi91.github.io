#
# @lc app=leetcode.cn id=44 lang=python3
# @lcpr version=30204
#
# [44] 通配符匹配
#
# https://leetcode.cn/problems/wildcard-matching/description/
#
# algorithms
# Hard (34.03%)
# Likes:    1149
# Dislikes: 0
# Total Accepted:    158.5K
# Total Submissions: 465.8K
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个输入字符串 (s) 和一个字符模式 (p) ，请你实现一个支持 '?' 和 '*' 匹配规则的通配符匹配：
# 
# 
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符序列（包括空字符序列）。
# 
# 
# 
# 
# 判定匹配成功的充要条件是：字符模式必须能够 完全匹配 输入字符串（而不是部分匹配）。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
# 
# 
# 示例 2：
# 
# 输入：s = "aa", p = "*"
# 输出：true
# 解释：'*' 可以匹配任意字符串。
# 
# 
# 示例 3：
# 
# 输入：s = "cb", p = "?a"
# 输出：false
# 解释：'?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length, p.length <= 2000
# s 仅由小写英文字母组成
# p 仅由小写英文字母、'?' 或 '*' 组成
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
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(i,j):
            if j==-1: return i==-1
            if i==-1 and p[j] != '*': return False
            if p[j] == '*':
                for pos in range(-1,i+1):
                    if dp(pos, j-1):
                        return True
                return False
            else:
                return (p[j]=='?' or s[i]==p[j]) and dp(i-1,j-1)

        return dp(len(s)-1,len(p)-1)
# @lc code=end



#
# @lcpr case=start
# "aa"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"*"\n
# @lcpr case=end

# @lcpr case=start
# "cb"\n"?a"\n
# @lcpr case=end

#

