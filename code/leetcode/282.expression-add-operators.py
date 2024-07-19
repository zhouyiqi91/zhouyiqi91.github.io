#
# @lc app=leetcode.cn id=282 lang=python3
# @lcpr version=30204
#
# [282] 给表达式添加运算符
#
# https://leetcode.cn/problems/expression-add-operators/description/
#
# algorithms
# Hard (46.71%)
# Likes:    482
# Dislikes: 0
# Total Accepted:    29K
# Total Submissions: 62K
# Testcase Example:  '"123"\n6'
#
# 给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回
# 所有 能够得到 target 的表达式。
# 
# 注意，返回表达式中的操作数 不应该 包含前导零。
# 
# 
# 
# 示例 1:
# 
# 输入: num = "123", target = 6
# 输出: ["1+2+3", "1*2*3"] 
# 解释: “1*2*3” 和 “1+2+3” 的值都是6。
# 
# 
# 示例 2:
# 
# 输入: num = "232", target = 8
# 输出: ["2*3+2", "2+3*2"]
# 解释: “2*3+2” 和 “2+3*2” 的值都是8。
# 
# 
# 示例 3:
# 
# 输入: num = "3456237490", target = 9191
# 输出: []
# 解释: 表达式 “3456237490” 无法得到 9191 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= num.length <= 10
# num 仅含数字
# -2^31 <= target <= 2^31 - 1
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
# eval： 7903ms
# isnum：有没有前导0
class Solution1:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        num = str(num)
        n = len(num)
        def dfs(i, p, isnum):
            if i == n:
                if eval(p) == target:
                    ans.append(p)
                return
            if i!=0:
                for op in ('+-*'):
                    dfs(i+1, p+op+num[i], num[i] != '0')
            if isnum:
                if i==0 and num[0] == '0': isnum=False
                dfs(i+1, p+num[i], isnum)                  
                
        dfs(0, "", True)
        return ans

# 使用字符数组, 避免字符串拼接，依然很慢8000ms
class Solution2:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        num = str(num)
        n = len(num)
        path = []
        def dfs(i, isnum):
            if i == n:
                p = "".join(path)
                if eval(p) == target:
                    ans.append(p)
                return
            if i!=0:
                for op in ('+-*'):
                    path.append(op)
                    path.append(num[i])
                    dfs(i+1, num[i] != '0')
                    path.pop()
                    path.pop()
            if isnum:
                if i==0 and num[0] == '0': 
                    isnum=False
                path.append(num[i])
                dfs(i+1, isnum)
                path.pop()              
                
        dfs(0, True)
        return ans

# pre最后一个连乘串的值，可以是单个数字
# 对于i，枚举所有下一个切割数字的位置，比枚举是否加符号要方便
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        def dfs(i, cur, pre, ss):
            if i==n:
                if cur==target: ans.append(ss)
                return
            
            d = 0
            for j in range(i, n):
                if j > i and num[i] == '0': #只允许单个0
                    break
                d = d * 10 + int(num[j])
                if i==0:
                    dfs(j+1,d,d,str(d))
                else:
                    dfs(j+1,cur+d,d,ss+'+'+str(d))
                    dfs(j+1,cur-d,-d,ss+'-'+str(d))
                    dfs(j+1,cur-pre+pre*d,pre*d,ss+'*'+str(d))
            
        dfs(0,0,0,"")
        return ans

# @lc code=end



#
# @lcpr case=start
# "123"\n6\n
# @lcpr case=end

# @lcpr case=start
# "232"\n8\n
# @lcpr case=end

# @lcpr case=start
# "3456237490"\n9191\n
# @lcpr case=end

#

