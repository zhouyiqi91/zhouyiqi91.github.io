#
# @lc app=leetcode.cn id=1349 lang=python3
# @lcpr version=30204
#
# [1349] 参加考试的最大学生数
#
# https://leetcode.cn/problems/maximum-students-taking-exam/description/
#
# algorithms
# Hard (63.69%)
# Likes:    238
# Dislikes: 0
# Total Accepted:    16.5K
# Total Submissions: 25.9K
# Testcase Example:  '[["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]'
#
# 给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。
# 
# 
# 学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的同时参加考试且无法作弊的
# 最大 学生人数。
# 
# 学生必须坐在状况良好的座位上。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：seats = [["#",".","#","#",".","#"],
# [".","#","#","#","#","."],
# ["#",".","#","#",".","#"]]
# 输出：4
# 解释：教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。 
# 
# 
# 示例 2：
# 
# 输入：seats = [[".","#"],
# ["#","#"],
# ["#","."],
# ["#","#"],
# [".","#"]]
# 输出：3
# 解释：让所有学生坐在可用的座位上。
# 
# 
# 示例 3：
# 
# 输入：seats = [["#",".",".",".","#"],
# [".","#",".","#","."],
# [".",".","#",".","."],
# [".","#",".","#","."],
# ["#",".",".",".","#"]]
# 输出：10
# 解释：让学生坐在第 1、3 和 5 列的可用座位上。
# 
# 
# 
# 
# 提示：
# 
# 
# seats 只包含字符 '.' 和'#'
# m == seats.length
# n == seats[i].length
# 1 <= m <= 8
# 1 <= n <= 8
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
# 状压dp，枚举所有集合，然后判断是否合法；93ms，13.89%
class Solution1:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m,n = len(seats),len(seats[0])
        seats = [sum(1<<i if x=='#' else 0 for i,x in enumerate(row))
            for row in seats
        ]
        def cv(r,cur):
            row = seats[r]
            return row & cur == 0 and cur & (cur << 1) == 0

        def pv(cur,pre):
            return (pre<<1) & cur == 0 and (pre>>1) & cur == 0        

        @cache
        def dp(r, pre):
            if r==m: return 0
            res = 0
            for cur in range(1<<n):    
                if cv(r,cur) and pv(cur, pre):
                    res = max(res, dp(r+1,cur) + cur.bit_count())
            return res

        ans = dp(0,0)
        return ans

# 枚举子集，包含空集 68 ms  31.48 %
# https://leetcode.cn/circle/discuss/CaOJ45/
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m,n = len(seats),len(seats[0])
        seats = [sum(1<<i if x=='.' else 0 for i,x in enumerate(row))
            for row in seats
        ]

        def pv(cur,pre):
            return (pre<<1) & cur == 0 and (pre>>1) & cur == 0        

        @cache
        def dp(r, pre):
            if r==m: return 0
            res = 0
            s = seats[r]
            cur = s
            while True:
                if cur & (cur << 1) == 0 and pv(cur, pre):
                    res = max(res, dp(r+1,cur) + cur.bit_count())
                cur = (cur-1) & s
                if cur == s:
                    break
            return res

        ans = dp(0,0)
        return ans
# @lc code=end



#
# @lcpr case=start
# [["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]\n
# @lcpr case=end

# @lcpr case=start
# [[".","#"],["#","#"],["#","."],["#","#"],[".","#"]]\n
# @lcpr case=end

# @lcpr case=start
# [["#",".",".",".","#"],[".","#",".","#","."],[".",".","#",".","."],[".","#",".","#","."],["#",".",".",".","#"]]\n
# @lcpr case=end

#

