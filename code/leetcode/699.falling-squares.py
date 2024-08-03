#
# @lc app=leetcode.cn id=699 lang=python3
# @lcpr version=30204
#
# [699] 掉落的方块
#
# https://leetcode.cn/problems/falling-squares/description/
#
# algorithms
# Hard (54.65%)
# Likes:    195
# Dislikes: 0
# Total Accepted:    25.8K
# Total Submissions: 46.6K
# Testcase Example:  '[[1,2],[2,3],[6,1]]'
#
# 在二维平面上的 x 轴上，放置着一些方块。
# 
# 给你一个二维整数数组 positions ，其中 positions[i] = [lefti, sideLengthi] 表示：第 i 个方块边长为
# sideLengthi ，其左侧边与 x 轴上坐标点 lefti 对齐。
# 
# 每个方块都从一个比目前所有的落地方块更高的高度掉落而下。方块沿 y 轴负方向下落，直到着陆到 另一个正方形的顶边 或者是 x 轴上
# 。一个方块仅仅是擦过另一个方块的左侧边或右侧边不算着陆。一旦着陆，它就会固定在原地，无法移动。
# 
# 在每个方块掉落后，你必须记录目前所有已经落稳的 方块堆叠的最高高度 。
# 
# 返回一个整数数组 ans ，其中 ans[i] 表示在第 i 块方块掉落后堆叠的最高高度。
# 
# 
# 
# 示例 1：
# 
# 输入：positions = [[1,2],[2,3],[6,1]]
# 输出：[2,5,5]
# 解释：
# 第 1 个方块掉落后，最高的堆叠由方块 1 组成，堆叠的最高高度为 2 。
# 第 2 个方块掉落后，最高的堆叠由方块 1 和 2 组成，堆叠的最高高度为 5 。
# 第 3 个方块掉落后，最高的堆叠仍然由方块 1 和 2 组成，堆叠的最高高度为 5 。
# 因此，返回 [2, 5, 5] 作为答案。
# 
# 
# 示例 2：
# 
# 输入：positions = [[100,100],[200,100]]
# 输出：[100,100]
# 解释：
# 第 1 个方块掉落后，最高的堆叠由方块 1 组成，堆叠的最高高度为 100 。
# 第 2 个方块掉落后，最高的堆叠可以由方块 1 组成也可以由方块 2 组成，堆叠的最高高度为 100 。
# 因此，返回 [100, 100] 作为答案。
# 注意，方块 2 擦过方块 1 的右侧边，但不会算作在方块 1 上着陆。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= positions.length <= 1000
# 1 <= lefti <= 10^8
# 1 <= sideLengthi <= 10^6
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

# 思路：动态开点线段树，注意当left与之前的right相等时，或者right与之前left相等时，不会堆叠而是落下，所以right统一减一

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
        self.lazy = 0

class SegmentTree:
    def __init__(self, left=0, right=10**9, a=None):
        self.root = Node(left,right)
        self.merge = max # 修改:合并函数
            
    # 修改节点和lazy的值
    def do(self, node, x):
        node.v = self.merge(node.v, x)
        node.lazy = self.merge(node.lazy, x) # 为什么lazy也需要max

    # 从p的left和right，向上更新p的区间值
    def pushup(self, node):
        node.v = self.merge(node.lc.v, node.rc.v)

    def pushdown(self, node):
        if node.lc is None:
            node.lc = Node(node.l, node.mid)
        if node.rc is None:
            node.rc = Node(node.mid+1, node.r)
        if node.lazy: # 之前修改过lazy，需要向下传递
            self.do(node.lc, node.lazy)
            self.do(node.rc, node.lazy)
            node.lazy = 0

    # 从根节点出发，递归找到叶子节点，然后从下往上更新
    def update(self, l, r, x, node=None):
        if node is None:
            node = self.root
        if l<=node.l and node.r<=r: 
            self.do(node, x)
            return
        self.pushdown(node)
        if l <= node.mid: self.update(l,r,x,node.lc)
        if node.mid < r:  self.update(l,r,x,node.rc)
        self.pushup(node)

    # 返回当前节点代表的区间与查询区间[l,r]交集的区间值
    def query(self,l,r,node=None):
        if node is None: node=self.root
        if r < l: return 0 # 边界情况
        if l<=node.l and node.r <= r: return node.v
        self.pushdown(node)
        res_left = res_right = 0 #视function要更改
        if l <= node.mid: res_left = self.query(l,r,node.lc)
        if r > node.mid: res_right = self.query(l,r,node.rc)
        return self.merge(res_left,res_right) 

class Solution1:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        seg = SegmentTree()
        hmax = 0
        ans = []
        for left,side in positions:
            right = left + side
            h = seg.query(left, right-1)
            cur = h + side
            hmax = max(hmax, cur)
            ans.append(hmax)
            seg.update(left,right-1,cur)
        return ans
    
# 思路 有序集合


# @lc code=end



#
# @lcpr case=start
# [[1,2],[2,3],[6,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[100,100],[200,100]]\n
# @lcpr case=end

#

