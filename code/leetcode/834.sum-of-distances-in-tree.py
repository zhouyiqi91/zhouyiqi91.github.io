#
# @lc app=leetcode.cn id=834 lang=python3
# @lcpr version=30204
#
# [834] 树中距离之和
#
# https://leetcode.cn/problems/sum-of-distances-in-tree/description/
#
# algorithms
# Hard (61.27%)
# Likes:    510
# Dislikes: 0
# Total Accepted:    29.9K
# Total Submissions: 48.8K
# Testcase Example:  '6\n[[0,1],[0,2],[2,3],[2,4],[2,5]]'
#
# 给定一个无向、连通的树。树中有 n 个标记为 0...n-1 的节点以及 n-1 条边 。
# 
# 给定整数 n 和数组 edges ， edges[i] = [ai, bi]表示树中的节点 ai 和 bi 之间有一条边。
# 
# 返回长度为 n 的数组 answer ，其中 answer[i] 是树中第 i 个节点与所有其他节点之间的距离之和。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 输入: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# 输出: [8,12,6,10,10,10]
# 解释: 树如图所示。
# 我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5) 
# 也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。
# 
# 
# 示例 2:
# 
# 输入: n = 1, edges = []
# 输出: [0]
# 
# 
# 示例 3:
# 
# 输入: n = 2, edges = [[1,0]]
# 输出: [1,1]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= n <= 3 * 10^4
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# 给定的输入保证为有效的树
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
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        self.s = 0
        size = [0] * n
        def dfs(x, fa, s):
            s += 1
            cur = 1
            for y in g[x]:
                if y != fa:
                    self.s += s
                    cur += dfs(y,x,s)
            size[x] = cur
            return cur
        dfs(0,-1,0)

        ans = [0] * n
        ans[0] = self.s
        def reroot(x, fa, s):
            for y in g[x]:
                if y != fa:
                    ans[y] = ans[x] - size[y] + n - size[y]
                    reroot(y,x,ans[y])
        reroot(0,-1,self.s)
        return ans





# @lc code=end



#
# @lcpr case=start
# 6\n[[0,1],[0,2],[2,3],[2,4],[2,5]]\n
# @lcpr case=end

# @lcpr case=start
# 1\n[]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

#

