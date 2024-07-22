#
# @lc app=leetcode.cn id=330 lang=python3
# @lcpr version=30204
#
# [330] 按要求补齐数组
#
# https://leetcode.cn/problems/patching-array/description/
#
# algorithms
# Hard (53.08%)
# Likes:    375
# Dislikes: 0
# Total Accepted:    25.8K
# Total Submissions: 48.6K
# Testcase Example:  '[1,3]\n6'
#
# 给定一个已排序的正整数数组 nums ，和一个正整数 n 。从 [1, n] 区间内选取任意个数字补充到 nums 中，使得 [1, n]
# 区间内的任何数字都可以用 nums 中某几个数字的和来表示。
# 
# 请返回 满足上述要求的最少需要补充的数字个数 。
# 
# 
# 
# 示例 1:
# 
# 输入: nums = [1,3], n = 6
# 输出: 1 
# 解释:
# 根据 nums 里现有的组合 [1], [3], [1,3]，可以得出 1, 3, 4。
# 现在如果我们将 2 添加到 nums 中， 组合变为: [1], [2], [3], [1,3], [2,3], [1,2,3]。
# 其和可以表示数字 1, 2, 3, 4, 5, 6，能够覆盖 [1, 6] 区间里所有的数。
# 所以我们最少需要添加一个数字。
# 
# 示例 2:
# 
# 输入: nums = [1,5,10], n = 20
# 输出: 2
# 解释: 我们需要添加 [2,4]。
# 
# 
# 示例 3:
# 
# 输入: nums = [1,2,2], n = 5
# 输出: 0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^4
# nums 按 升序排列
# 1 <= n <= 2^31 - 1
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
# 贪心
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        cur = 0 #目前区间右端点
        ans = 0
        i = 0
        while cur < n:
            nxt = cur + 1
            if i==len(nums) or nxt < nums[i]:
                ans += 1
                cur = cur + nxt
            else:
                cur += nums[i]
                i += 1
        return ans        
            

# @lc code=end



#
# @lcpr case=start
# [1,3]\n6\n
# @lcpr case=end

# @lcpr case=start
# [1,5,10]\n20\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2]\n5\n
# @lcpr case=end

#

