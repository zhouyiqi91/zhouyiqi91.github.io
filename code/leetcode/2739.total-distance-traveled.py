#
# @lc app=leetcode.cn id=2739 lang=python3
# @lcpr version=30204
#
# [2739] 总行驶距离
#
# https://leetcode.cn/problems/total-distance-traveled/description/
#
# algorithms
# Easy (57.63%)
# Likes:    56
# Dislikes: 0
# Total Accepted:    30.4K
# Total Submissions: 52.8K
# Testcase Example:  '5\n10'
#
# 卡车有两个油箱。给你两个整数，mainTank 表示主油箱中的燃料（以升为单位），additionalTank 表示副油箱中的燃料（以升为单位）。
# 
# 该卡车每耗费 1 升燃料都可以行驶 10 km。每当主油箱使用了 5 升燃料时，如果副油箱至少有 1 升燃料，则会将 1 升燃料从副油箱转移到主油箱。
# 
# 返回卡车可以行驶的最大距离。
# 
# 注意：从副油箱向主油箱注入燃料不是连续行为。这一事件会在每消耗 5 升燃料时突然且立即发生。
# 
# 
# 
# 示例 1：
# 
# 输入：mainTank = 5, additionalTank = 10
# 输出：60
# 解释：
# 在用掉 5 升燃料后，主油箱中燃料还剩下 (5 - 5 + 1) = 1 升，行驶距离为 50km 。
# 在用掉剩下的 1 升燃料后，没有新的燃料注入到主油箱中，主油箱变为空。
# 总行驶距离为 60km 。
# 
# 
# 示例 2：
# 
# 输入：mainTank = 1, additionalTank = 2
# 输出：10
# 解释：
# 在用掉 1 升燃料后，主油箱变为空。
# 总行驶距离为 10km 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= mainTank, additionalTank <= 100
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
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        a = (mainTank - 1) // 4
        return (min(additionalTank, a) + mainTank) * 10

# @lc code=end



#
# @lcpr case=start
# 5\n10\n
# @lcpr case=end

# @lcpr case=start
# 1\n2\n
# @lcpr case=end

#

