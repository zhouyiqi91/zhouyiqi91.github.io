#
# @lc app=leetcode.cn id=149 lang=python3
# @lcpr version=30204
#
# [149] 直线上最多的点数
#
# https://leetcode.cn/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (40.69%)
# Likes:    557
# Dislikes: 0
# Total Accepted:    95.8K
# Total Submissions: 235.3K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
# 
# 
# 
# 示例 1：
# 
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：3
# 
# 
# 示例 2：
# 
# 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出：4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= points.length <= 300
# points[i].length == 2
# -10^4 <= xi, yi <= 10^4
# points 中的所有点 互不相同
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
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        def f(x1,y1,x2,y2):
            dx,dy = x1-x2,y1-y2
            g = gcd(abs(dx),abs(dy))
            mx,my = dx/g,dy/g
            if mx < 0:
                mx,my=-mx,-my
            return (mx,my)

        ans = 1
        for x1,y1 in points:
            cnt = defaultdict(int)
            for x2,y2 in points:
                if x1!=x2 or y1!=y2:
                    cnt[f(x1,y1,x2,y2)] += 1
            if cnt:
                ans = max(ans, max(cnt.values())+1)
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,1],[2,2],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]\n
# @lcpr case=end

#

