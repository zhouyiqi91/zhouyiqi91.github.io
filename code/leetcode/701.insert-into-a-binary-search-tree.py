#
# @lc app=leetcode.cn id=701 lang=python3
# @lcpr version=30204
#
# [701] 二叉搜索树中的插入操作
#
# https://leetcode.cn/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (70.06%)
# Likes:    572
# Dislikes: 0
# Total Accepted:    250.5K
# Total Submissions: 357.6K
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# 给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证
# ，新值和原始二叉搜索树中的任意节点值都不同。
# 
# 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。
# 
# 
# 
# 示例 1：
# 
# 输入：root = [4,2,7,1,3], val = 5
# 输出：[4,2,7,1,3,5]
# 解释：另一个满足题目要求可以通过的树是：
# 
# 
# 
# 示例 2：
# 
# 输入：root = [40,20,60,10,30,50,70], val = 25
# 输出：[40,20,60,10,30,50,70,null,null,25]
# 
# 
# 示例 3：
# 
# 输入：root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# 输出：[4,2,7,1,3,5]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数将在 [0, 10^4]的范围内。
# -10^8 <= Node.val <= 10^8
# 所有值 Node.val 是 独一无二 的。
# -10^8 <= val <= 10^8
# 保证 val 在原始BST中不存在。
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

# 递归有返回值，这样不需要记录父节点
class Solution1:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: 
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
    
# 迭代
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        p = root
        while True:
            if val < p.val:
                if p.left is None:
                    p.left = TreeNode(val)
                    break
                else:
                    p = p.left
            else:
                if p.right is None:
                    p.right = TreeNode(val)
                    break
                else:
                    p = p.right
        return root
            

# @lc code=end



#
# @lcpr case=start
# [4,2,7,1,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [40,20,60,10,30,50,70]\n25\n
# @lcpr case=end

# @lcpr case=start
# [4,2,7,1,3,null,null,null,null,null,null]\n5\n
# @lcpr case=end

#

