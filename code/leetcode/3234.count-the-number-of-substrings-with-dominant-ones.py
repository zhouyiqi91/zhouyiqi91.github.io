#
# @lc app=leetcode.cn id=3234 lang=python3
# @lcpr version=30204
#
# [3234] 统计 1 显著的字符串的数量
#
# https://leetcode.cn/problems/count-the-number-of-substrings-with-dominant-ones/description/
#
# algorithms
# Medium (29.71%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 7.4K
# Testcase Example:  '"00011"'
#
# 给你一个二进制字符串 s。
# 
# 请你统计并返回其中 1 显著  的 子字符串 的数量。
# 
# 如果字符串中 1 的数量 大于或等于 0 的数量的 平方，则认为该字符串是一个 1 显著 的字符串 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "00011"
# 
# 输出：5
# 
# 解释：
# 
# 1 显著的子字符串如下表所示。
# 
# 
# 
# 
# 
# i
# j
# s[i..j]
# 0 的数量
# 1 的数量
# 
# 
# 
# 
# 3
# 3
# 1
# 0
# 1
# 
# 
# 4
# 4
# 1
# 0
# 1
# 
# 
# 2
# 3
# 01
# 1
# 1
# 
# 
# 3
# 4
# 11
# 0
# 2
# 
# 
# 2
# 4
# 011
# 1
# 2
# 
# 
# 
# 
# 示例 2：
# 
# 
# 输入：s = "101101"
# 
# 输出：16
# 
# 解释：
# 
# 1 不显著的子字符串如下表所示。
# 
# 总共有 21 个子字符串，其中 5 个是 1 不显著字符串，因此有 16 个 1 显著子字符串。
# 
# 
# 
# 
# 
# i
# j
# s[i..j]
# 0 的数量
# 1 的数量
# 
# 
# 
# 
# 1
# 1
# 0
# 1
# 0
# 
# 
# 4
# 4
# 0
# 1
# 0
# 
# 
# 1
# 4
# 0110
# 2
# 2
# 
# 
# 0
# 4
# 10110
# 2
# 3
# 
# 
# 1
# 5
# 01101
# 2
# 3
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 4 * 10^4
# s 仅包含字符 '0' 和 '1'。
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
    def numberOfSubstrings(self, s: str) -> int:
        a = deque([i for i,x in enumerate(s) if x=='0'])
        n = len(s)
        a.append(n)
        ans = 0
        for i in range(n):
            if a[0] < i: a.popleft()
            for j in range(len(a)):
                x = j*j+j+i-1
                left = a[j-1] if j>0 else i
                x = max(x, left)
                if x < a[j]:
                    ans += a[j] - x
        return ans



            

# @lc code=end



#
# @lcpr case=start
# "00011"\n
# @lcpr case=end

# @lcpr case=start
# "101101"\n
# @lcpr case=end

#

