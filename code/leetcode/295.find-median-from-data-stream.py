#
# @lc app=leetcode.cn id=295 lang=python3
# @lcpr version=30204
#
# [295] 数据流的中位数
#
# https://leetcode.cn/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (54.65%)
# Likes:    1014
# Dislikes: 0
# Total Accepted:    155.7K
# Total Submissions: 284.2K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
#  '[[],[1],[2],[],[3],[]]'
#
# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
# 
# 
# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 
# 
# 实现 MedianFinder 类:
# 
# 
# 
# MedianFinder() 初始化 MedianFinder 对象。
# 
# 
# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
# 
# 
# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10^-5 以内的答案将被接受。
# 
# 
# 
# 示例 1：
# 
# 输入
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# 输出
# [null, null, null, 1.5, null, 2.0]
# 
# 解释
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
# 
# 提示:
# 
# 
# -10^5 <= num <= 10^5
# 在调用 findMedian 之前，数据结构中至少有一个元素
# 最多 5 * 10^4 次调用 addNum 和 findMedian
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

# 对顶堆
class MedianFinder:
    
    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        if not self.lo or num <= -self.lo[0]:
            heappush(self.lo, -num) # lo是大根堆
        else:
            heappush(self.hi, num)

    def findMedian(self) -> float:
        while len(self.lo) > len(self.hi) + 1:
            heappush(self.hi, -heappop(self.lo))
        while len(self.lo) < len(self.hi):
            heappush(self.lo, -heappop(self.hi))
        if len(self.lo) == len(self.hi):
            return (-self.lo[0] + self.hi[0] ) /2 #不能写右移
        else:
            return -self.lo[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end



