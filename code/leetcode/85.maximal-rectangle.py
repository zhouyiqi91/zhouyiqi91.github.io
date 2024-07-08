#
# @lc app=leetcode.cn id=85 lang=python3
# @lcpr version=30204
#
# [85] 最大矩形
#
# https://leetcode.cn/problems/maximal-rectangle/description/
#
# algorithms
# Hard (55.20%)
# Likes:    1647
# Dislikes: 0
# Total Accepted:    199.6K
# Total Submissions: 361.4K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
# 
# 
# 
# 示例 1：
# 
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
# 
# 
# 示例 2：
# 
# 输入：matrix = [["0"]]
# 输出：0
# 
# 
# 示例 3：
# 
# 输入：matrix = [["1"]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# rows == matrix.length
# cols == matrix[0].length
# 1 <= row, cols <= 200
# matrix[i][j] 为 '0' 或 '1'
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
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        dp = [[int(x) for x in row] for row in matrix]
        m,n=len(dp),len(dp[0])
        ans = 0
        for x in range(m):
            for y in range(n):
                if dp[x][y] != 1:
                    continue
                if y > 0:
                    dp[x][y] = dp[x][y-1] + 1
                nx = x
                row_len = dp[x][y]
                while nx>=0 and dp[nx][y] > 0:
                    row_len = min(row_len, dp[nx][y])
                    ans = max(ans, row_len * (x-nx+1))
                    nx -= 1
        return ans


# @lc code=end



#
# @lcpr case=start
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1"]]\n
# @lcpr case=end

#

