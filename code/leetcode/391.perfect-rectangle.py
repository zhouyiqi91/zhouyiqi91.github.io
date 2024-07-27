#
# @lc app=leetcode.cn id=391 lang=python3
# @lcpr version=30204
#
# [391] 完美矩形
#
# https://leetcode.cn/problems/perfect-rectangle/description/
#
# algorithms
# Hard (45.94%)
# Likes:    268
# Dislikes: 0
# Total Accepted:    29.1K
# Total Submissions: 63.3K
# Testcase Example:  '[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]'
#
# 给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi]
# 表示一个坐标轴平行的矩形。这个矩形的左下顶点是 (xi, yi) ，右上顶点是 (ai, bi) 。
# 
# 如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 。
# 
# 
# 示例 1：
# 
# 输入：rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
# 输出：true
# 解释：5 个矩形一起可以精确地覆盖一个矩形区域。 
# 
# 
# 示例 2：
# 
# 输入：rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
# 输出：false
# 解释：两个矩形之间有间隔，无法覆盖成一个矩形。
# 
# 示例 3：
# 
# 输入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
# 输出：false
# 解释：因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
# 
# 
# 
# 提示：
# 
# 
# 1 <= rectangles.length <= 2 * 10^4
# rectangles[i].length == 4
# -10^5 <= xi, yi, ai, bi <= 10^5
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

# 犯错 即使大矩形的四个点都存在，也可能内部重叠
"""
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        s = 0
        mx = my = inf
        ma = mb = -inf
        for (x,y,a,b) in rectangles:
            mx = min(mx,x)
            my = min(my,y)
            ma = max(ma,a)
            mb = max(mb,b)
            s += (a-x) * (b-y)
        if (mx,my) not in set((x,y) for x,y,a,b in rectangles): return False
        if (ma,mb) not in set((a,b) for x,y,a,b in rectangles): return False
        if (ma,my) not in set((a,y) for x,y,a,b in rectangles): return False
        if (mx,mb) not in set((x,b) for x,y,a,b in rectangles): return False
        return s == (ma-mx) * (mb-my)
"""

# 思路：判断顶点出现次数
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        s = 0
        mx = my = inf
        ma = mb = -inf
        cnt = defaultdict(int)
        for (x,y,a,b) in rectangles:
            mx = min(mx,x)
            my = min(my,y)
            ma = max(ma,a)
            mb = max(mb,b)
            s += (a-x) * (b-y)
            cnt[(x,y)] += 1
            cnt[(a,b)] += 1
            cnt[(a,y)] += 1
            cnt[(x,b)] += 1
        for k,v in cnt.items():
            if k in {(mx,my),(ma,mb),(ma,my),(mx,mb)}:
                if v != 1: 
                    return False
            elif v not in (2,4):
                return False

        return s == (ma-mx) * (mb-my)
# @lc code=end



#
# @lcpr case=start
# [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]\n
# @lcpr case=end

#

