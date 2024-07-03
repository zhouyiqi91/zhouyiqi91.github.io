# @lcpr-before-debug-begin
from python3problem357 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=357 lang=python3
# @lcpr version=30204
#
# [357] 统计各位数字都不同的数字个数
#
# https://leetcode.cn/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (60.71%)
# Likes:    352
# Dislikes: 0
# Total Accepted:    73.8K
# Total Submissions: 121.5K
# Testcase Example:  '2'
#
# 给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10^n^ 。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：n = 2
# 输出：91
# 解释：答案应为除去 11、22、33、44、55、66、77、88、99 外，在 0 ≤ x < 100 范围内的所有数字。 
# 
# 
# 示例 2：
# 
# 输入：n = 0
# 输出：1
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 8
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
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        @cache
        def dp(i, bitmask):
            if i == n:
                return 1
            res = 0
            for x in range(10):
                if bitmask & (1 << x):
                    continue
                if x == 0 and bitmask == 0: #前导0不计入mask
                    res += dp(i+1, 0)
                else:
                    res += dp(i + 1, bitmask | (1 << x))
            return res

        return dp(0,0)

# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

#

