#
# @lc app=leetcode.cn id=140 lang=python3
# @lcpr version=30204
#
# [140] 单词拆分 II
#
# https://leetcode.cn/problems/word-break-ii/description/
#
# algorithms
# Hard (59.12%)
# Likes:    752
# Dislikes: 0
# Total Accepted:    101.8K
# Total Submissions: 172.1K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 给定一个字符串 s 和一个字符串字典 wordDict ，在字符串 s 中增加空格来构建一个句子，使得句子中所有的单词都在词典中。以任意顺序
# 返回所有这些可能的句子。
# 
# 注意：词典中的同一个单词可能在分段中被重复使用多次。
# 
# 
# 
# 示例 1：
# 
# 输入:s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# 输出:["cats and dog","cat sand dog"]
# 
# 
# 示例 2：
# 
# 输入:s = "pineapplepenapple", wordDict =
# ["apple","pen","applepen","pine","pineapple"]
# 输出:["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# 解释: 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入:s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# 输出:[]
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s 和 wordDict[i] 仅有小写英文字母组成
# wordDict 中所有字符串都 不同
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
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        path = []
        ans = []
        d = set(wordDict)
        n = len(s)
        def dfs(i, pre):
            if i==n:
                if pre == n:
                    ans.append(" ".join(path))
                return
            if s[pre:i+1] in d:
                path.append(s[pre:i+1])
                dfs(i+1,i+1)
                path.pop()
            dfs(i+1, pre)

        dfs(0,0)
        return ans
            
    

# @lc code=end



#
# @lcpr case=start
# "catsanddog"\n["cat","cats","and","sand","dog"]\n
# @lcpr case=end

# @lcpr case=start
# "pineapplepenapple"\n["apple","pen","applepen","pine","pineapple"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats","dog","sand","and","cat"]\n
# @lcpr case=end

#

