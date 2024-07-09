#
# @lc app=leetcode.cn id=60 lang=python3
# @lcpr version=30204
#
# [60] 排列序列
#
# https://leetcode.cn/problems/permutation-sequence/description/
#
# algorithms
# Hard (53.77%)
# Likes:    845
# Dislikes: 0
# Total Accepted:    143.2K
# Total Submissions: 266.4K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
# 
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# 给定 n 和 k，返回第 k 个排列。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 3, k = 3
# 输出："213"
# 
# 
# 示例 2：
# 
# 输入：n = 4, k = 9
# 输出："2314"
# 
# 
# 示例 3：
# 
# 输入：n = 3, k = 1
# 输出："123"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 9
# 1 <= k <= n!
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
#     def getPermutation(self, n: int, k: int) -> str:
#         a = list(range(1, n+1))

#         def next_permutation():
#             """Generate the lexicographically next permutation inplace.

#             https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
#             Return false if there is no next permutation.
#             """
#             # Find the largest index i such that a[i] < a[i + 1]. If no such
#             # index exists, the permutation is the last permutation
#             for i in reversed(range(len(a) - 1)):
#                 if a[i] < a[i + 1]:
#                     break  # found
#             else:  # no break: not found
#                 return False  # no next permutation

#             # Find the largest index j greater than i such that a[i] < a[j]
#             j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])

#             # Swap the value of a[i] with that of a[j]
#             a[i], a[j] = a[j], a[i]

#             # Reverse sequence from a[i + 1] up to and including the final element a[n]
#             a[i + 1:] = reversed(a[i + 1:])
#             return True

#         for _ in range(k-1):
#             next_permutation()
#         return ''.join(map(str,a))

facs = [1]
for i in range(1,9):
    facs.append(facs[-1] * i)

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        a = list(range(n+1))
        for i in range(n,0,-1):
            fac = facs[i-1]
            cur = (k-1) // fac + 1 
            k = (k-1) % fac + 1
            # k -= (cur-1) * frac
            ans.append(str(a[cur]))
            a.pop(cur)
        return ''.join(ans)


# @lc code=end



#
# @lcpr case=start
# 3\n3\n
# @lcpr case=end

# @lcpr case=start
# 4\n9\n
# @lcpr case=end

# @lcpr case=start
# 3\n1\n
# @lcpr case=end

#

