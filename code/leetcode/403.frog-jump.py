#
# @lc app=leetcode.cn id=403 lang=python3
# @lcpr version=30204
#
# [403] 青蛙过河
#
# https://leetcode.cn/problems/frog-jump/description/
#
# algorithms
# Hard (46.23%)
# Likes:    549
# Dislikes: 0
# Total Accepted:    68K
# Total Submissions: 147.1K
# Testcase Example:  '[0,1,3,5,6,8,12,17]'
#
# 一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。
# 
# 给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。开始时，
# 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃 1 个单位（即只能从单元格 1 跳至单元格 2 ）。
# 
# 如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。
# 另请注意，青蛙只能向前方（终点的方向）跳跃。
# 
# 
# 
# 示例 1：
# 
# 输入：stones = [0,1,3,5,6,8,12,17]
# 输出：true
# 解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子, 接着 跳 2 个单位到第 4 块石子,
# 然后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子, 最后，跳 5 个单位到第 8 个石子（即最后一块石子）。
# 
# 示例 2：
# 
# 输入：stones = [0,1,2,3,4,8,9,11]
# 输出：false
# 解释：这是因为第 5 和第 6 个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。
# 
# 
# 
# 提示：
# 
# 
# 2 <= stones.length <= 2000
# 0 <= stones[i] <= 2^31 - 1
# stones[0] == 0
# stones 按严格升序排列
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

# 易错 跳到最后一个即可，最后一个无法再往下跳。dp的第一个参数可以直接用单位，而不用stones的下标
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        se = set(stones)
        @cache
        def dp(x, k):
            if x == stones[-1]: 
                return True
            for y in range(k-1,k+2):
                if y > 0:
                    nxt = x + y
                    if nxt in se:
                        if dp(nxt, y):
                            return True
            return False
        if stones[1] != 1: return False
        ans = dp(1,1)
        dp.cache_clear()
        return ans
# @lc code=end



#
# @lcpr case=start
# [0,1,3,5,6,8,12,17]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,3,4,8,9,11]\n
# @lcpr case=end

#

