#
# @lc app=leetcode.cn id=407 lang=python3
# @lcpr version=30204
#
# [407] 接雨水 II
#
# https://leetcode.cn/problems/trapping-rain-water-ii/description/
#
# algorithms
# Hard (57.00%)
# Likes:    736
# Dislikes: 0
# Total Accepted:    39.8K
# Total Submissions: 69.8K
# Testcase Example:  '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]'
#
# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# 输出: 4
# 解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。
# 
# 
# 示例 2:
# 
# 
# 
# 输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# 输出: 10
# 
# 
# 
# 
# 提示:
# 
# 
# m == heightMap.length
# n == heightMap[i].length
# 1 <= m, n <= 200
# 0 <= heightMap[i][j] <= 2 * 10^4
# 
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
# 犯错 不能套用2维动态规划的解法，因为水可以用侧面流出
class Solution_wrong:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        def f(a):
            n = len(a)
            res = [0] * n
            i = 1
            j = n - 2
            lmax = a[0]
            rmax = a[n-1]
            while i<=j:
                if lmax < rmax:
                    cur = lmax - a[i]
                    if cur > 0:
                        res[i] = cur
                    else:
                        lmax = a[i]
                    i += 1
                else:
                    cur = rmax - a[j]
                    if cur > 0:
                        res[j] = cur
                    else:
                        rmax = a[j]
                    j -= 1
            return res
        
        m,n = len(heightMap), len(heightMap[0])
        rows = [[] *n for _ in range(m)]
        cols = [[] *m for _ in range(n)]
        for i,x in enumerate(heightMap):
            rows[i] = f(x)
        for i,x in enumerate(zip(*heightMap)):
            cols[i] = f(x)
        #print(rows, cols)
        ans = 0
        for i in range(1,m-1):
            for j in range(1,n-1):
                ans += min(rows[i][j],cols[j][i])
        return ans
    
# 思路：最小堆依次更新内部节点
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m,n= len(heightMap), len(heightMap[0])
        vis = [[False] * n for _ in range(m)]
        hq = []
        for i in (0,m-1):
            for j in range(n):
                heappush(hq, (heightMap[i][j],i,j))
        for j in (0,n-1):
            for i in range(1,m-1):
                heappush(hq, (heightMap[i][j],i,j))
        
        ans = 0
        DX = [0,0,1,-1]
        DY = [-1,1,0,0]
        while hq:
            h,x,y = heappop(hq)
            for dx,dy in zip(DX,DY):
                nx,ny = x+dx,y+dy
                # 犯错 这里0<nx是不能取第一行，而不是1<nx
                if 0<nx<m-1 and 0<ny<n-1 and not vis[nx][ny]:
                    vis[nx][ny] = True
                    nh = heightMap[nx][ny]
                    if h > nh:
                        ans += h-nh
                        heappush(hq, (h,nx,ny))
                    else:
                        heappush(hq, (nh,nx,ny))
        return ans

# @lc code=end



#
# @lcpr case=start
# [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]\n
# @lcpr case=end

#

