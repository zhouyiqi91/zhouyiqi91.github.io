#
# @lc app=leetcode.cn id=127 lang=python3
# @lcpr version=30204
#
# [127] 单词接龙
#
# https://leetcode.cn/problems/word-ladder/description/
#
# algorithms
# Hard (48.89%)
# Likes:    1387
# Dislikes: 0
# Total Accepted:    222.5K
# Total Submissions: 454.5K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 字典 wordList 中从单词 beginWord 到 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 ->
# s2 -> ... -> sk：
# 
# 
# 每一对相邻的单词只差一个字母。
# 对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
# sk == endWord
# 
# 
# 给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列
# 中的 单词数目 。如果不存在这样的转换序列，返回 0 。
# 
# 
# 示例 1：
# 
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# 输出：5
# 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
# 
# 
# 示例 2：
# 
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# 输出：0
# 解释：endWord "cog" 不在字典中，所以无法进行转换。
# 
# 
# 
# 提示：
# 
# 
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord、endWord 和 wordList[i] 由小写英文字母组成
# beginWord != endWord
# wordList 中的所有字符串 互不相同
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

# 优化建图：使用虚拟节点，这样建图复杂度O(nC),比两两比较少一个n
class Solution1:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList: return 0
        wordList.add(beginWord)
        g = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                sub = w[:i] + '*' + w[i+1:]
                g[sub].append(w)
                g[w].append(sub)

        q = deque([beginWord])
        dis = 0
        vis = defaultdict(int)
        vis[beginWord] = True
        while q:
            dis += 1
            for _ in range(len(q)):
                x = q.pop()
                for y in g[x]:
                    if not vis[y]:
                        if y==endWord: return dis//2 + 1
                        vis[y] = True
                        q.appendleft(y)
        return 0
    
# 双向广搜优化 用1和2来标记两个方向的点，队列中也要存储方向。如果碰到已经搜索的点的方向跟当前方向不同，说明相遇。
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList: return 0
        wordList.add(beginWord)
        g = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                sub = w[:i] + '*' + w[i+1:]
                g[sub].append(w)
                g[w].append(sub)
        
        q = deque([(beginWord,1),(endWord,2)])
        dis = 0
        vis = defaultdict(int)
        vis[beginWord] = 1
        vis[endWord] = 2
        while q:
            dis += 1
            for _ in range(len(q)):
                x, flag = q.pop()
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = flag
                        q.appendleft((y,flag))
                    elif vis[y] != flag:
                        return dis + 1
        return 0


# @lc code=end



#
# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]\n
# @lcpr case=end

# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log"]\n
# @lcpr case=end

#

