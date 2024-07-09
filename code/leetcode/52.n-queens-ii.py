#
# @lc app=leetcode.cn id=52 lang=python3
# @lcpr version=30204
#
# [52] N 皇后 II
#
# https://leetcode.cn/problems/n-queens-ii/description/
#
# algorithms
# Hard (82.29%)
# Likes:    519
# Dislikes: 0
# Total Accepted:    153.5K
# Total Submissions: 186.5K
# Testcase Example:  '4'
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 
# 
# 示例 2：
# 
# 输入：n = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 9
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
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [False] * n
        dig1 = defaultdict(int)
        dig2 = defaultdict(int)
        self.ans = 0
        def dfs(row):
            if row==n:
                self.ans += 1
                return
            for col in range(n):
                if not cols[col]:
                    d1 = col - row
                    d2 = col + row
                    if not dig1[d1] and not dig2[d2]:
                        cols[col] = True
                        dig1[d1] = 1
                        dig2[d2] = 1
                        dfs(row+1)
                        cols[col] = False
                        dig1[d1] = 0
                        dig2[d2] = 0
        dfs(0)
        return self.ans


# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

