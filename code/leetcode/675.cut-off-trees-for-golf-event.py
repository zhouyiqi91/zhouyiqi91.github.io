#
# @lc app=leetcode.cn id=675 lang=python3
# @lcpr version=30204
#
# [675] 为高尔夫比赛砍树
#
# https://leetcode.cn/problems/cut-off-trees-for-golf-event/description/
#
# algorithms
# Hard (51.26%)
# Likes:    231
# Dislikes: 0
# Total Accepted:    23.5K
# Total Submissions: 45.9K
# Testcase Example:  '[[1,2,3],[0,0,4],[7,6,5]]'
#
# 你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个 m x n 的矩阵表示， 在这个矩阵中：
# 
# 
# 0 表示障碍，无法触碰
# 1 表示地面，可以行走
# 比 1 大的数 表示有树的单元格，可以行走，数值表示树的高度
# 
# 
# 每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。
# 
# 你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 1（即变为地面）。
# 
# 你将从 (0, 0) 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。
# 
# 可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。
# 
# 
# 
# 示例 1：
# 
# 输入：forest = [[1,2,3],[0,0,4],[7,6,5]]
# 输出：6
# 解释：沿着上面的路径，你可以用 6 步，按从最矮到最高的顺序砍掉这些树。
# 
# 示例 2：
# 
# 输入：forest = [[1,2,3],[0,0,0],[7,6,5]]
# 输出：-1
# 解释：由于中间一行被障碍阻塞，无法访问最下面一行中的树。
# 
# 
# 示例 3：
# 
# 输入：forest = [[2,3,4],[0,0,5],[8,7,6]]
# 输出：6
# 解释：可以按与示例 1 相同的路径来砍掉所有的树。
# (0,0) 位置的树，可以直接砍去，不用算步数。
# 
# 
# 
# 
# 提示：
# 
# 
# m == forest.length
# n == forest[i].length
# 1 <= m, n <= 50
# 0 <= forest[i][j] <= 10^9
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

# BFS
class Solution1:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m,n=len(forest),len(forest[0])

        DX = [0,0,1,-1]
        DY = [1,-1,0,0]
        def neighbor(cur):
            x,y = cur
            for dx,dy in zip(DX,DY):
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and forest[nx][ny] != 0:
                    yield (nx,ny)
        
        def bfs(start, target):
            if start==target: return 0
            vis = set([start])
            dq = deque([start])
            res = 0
            while dq:
                res += 1
                for _ in range(len(dq)):
                    cur = dq.popleft()
                    for nxt in neighbor(cur):
                        if nxt in vis: continue
                        if nxt==target: return res
                        vis.add(nxt)
                        dq.append(nxt)
            return inf
        
        a = [(forest[x][y],x,y) for x in range(m) for y in range(n) if forest[x][y] > 1 ]
        if not a: return -1
        a.sort()
        a = [(0,0,0)] + a
        ans = 0
        for (_,x1,y1),(_,x2,y2) in pairwise(a):
            cur = bfs((x1,y1),(x2,y2))
            if cur == inf: return -1
            ans += cur
        return ans

# ASTAR A*
     
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m,n=len(forest),len(forest[0])

        DX = [0,0,1,-1]
        DY = [1,-1,0,0]
        def neighbor(cur):
            x,y = cur
            for dx,dy in zip(DX,DY):
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and forest[nx][ny] != 0:
                    yield (nx,ny)

        def h(cur, target):
            return abs(cur[0]-target[0]) + abs(cur[1]-target[1])
        
        def astar(start, target):
            dis = defaultdict(lambda: inf)
            dis[start] = 0
            # 加了vis更慢
            #vis = set() 
            q = [(0,start)]
            while q:
                _, cur = heappop(q)
                if cur == target: break
                #if cur in vis: continue
                #vis.add(cur)
                for nxt in neighbor(cur):
                    if dis[nxt] > dis[cur] + 1:
                        dis[nxt] = dis[cur] + 1
                        #print(q, dis[nxt])
                        heappush(q, (dis[nxt]+h(nxt,target), nxt) )
            return dis[target]
        
        a = [(forest[x][y],x,y) for x in range(m) for y in range(n) if forest[x][y] > 1 ]
        if not a: return -1
        a.sort()
        a = [(0,0,0)] + a
        ans = 0
        for (_,x1,y1),(_,x2,y2) in pairwise(a):
            cur = astar((x1,y1),(x2,y2))
            if cur == inf: return -1
            ans += cur
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[0,0,4],[7,6,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[0,0,0],[7,6,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,3,4],[0,0,5],[8,7,6]]\n
# @lcpr case=end

#

