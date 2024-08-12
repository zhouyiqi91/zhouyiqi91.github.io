#
# @lc app=leetcode.cn id=676 lang=python3
# @lcpr version=30204
#
# [676] 实现一个魔法字典
#
# https://leetcode.cn/problems/implement-magic-dictionary/description/
#
# algorithms
# Medium (65.27%)
# Likes:    239
# Dislikes: 0
# Total Accepted:    44.7K
# Total Submissions: 67.8K
# Testcase Example:  '["MagicDictionary", "buildDict", "search", "search", "search", "search"]\n' +
#  '[[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]'
#
# 设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 互不相同 。
# 如果给出一个单词，请判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。
# 
# 实现 MagicDictionary 类：
# 
# 
# MagicDictionary() 初始化对象
# void buildDict(String[] dictionary) 使用字符串数组 dictionary 设定该数据结构，dictionary
# 中的字符串互不相同
# bool search(String searchWord) 给定一个字符串 searchWord ，判定能否只将字符串中 一个
# 字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 true ；否则，返回 false 。
# 
# 
# 
# 
# 
# 
# 
# 示例：
# 
# 输入
# ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
# [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
# 输出
# [null, null, false, true, false, false]
# 
# 解释
# MagicDictionary magicDictionary = new MagicDictionary();
# magicDictionary.buildDict(["hello", "leetcode"]);
# magicDictionary.search("hello"); // 返回 False
# magicDictionary.search("hhllo"); // 将第二个 'h' 替换为 'e' 可以匹配 "hello" ，所以返回 True
# magicDictionary.search("hell"); // 返回 False
# magicDictionary.search("leetcoded"); // 返回 False
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= dictionary.length <= 100
# 1 <= dictionary[i].length <= 100
# dictionary[i] 仅由小写英文字母组成
# dictionary 中的所有字符串 互不相同
# 1 <= searchWord.length <= 100
# searchWord 仅由小写英文字母组成
# buildDict 仅在 search 之前调用一次
# 最多调用 100 次 search
# 
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

# 字典树优化查找
class Trie:
    __slots__ = ['children','isWord']
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isWord = False
    
    def add(self, word):
        node = self
        for c in word:
            node = node.children[c]
        node.isWord = True

    def search(self, word, pos, change):
        if pos==len(word):
            return change == 0 and self.isWord
        res = False
        c = word[pos]
        if c in self.children:
            if self.children[c].search(word, pos+1, change):
                return True
        if change == 1:
            for x in self.children:
                if x != c and self.children[x].search(word, pos+1, 0):
                    return True
        return False


class MagicDictionary:

    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.add(word)


    def search(self, searchWord: str) -> bool:
        return self.trie.search(searchWord, 0, 1)



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end



