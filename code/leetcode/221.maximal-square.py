#
# @lc app=leetcode.cn id=221 lang=python3
# @lcpr version=30204
#
# [221] 最大正方形
#
# https://leetcode.cn/problems/maximal-square/description/
#
# algorithms
# Medium (50.46%)
# Likes:    1674
# Dislikes: 0
# Total Accepted:    335.7K
# Total Submissions: 664.5K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
# 
# 
# 
# 示例 1：
# 
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：4
# 
# 
# 示例 2：
# 
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
# 
# 
# 示例 3：
# 
# 输入：matrix = [["0"]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
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

# dp，由左侧，上方最长连续1 + 对角线最大正方形边长转移
class Solution1:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0])
        ans = 0
        diag = [[0]*n for _ in range(2)]
        up = [[0]*n for _ in range(2)]
        for i in range(m):
            left = 0
            for j in range(n):
                if matrix[i][j] != '1': 
                    up[1][j] = 0
                    left = 0
                    diag[1][j] = 0
                    continue
                left += 1
                up[1][j] = up[0][j] + 1  
                if j > 0:
                    diag[1][j] = min(diag[0][j-1]+1,left,up[1][j])
                else:
                    diag[1][0] = 1
                ans = max(ans, diag[1][j])
            #print(i, up, diag)        
            up[0] = up[1].copy()
            diag[0] = diag[1].copy()
        return ans**2
    
# 实际上不需要额外保存连续1的个数，只需要dp一个数组，表示以当前格子为右下角的最大正方形边长。
# 滚动数组优化空间

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0])
        ans = 0
        dp = [[0]*n for _ in range(2)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != '1': 
                    dp[1][j] = 0
                    continue 
                if j > 0:
                    dp[1][j] = min(dp[0][j-1],dp[0][j],dp[1][j-1]) + 1
                else:
                    dp[1][0] = 1
                ans = max(ans, dp[1][j])       
            dp[0] = dp[1].copy()
        return ans**2
# @lc code=end



#
# @lcpr case=start
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0","1"],["1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0"]]\n
# @lcpr case=end

#

