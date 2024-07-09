#
# @lc app=leetcode.cn id=1782 lang=python3
# @lcpr version=30204
#
# [1782] 统计点对的数目
#
# https://leetcode.cn/problems/count-pairs-of-nodes/description/
#
# algorithms
# Hard (54.25%)
# Likes:    171
# Dislikes: 0
# Total Accepted:    13.4K
# Total Submissions: 24.7K
# Testcase Example:  '4\n[[1,2],[2,4],[1,3],[2,3],[2,1]]\n[2,3]'
#
# 给你一个无向图，无向图由整数 n  ，表示图中节点的数目，和 edges 组成，其中 edges[i] = [ui, vi] 表示 ui 和 vi
# 之间有一条无向边。同时给你一个代表查询的整数数组 queries 。
# 
# 第 j 个查询的答案是满足如下条件的点对 (a, b) 的数目：
# 
# 
# a < b
# cnt 是与 a 或者 b 相连的边的数目，且 cnt 严格大于 queries[j] 。
# 
# 
# 请你返回一个数组 answers ，其中 answers.length == queries.length 且 answers[j] 是第 j
# 个查询的答案。
# 
# 请注意，图中可能会有 多重边 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
# 输出：[6,5]
# 解释：每个点对中，与至少一个点相连的边的数目如上图所示。
# answers[0] = 6。所有的点对(a, b)中边数和都大于2，故有6个；
# answers[1] = 5。所有的点对(a, b)中除了(3,4)边数等于3，其它点对边数和都大于3，故有5个。
# 
# 
# 示例 2：
# 
# 输入：n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries
# = [1,2,3,4,5]
# 输出：[10,10,9,8,6]
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= n <= 2 * 10^4
# 1 <= edges.length <= 10^5
# 1 <= ui, vi <= n
# ui != vi
# 1 <= queries.length <= 20
# 0 <= queries[j] < edges.length
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
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
# @lc code=end



#
# @lcpr case=start
# 4\n[[1,2],[2,4],[1,3],[2,3],[2,1]]\n[2,3]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]]\n[1,2,3,4,5]\n
# @lcpr case=end

#

