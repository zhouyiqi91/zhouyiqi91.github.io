#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30204
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (42.36%)
# Likes:    7174
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.7M
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
# 
# 算法的时间复杂度应该为 O(log (m+n)) 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
# 
# 
# 示例 2：
# 
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
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

# 思路 要找排序后第k个元素，比较a1[k//2]和a2[k//2]，每次可以排除掉k//2个元素
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def findk(a1,a2,k):
            # a1更长
            if len(a2) > len(a1): a1,a2 = a2,a1
            if not a2: return a1[k-1]
            if k==1: return min(a1[0],a2[0])
            mid = k//2
            n1 = mid
            n2 = min(k-n1, len(a2))
            if a1[n1-1] < a2[n2-1]:
                return findk(a1[n1:],a2,k-n1)
            else:
                return findk(a1,a2[n2:],k-n2)

        k = len(nums1) + len(nums2)
        if k % 2 == 1:
            return findk(nums1,nums2, k//2+1)
        else:
            return (findk(nums1,nums2,k//2) + findk(nums1,nums2,k//2+1)) / 2
# @lc code=end



#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#

