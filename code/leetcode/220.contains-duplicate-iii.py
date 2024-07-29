#
# @lc app=leetcode.cn id=220 lang=python3
# @lcpr version=30204
#
# [220] 存在重复元素 III
#
# https://leetcode.cn/problems/contains-duplicate-iii/description/
#
# algorithms
# Hard (30.63%)
# Likes:    734
# Dislikes: 0
# Total Accepted:    102.4K
# Total Submissions: 334.2K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# 给你一个整数数组 nums 和两个整数 indexDiff 和 valueDiff 。
# 
# 找出满足下述条件的下标对 (i, j)：
# 
# 
# i != j,
# abs(i - j) <= indexDiff
# abs(nums[i] - nums[j]) <= valueDiff
# 
# 
# 如果存在，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
# 输出：true
# 解释：可以找出 (i, j) = (0, 3) 。
# 满足下述 3 个条件：
# i != j --> 0 != 3
# abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
# abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
# 
# 
# 示例 2：
# 
# 输入：nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
# 输出：false
# 解释：尝试所有可能的下标对 (i, j) ，均无法满足这 3 个条件，因此返回 false 。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 1 <= indexDiff <= nums.length
# 0 <= valueDiff <= 10^9
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
# 有序集合
from sortedcontainers import SortedList
class Solution1:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        l = 0
        sl = SortedList()
        for r,rx in enumerate(nums):
            if r-l > indexDiff:
                sl.remove(nums[l])
                l += 1
            j = sl.bisect_left(rx - valueDiff)
            if j < len(sl) and sl[j] <= rx + valueDiff:
                return True
            sl.add(rx)
        return False


# 桶排序思想
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        mp = defaultdict(lambda: inf)
        l = 0
        for r,rx in enumerate(nums):
            if r-l>indexDiff:
                i = nums[l] // (valueDiff + 1)
                mp[i] = inf
                l += 1
            i = rx // (valueDiff + 1)
            if mp[i] != inf or any(abs(rx - mp[i+j]) <= valueDiff for j in (-1,1)) :
                return True
            mp[i] = rx
        return False

        
            
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n3\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,5,9,1,5,9]\n2\n3\n
# @lcpr case=end

#

