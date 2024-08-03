#
# @lc app=leetcode.cn id=432 lang=python3
# @lcpr version=30204
#
# [432] 全 O(1) 的数据结构
#
# https://leetcode.cn/problems/all-oone-data-structure/description/
#
# algorithms
# Hard (46.43%)
# Likes:    319
# Dislikes: 0
# Total Accepted:    30.8K
# Total Submissions: 66.3K
# Testcase Example:  '["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]\n' +
# '[[],["hello"],["hello"],[],[],["leet"],[],[]]'
#
# 请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。
# 
# 实现 AllOne 类：
# 
# 
# AllOne() 初始化数据结构的对象。
# inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
# dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key
# 从数据结构中删除。测试用例保证：在减少计数前，key 存在于数据结构中。
# getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
# getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。
# 
# 
# 注意：每个函数都应当满足 O(1) 平均时间复杂度。
# 
# 
# 
# 示例：
# 
# 输入
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey",
# "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# 输出
# [null, null, null, "hello", "hello", null, "hello", "leet"]
# 
# 解释
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // 返回 "hello"
# allOne.getMinKey(); // 返回 "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // 返回 "hello"
# allOne.getMinKey(); // 返回 "leet"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= key.length <= 10
# key 由小写英文字母组成
# 测试用例保证：在每次调用 dec 时，数据结构中总存在 key
# 最多调用 inc、dec、getMaxKey 和 getMinKey 方法 5 * 10^4 次
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

# 思路 双向链表，类似LFU(least frequently used)
class Node:
    __slots__ = ['nxt','pre','count','strs']
    def __init__(self, count=0, nxt=None, pre=None, strs=set()):
        self.nxt = nxt
        self.pre = pre
        self.count = count
        self.strs = strs

    # self后插入node
    def insert(self, node): 
        nxt = self.nxt
        self.nxt = node
        node.pre = self
        node.nxt = nxt
        nxt.pre = node

    # 移除self
    def remove(self):
        self.pre.nxt = self.nxt
        self.nxt.pre = self.pre

class AllOne:

    def __init__(self):
        self.d1 = Node()
        self.d2 = Node(pre=self.d1)
        self.d1.nxt = self.d2
        self.nodes = {}

    def inc(self, key: str) -> None:
        if key not in self.nodes:
            if self.d1.nxt.count != 1:
                self.d1.insert(Node(count=1, strs=set([key])))
            else:
                self.d1.nxt.strs.add(key)
            self.nodes[key] = self.d1.nxt
        else:
            cur = self.nodes[key]
            if cur.nxt.count != cur.count + 1:
                cur.insert(Node(count=cur.count+1, strs=set([key])))
            else:
                cur.nxt.strs.add(key)
            self.nodes[key] = cur.nxt
            cur.strs.remove(key)
            if len(cur.strs) == 0:
                cur.remove()

    def dec(self, key: str) -> None:
        cur = self.nodes[key]
        cur.strs.remove(key)
        if cur.count > 1:
            if cur.pre.count != cur.count - 1:
                cur.pre.insert(Node(count=cur.count-1,strs=set([key])))
            else:
                cur.pre.strs.add(key)
            self.nodes[key] = cur.pre
        else:
            del self.nodes[key]
        if len(cur.strs) == 0:
            cur.remove()       


    def getMaxKey(self) -> str:
        if self.d2.pre.count > 0:
            return list(self.d2.pre.strs)[0]
        return ""

    def getMinKey(self) -> str:
        if self.d1.nxt.count > 0:
            return list(self.d1.nxt.strs)[0]
        return ""



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end



