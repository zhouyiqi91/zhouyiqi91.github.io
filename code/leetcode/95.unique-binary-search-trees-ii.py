#
# @lc app=leetcode.cn id=95 lang=python3
# @lcpr version=30204
#
# [95] 不同的二叉搜索树 II
#
# https://leetcode.cn/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (74.06%)
# Likes:    1566
# Dislikes: 0
# Total Accepted:    193.9K
# Total Submissions: 261.7K
# Testcase Example:  '3'
#
# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：n = 3
# 输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
# 
# 
# 示例 2：
# 
# 输入：n = 1
# 输出：[[1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 8
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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dp(l,r):
            if l>r: return [None]
            if l==r: return [TreeNode(l)]
            res = []
            for val in range(l, r+1):
                for left in dp(l, val-1):
                    for right in dp(val+1, r):
                        res.append(TreeNode(val, left=left,right=right))
            return res
        
        return dp(1,n)



# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

