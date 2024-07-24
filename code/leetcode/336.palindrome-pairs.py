#
# @lc app=leetcode.cn id=336 lang=python3
# @lcpr version=30204
#
# [336] 回文对
#
# https://leetcode.cn/problems/palindrome-pairs/description/
#
# algorithms
# Hard (38.17%)
# Likes:    393
# Dislikes: 0
# Total Accepted:    29.6K
# Total Submissions: 77.7K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# 给定一个由唯一字符串构成的 0 索引 数组 words 。
# 
# 回文对 是一对整数 (i, j) ，满足以下条件：
# 
# 
# 0 <= i, j < words.length，
# i != j ，并且
# words[i] + words[j]（两个字符串的连接）是一个回文串。
# 
# 
# 返回一个数组，它包含 words 中所有满足 回文对 条件的字符串。
# 
# 你必须设计一个时间复杂度为 O(sum of words[i].length) 的算法。
# 
# 
# 
# 示例 1：
# 
# 输入：words = ["abcd","dcba","lls","s","sssll"]
# 输出：[[0,1],[1,0],[3,2],[2,4]] 
# 解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
# 
# 
# 示例 2：
# 
# 输入：words = ["bat","tab","cat"]
# 输出：[[0,1],[1,0]] 
# 解释：可拼接成的回文串为 ["battab","tabbat"]
# 
# 示例 3：
# 
# 输入：words = ["a",""]
# 输出：[[0,1],[1,0]]
# 
# 
# 
# 提示：
# 
# 
# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300
# words[i] 由小写英文字母组成
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

# 进制哈希判断前后缀是否是回文
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        base = 131
        MOD = 10**9+7
        offset = ord('a')
        def prefix_palindrome(word):
            res = []
            mul = 1
            left = right = 0
            i = -1
            n = len(word)
            for i,x in enumerate(word):
                x = ord(x) - offset
                left = (left * base + x) % MOD
                right = (right + x * mul) % MOD
                mul = (mul * base) % MOD
                if left == right:
                    res.append(i+1)
            return res

        words = {word: i for i, word in enumerate(words)}
        ans = []

        for word,k in words.items():
            for i in prefix_palindrome(word) + [0]:
                suf = word[i:][::-1]
                if suf in words and (j:=words[suf]) != k:
                    ans.append([j,k])
            n = len(word)
            for i in prefix_palindrome(word[::-1]):
                pre = word[:n-i][::-1]
                if pre in words and (j:=words[pre]) != k:
                    ans.append([k,j])
            
        return ans
# @lc code=end



#
# @lcpr case=start
# ["abcd","dcba","lls","s","sssll"]\n
# @lcpr case=end

# @lcpr case=start
# ["bat","tab","cat"]\n
# @lcpr case=end

# @lcpr case=start
# ["a",""]\n
# @lcpr case=end

#

