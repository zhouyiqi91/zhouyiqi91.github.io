#
# @lc app=leetcode.cn id=332 lang=python3
# @lcpr version=30204
#
# [332] 重新安排行程
#
# https://leetcode.cn/problems/reconstruct-itinerary/description/
#
# algorithms
# Hard (45.09%)
# Likes:    914
# Dislikes: 0
# Total Accepted:    110.1K
# Total Submissions: 244.7K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# 给你一份航线列表 tickets ，其中 tickets[i] = [fromi, toi]
# 表示飞机出发和降落的机场地点。请你对该行程进行重新规划排序。
# 
# 所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK
# 开始。如果存在多种有效的行程，请你按字典排序返回最小的行程组合。
# 
# 
# 例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前。
# 
# 
# 假定所有机票至少存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。
# 
# 
# 
# 示例 1：
# 
# 输入：tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# 输出：["JFK","MUC","LHR","SFO","SJC"]
# 
# 
# 示例 2：
# 
# 输入：tickets =
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# 输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
# 解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"] ，但是它字典排序更大更靠后。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi 和 toi 由大写英文字母组成
# fromi != toi
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

# 欧拉路径
# 1. 遍历时删除边
# 2. 遍历完所有邻居后再记录节点。这样死胡同上的节点最先被记录，因为不会返回当前节点。返回当前节点的路径不会先被记录，因为当前节点还没有遍历结束。
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        for x,y in tickets:
            g[x].append(y)
        for x in g:
            g[x].sort(reverse=True)
        
        st = []
        def dfs(x):
            while g[x]:
                dfs(g[x].pop())
            st.append(x)

        dfs("JFK")
        return st[::-1]

# @lc code=end



#
# @lcpr case=start
# [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]\n
# @lcpr case=end

# @lcpr case=start
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]\n
# @lcpr case=end

#

