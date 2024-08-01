#
# @lc app=leetcode.cn id=483 lang=python3
# @lcpr version=30204
#
# [483] 最小好进制
#
# https://leetcode.cn/problems/smallest-good-base/description/
#
# algorithms
# Hard (58.66%)
# Likes:    169
# Dislikes: 0
# Total Accepted:    20.1K
# Total Submissions: 34.4K
# Testcase Example:  '"13"'
#
# 以字符串的形式给出 n , 以字符串的形式返回 n 的最小 好进制  。
# 
# 如果 n 的  k(k>=2) 进制数的所有数位全为1，则称 k(k>=2) 是 n 的一个 好进制 。
# 
# 
# 
# 示例 1：
# 
# 输入：n = "13"
# 输出："3"
# 解释：13 的 3 进制是 111。
# 
# 
# 示例 2：
# 
# 输入：n = "4681"
# 输出："8"
# 解释：4681 的 8 进制是 11111。
# 
# 
# 示例 3：
# 
# 输入：n = "1000000000000000000"
# 输出："999999999999999999"
# 解释：1000000000000000000 的 999999999999999999 进制是 11。
# 
# 
# 
# 
# 提示：
# 
# 
# n 的取值范围是 [3, 10^18]
# n 没有前导 0
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

# n次根，nth root: pow(a, n) == a**(1/n)
# 数学判定k的范围，就不需要二分了
# 等比数列通项公式
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        maxM = int(log(n, 2))
        for m in range(maxM, 1, -1):
            k = int(pow(n,1/m))
            if (pow(k,m+1) - 1) == (k-1) * n:
                return str(k)
        return str(n-1)


# @lc code=end



#
# @lcpr case=start
# "13"\n
# @lcpr case=end

# @lcpr case=start
# "4681"\n
# @lcpr case=end

# @lcpr case=start
# "1000000000000000000"\n
# @lcpr case=end

#

