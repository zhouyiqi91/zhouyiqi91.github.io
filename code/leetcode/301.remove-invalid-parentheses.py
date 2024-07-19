#
# @lc app=leetcode.cn id=301 lang=python3
# @lcpr version=30204
#
# [301] 删除无效的括号
#
# https://leetcode.cn/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (55.36%)
# Likes:    929
# Dislikes: 0
# Total Accepted:    109.5K
# Total Submissions: 197.8K
# Testcase Example:  '"()())()"'
#
# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
# 
# 返回所有可能的结果。答案可以按 任意顺序 返回。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "()())()"
# 输出：["(())()","()()()"]
# 
# 
# 示例 2：
# 
# 输入：s = "(a)())()"
# 输出：["(a())()","(a)()()"]
# 
# 
# 示例 3：
# 
# 输入：s = ")("
# 输出：[""]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 25
# s 由小写英文字母以及括号 '(' 和 ')' 组成
# s 中至多含 20 个括号
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
# 剪枝：剩下字符数小于需要移除的个数： 1000ms -> 50ms
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        nl = nr = 0
        st = []
        for x in s:
            if x == '(':
                nl += 1
            elif x == ')':
                if nl > 0:
                    nl -= 1
                else:
                    nr += 1

        ans = set()
        n = len(s)
        def dfs(i, l, r, slot, p):
            if i == n:
                if l==0 and r==0:
                    ans.add(p)
                return
            if n - i < l + r: return #小于需要移除的个数

            if s[i] == '(':
                dfs(i+1,l,r,slot+1,p+'(')
                if l > 0:
                    dfs(i+1,l-1,r,slot,p)
            elif s[i] == ')':
                if slot > 0:
                    dfs(i+1,l,r,slot-1,p+')')
                if r > 0:
                    dfs(i+1,l,r-1,slot,p)
            else:
                dfs(i+1,l,r,slot,p+s[i])
        
        dfs(0,nl,nr,0,"")
        return list(ans)
# @lc code=end



#
# @lcpr case=start
# "()())()"\n
# @lcpr case=end

# @lcpr case=start
# "(a)())()"\n
# @lcpr case=end

# @lcpr case=start
# ")("\n
# @lcpr case=end

#

