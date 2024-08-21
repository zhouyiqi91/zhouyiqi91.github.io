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

grid = [[1] * 10 for _ in range(10)]
g = defaultdict(list)

# 矩阵邻居
m, n = len(grid), len(grid[0])
DX = [0,0,1,-1]
DY = [1,-1,0,0]
def neighbor(x,y):
    for dx,dy in zip(DX,DY):
        nx,ny = x+dx, y+dy
        if 0<=nx<m and 0<=ny<n:
            yield (nx,ny)

# BFS求距离
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

# dijkstra 单源最短路
def dijkstra(start, target):
    dis = defaultdict(lambda: inf)
    dis[start] = 0
    hq = [(0,start)]
    while hq:
        dx, x = heappop(hq)
        if x == target: break
        if dx > dis[x]: # 出过堆，也可以用一个vis数组判断
            continue
        for y, w in g[x]:
            if dx + w < dis[y]:
                dis[y] = dx + w
                heappush(hq, (dis[y],y))
    return dis[target]

# Astar
def h(cur, target):
    # 曼哈顿距离
    return abs(cur[0]-target[0]) + abs(cur[1]-target[1])

def astar(start, target):
    dis = defaultdict(lambda: inf)
    dis[start] = 0
    vis = set()
    q = [(0,start)]
    while q:
        _, cur = heappop(q)
        if cur == target: break
        if cur in vis: continue
        vis.add(cur)
        for nxt in neighbor(cur):
            if dis[nxt] > dis[cur] + 1:
                dis[nxt] = dis[cur] + 1
                heappush(q, (dis[nxt]+h(nxt,target), nxt) )
    return dis[target]

# 并查集
class UF:
    def __init__(self,n):
        self.pa = list(range(n))
        self.size = [1] * n
        self.cnt = n #连通分量数目

    def find(self,x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self,x,y):
        px,py = self.find(x),self.find(y)
        if px != py:
            self.pa[px] = py
            self.size[py] += self.size[px]
            self.cnt -= 1
            return True
        return False

    def same(self,x,y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self.size[self.find(x)]