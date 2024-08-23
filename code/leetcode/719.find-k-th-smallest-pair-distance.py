#
# @lc app=leetcode.cn id=719 lang=python3
# @lcpr version=30204
#
# [719] 找出第 K 小的数对距离
#
# https://leetcode.cn/problems/find-k-th-smallest-pair-distance/description/
#
# algorithms
# Hard (47.46%)
# Likes:    454
# Dislikes: 0
# Total Accepted:    38.9K
# Total Submissions: 81.8K
# Testcase Example:  '[1,3,1]\n1'
#
# 数对 (a,b) 由整数 a 和 b 组成，其数对距离定义为 a 和 b 的绝对差值。
# 
# 给你一个整数数组 nums 和一个整数 k ，数对由 nums[i] 和 nums[j] 组成且满足 0 <= i < j < nums.length
# 。返回 所有数对距离中 第 k 小的数对距离。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,3,1], k = 1
# 输出：0
# 解释：数对和对应的距离如下：
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# 距离第 1 小的数对是 (1,1) ，距离为 0 。
# 
# 
# 示例 2：
# 
# 输入：nums = [1,1,1], k = 2
# 输出：0
# 
# 
# 示例 3：
# 
# 输入：nums = [1,6,1], k = 3
# 输出：5
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 2 <= n <= 10^4
# 0 <= nums[i] <= 10^6
# 1 <= k <= n * (n - 1) / 2
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
class Solution0:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def f(x):
            res = 0
            for i,ni in enumerate(nums):
                if ni+x > nums[-1]:
                    break
                j = bisect_right(nums, ni+x) - 1
                res += j-i
            return res
        
        r = nums[-1] - nums[0]
        return bisect_left(range(r+1), k, key=lambda x:f(x))

# 小优化，剪枝
class Solution1:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def f(x):
            res = 0
            for i,ni in enumerate(nums):
                if ni+x > nums[-1]:
                    y = len(nums)-i-1
                    res += y*(y+1)//2
                    break
                j = bisect_right(nums, ni+x) - 1
                res += j-i
            return res
        
        r = nums[-1] - nums[0]
        return bisect_left(range(r+1), k, key=lambda x:f(x))
    
# 双指针 复杂度最优
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def f(x):
            res = 0
            j = 0
            for i,ni in enumerate(nums):
                while j < n and nums[j] - ni <= x:
                    j += 1
                if j==n:
                    y = n-i-1
                    res += y*(y+1)//2
                    break
                res += j-i-1
            return res
        
        r = nums[-1] - nums[0]
        return bisect_left(range(r+1), k, key=lambda x:f(x))

# @lc code=end



#
# @lcpr case=start
# [1,3,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,6,1]\n3\n
# @lcpr case=end

#

