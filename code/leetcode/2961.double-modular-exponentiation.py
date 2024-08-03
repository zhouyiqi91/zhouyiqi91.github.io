#
# @lc app=leetcode.cn id=2961 lang=python3
# @lcpr version=30204
#
# [2961] 双模幂运算
#
# https://leetcode.cn/problems/double-modular-exponentiation/description/
#
# algorithms
# Medium (48.72%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    8.4K
# Total Submissions: 15.2K
# Testcase Example:  '[[2,3,3,10],[3,3,3,1],[6,1,1,4]]\n2'
#
# 给你一个下标从 0 开始的二维数组 variables ，其中 variables[i] = [ai, bi, ci, mi]，以及一个整数 target
# 。
# 
# 如果满足以下公式，则下标 i 是 好下标：
# 
# 
# 0 <= i < variables.length
# ((ai^bi % 10)^ci) % mi == target
# 
# 
# 返回一个由 好下标 组成的数组，顺序不限 。
# 
# 
# 
# 示例 1：
# 
# 输入：variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2
# 输出：[0,2]
# 解释：对于 variables 数组中的每个下标 i ：
# 1) 对于下标 0 ，variables[0] = [2,3,3,10] ，(2^3 % 10)^3 % 10 = 2 。
# 2) 对于下标 1 ，variables[1] = [3,3,3,1] ，(3^3 % 10)^3 % 1 = 0 。
# 3) 对于下标 2 ，variables[2] = [6,1,1,4] ，(6^1 % 10)^1 % 4 = 2 。
# 因此，返回 [0,2] 作为答案。
# 
# 
# 示例 2：
# 
# 输入：variables = [[39,3,1000,1000]], target = 17
# 输出：[]
# 解释：对于 variables 数组中的每个下标 i ：
# 1) 对于下标 0 ，variables[0] = [39,3,1000,1000] ，(39^3 % 10)^1000 % 1000 = 1 。
# 因此，返回 [] 作为答案。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= variables.length <= 100
# variables[i] == [ai, bi, ci, mi]
# 1 <= ai, bi, ci, mi <= 10^3
# 0 <= target <= 10^3
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
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i,(a,b,c,m) in enumerate(variables):
            x = pow(a,b,10)
            if pow(x,c,m) == target:
                ans.append(i)
        return ans
# @lc code=end



#
# @lcpr case=start
# [[2,3,3,10],[3,3,3,1],[6,1,1,4]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[39,3,1000,1000]]\n17\n
# @lcpr case=end

#

