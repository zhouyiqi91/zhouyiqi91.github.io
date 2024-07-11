#
# @lc app=leetcode.cn id=894 lang=python3
# @lcpr version=30204
#
# [894] 所有可能的真二叉树
#
# https://leetcode.cn/problems/all-possible-full-binary-trees/description/
#
# algorithms
# Medium (80.60%)
# Likes:    407
# Dislikes: 0
# Total Accepted:    38.2K
# Total Submissions: 47.4K
# Testcase Example:  '7'
#
# 给你一个整数 n ，请你找出所有可能含 n 个节点的 真二叉树 ，并以列表形式返回。答案中每棵树的每个节点都必须符合 Node.val == 0 。
# 
# 答案的每个元素都是一棵真二叉树的根节点。你可以按 任意顺序 返回最终的真二叉树列表。
# 
# 真二叉树 是一类二叉树，树中每个节点恰好有 0 或 2 个子节点。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 7
# 
# 输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# 
# 
# 示例 2：
# 
# 输入：n = 3
# 输出：[[0,0,0]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 20
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

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0: 
            return []
        @cache
        def dfs(n):
            if n==1: 
                return [TreeNode()]
            res = []
            for nl in range(1,n-1,2):
                nr = n-1-nl
                for left in dfs(nl):
                    for right in dfs(nr):
                        res.append(TreeNode(0,left,right))
            return res
                
        ans = dfs(n)
        return ans

        



# @lc code=end



#
# @lcpr case=start
# 7\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

