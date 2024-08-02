#
# @lc app=leetcode.cn id=546 lang=python3
# @lcpr version=30204
#
# [546] 移除盒子
#
# https://leetcode.cn/problems/remove-boxes/description/
#
# algorithms
# Hard (60.50%)
# Likes:    427
# Dislikes: 0
# Total Accepted:    19.9K
# Total Submissions: 33K
# Testcase Example:  '[1,3,2,2,2,3,4,3,1]'
#
# 给出一些不同颜色的盒子 boxes ，盒子的颜色由不同的正数表示。
# 
# 你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k * k
# 个积分。
# 
# 返回 你能获得的最大积分和 。
# 
# 
# 
# 示例 1：
# 
# 输入：boxes = [1,3,2,2,2,3,4,3,1]
# 输出：23
# 解释：
# [1, 3, 2, 2, 2, 3, 4, 3, 1] 
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 分) 
# ----> [1, 3, 3, 3, 1] (1*1=1 分) 
# ----> [1, 1] (3*3=9 分) 
# ----> [] (2*2=4 分)
# 
# 
# 示例 2：
# 
# 输入：boxes = [1,1,1]
# 输出：9
# 
# 
# 示例 3：
# 
# 输入：boxes = [1]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= boxes.length <= 100
# 1 <= boxes[i] <= 100
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

# 思路：很难想的dp，难度分3000+
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dp(left, right, same):
            if left > right: return 0
            res = dp(left, right-1, 0) + (same+1)**2
            for i in range(left, right):
                if boxes[i] == boxes[right]:
                    res = max(res, dp(left, i, same+1) + dp(i+1,right-1, 0))
            return res
        ans = dp(0, len(boxes)-1, 0)
        dp.cache_clear()
        return ans



# @lc code=end



#
# @lcpr case=start
# [1,3,2,2,2,3,4,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

