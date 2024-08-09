#
# @lc app=leetcode.cn id=721 lang=python3
# @lcpr version=30204
#
# [721] 账户合并
#
# https://leetcode.cn/problems/accounts-merge/description/
#
# algorithms
# Medium (48.92%)
# Likes:    504
# Dislikes: 0
# Total Accepted:    45.2K
# Total Submissions: 91.5K
# Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
#
# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称
# (name)，其余元素是 emails 表示该账户的邮箱地址。
# 
# 
# 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
# 
# 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是 按字符 ASCII 顺序排列 的邮箱地址。账户本身可以以 任意顺序 返回。
# 
# 
# 
# 示例 1：
# 
# 输入：accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
# "johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
# "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# 输出：[["John", 'john00@mail.com', 'john_newyork@mail.com',
# 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary",
# "mary@mail.com"]]
# 解释：
# 第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。 
# 第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
# 可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
# ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']]
# 也是正确的。
# 
# 
# 示例 2：
# 
# 输入：accounts =
# [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# 
# 输出：[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= accounts.length <= 1000
# 2 <= accounts[i].length <= 10
# 1 <= accounts[i][j].length <= 30
# accounts[i][0] 由英文字母组成
# accounts[i][j] (for j > 0) 是有效的邮箱地址
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
class UF:
    def __init__(self,n):
        self.pa = list(range(n))

    def find(self,x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self,x,y):
        px,py = self.find(x),self.find(y)
        if px != py:
            self.pa[px] = py

    def isConnected(self,x,y):
        return self.find(x) == self.find(y)

# enumerate 简化写法
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UF(n)
        email_index = {}
        for i,(_,*emails) in enumerate(accounts):
            for e in emails:
                if e in email_index:
                    uf.union(email_index[e], i)
                else:
                    email_index[e] = i
        
        root_emails = defaultdict(set)
        for i, (_, *emails) in enumerate(accounts):
            root_emails[uf.find(i)] |= set(emails)
        return [[accounts[i][0]] + sorted(list(emails)) for i,emails in root_emails.items()]


class Solution1:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        name_index = defaultdict(list)
        index_emails = defaultdict(set)
        n = len(accounts)
        uf = UF(n)

        for i,x in enumerate(accounts):
            name = x[0]
            emails = set(x[1:])
            for j in name_index[name]:
                if emails.intersection(index_emails[j]):
                    uf.union(i,j)

            name_index[name].append(i)
            index_emails[i] = emails

        for i in range(n):
            index_emails[uf.find(i)] |= index_emails[i]

        ans = []
        for name, index in name_index.items():
            for i in index:
                if uf.find(i) == i:
                    ans.append([name] + list(sorted(index_emails[i])))
        return ans




        

# @lc code=end



#
# @lcpr case=start
# [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John","johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]\n
# @lcpr case=end

# @lcpr case=start
# [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]\n
# @lcpr case=end

#

