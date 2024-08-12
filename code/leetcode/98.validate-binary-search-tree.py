#
# @lc app=leetcode.cn id=98 lang=python3
# @lcpr version=30204
#
# [98] 验证二叉搜索树
#
# https://leetcode.cn/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (38.18%)
# Likes:    2391
# Dislikes: 0
# Total Accepted:    963.4K
# Total Submissions: 2.5M
# Testcase Example:  '[2,1,3]'
#
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
# 
# 有效 二叉搜索树定义如下：
# 
# 
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：root = [2,1,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目范围在[1, 10^4] 内
# -2^31 <= Node.val <= 2^31 - 1
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(x, low, high):
            if not x: return True
            return low < x.val < high and dfs(x.left, low, x.val) and dfs(x.right, x.val, high)

        return dfs(root, -inf, inf)
# @lc code=end



#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,4,null,null,3,6]\n
# @lcpr case=end

#

