#
# @lc app=leetcode.cn id=1192 lang=python3
# @lcpr version=30204
#
# [1192] 查找集群内的关键连接
#
# https://leetcode.cn/problems/critical-connections-in-a-network/description/
#
# algorithms
# Hard (55.70%)
# Likes:    277
# Dislikes: 0
# Total Accepted:    10.3K
# Total Submissions: 18.5K
# Testcase Example:  '4\n[[0,1],[1,2],[2,0],[1,3]]'
#
# 力扣数据中心有 n 台服务器，分别按从 0 到 n-1 的方式进行了编号。它们之间以 服务器到服务器 的形式相互连接组成了一个内部集群，连接是无向的。用
# connections 表示集群网络，connections[i] = [a, b] 表示服务器 a 和 b
# 之间形成连接。任何服务器都可以直接或者间接地通过网络到达任何其他服务器。
# 
# 关键连接 是在该集群中的重要连接，假如我们将它移除，便会导致某些服务器无法访问其他服务器。
# 
# 请你以任意顺序返回该集群内的所有 关键连接 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# 输出：[[1,3]]
# 解释：[[3,1]] 也是正确的。
# 
# 示例 2:
# 
# 输入：n = 2, connections = [[0,1]]
# 输出：[[0,1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= n <= 10^5
# n - 1 <= connections.length <= 10^5
# 0 <= ai, bi <= n - 1
# ai != bi
# 不存在重复的连接
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

# tarjan 
# 割边（bridge，桥）：删除一条边后连通分量增加了
# low[x]: 以x为根的子树通过不在dfs树上的边（即back edge)，能够到达x子树上节点的最小时间戳。
# 根据定义, 当time[x] < low[y]时，说明y无法通过不在dfs树上的边回到x或x的祖先节点，说明边(x,y)是割边; time[x] == low[y]说明y还是可以回到x，所以不是割边；
# 更新low[x]时，如果遇到back edge(x,y)，且y不是x的父亲，则可以用最小的time[y]更新low[x]。（可能有多个满足条件的y）

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        for x,y in connections:
            g[x].append(y)
            g[y].append(x)

        ans = []
        self.time = 0
        time = [0] * n
        low = [0] * n
        def dfs(x, fa):
            self.time += 1
            time[x] = low[x] = self.time
            for y in g[x]:
                if not time[y]:
                    dfs(y,x)
                    low[x] = min(low[x], low[y])
                    if time[x] < low[y]:
                        ans.append([x,y])
                elif y != fa:
                    low[x] = min(low[x], time[y]) #这里写成low[y]也正确，因为此时low[y]==time[y]
        dfs(0,-1)
        return ans



# @lc code=end



#
# @lcpr case=start
# 4\n[[0,1],[1,2],[2,0],[1,3]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[0,1]]\n
# @lcpr case=end

#

