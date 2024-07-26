#
# @lc app=leetcode.cn id=126 lang=python3
# @lcpr version=30204
#
# [126] 单词接龙 II
#
# https://leetcode.cn/problems/word-ladder-ii/description/
#
# algorithms
# Hard (36.80%)
# Likes:    718
# Dislikes: 0
# Total Accepted:    60K
# Total Submissions: 163K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord ->
# s1 -> s2 -> ... -> sk 这样的单词序列，并满足：
# 
# 
# 
# 
# 每对相邻的单词之间仅有单个字母不同。
# 转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList
# 中的单词。
# sk == endWord
# 
# 
# 给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。请你找出并返回所有从 beginWord 到 endWord 的
# 最短转换序列 ，如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk]
# 的形式返回。
# 
# 
# 
# 示例 1：
# 
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# 输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# 解释：存在 2 种最短的转换序列：
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
# 
# 
# 示例 2：
# 
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# 输出：[]
# 解释：endWord "cog" 不在字典 wordList 中，所以不存在符合要求的转换序列。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= beginWord.length <= 5
# endWord.length == beginWord.length
# 1 <= wordList.length <= 500
# wordList[i].length == beginWord.length
# beginWord、endWord 和 wordList[i] 由小写英文字母组成
# beginWord != endWord
# wordList 中的所有单词 互不相同
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

# 思路 记录所有BFS路径，使用pre记录所有上一个节点，然后dfs获取路径
class Solution1:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        se = set(wordList)
        if endWord not in se: return []
        # 因为beginword可能在wordlist中,所以可能会有重复
        if beginWord not in set(wordList):
            wordList.append(beginWord)

        def isconnected(x,y):
            res = 0
            for c1,c2 in zip(x,y):
                if c1 != c2:
                    res += 1
                    if res > 1:
                        return False
            return True

        g = defaultdict(list)
        n = len(wordList)
        for i in range(n):
            for j in range(i+1,n):
                ci,cj = wordList[i], wordList[j]
                if isconnected(ci,cj):
                    g[ci].append(cj)
                    g[cj].append(ci)
        
        pre = defaultdict(list)
        q = {beginWord}
        found = False
        vis = defaultdict(int)
        vis[beginWord] = True
        while q:
            nxt = set() #存储新加入的节点
            for x in q:
                for y in g[x]:
                    if not vis[y]:
                        pre[y].append(x)
                        vis[y] = True
                        nxt.add(y)
                        if y == endWord:
                            found = True
                    elif y in nxt:
                        pre[y].append(x)
            if found: break
            q = nxt

        path = [endWord]
        ans = []
        def dfs(x):
            if x==beginWord:
                ans.append(path[::-1])
                return
            for y in pre[x]:
                path.append(y)
                dfs(y)
                path.pop()
                    
        dfs(endWord)
        return ans

# 优化建图，速度加快
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList: return []
        wordList.add(beginWord)
        g = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                t = word[:i] + '*' + word[i+1:]
                g[t].append(word)
                g[word].append(t)
        
        # BFS
        q = set([beginWord])
        vis = defaultdict(int)
        vis[beginWord] = 1
        pre = defaultdict(set)
        found = False
        while q:
            nxt = set()
            for x in q:
                for y in g[x]:
                    if y in nxt:
                        pre[y].add(x)
                    elif not vis[y]:
                        pre[y].add(x)
                        nxt.add(y)
                        vis[y] = 1
                        if y == endWord: found = True
            if found: break
            q = nxt
        if not found: return []

        # dfs
        ans = []
        path = []
        def dfs(x):
            if x in wordList: path.append(x) #由于加了*号
            if x==beginWord:
                ans.append(path[::-1])
                path.pop()
                return 
            for y in pre[x]:
                dfs(y)
            if x in wordList: path.pop()
        dfs(endWord)
        return ans
# @lc code=end



#
# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]\n
# @lcpr case=end

# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log"]\n
# @lcpr case=end

#

