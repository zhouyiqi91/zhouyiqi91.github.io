#
# @lc app=leetcode.cn id=2719 lang=python3
# @lcpr version=30204
#
# [2719] 统计整数数目
#
# https://leetcode.cn/problems/count-of-integers/description/
#
# algorithms
# Hard (55.30%)
# Likes:    99
# Dislikes: 0
# Total Accepted:    15.4K
# Total Submissions: 27.8K
# Testcase Example:  '"1"\n"12"\n1\n8'
#
# 给你两个数字字符串 num1 和 num2 ，以及两个整数 max_sum 和 min_sum 。如果一个整数 x
# 满足以下条件，我们称它是一个好整数：
# 
# 
# num1 <= x <= num2
# min_sum <= digit_sum(x) <= max_sum.
# 
# 
# 请你返回好整数的数目。答案可能很大，请返回答案对 10^9 + 7 取余后的结果。
# 
# 注意，digit_sum(x) 表示 x 各位数字之和。
# 
# 
# 
# 示例 1：
# 
# 输入：num1 = "1", num2 = "12", min_num = 1, max_num = 8
# 输出：11
# 解释：总共有 11 个整数的数位和在 1 到 8 之间，分别是 1,2,3,4,5,6,7,8,10,11 和 12 。所以我们返回 11 。
# 
# 
# 示例 2：
# 
# 输入：num1 = "1", num2 = "5", min_num = 1, max_num = 5
# 输出：5
# 解释：数位和在 1 到 5 之间的 5 个整数分别为 1,2,3,4 和 5 。所以我们返回 5 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= num1 <= num2 <= 10^22
# 1 <= min_sum <= max_sum <= 400
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
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        finish = num2
        n = len(finish)
        start = '0' * (n-len(num1)) + num1
        MOD = 10 ** 9 + 7

        @cache
        def dp(i: int, low_limit: bool, high_limit: bool, s) -> int:
            if i == n:
                return 1 if min_sum <= s else 0
            low = int(start[i]) if low_limit else 0
            high = int(finish[i]) if high_limit else 9

            res = 0
            for x in range(low, high + 1):
                if s+x > max_sum: break
                res += dp(i + 1, low_limit and x==low, high_limit and x == high, s+x)
            return res % MOD

        return dp(0, True, True, 0)
# @lc code=end



#
# @lcpr case=start
# "1"\n"12"\n1\n8\n
# @lcpr case=end

# @lcpr case=start
# "1"\n"5"\n1\n5\n
# @lcpr case=end

#

