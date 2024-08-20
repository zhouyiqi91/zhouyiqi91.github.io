#
# @lc app=leetcode.cn id=668 lang=python3
# @lcpr version=30204
#
# [668] 乘法表中第k小的数
#
# https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table/description/
#
# algorithms
# Hard (58.79%)
# Likes:    364
# Dislikes: 0
# Total Accepted:    32.5K
# Total Submissions: 55.3K
# Testcase Example:  '3\n3\n5'
#
# 几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第 k 小的数字吗？
# 
# 乘法表是大小为 m x n 的一个整数矩阵，其中 mat[i][j] == i * j（下标从 1 开始）。
# 
# 给你三个整数 m、n 和 k，请你在大小为 m x n 的乘法表中，找出并返回第 k 小的数字。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：m = 3, n = 3, k = 5
# 输出：3
# 解释：第 5 小的数字是 3 。
# 
# 
# 示例 2：
# 
# 输入：m = 2, n = 3, k = 6
# 输出：6
# 解释：第 6 小的数字是 6 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= m, n <= 3 * 10^4
# 1 <= k <= m * n
# 
# 
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

# 二分答案
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        def f(x):
            return sum(min(n,x//i) for i in range(1,m+1))

        return bisect_left(range(m*n), k, key=lambda x:f(x))

# @lc code=end



#
# @lcpr case=start
# 3\n3\n5\n
# @lcpr case=end

# @lcpr case=start
# 2\n3\n6\n
# @lcpr case=end

#

