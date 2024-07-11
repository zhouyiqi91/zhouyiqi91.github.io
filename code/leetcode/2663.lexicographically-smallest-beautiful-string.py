#
# @lc app=leetcode.cn id=2663 lang=python3
# @lcpr version=30204
#
# [2663] 字典序最小的美丽字符串
#
# https://leetcode.cn/problems/lexicographically-smallest-beautiful-string/description/
#
# algorithms
# Hard (60.72%)
# Likes:    42
# Dislikes: 0
# Total Accepted:    10.2K
# Total Submissions: 16.7K
# Testcase Example:  '"abcz"\n26'
#
# 如果一个字符串满足以下条件，则称其为 美丽字符串 ：
# 
# 
# 它由英语小写字母表的前 k 个字母组成。
# 它不包含任何长度为 2 或更长的回文子字符串。
# 
# 
# 给你一个长度为 n 的美丽字符串 s 和一个正整数 k 。
# 
# 请你找出并返回一个长度为 n 的美丽字符串，该字符串还满足：在字典序大于 s 的所有美丽字符串中字典序最小。如果不存在这样的字符串，则返回一个空字符串。
# 
# 对于长度相同的两个字符串 a 和 b ，如果字符串 a 在与字符串 b 不同的第一个位置上的字符字典序更大，则字符串 a 的字典序大于字符串 b
# 。
# 
# 
# 例如，"abcd" 的字典序比 "abcc" 更大，因为在不同的第一个位置（第四个字符）上 d 的字典序大于 c 。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：s = "abcz", k = 26
# 输出："abda"
# 解释：字符串 "abda" 既是美丽字符串，又满足字典序大于 "abcz" 。
# 可以证明不存在字符串同时满足字典序大于 "abcz"、美丽字符串、字典序小于 "abda" 这三个条件。
# 
# 
# 示例 2：
# 
# 输入：s = "dc", k = 4
# 输出：""
# 解释：可以证明，不存在既是美丽字符串，又字典序大于 "dc" 的字符串。
# 
# 
# 
# 提示：
# 
# 
# 1 <= n == s.length <= 10^5
# 4 <= k <= 26
# s 是一个美丽字符串
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
    def smallestBeautifulString(self, s: str, k: int) -> str:
        offset = ord('a')
        a = [ord(x) - offset for x in s]
        n = len(a)
        res = False
        for i in range(n-1,-1,-1):
            for c in range(a[i]+1, k):
                res = (i<1 or a[i-1] != c) and (i<2 or a[i-2] != c)
                if res:
                    a[i] = c
                    break
            if res:
                break
        if not res: return ""

        for j in range(i+1,n):
            for c in range(3):
                if c != a[j-1] and (j<2 or c!=a[j-2]):
                    a[j] = c
                    break
        print(a)
        return "".join([chr(x+offset) for x in a])
        
# @lc code=end



#
# @lcpr case=start
# "abcz"\n26\n
# @lcpr case=end

# @lcpr case=start
# "dc"\n4\n
# @lcpr case=end

#

