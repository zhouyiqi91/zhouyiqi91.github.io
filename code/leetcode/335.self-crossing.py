#
# @lc app=leetcode.cn id=335 lang=python3
# @lcpr version=30204
#
# [335] 路径交叉
#
# https://leetcode.cn/problems/self-crossing/description/
#
# algorithms
# Hard (42.46%)
# Likes:    171
# Dislikes: 0
# Total Accepted:    19.6K
# Total Submissions: 46.2K
# Testcase Example:  '[2,1,1,2]'
#
# 给你一个整数数组 distance 。
# 
# 从 X-Y 平面上的点 (0,0) 开始，先向北移动 distance[0] 米，然后向西移动 distance[1] 米，向南移动
# distance[2] 米，向东移动 distance[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。
# 
# 判断你所经过的路径是否相交。如果相交，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 输入：distance = [2,1,1,2]
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：distance = [1,2,3,4]
# 输出：false
# 
# 
# 示例 3：
# 
# 输入：distance = [1,1,1,1]
# 输出：true
# 
# 
# 
# 提示：
# 
# 
# 1 <= distance.length <= 10^5
# 1 <= distance[i] <= 10^5
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
# 找规律，分情况
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        d = distance
        n = len(d)
        if n < 4: return False
        for i in range(3, n):
            if d[i-1] <= d[i-3] and d[i] >= d[i-2]: return True
            if i>=4 and d[i-1] == d[i-3] and d[i] >= d[i-2] - d[i-4]: return True
            if i>=5 and d[i-1] + d[i-5] >= d[i-3] and d[i-1] <= d[i-3] and d[i]+d[i-4] >= d[i-2] and d[i-2] >= d[i-4] : return True
        return False
# @lc code=end



#
# @lcpr case=start
# [2,1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n
# @lcpr case=end

#

