#
# @lc app=leetcode.cn id=2454 lang=python3
# @lcpr version=30204
#
# [2454] 下一个更大元素 IV
#
# https://leetcode.cn/problems/next-greater-element-iv/description/
#
# algorithms
# Hard (54.99%)
# Likes:    141
# Dislikes: 0
# Total Accepted:    18K
# Total Submissions: 32.8K
# Testcase Example:  '[2,4,0,9,6]'
#
# 给你一个下标从 0 开始的非负整数数组 nums 。对于 nums 中每一个整数，你必须找到对应元素的 第二大 整数。
# 
# 如果 nums[j] 满足以下条件，那么我们称它为 nums[i] 的 第二大 整数：
# 
# 
# j > i
# nums[j] > nums[i]
# 恰好存在 一个 k 满足 i < k < j 且 nums[k] > nums[i] 。
# 
# 
# 如果不存在 nums[j] ，那么第二大整数为 -1 。
# 
# 
# 比方说，数组 [1, 2, 4, 3] 中，1 的第二大整数是 4 ，2 的第二大整数是 3 ，3 和 4 的第二大整数是 -1 。
# 
# 
# 请你返回一个整数数组 answer ，其中 answer[i]是 nums[i] 的第二大整数。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [2,4,0,9,6]
# 输出：[9,6,6,-1,-1]
# 解释：
# 下标为 0 处：2 的右边，4 是大于 2 的第一个整数，9 是第二个大于 2 的整数。
# 下标为 1 处：4 的右边，9 是大于 4 的第一个整数，6 是第二个大于 4 的整数。
# 下标为 2 处：0 的右边，9 是大于 0 的第一个整数，6 是第二个大于 0 的整数。
# 下标为 3 处：右边不存在大于 9 的整数，所以第二大整数为 -1 。
# 下标为 4 处：右边不存在大于 6 的整数，所以第二大整数为 -1 。
# 所以我们返回 [9,6,6,-1,-1] 。
# 
# 
# 示例 2：
# 
# 输入：nums = [3,3]
# 输出：[-1,-1]
# 解释：
# 由于每个数右边都没有更大的数，所以我们返回 [-1,-1] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
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

# 两个单调递减栈
class Solution1:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        st1 = []
        st2 = []
        n = len(nums)
        ans = [-1] * n
        for i,x in enumerate(nums):
            while st2 and x > nums[st2[-1]]:
                ans[st2.pop()] = x
            tmp = []
            while st1 and x > nums[st1[-1]]:
                tmp.append(st1.pop())
            st2.extend(tmp[::-1])
            st1.append(i)
        return ans
    
# 排序+有序集合 O(nlogn)
# 遍历x时，sl中是>=x的元素，由于index是按从小到大排序的，所以值相等的不影响结果。
from sortedcontainers import SortedList
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        sl = SortedList()
        a = [(i,x) for i,x in enumerate(nums)]
        a.sort(key=lambda x: (-x[1],x[0]))
        ans = [-1] * len(nums)
        for i,x in a:
            j = sl.bisect_right(i) + 1
            if j < len(sl):
                ans[i] = nums[sl[j]]
            sl.add(i)
        return ans
# @lc code=end



#
# @lcpr case=start
# [2,4,0,9,6]\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n
# @lcpr case=end

#

