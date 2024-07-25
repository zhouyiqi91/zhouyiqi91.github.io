#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30204
#
# [25] K 个一组翻转链表
#
# https://leetcode.cn/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (68.10%)
# Likes:    2363
# Dislikes: 0
# Total Accepted:    630.9K
# Total Submissions: 925.1K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
# 
# 
# 示例 2：
# 
# 
# 
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
# 
# 
# 
# 提示：
# 
# 
# 链表中的节点数目为 n
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
# 
# 
# 
# 
# 进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
# 
# 
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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：反转链表存储当前节点的pre和next，即p0和p2
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = pre = ListNode(next=head)

        def reverse(head):
            p0 = None
            p1 = head
            for _ in range(k):
                p2 = p1.next
                p1.next = p0
                p0,p1 = p1,p2
            return p0, p1

        n = 0
        p = pre
        while p.next:
            p = p.next
            n += 1 
        for _ in range(n//k):
            h = pre.next
            p0,p1 = reverse(h)
            pre.next = p0
            pre = h
            pre.next = p1 # 犯错：next写成hext, 运行并不会报错

        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#

