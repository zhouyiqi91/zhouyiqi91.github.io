#
# @lc app=leetcode.cn id=587 lang=python3
# @lcpr version=30204
#
# [587] 安装栅栏
#
# https://leetcode.cn/problems/erect-the-fence/description/
#
# algorithms
# Hard (60.17%)
# Likes:    227
# Dislikes: 0
# Total Accepted:    18.7K
# Total Submissions: 31.2K
# Testcase Example:  '[[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]'
#
# 给定一个数组 trees，其中 trees[i] = [xi, yi] 表示树在花园中的位置。
# 
# 你被要求用最短长度的绳子把整个花园围起来，因为绳子很贵。只有把 所有的树都围起来，花园才围得很好。
# 
# 返回恰好位于围栏周边的树木的坐标。
# 
# 示例 1:
# 
# 
# 
# 输入: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# 输出: [[1,1],[2,0],[3,3],[2,4],[4,2]]
# 
# 示例 2:
# 
# 
# 
# 输入: points = [[1,2],[2,2],[4,2]]
# 输出: [[4,2],[2,2],[1,2]]
# 
# 
# 
# 注意:
# 
# 
# 1 <= points.length <= 3000
# points[i].length == 2
# 0 <= xi, yi <= 100
# 
# 所有给定的点都是 唯一 的。
# 
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

# 凸包 
# 向量的点积是有正负的，正说明逆时针夹角小于180
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(a,b):
            return a[0]*b[1] - a[1]*b[0]
        
        def f(s2,s1,cur):
            s1,s2,cur = trees[s1],trees[s2],trees[cur]
            return cross((s1[0]-s2[0], s1[1]-s2[1]), (cur[0]-s1[0],cur[1]-s1[1])) < 0
        
        n = len(trees)
        if n<4: return trees
        trees.sort()
        used = [False] * n
        hull = [0]
        for i in range(1,n):
            while len(hull) >= 2 and f(hull[-2],hull[-1],i):
                used[hull.pop()] = False
            hull.append(i)
            used[i] = True
        m = len(hull)
        for i in range(n-2,-1,-1):
            if used[i]: continue
            while len(hull) > m and f(hull[-2],hull[-1],i):
                hull.pop()
            hull.append(i)
        hull.pop()

        return [trees[i] for i in hull]


# @lc code=end



#
# @lcpr case=start
# [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,2],[4,2]]\n
# @lcpr case=end

#

