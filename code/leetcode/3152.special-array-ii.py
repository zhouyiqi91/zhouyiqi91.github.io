#
# @lc app=leetcode.cn id=3152 lang=python3
# @lcpr version=30204
#
# [3152] 特殊数组 II
#
# https://leetcode.cn/problems/special-array-ii/description/
#
# algorithms
# Medium (32.07%)
# Likes:    19
# Dislikes: 0
# Total Accepted:    9.9K
# Total Submissions: 25.6K
# Testcase Example:  '[3,4,1,2,6]\n[[0,4]]'
#
# 如果数组的每一对相邻元素都是两个奇偶性不同的数字，则该数组被认为是一个 特殊数组 。
# 
# 周洋哥有一个整数数组 nums 和一个二维整数矩阵 queries，对于 queries[i] = [fromi, toi]，请你帮助周洋哥检查子数组
# nums[fromi..toi] 是不是一个 特殊数组 。
# 
# 返回布尔数组 answer，如果 nums[fromi..toi] 是特殊数组，则 answer[i] 为 true ，否则，answer[i] 为
# false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,4,1,2,6], queries = [[0,4]]
# 
# 输出：[false]
# 
# 解释：
# 
# 子数组是 [3,4,1,2,6]。2 和 6 都是偶数。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [4,3,1,6], queries = [[0,2],[2,3]]
# 
# 输出：[false,true]
# 
# 解释：
# 
# 
# 子数组是 [4,3,1]。3 和 1 都是奇数。因此这个查询的答案是 false。
# 子数组是 [1,6]。只有一对：(1,6)，且包含了奇偶性不同的数字。因此这个查询的答案是 true。
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 1 <= queries.length <= 10^5
# queries[i].length == 2
# 0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
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
# 思路1 前缀和，看from..to是否包含断点
class Solution1:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        a = [0]
        for i,x in enumerate(nums[1:], start=1):
            a.append(x % 2 == nums[i-1] % 2)
        pre = list(accumulate(a, initial=0))
        ans = []
        for lo,hi in queries:
            res = (pre[hi+1] - pre[lo+1]) == 0
            ans.append(res)
        return ans

# 思路2 dp 找到每个to位置的最左边的from
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        dp = [0]
        for i,x in enumerate(nums[1:], start=1):
            if x % 2 == nums[i-1] % 2:
                cur = i
            else:
                cur = dp[i-1]
            dp.append(cur)
        return [f>=dp[t] for f,t in queries]

# @lc code=end



#
# @lcpr case=start
# [3,4,1,2,6]\n[[0,4]]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,1,6]\n[[0,2],[2,3]]\n
# @lcpr case=end

#

