#
# @lc app=leetcode.cn id=2999 lang=python3
# @lcpr version=30204
#
# [2999] 统计强大整数的数目
#
# https://leetcode.cn/problems/count-the-number-of-powerful-integers/description/
#
# algorithms
# Hard (40.09%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    2.3K
# Total Submissions: 5.7K
# Testcase Example:  '1\n6000\n4\n"124"'
#
# 给你三个整数 start ，finish 和 limit 。同时给你一个下标从 0 开始的字符串 s ，表示一个 正 整数。
# 
# 如果一个 正 整数 x 末尾部分是 s （换句话说，s 是 x 的 后缀），且 x 中的每个数位至多是 limit ，那么我们称 x 是 强大的 。
# 
# 请你返回区间 [start..finish] 内强大整数的 总数目 。
# 
# 如果一个字符串 x 是 y 中某个下标开始（包括 0 ），到下标为 y.length - 1 结束的子字符串，那么我们称 x 是 y
# 的一个后缀。比方说，25 是 5125 的一个后缀，但不是 512 的后缀。
# 
# 
# 
# 示例 1：
# 
# 输入：start = 1, finish = 6000, limit = 4, s = "124"
# 输出：5
# 解释：区间 [1..6000] 内的强大数字为 124 ，1124 ，2124 ，3124 和 4124 。这些整数的各个数位都 <= 4 且 "124"
# 是它们的后缀。注意 5124 不是强大整数，因为第一个数位 5 大于 4 。
# 这个区间内总共只有这 5 个强大整数。
# 
# 
# 示例 2：
# 
# 输入：start = 15, finish = 215, limit = 6, s = "10"
# 输出：2
# 解释：区间 [15..215] 内的强大整数为 110 和 210 。这些整数的各个数位都 <= 6 且 "10" 是它们的后缀。
# 这个区间总共只有这 2 个强大整数。
# 
# 
# 示例 3：
# 
# 输入：start = 1000, finish = 2000, limit = 4, s = "3000"
# 输出：0
# 解释：区间 [1000..2000] 内的整数都小于 3000 ，所以 "3000" 不可能是这个区间内任何整数的后缀。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= start <= finish <= 10^15
# 1 <= limit <= 9
# 1 <= s.length <= floor(log10(finish)) + 1
# s 数位中每个数字都小于等于 limit 。
# s 不包含任何前导 0 。
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

import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        n = len(str(finish))
        start = str(start)
        start =  '0' * (n-len(start)) + str(start) 
        finish = str(finish)
        diff = n - len(s)
        @cache
        def dp(i: int, low_limit: bool, high_limit: bool) -> int:
            if i == n:
                return 1
            low = int(start[i]) if low_limit else 0
            high = int(finish[i]) if high_limit else 9

            res = 0
            for x in range(low, min(limit,high) + 1):
                if i >= diff and x != int(s[i - diff]):
                    continue
                res += dp(i + 1, low_limit and x==low, high_limit and x == high)
            return res
        
        return dp(0, True, True)
# @lc code=end



#
# @lcpr case=start
# 1\n6000\n4\n"124"\n
# @lcpr case=end

# @lcpr case=start
# 15\n215\n6\n"10"\n
# @lcpr case=end

# @lcpr case=start
# 1000\n2000\n4\n"3000"\n
# @lcpr case=end

#

