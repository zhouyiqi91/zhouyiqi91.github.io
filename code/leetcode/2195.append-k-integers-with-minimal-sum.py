#
# @lc app=leetcode.cn id=2195 lang=python3
# @lcpr version=30204
#
# [2195] 向数组中追加 K 个整数
#
# https://leetcode.cn/problems/append-k-integers-with-minimal-sum/description/
#
# algorithms
# Medium (24.69%)
# Likes:    56
# Dislikes: 0
# Total Accepted:    12.9K
# Total Submissions: 52K
# Testcase Example:  '[1,4,25,10,25]\n2'
#
# 给你一个整数数组 nums 和一个整数 k 。请你向 nums 中追加 k 个 未 出现在 nums 中的、互不相同 的 正 整数，并使结果数组的元素和
# 最小 。
# 
# 返回追加到 nums 中的 k 个整数之和。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,4,25,10,25], k = 2
# 输出：5
# 解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 2 和 3 。
# nums 最终元素和为 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70 ，这是所有情况中的最小值。
# 所以追加到数组中的两个整数之和是 2 + 3 = 5 ，所以返回 5 。
# 
# 示例 2：
# 
# 输入：nums = [5,6], k = 6
# 输出：25
# 解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 1 、2 、3 、4 、7 和 8 。
# nums 最终元素和为 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36 ，这是所有情况中的最小值。
# 所以追加到数组中的两个整数之和是 1 + 2 + 3 + 4 + 7 + 8 = 25 ，所以返回 25 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i], k <= 10^9
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

# 哨兵简化判断
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.extend([0,inf])
        nums.sort()
        ans = 0
        for x,y in pairwise(nums):
            cnt = min(y-x-1, k)
            if cnt <= 0: continue
            ans += (x+1+x+cnt) * cnt // 2
            k -= cnt
            if k==0: return ans
# @lc code=end



#
# @lcpr case=start
# [1,4,25,10,25]\n2\n
# @lcpr case=end

# @lcpr case=start
# [5,6]\n6\n
# @lcpr case=end

#

