#
# @lc app=leetcode.cn id=3154 lang=python3
# @lcpr version=30204
#
# [3154] 到达第 K 级台阶的方案数
#
# https://leetcode.cn/problems/find-number-of-ways-to-reach-the-k-th-stair/description/
#
# algorithms
# Hard (45.38%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    6.1K
# Total Submissions: 11.6K
# Testcase Example:  '0'
#
# 给你有一个 非负 整数 k 。有一个无限长度的台阶，最低 一层编号为 0 。
# 
# Alice 有一个整数 jump ，一开始值为 0 。Alice 从台阶 1 开始，可以使用 任意 次操作，目标是到达第 k 级台阶。假设 Alice
# 位于台阶 i ，一次 操作 中，Alice 可以：
# 
# 
# 向下走一级到 i - 1 ，但该操作 不能 连续使用，如果在台阶第 0 级也不能使用。
# 向上走到台阶 i + 2^jump 处，然后 jump 变为 jump + 1 。
# 
# 
# 请你返回 Alice 到达台阶 k 处的总方案数。
# 
# 注意，Alice 可能到达台阶 k 处后，通过一些操作重新回到台阶 k 处，这视为不同的方案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：k = 0
# 
# 输出：2
# 
# 解释：
# 
# 2 种到达台阶 0 的方案为：
# 
# 
# Alice 从台阶 1 开始。
# 
# 执行第一种操作，从台阶 1 向下走到台阶 0 。
# 
# 
# Alice 从台阶 1 开始。
# 
# 执行第一种操作，从台阶 1 向下走到台阶 0 。
# 执行第二种操作，向上走 2^0 级台阶到台阶 1 。
# 执行第一种操作，从台阶 1 向下走到台阶 0 。
# 
# 
# 
# 
# 
# 示例 2：
# 
# 
# 输入：k = 1
# 
# 输出：4
# 
# 解释：
# 
# 4 种到达台阶 1 的方案为：
# 
# 
# Alice 从台阶 1 开始，已经到达台阶 1 。
# Alice 从台阶 1 开始。
# 
# 执行第一种操作，从台阶 1 向下走到台阶 0 。
# 执行第二种操作，向上走 2^0 级台阶到台阶 1 。
# 
# 
# Alice 从台阶 1 开始。
# 
# 执行第二种操作，向上走 2^0 级台阶到台阶 2 。
# 执行第一种操作，向下走 1 级台阶到台阶 1 。
# 
# 
# Alice 从台阶 1 开始。
# 
# 执行第一种操作，从台阶 1 向下走到台阶 0 。
# 执行第二种操作，向上走 2^0 级台阶到台阶 1 。
# 执行第一种操作，向下走 1 级台阶到台阶 0 。
# 执行第二种操作，向上走 2^1 级台阶到台阶 2 。
# 执行第一种操作，向下走 1 级台阶到台阶 1 。
# 
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= k <= 10^9
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

# 计数DP
class Solution1:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def dp(i, jump, pre):
            res = 0
            if i==k: 
                res += 1
            if i>k+1: return 0
            if not pre:
                res += dp(i-1, jump, 1)
            res += dp(i+2**jump, jump+1,0)
            return res

        ans = dp(1, 0, 0)
        return ans
    
# 组合数学
# itertools.count(start,step=1)
# 从2**j >= k的第一个j开始枚举； (k-1).bit_length()
class Solution:
    def waysToReachStair(self, k: int) -> int:
        if k==0: return 2
        ans = 0
        for j in count((k-1).bit_length()):
            m = (1<<j) - k
            if m > j+1: break
            ans += comb(j+1,m)
        return ans

# @lc code=end



#
# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

