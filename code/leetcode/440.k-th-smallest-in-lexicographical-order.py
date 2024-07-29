#
# @lc app=leetcode.cn id=440 lang=python3
# @lcpr version=30204
#
# [440] 字典序的第K小数字
#
# https://leetcode.cn/problems/k-th-smallest-in-lexicographical-order/description/
#
# algorithms
# Hard (42.36%)
# Likes:    588
# Dislikes: 0
# Total Accepted:    53K
# Total Submissions: 125.2K
# Testcase Example:  '13\n2'
#
# 给定整数 n 和 k，返回  [1, n] 中字典序第 k 小的数字。
# 
# 
# 
# 示例 1:
# 
# 输入: n = 13, k = 2
# 输出: 10
# 解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
# 
# 
# 示例 2:
# 
# 输入: n = 1, k = 1
# 输出: 1
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= k <= n <= 10^9
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

# 思路：前缀子树类似字典树；计算每一个前缀子树的节点数的方法：递归每一层，每一层的节点数就是r-l+1
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        # l,r：当前子树每一层的最小和最大的数
        def cnt(l, r):
            if l > n: return 0
            return r-l+1 + cnt(l*10, min(r*10+9,n))

        x = 1
        while k > 1:
            c = cnt(x,x)
            if k>c:
                x += 1
                k -= c
            else:
                k -= 1
                x *= 10
        return x
# @lc code=end



#
# @lcpr case=start
# 13\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#

