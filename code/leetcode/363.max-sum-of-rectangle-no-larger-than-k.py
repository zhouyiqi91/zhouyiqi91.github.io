#
# @lc app=leetcode.cn id=363 lang=python3
# @lcpr version=30204
#
# [363] 矩形区域不超过 K 的最大数值和
#
# https://leetcode.cn/problems/max-sum-of-rectangle-no-larger-than-k/description/
#
# algorithms
# Hard (48.33%)
# Likes:    485
# Dislikes: 0
# Total Accepted:    44.7K
# Total Submissions: 92.4K
# Testcase Example:  '[[1,0,1],[0,-2,3]]\n2'
#
# 给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。
# 
# 题目数据保证总会存在一个数值和不超过 k 的矩形区域。
# 
# 
# 
# 示例 1：
# 
# 输入：matrix = [[1,0,1],[0,-2,3]], k = 2
# 输出：2
# 解释：蓝色边框圈出来的矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
# 
# 
# 示例 2：
# 
# 输入：matrix = [[2,2,-1]], k = 3
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -100 <= matrix[i][j] <= 100
# -10^5 <= k <= 10^5
# 
# 
# 
# 
# 进阶：如果行数远大于列数，该如何设计解决方案？
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

# 二维前缀和 暴力， 超时
class MatrixSum:
    def __init__(self, matrix):
        m,n=len(matrix),len(matrix[0])
        self.s = [[0]*(n+1) for _ in range(m+1)]
        s = self.s
        for i,row in enumerate(matrix):
            for j,x in enumerate(row):
                s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + x

    def query(self,x1,y1,x2,y2):
        # 左闭右开
        s = self.s
        return s[x2][y2] - s[x1][y2] - s[x2][y1] + s[x1][y1]

class Solution1:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m,n = len(matrix), len(matrix[0])
        ms = MatrixSum(matrix)
        ans = -inf
        for x1 in range(m):
            for y1 in range(n):
                for x2 in range(x1+1,m+1):
                    for y2 in range(y1+1,n+1):
                        cur = ms.query(x1,y1,x2,y2)
                        #print(x1,y1,x2,y2,cur)
                        if cur == k: return k
                        if cur < k:
                            ans = max(ans,cur)
        return ans

# 有序集合，固定三条边，枚举第四条边; 转化为在一维有序数组中查找左侧的边。
# sl.bisect

from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = -inf
        for x1 in range(m):
            s = [0] * n # 当前区域每一列的和
            for x2 in range(x1,m):
                for y2 in range(n):
                    s[y2] += matrix[x2][y2] 

                sl = SortedList([0])
                ps = 0
                for x in s:
                    ps += x
                    y1 = sl.bisect_left(ps-k) # bisect不行，默认是bisect_right
                    if y1 < len(sl):
                        ans = max(ans, ps - sl[y1])
                        if ans == k: return k
                    sl.add(ps)
        return ans

                
        

# @lc code=end



#
# @lcpr case=start
# [[1,0,1],[0,-2,3]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[2,2,-1]]\n3\n
# @lcpr case=end

#

