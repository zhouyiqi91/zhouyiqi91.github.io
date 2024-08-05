#
# @lc app=leetcode.cn id=572 lang=python3
# @lcpr version=30204
#
# [572] 另一棵树的子树
#
# https://leetcode.cn/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (47.80%)
# Likes:    1078
# Dislikes: 0
# Total Accepted:    224.2K
# Total Submissions: 462.4K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 
# 
# 给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true
# ；否则，返回 false 。
# 
# 二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。
# 
# 
# 
# 示例 1：
# 
# 输入：root = [3,4,5,1,2], subRoot = [4,1,2]
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# root 树上的节点数量范围是 [1, 2000]
# subRoot 树上的节点数量范围是 [1, 1000]
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def same(self, x, y):
        if x is None or y is None:
            return x is y
        return x.val==y.val and \
            self.same(x.left,y.left) and \
            self.same(x.right,y.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        return self.same(root, subRoot) or \
            self.isSubtree(root.left, subRoot) or \
            self.isSubtree(root.right, subRoot)
        
# @lc code=end



#
# @lcpr case=start
# [3,4,5,1,2]\n[4,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,2,null,null,null,null,0]\n[4,1,2]\n
# @lcpr case=end

#

