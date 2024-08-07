#
# @lc app=leetcode.cn id=260 lang=python3
# @lcpr version=30204
#
# [260] 只出现一次的数字 III
#
# https://leetcode.cn/problems/single-number-iii/description/
#
# algorithms
# Medium (71.49%)
# Likes:    910
# Dislikes: 0
# Total Accepted:    156.4K
# Total Submissions: 218.8K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# 给你一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
# 
# 你必须设计并实现线性时间复杂度的算法且仅使用常量额外空间来解决此问题。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2,1,3,2,5]
# 输出：[3,5]
# 解释：[5, 3] 也是有效的答案。
# 
# 
# 示例 2：
# 
# 输入：nums = [-1,0]
# 输出：[-1,0]
# 
# 
# 示例 3：
# 
# 输入：nums = [0,1]
# 输出：[1,0]
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= nums.length <= 3 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 除两个只出现一次的整数外，nums 中的其他数字都出现两次
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
# 位运算 异或+lowbit
# 转化为 136. 只出现一次的数字
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_sum = reduce(xor, nums)
        lowbit = xor_sum & (-xor_sum)
        ans = [0,0]
        for x in nums:
            ans[(x & lowbit) == 0] ^= x
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,1,3,2,5]\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

#

