#
# @lc app=leetcode.cn id=679 lang=python3
# @lcpr version=30204
#
# [679] 24 点游戏
#
# https://leetcode.cn/problems/24-game/description/
#
# algorithms
# Hard (53.74%)
# Likes:    462
# Dislikes: 0
# Total Accepted:    44.5K
# Total Submissions: 82.8K
# Testcase Example:  '[4,1,8,7]'
#
# 给定一个长度为4的整数数组 cards 。你有 4 张卡片，每张卡片上都包含一个范围在 [1,9] 的数字。您应该使用运算符 ['+', '-',
# '*', '/'] 和括号 '(' 和 ')' 将这些卡片上的数字排列成数学表达式，以获得值24。
# 
# 你须遵守以下规则:
# 
# 
# 除法运算符 '/' 表示实数除法，而不是整数除法。
# 
# 
# 例如， 4 /(1 - 2 / 3)= 4 /(1 / 3)= 12 。
# 
# 
# 每个运算都在两个数字之间。特别是，不能使用 “-” 作为一元运算符。
# 
# 例如，如果 cards =[1,1,1,1] ，则表达式 “-1 -1 -1 -1” 是 不允许 的。
# 
# 
# 你不能把数字串在一起
# 
# 例如，如果 cards =[1,2,1,2] ，则表达式 “12 + 12” 无效。
# 
# 
# 
# 
# 如果可以得到这样的表达式，其计算结果为 24 ，则返回 true ，否则返回 false 。
# 
# 
# 
# 示例 1:
# 
# 输入: cards = [4, 1, 8, 7]
# 输出: true
# 解释: (8-4) * (7-1) = 24
# 
# 
# 示例 2:
# 
# 输入: cards = [1, 2, 1, 2]
# 输出: false
# 
# 
# 
# 
# 提示:
# 
# 
# cards.length == 4
# 1 <= cards[i] <= 9
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

# 回溯
# 加cache从220ms -> 70ms
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        eps = 1e-6
        @cache
        def f(a):
            n = len(a)
            if n==1: return abs(a[0]-24) < eps
            indices = set(range(n))
            for s in permutations(indices,2):
                x,y = a[s[0]],a[s[1]]
                rest = indices - set(s)
                new = [x+y,x-y,x*y]
                if abs(y) > eps: new.append(x/y)
                for t in new:
                    b = tuple([a[x] for x in rest] + [t])
                    if f(b):
                        return True
            return False

        return f(tuple(cards))

# @lc code=end



#
# @lcpr case=start
# [4, 1, 8, 7]\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 1, 2]\n
# @lcpr case=end

#

