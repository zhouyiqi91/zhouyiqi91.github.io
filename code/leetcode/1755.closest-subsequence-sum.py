#
# @lc app=leetcode.cn id=1755 lang=python3
# @lcpr version=30204
#
# [1755] 最接近目标值的子序列和
#
# https://leetcode.cn/problems/closest-subsequence-sum/description/
#
# algorithms
# Hard (47.14%)
# Likes:    104
# Dislikes: 0
# Total Accepted:    7.8K
# Total Submissions: 16.6K
# Testcase Example:  '[5,-7,3,5]\n6'
#
# 给你一个整数数组 nums 和一个目标值 goal 。
# 
# 你需要从 nums 中选出一个子序列，使子序列元素总和最接近 goal 。也就是说，如果子序列元素和为 sum ，你需要 最小化绝对差 abs(sum -
# goal) 。
# 
# 返回 abs(sum - goal) 可能的 最小值 。
# 
# 注意，数组的子序列是通过移除原始数组中的某些元素（可能全部或无）而形成的数组。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [5,-7,3,5], goal = 6
# 输出：0
# 解释：选择整个数组作为选出的子序列，元素和为 6 。
# 子序列和与目标值相等，所以绝对差为 0 。
# 
# 
# 示例 2：
# 
# 输入：nums = [7,-9,15,-2], goal = -5
# 输出：1
# 解释：选出子序列 [7,-9,-2] ，元素和为 -4 。
# 绝对差为 abs(-4 - (-5)) = abs(1) = 1 ，是可能的最小值。
# 
# 
# 示例 3：
# 
# 输入：nums = [1,2,3], goal = -7
# 输出：7
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 40
# -10^7 <= nums[i] <= 10^7
# -10^9 <= goal <= 10^9
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

# 双向搜索，折半搜索，meet in the middle
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def f(a):
            length = len(a)
            res = set()
            def dfs(i,s):
                if i==length: 
                    res.add(s)
                    return
                dfs(i+1, s+a[i])
                dfs(i+1, s)
            dfs(0,0)
            return sorted(res)
        
        n = len(nums)
        mid = (n+1)//2
        a1,a2 = f(nums[:mid]), f(nums[mid:])
        i = 0
        j = len(a2)-1
        ans = inf
        """
        while i<len(a1) or j >=0:
            x = a1[i] if i<len(a1) else 0
            y = a2[j] if j>=0 else 0
            s = x+y
            cur = abs(s-goal)
            if cur == 0: return 0
            ans = min(ans, cur)
            if s > goal:
                if j<0: break
                j -= 1
            else:
                if i>=len(a1): break
                i += 1
        """
        # 改进 一个指针到达边界后，无需再移动另一个指针
        while i<len(a1) and j >=0:
            diff = a1[i] + a2[j] - goal
            ans = min(ans, abs(diff))
            if diff == 0: return 0
            if diff > 0:
                j -= 1
            else:
                i += 1
        return ans
        


# @lc code=end



#
# @lcpr case=start
# [5,-7,3,5]\n6\n
# @lcpr case=end

# @lcpr case=start
# [7,-9,15,-2]\n-5\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n-7\n
# @lcpr case=end

#

