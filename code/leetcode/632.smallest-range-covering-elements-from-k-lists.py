#
# @lc app=leetcode.cn id=632 lang=python3
# @lcpr version=30204
#
# [632] 最小区间
#
# https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/description/
#
# algorithms
# Hard (61.19%)
# Likes:    444
# Dislikes: 0
# Total Accepted:    29.3K
# Total Submissions: 47.8K
# Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
#
# 你有 k 个 非递减排列 的整数列表。找到一个 最小 区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
# 
# 我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# 输出：[20,24]
# 解释： 
# 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
# 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
# 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
# 
# 
# 示例 2：
# 
# 输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
# 输出：[1,1]
# 
# 
# 
# 
# 提示：
# 
# 
# nums.length == k
# 1 <= k <= 3500
# 1 <= nums[i].length <= 50
# -10^5 <= nums[i][j] <= 10^5
# nums[i] 按非递减顺序排列
# 
# 
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


# 思路 从小到大依次枚举区间左端点，将每个左端点放入一个最小堆中，右端点即为堆中所有点的最大值。
class Solution1:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        length = inf
        ans = [-1,-1]
        hq = [(x[0],i,0) for i,x in enumerate(nums)]
        heapify(hq)
        while True:
            left, i, j = heappop(hq)
            nxt = j+1
            if not hq:
                right = left
            else:
                right = max(x for x,_,_ in hq)             
            if right - left < length:
                length = right - left
                ans = [left, right]               
            if nxt == len(nums[i]):
                break
            heappush(hq, (nums[i][nxt], i, nxt))
        return ans

# 优化：不用每次都获取最大值
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = [-inf,inf]
        right = -inf
        hq = []
        for i,x in enumerate(nums):
            hq.append((x[0],i,0))
            right = max(right, x[0])
        heapify(hq)
        while True:
            left, i, j = heappop(hq)
            nxt = j+1            
            if right - left < ans[1] - ans[0]:
                ans = [left, right]               
            if nxt == len(nums[i]):
                break
            heappush(hq, (nums[i][nxt], i, nxt))
            right = max(right, nums[i][nxt])
        return ans


# @lc code=end



#
# @lcpr case=start
# [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[1,2,3],[1,2,3]]\n
# @lcpr case=end

#

