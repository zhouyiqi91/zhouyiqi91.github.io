#
# @lc app=leetcode.cn id=10 lang=python3
# @lcpr version=30204
#
# [10] 正则表达式匹配
#
# https://leetcode.cn/problems/regular-expression-matching/description/
#
# algorithms
# Hard (30.70%)
# Likes:    3921
# Dislikes: 0
# Total Accepted:    424.7K
# Total Submissions: 1.4M
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# 
# 
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 
# 
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
# 
# 
# 示例 1：
# 
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
# 
# 
# 示例 2:
# 
# 输入：s = "aa", p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 
# 
# 示例 3：
# 
# 输入：s = "ab", p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s 只包含从 a-z 的小写字母。
# p 只包含从 a-z 的小写字母，以及字符 . 和 *。
# 保证每次出现字符 * 时，前面都匹配到有效的字符
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
                pre = p[j-1]
                if dp(i,j-2):
                    return True
                pos = i
                while pos>=0 and (pre=='.' or s[pos]==pre):
                    if dp(pos-1,j-2):
                        return True
                    pos -= 1
                return False
            else:
                return (p[j]=='.' or s[i]==p[j]) and dp(i-1,j-1)
        
        return dp(len(s)-1,len(p)-1)
# @lc code=end



#
# @lcpr case=start
# "aa"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"a*"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n".*"\n
# @lcpr case=end

#

