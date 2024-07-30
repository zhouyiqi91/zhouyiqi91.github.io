#
# @lc app=leetcode.cn id=530 lang=python3
# @lcpr version=30204
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (62.78%)
# Likes:    575
# Dislikes: 0
# Total Accepted:    263.7K
# Total Submissions: 419.9K
# Testcase Example:  '[4,2,6,1,3]'
#
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 
# 差值是一个正数，其数值等于两值之差的绝对值。
# 
# 
# 
# 示例 1：
# 
# 输入：root = [4,2,6,1,3]
# 输出：1
# 
# 
# 示例 2：
# 
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目范围是 [2, 10^4]
# 0 <= Node.val <= 10^5
# 
# 
# 
# 
# 注意：本题与 783
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
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

# 二叉搜索树中序遍历，同时记录前一个节点的值
class Solution1:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = inf
        pre = -inf
        def dfs(x):
            if not x: return
            nonlocal ans,pre
            dfs(x.left)
            ans = min(ans, x.val - pre)
            pre = x.val
            dfs(x.right)
            
        dfs(root)
        return ans

# yield from写法
# https://discuss.python.org/t/what-is-yield-from/40197
# Exactly what it sounds like: it yields the values from the other source, one at a time, until it runs out. Every time there is a request for the next element from this generator, if there is still something in the other source, it will use that. Otherwise, the logic proceeds.
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return
            yield from dfs(node.left)
            yield node.val
            yield from dfs(node.right)
        
        return min(b - a for a, b in pairwise(dfs(root)))
# @lc code=end



#
# @lcpr case=start
# [4,2,6,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,48,null,null,12,49]\n
# @lcpr case=end

#

