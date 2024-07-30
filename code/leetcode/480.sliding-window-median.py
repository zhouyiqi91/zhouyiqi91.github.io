#
# @lc app=leetcode.cn id=480 lang=python3
# @lcpr version=30204
#
# [480] 滑动窗口中位数
#
# https://leetcode.cn/problems/sliding-window-median/description/
#
# algorithms
# Hard (41.93%)
# Likes:    470
# Dislikes: 0
# Total Accepted:    44.5K
# Total Submissions: 106.6K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。
# 
# 例如：
# 
# 
# [2,3,4]，中位数是 3
# [2,3]，中位数是 (2 + 3) / 2 = 2.5
# 
# 
# 给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1
# 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。
# 
# 
# 
# 示例：
# 
# 给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。
# 
# 窗口位置                      中位数
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
# ⁠1 [3  -1  -3] 5  3  6  7      -1
# ⁠1  3 [-1  -3  5] 3  6  7      -1
# ⁠1  3  -1 [-3  5  3] 6  7       3
# ⁠1  3  -1  -3 [5  3  6] 7       5
# ⁠1  3  -1  -3  5 [3  6  7]      6
# 
# 
# 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。
# 
# 
# 
# 提示：
# 
# 
# 你可以假设 k 始终有效，即：k 始终小于等于输入的非空数组的元素个数。
# 与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。
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

# 官解： 对顶堆+延迟删除标记

# 有序集合
from sortedcontainers import SortedList
class Solution1:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        l = 0
        sl = SortedList()
        ans = []
        for r,rx in enumerate(nums):
            sl.add(rx)
            if len(sl) < k: continue
            if len(sl) > k:
                i = sl.bisect_left(nums[l])
                sl.pop(i)
                l += 1
            n = len(sl)
            if n % 2 == 0:
                cur = (sl[n//2-1] + sl[n//2]) / 2
            else:
                cur = sl[n//2]
            ans.append(cur)
        return ans
            
# 改进 有多个重复value时，sl.remove只会移除一个；
# 中位数可以用(a[(n-1)//2] + a[n//2]) / 2 统一奇偶
from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        l = 0
        sl = SortedList()
        ans = []
        for r,rx in enumerate(nums):
            sl.add(rx)
            if len(sl) < k: continue
            if len(sl) > k:
                sl.remove(nums[l])
                l += 1
            n = len(sl)
            ans.append((sl[n//2] + sl[(n-1)//2]) / 2)
        return ans
# @lc code=end



