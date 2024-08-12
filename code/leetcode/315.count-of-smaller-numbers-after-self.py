#
# @lc app=leetcode.cn id=315 lang=python3
# @lcpr version=30204
#
# [315] 计算右侧小于当前元素的个数
#
# https://leetcode.cn/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (43.81%)
# Likes:    1087
# Dislikes: 0
# Total Accepted:    95.7K
# Total Submissions: 218.4K
# Testcase Example:  '[5,2,6,1]'
#
# 给你一个整数数组 nums ，按要求返回一个新数组 counts 。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于
# nums[i] 的元素的数量。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [5,2,6,1]
# 输出：[2,1,1,0] 
# 解释：
# 5 的右侧有 2 个更小的元素 (2 和 1)
# 2 的右侧仅有 1 个更小的元素 (1)
# 6 的右侧有 1 个更小的元素 (1)
# 1 的右侧有 0 个更小的元素
# 
# 
# 示例 2：
# 
# 输入：nums = [-1]
# 输出：[0]
# 
# 
# 示例 3：
# 
# 输入：nums = [-1,-1]
# 输出：[0,0]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
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

# 树状数组模板题 逆序对
def lowbit(x):
    return x & (-x)

class BIT:
    def __init__(self,n):
        self.n = n
        self.tree = [0] * (n+1) #下标从1开始

    def add(self,i,v):
        while i <= self.n:
            self.tree[i] += v
            i += lowbit(i)
    
    def prefixSum(self,i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= lowbit(i)
        return s
    
    def query(self,i,j):
        # 左闭右闭
        return self.prefixSum(j) - self.prefixSum(i-1)

class Solution1:

    def countSmaller(self, nums: List[int]) -> List[int]:
        mp = {}
        for i,x in enumerate(sorted(set(nums)),start=1):
            mp[x] = i
        bit = BIT(len(mp))
        ans = [0] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            x = mp[nums[i]]
            ans[i] = bit.prefixSum(x - 1)
            bit.add(x,1)
        return ans

# 有序集合 + 二分
from sortedcontainers import SortedList
class Solution:
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        sl = SortedList()
        for i in range(len(nums)-1,-1,-1):
            ans[i] = sl.bisect_left(nums[i])
            sl.add(nums[i])
        return ans
# @lc code=end



#
# @lcpr case=start
# [5,2,6,1]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n
# @lcpr case=end

# @lcpr case=start
# [-1,-1]\n
# @lcpr case=end

#

