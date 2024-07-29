#
# @lc app=leetcode.cn id=327 lang=python3
# @lcpr version=30204
#
# [327] 区间和的个数
#
# https://leetcode.cn/problems/count-of-range-sum/description/
#
# algorithms
# Hard (40.38%)
# Likes:    586
# Dislikes: 0
# Total Accepted:    46.9K
# Total Submissions: 116K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# 给你一个整数数组 nums 以及两个整数 lower 和 upper 。求数组中，值位于范围 [lower, upper] （包含 lower 和
# upper）之内的 区间和的个数 。
# 
# 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
# 
# 
# 示例 1：
# 
# 输入：nums = [-2,5,-1], lower = -2, upper = 2
# 输出：3
# 解释：存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。
# 
# 
# 示例 2：
# 
# 输入：nums = [0], lower = 0, upper = 0
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# -10^5 <= lower <= upper <= 10^5
# 题目数据保证答案是一个 32 位 的整数
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

# 有序集合
from sortedcontainers import SortedList
class Solution1:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        s = 0
        ans = 0
        sl = SortedList()
        sl.add(0)
        for x in nums:
            s += x
            r = sl.bisect_right(s-lower) - 1
            l = sl.bisect_left(s-upper)
            ans += r-l+1
            sl.add(s)
        return ans

# 基础线段树，值域TODO

class Node:
    # lc:left_child
    __slots__ = ['l','r','mid', 'lc','rc','v','lazy']
    def __init__(self, l, r, v=0):
        self.l = l
        self.r = r
        self.mid = l+r>>1
        self.lc = None
        self.rc = None
        self.v = v
class SegmentTree:
    def __init__(self, left=0, right=10**9, a=None):
        self.root = Node(left,right)
        if a:
            self.a = a
            self.build(self.root)

    def build(self, node):
        # TODO
        self.pushdown(node)
            
    def pushdown(self, node):
        if node.lc is None: 
            node.lc = Node(node.l, node.mid)
        if node.rc is None: 
            node.rc = Node(node.mid+1, node.r)

    def pushup(self, node):
        node.v = node.lc.v + node.rc.v

    # 从根节点出发，递归找到叶子节点，然后从下往上更新
    def add(self, pos, val, node=None):
        if node is None: node = self.root
        if node.l == node.r: #叶子节点
            node.v += val
            return
        self.pushdown(node)
        if pos <= node.mid:  self.add(pos, val, node.lc)
        else:                self.add(pos, val, node.rc)
        self.pushup(node)

    # 返回当前节点代表的区间与查询区间[l,r]交集的区间值
    def ask(self,l,r,node=None):
        if node is None: node=self.root
        if l<=node.l and node.r <= r: return node.v
        self.pushdown(node)
        res_left = res_right = 0 #视function要更改
        if l <= node.mid: res_left = self.ask(l,r,node.lc)
        if r > node.mid: res_right = self.ask(l,r,node.rc)
        return res_left + res_right    

class Solution1:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        seg = SegmentTree(left=-2**31,right=2**31)
        seg.add(0,1)
        s = 0
        ans = 0
        for x in nums:
            s += x
            res = seg.ask(s-upper,s-lower)
            ans += res
            seg.add(s,1)
        return ans


# @lc code=end



#
# @lcpr case=start
# [-2,5,-1]\n-2\n2\n
# @lcpr case=end

# @lcpr case=start
# [0]\n0\n0\n
# @lcpr case=end

#

