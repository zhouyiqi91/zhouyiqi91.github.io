#
# @lc app=leetcode.cn id=3132 lang=python3
# @lcpr version=30204
#
# [3132] 找出与数组相加的整数 II
#
# https://leetcode.cn/problems/find-the-integer-added-to-array-ii/description/
#
# algorithms
# Medium (39.18%)
# Likes:    6
# Dislikes: 0
# Total Accepted:    4.6K
# Total Submissions: 11.6K
# Testcase Example:  '[4,20,16,12,8]\n[14,18,10]'
#
# 给你两个整数数组 nums1 和 nums2。
# 
# 从 nums1 中移除两个元素，并且所有其他元素都与变量 x 所表示的整数相加。如果 x 为负数，则表现为元素值的减少。
# 
# 执行上述操作后，nums1 和 nums2 相等 。当两个数组中包含相同的整数，并且这些整数出现的频次相同时，两个数组 相等 。
# 
# 返回能够实现数组相等的 最小 整数 x 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入：nums1 = [4,20,16,12,8], nums2 = [14,18,10]
# 
# 输出：-2
# 
# 解释：
# 
# 移除 nums1 中下标为 [0,4] 的两个元素，并且每个元素与 -2 相加后，nums1 变为 [18,14,10] ，与 nums2 相等。
# 
# 
# 示例 2:
# 
# 
# 输入：nums1 = [3,5,5,3], nums2 = [7,7]
# 
# 输出：2
# 
# 解释：
# 
# 移除 nums1 中下标为 [0,3] 的两个元素，并且每个元素与 2 相加后，nums1 变为 [7,7] ，与 nums2 相等。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= nums1.length <= 200
# nums2.length == nums1.length - 2
# 0 <= nums1[i], nums2[i] <= 1000
# 测试用例以这样的方式生成：存在一个整数 x，nums1 中的每个元素都与 x 相加后，再移除两个元素，nums1 可以与 nums2 相等。
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

# 思路 枚举第一个元素是0,1,2
class Solution1:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for i in range(2,-1,-1):
            remove = 2 - i
            p1 = i
            p2 = 0
            x = nums2[0] - nums1[i]
            while p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] + x != nums2[p2]:
                    p1 += 1
                    remove -= 1
                else:
                    p1 += 1
                    p2 += 1
                if remove < 0: break
            if remove >= 0: return x

# 双指针判断子序列，简化代码
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for i in [2,1]:
            x = nums2[0] - nums1[i]
            p2 = 0
            for x1 in nums1[i:]:
                if x1+x == nums2[p2]:
                    p2 += 1
                if p2 == len(nums2):
                    return x
        return nums2[0] - nums1[0]
# @lc code=end



#
# @lcpr case=start
# [4,20,16,12,8]\n[14,18,10]\n
# @lcpr case=end

# @lcpr case=start
# [3,5,5,3]\n[7,7]\n
# @lcpr case=end

#

