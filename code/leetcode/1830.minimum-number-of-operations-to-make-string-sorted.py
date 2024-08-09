#
# @lc app=leetcode.cn id=1830 lang=python3
# @lcpr version=30204
#
# [1830] 使字符串有序的最少操作次数
#
# https://leetcode.cn/problems/minimum-number-of-operations-to-make-string-sorted/description/
#
# algorithms
# Hard (52.40%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    1.7K
# Total Submissions: 3.3K
# Testcase Example:  '"cba"'
#
# 给你一个字符串 s （下标从 0 开始）。你需要对 s 执行以下操作直到它变为一个有序字符串：
# 
# 
# 找到 最大下标 i ，使得 1 <= i < s.length 且 s[i] < s[i - 1] 。
# 找到 最大下标 j ，使得 i <= j < s.length 且对于所有在闭区间 [i, j] 之间的 k 都有 s[k] < s[i - 1]
# 。
# 交换下标为 i - 1​​​​ 和 j​​​​ 处的两个字符。
# 将下标 i 开始的字符串后缀反转。
# 
# 
# 请你返回将字符串变成有序的最少操作次数。由于答案可能会很大，请返回它对 10^9 + 7 取余 的结果。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "cba"
# 输出：5
# 解释：模拟过程如下所示：
# 操作 1：i=2，j=2。交换 s[1] 和 s[2] 得到 s="cab" ，然后反转下标从 2 开始的后缀字符串，得到 s="cab" 。
# 操作 2：i=1，j=2。交换 s[0] 和 s[2] 得到 s="bac" ，然后反转下标从 1 开始的后缀字符串，得到 s="bca" 。
# 操作 3：i=2，j=2。交换 s[1] 和 s[2] 得到 s="bac" ，然后反转下标从 2 开始的后缀字符串，得到 s="bac" 。
# 操作 4：i=1，j=1。交换 s[0] 和 s[1] 得到 s="abc" ，然后反转下标从 1 开始的后缀字符串，得到 s="acb" 。
# 操作 5：i=2，j=2。交换 s[1] 和 s[2] 得到 s="abc" ，然后反转下标从 2 开始的后缀字符串，得到 s="abc" 。
# 
# 
# 示例 2：
# 
# 输入：s = "aabaa"
# 输出：2
# 解释：模拟过程如下所示：
# 操作 1：i=3，j=4。交换 s[2] 和 s[4] 得到 s="aaaab" ，然后反转下标从 3 开始的后缀字符串，得到 s="aaaba" 。
# 操作 2：i=4，j=4。交换 s[3] 和 s[4] 得到 s="aaaab" ，然后反转下标从 4 开始的后缀字符串，得到 s="aaaab" 。
# 
# 
# 示例 3：
# 
# 输入：s = "cdbea"
# 输出：63
# 
# 示例 4：
# 
# 输入：s = "leetcodeleetcodeleetcode"
# 输出：982157772
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 3000
# s​ 只包含小写英文字母。
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

# 思路 floyd 算法
# 枚举powerset
# 犯错 依次增加问题规模（k 从 1 到 n），所以k要放在最外层循环
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        def powerset(n):
            for mask in range(1<<n):
                yield([ y for y in range(n) if (1 << y) & mask])
        
        g = [[inf] * n for _ in range(n)]
        for u,v,w in roads:
            g[u][v] = min(g[u][v], w)
            g[v][u] = min(g[v][u], w)

        ans = 0
        for s in powerset(n):
            h = [row.copy() for row in g]
            for k in s:
                for i in s:
                    for j in s:
                        h[i][j] = min(h[i][j], h[i][k]+h[k][j])

            if all(h[i][j]<= maxDistance for i in s for j in s if i!=j):
                ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# "cba"\n
# @lcpr case=end

# @lcpr case=start
# "aabaa"\n
# @lcpr case=end

# @lcpr case=start
# "cdbea"\n
# @lcpr case=end

# @lcpr case=start
# "leetcodeleetcodeleetcode"\n
# @lcpr case=end

#

