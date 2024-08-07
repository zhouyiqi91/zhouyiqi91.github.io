#
# @lc app=leetcode.cn id=1146 lang=python3
# @lcpr version=30204
#
# [1146] 快照数组
#
# https://leetcode.cn/problems/snapshot-array/description/
#
# algorithms
# Medium (37.21%)
# Likes:    173
# Dislikes: 0
# Total Accepted:    26.5K
# Total Submissions: 71.2K
# Testcase Example:  '["SnapshotArray","set","snap","set","get"]\n[[3],[0,5],[],[0,6],[0,0]]'
#
# 实现支持下列接口的「快照数组」- SnapshotArray：
# 
# 
# SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
# void set(index, val) - 会将指定索引 index 处的元素设置为 val。
# int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
# int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。
# 
# 
# 
# 
# 示例：
# 
# 输入：["SnapshotArray","set","snap","set","get"]
# ⁠    [[3],[0,5],[],[0,6],[0,0]]
# 输出：[null,null,0,null,5]
# 解释：
# SnapshotArray snapshotArr = new SnapshotArray(3); // 初始化一个长度为 3 的快照数组
# snapshotArr.set(0,5);  // 令 array[0] = 5
# snapshotArr.snap();  // 获取快照，返回 snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5
# 
# 
# 
# 提示：
# 
# 
# 1 <= length <= 50000
# 题目最多进行50000 次set，snap，和 get的调用 。
# 0 <= index < length
# 0 <= snap_id < 我们调用 snap() 的总次数
# 0 <= val <= 10^9
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
class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.index_id_val = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        self.index_id_val[index].append((self.id, val))

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        a = self.index_id_val[index]
        i = bisect_right(a, snap_id, key=lambda x:x[0]) - 1
        if i == -1: return 0
        return a[i][1]



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end



#
# @lcpr case=start
# ["SnapshotArray","set","snap","set","get"][[3],[0,5],[],[0,6],[0,0]]\n
# @lcpr case=end

#

