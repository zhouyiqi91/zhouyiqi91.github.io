#
# @lc app=leetcode.cn id=212 lang=python3
# @lcpr version=30204
#
# [212] 单词搜索 II
#
# https://leetcode.cn/problems/word-search-ii/description/
#
# algorithms
# Hard (43.16%)
# Likes:    874
# Dislikes: 0
# Total Accepted:    109.6K
# Total Submissions: 253.9K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
  '["oath","pea","eat","rain"]'
#
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。
# 
# 单词必须按照字母顺序，通过 相邻的单元格
# 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
# 
# 
# 
# 示例 1：
# 
# 输入：board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
# 
# 
# 示例 2：
# 
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] 是一个小写英文字母
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] 由小写英文字母组成
# words 中的所有字符串互不相同
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
         
        
      
# 思路 字典树 从字典树中及时移除已经发现的单词

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ''

    def add(self, word):
        node = self
        for c in word:
            node = node.children[c]
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        for word in words:
            t.add(word)
        
        DX = [0,0,1,-1]
        DY = [-1,1,0,0]
        m,n=len(board),len(board[0])
        ans = []
        def dfs(x,y,node):
            c = board[x][y]
            if not c in node.children: return
            nxt = node.children[c]
            board[x][y] = '#'
            if nxt.word:
                ans.append(nxt.word)
                nxt.word = ""
            for dx,dy in zip(DX,DY):
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n:
                    dfs(nx,ny,nxt)
            board[x][y] = c
            if not nxt.children:
                del node.children[c]

        for x in range(m):
            for y in range(n):
                dfs(x,y,t)
        return sorted(ans)
# @lc code=end



#
# @lcpr case=start
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n["oath","pea","eat","rain"]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"],["c","d"]]\n["abcb"]\n
# @lcpr case=end

#

