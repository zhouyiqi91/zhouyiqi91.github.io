#
# @lc app=leetcode.cn id=458 lang=python3
# @lcpr version=30204
#
# [458] 可怜的小猪
#
# https://leetcode.cn/problems/poor-pigs/description/
#
# algorithms
# Hard (66.18%)
# Likes:    430
# Dislikes: 0
# Total Accepted:    28.8K
# Total Submissions: 43.6K
# Testcase Example:  '4\n15\n15'
#
# 有 buckets 桶液体，其中 正好有一桶
# 含有毒药，其余装的都是水。它们从外观看起来都一样。为了弄清楚哪只水桶含有毒药，你可以喂一些猪喝，通过观察猪是否会死进行判断。不幸的是，你只有
# minutesToTest 分钟时间来确定哪桶液体是有毒的。
# 
# 喂猪的规则如下：
# 
# 
# 选择若干活猪进行喂养
# 可以允许小猪同时饮用任意数量的桶中的水，并且该过程不需要时间。
# 小猪喝完水后，必须有 minutesToDie 分钟的冷却时间。在这段时间里，你只能观察，而不允许继续喂猪。
# 过了 minutesToDie 分钟后，所有喝到毒药的猪都会死去，其他所有猪都会活下来。
# 重复这一过程，直到时间用完。
# 
# 
# 给你桶的数目 buckets ，minutesToDie 和 minutesToTest ，返回 在规定时间内判断哪个桶有毒所需的 最小 猪数 。
# 
# 
# 
# 示例 1：
# 
# 输入：buckets = 1000, minutesToDie = 15, minutesToTest = 60
# 输出：5
# 
# 
# 示例 2：
# 
# 输入：buckets = 4, minutesToDie = 15, minutesToTest = 15
# 输出：2
# 
# 
# 示例 3：
# 
# 输入：buckets = 4, minutesToDie = 15, minutesToTest = 30
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= buckets <= 1000
# 1 <= minutesToDie <= minutesToTest <= 100
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
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        k = minutesToTest // minutesToDie
        return ceil(log(buckets,2) / log(k+1, 2) - 1e-5)
# @lc code=end



#
# @lcpr case=start
# 1000\n15\n60\n
# @lcpr case=end

# @lcpr case=start
# 4\n15\n15\n
# @lcpr case=end

# @lcpr case=start
# 4\n15\n30\n
# @lcpr case=end

#

