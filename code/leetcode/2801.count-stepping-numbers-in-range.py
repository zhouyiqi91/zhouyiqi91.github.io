#
# @lc app=leetcode.cn id=2801 lang=python3
# @lcpr version=30204
#
# [2801] 统计范围内的步进数字数目
#
# https://leetcode.cn/problems/count-stepping-numbers-in-range/description/
#
# algorithms
# Hard (43.32%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 7.6K
# Testcase Example:  '"1"\n"11"'
#
# 给你两个正整数 low 和 high ，都用字符串表示，请你统计闭区间 [low, high] 内的 步进数字 数目。
# 
# 如果一个整数相邻数位之间差的绝对值都 恰好 是 1 ，那么这个数字被称为 步进数字 。
# 
# 请你返回一个整数，表示闭区间 [low, high] 之间步进数字的数目。
# 
# 由于答案可能很大，请你将它对 10^9 + 7 取余 后返回。
# 
# 注意：步进数字不能有前导 0 。
# 
# 
# 
# 示例 1：
# 
# 输入：low = "1", high = "11"
# 输出：10
# 解释：区间 [1,11] 内的步进数字为 1 ，2 ，3 ，4 ，5 ，6 ，7 ，8 ，9 和 10 。总共有 10 个步进数字。所以输出为 10 。
# 
# 示例 2：
# 
# 输入：low = "90", high = "101"
# 输出：2
# 解释：区间 [90,101] 内的步进数字为 98 和 101 。总共有 2 个步进数字。所以输出为 2 。
# 
# 
# 
# 提示：
# 
# 
# 1 <= int(low) <= int(high) < 10^100
# 1 <= low.length, high.length <= 100
# low 和 high 只包含数字。
# low 和 high 都不含前导 0 。
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
MOD = 10 **9 + 7
class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        finish = high
        n = len(finish)
        start = '0' * (n-len(low)) + low

        @cache
        def dp(i: int, low_limit: bool, high_limit: bool, pre: int) -> int:
            if i == n:
                return 1 if pre!=-1 else 0
            low = int(start[i]) if low_limit else 0
            high = int(finish[i]) if high_limit else 9

            res = 0
            for x in range(low, high+1):
                if pre != -1 and abs(x-pre) != 1:
                    continue
                cur_pre = x
                if x==0 and pre==-1: cur_pre = -1
                res += dp(i + 1, low_limit and x==low, high_limit and x == high, cur_pre)
            return res % MOD
        
        return dp(0, True, True, -1) % MOD
# @lc code=end



#
# @lcpr case=start
# "1"\n"11"\n
# @lcpr case=end

# @lcpr case=start
# "90"\n"101"\n
# @lcpr case=end

#

