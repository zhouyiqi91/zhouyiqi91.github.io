#
# @lc app=leetcode.cn id=902 lang=python3
# @lcpr version=30204
#
# [902] 最大为 N 的数字组合
#
# https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/description/
#
# algorithms
# Hard (47.58%)
# Likes:    276
# Dislikes: 0
# Total Accepted:    31.3K
# Total Submissions: 65.8K
# Testcase Example:  '["1","3","5","7"]\n100'
#
# 给定一个按 非递减顺序 排列的数字数组 digits 。你可以用任意次数 digits[i] 来写的数字。例如，如果 digits =
# ['1','3','5']，我们可以写数字，如 '13', '551', 和 '1351315'。
# 
# 返回 可以生成的小于或等于给定整数 n 的正整数的个数 。
# 
# 
# 
# 示例 1：
# 
# 输入：digits = ["1","3","5","7"], n = 100
# 输出：20
# 解释：
# 可写出的 20 个数字是：
# 1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
# 
# 
# 示例 2：
# 
# 输入：digits = ["1","4","9"], n = 1000000000
# 输出：29523
# 解释：
# 我们可以写 3 个一位数字，9 个两位数字，27 个三位数字，
# 81 个四位数字，243 个五位数字，729 个六位数字，
# 2187 个七位数字，6561 个八位数字和 19683 个九位数字。
# 总共，可以使用D中的数字写出 29523 个整数。
# 
# 示例 3:
# 
# 输入：digits = ["7"], n = 8
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 1 <= digits.length <= 9
# digits[i].length == 1
# digits[i] 是从 '1' 到 '9' 的数
# digits 中的所有值都 不同 
# digits 按 非递减顺序 排列
# 1 <= n <= 10^9
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
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = set(map(int, digits))
        finish = str(n)
        n = len(finish)
        start = '0' * n

        @cache
        def dp(i: int, low_limit: bool, high_limit: bool, isNum: bool) -> int:
            if i == n:
                return int(isNum)
            low = int(start[i]) if low_limit else 0
            high = int(finish[i]) if high_limit else 9

            res = 0
            if not isNum:
                res += dp(i+1, False, False, False)
            for x in range(low, high+1):
                if x in digits:
                    res += dp(i + 1, low_limit and x==low, high_limit and x == high, True)
            return res
        
        return dp(0, True, True, False)

# @lc code=end



#
# @lcpr case=start
# ["1","3","5","7"]\n100\n
# @lcpr case=end

# @lcpr case=start
# ["1","4","9"]\n1000000000\n
# @lcpr case=end

# @lcpr case=start
# ["7"]\n8\n
# @lcpr case=end

#

