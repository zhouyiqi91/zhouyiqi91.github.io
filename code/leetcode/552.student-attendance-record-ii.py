#
# @lc app=leetcode.cn id=552 lang=python3
# @lcpr version=30204
#
# [552] 学生出勤记录 II
#
# https://leetcode.cn/problems/student-attendance-record-ii/description/
#
# algorithms
# Hard (58.22%)
# Likes:    315
# Dislikes: 0
# Total Accepted:    30.6K
# Total Submissions: 52.6K
# Testcase Example:  '2'
#
# 可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
# 
# 'A'：Absent，缺勤
# 'L'：Late，迟到
# 'P'：Present，到场
# 
# 
# 如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
# 
# 
# 按 总出勤 计，学生缺勤（'A'）严格 少于两天。
# 学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。
# 
# 
# 给你一个整数 n ，表示出勤记录的长度（次数）。请你返回记录长度为 n 时，可能获得出勤奖励的记录情况 数量 。答案可能很大，所以返回对 10^9 + 7
# 取余 的结果。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 2
# 输出：8
# 解释：
# 有 8 种长度为 2 的记录将被视为可奖励：
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL" 
# 只有"AA"不会被视为可奖励，因为缺勤次数为 2 次（需要少于 2 次）。
# 
# 
# 示例 2：
# 
# 输入：n = 1
# 输出：3
# 
# 
# 示例 3：
# 
# 输入：n = 10101
# 输出：183236316
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^5
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
class Solution1:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9+7
        @cache
        def dp(i, a, l):
            if i==n: return 1
            res = dp(i+1,a,0)
            if a == 0:
                res += dp(i+1, 1, 0)
            if l < 2:
                res += dp(i+1, a, l+1)
            return res % MOD
        ans = dp(0, 0, 0)
        dp.cache_clear()
        return ans
    
# 矩阵快速幂优化dp
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        mat = [
            [1, 1, 0, 1, 0, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0],
        ]
        
        def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            rows, columns, temp = len(a), len(b[0]), len(b)
            c = [[0] * columns for _ in range(rows)]
            for i in range(rows):
                for j in range(columns):
                    for k in range(temp):
                        c[i][j] += a[i][k] * b[k][j]
                        c[i][j] %= MOD
            return c
        
        def matrixPow(mat: List[List[int]], n: int) -> List[List[int]]:
            ret = [[1, 0, 0, 0, 0, 0]]
            while n > 0:
                if (n & 1) == 1:
                    ret = multiply(ret, mat)
                n >>= 1
                mat = multiply(mat, mat)
            return ret

        res = matrixPow(mat, n)
        ans = sum(res[0])
        return ans % MOD
    
# numpy
# mat = np.matrix(mat, dtype='object')
# res = np.linalg.matrix_power(mat, n)

# ans = res.sum(axis=1)[0].tolist()[0][0]
# return ans % MOD

# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 10101\n
# @lcpr case=end

#

