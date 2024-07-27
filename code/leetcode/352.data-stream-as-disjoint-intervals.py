#
# @lc app=leetcode.cn id=352 lang=python3
# @lcpr version=30204
#
# [352] 将数据流变为多个不相交区间
#
# https://leetcode.cn/problems/data-stream-as-disjoint-intervals/description/
#
# algorithms
# Hard (66.81%)
# Likes:    200
# Dislikes: 0
# Total Accepted:    26.8K
# Total Submissions: 40.1K
# Testcase Example:  '["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]\n' +
  '[[],[1],[],[3],[],[7],[],[2],[],[6],[]]'
#
#  给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。
# 
# 实现 SummaryRanges 类：
# 
# 
# 
# 
# SummaryRanges() 使用一个空数据流初始化对象。
# void addNum(int val) 向数据流中加入整数 val 。
# int[][] getIntervals() 以不相交区间 [starti, endi] 的列表形式返回对数据流中整数的总结。
# 
# 
# 
# 
# 示例：
# 
# 输入：
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals",
# "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# 输出：
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7,
# 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
# 
# 解释：
# SummaryRanges summaryRanges = new SummaryRanges();
# summaryRanges.addNum(1);      // arr = [1]
# summaryRanges.getIntervals(); // 返回 [[1, 1]]
# summaryRanges.addNum(3);      // arr = [1, 3]
# summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      // arr = [1, 3, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= val <= 10^4
# 最多调用 addNum 和 getIntervals 方法 3 * 10^4 次
# 
# 
# 
# 
# 
# 
# 进阶：如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?
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
# 有序集合
from sortedcontainers import SortedList
class SummaryRanges:

    def __init__(self):
        self.sl = SortedList()

    def addNum(self, value: int) -> None:
        if value not in self.sl:
            self.sl.add(value)

    def getIntervals(self) -> List[List[int]]:
        i = 0
        sl = self.sl
        n = len(sl)
        res = []
        while i<n:
            start = i
            while i<n-1 and sl[i+1] == sl[i] + 1:
                i += 1
            res.append([sl[start],sl[i]])
            i += 1
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
# @lc code=end



#
# @lcpr case=start
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum","getIntervals", "addNum", "getIntervals"][[], [1], [], [3], [], [7], [], [2], [], [6], []]\n
# @lcpr case=end

#

