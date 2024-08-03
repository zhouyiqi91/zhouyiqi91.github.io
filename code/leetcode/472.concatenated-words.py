#
# @lc app=leetcode.cn id=472 lang=python3
# @lcpr version=30204
#
# [472] 连接词
#
# https://leetcode.cn/problems/concatenated-words/description/
#
# algorithms
# Hard (52.00%)
# Likes:    317
# Dislikes: 0
# Total Accepted:    29.3K
# Total Submissions: 56.4K
# Testcase Example:  '["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]'
#
# 给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。
# 
# 连接词 定义为：一个完全由给定数组中的至少两个较短单词（不一定是不同的两个单词）组成的字符串。
# 
# 
# 
# 示例 1：
# 
# 输入：words =
# ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# 输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
# 解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成; 
# ⁠    "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成; 
# ⁠    "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。
# 
# 
# 示例 2：
# 
# 输入：words = ["cat","dog","catdog"]
# 输出：["catdog"]
# 
# 
# 
# 提示：
# 
# 
# 1 <= words.length <= 10^4
# 1 <= words[i].length <= 30
# words[i] 仅由小写英文字母组成。 
# words 中的所有字符串都是 唯一 的。
# 1 <= sum(words[i].length) <= 10^5
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

# 思路 字典树
# 加上__slots__提高速度
# 按长度排序，依次添加，只加非连接词，可以避免从字典树中删除的操作
class Trie:
    __slots__ = ['children','word']
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = False

    def add(self, word):
        node = self
        for c in word:
            node = node.children[c]
        node.word = True


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = sorted(words, key=lambda x:len(x))
        trie = Trie()
        def dfs(i, node):
            if i==n:
                return node.word
            c = word[i]
            if c in node.children:
                node = node.children[c]
                if dfs(i+1, node): return True
                if node.word and dfs(i+1, trie): return True   
            return False       

        ans = []
        for word in words:
            n = len(word)
            if dfs(0, trie):
                ans.append(word)
            else:
                trie.add(word)
        return ans


# @lc code=end



#
# @lcpr case=start
# ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]\n
# @lcpr case=end

# @lcpr case=start
# ["cat","dog","catdog"]\n
# @lcpr case=end

#

