#
# @lc app=leetcode.cn id=LCP 40 lang=python3
# @lcpr version=30204
#
# [LCP 40] 心算挑战
#
# https://leetcode.cn/problems/uOAnQW/description/
#
# algorithms
# Easy (31.94%)
# Likes:    86
# Dislikes: 0
# Total Accepted:    14.4K
# Total Submissions: 40.6K
# Testcase Example:  '[1,2,8,9]\n3'
#
# 「力扣挑战赛」心算项目的挑战比赛中，要求选手从 `N` 张卡牌中选出 `cnt` 张卡牌，若这 `cnt`
# 张卡牌数字总和为偶数，则选手成绩「有效」且得分为 `cnt` 张卡牌数字总和。
# 给定数组 `cards` 和 `cnt`，其中 `cards[i]` 表示第 `i` 张卡牌上的数字。
# 请帮参赛选手计算最大的有效得分。若不存在获取有效得分的卡牌方案，则返回 0。
# 
# **示例 1：**
# >输入：`cards = [1,2,8,9], cnt = 3`
# >
# >输出：`18`
# >
# >解释：选择数字为 1、8、9 的这三张卡牌，此时可获得最大的有效得分 1+8+9=18。
# 
# **示例 2：**
# >输入：`cards = [3,3,1], cnt = 1`
# >
# >输出：`0`
# >
# >解释：不存在获取有效得分的卡牌方案。
# 
# **提示：**
# - `1 <= cnt <= cards.length <= 10^5`
# - `1 <= cards[i] <= 1000`
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

# 犯错 分奇偶数每次-2讨论
class Solution_wrong:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        a0,a1 = [],[]
        for x in cards:
            if x % 2 == 0:
                a0.append(x)
            else:
                a1.append(x)
        a0.sort()
        a1.sort()
        ans = 0
        while cnt:
            if cnt==1:
                if not a0: return 0
                return ans + a0[-1]
            if len(a1) >= 2 and (len(a0) < 2 or (a1[-1] + a1[-2]) >= (a0[-1] + a0[-2])):
                ans += a1[-1] + a1[-2]
                a1.pop()
                a1.pop()
            else:
                if len(a0) < 2: return 0
                ans += a0[-1] + a0[-2]
                a0.pop()
                a0.pop()
            cnt -= 2
        return ans

# 排序 + 贪心替换

class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        s = sum(cards[:cnt])
        if s % 2 ==0: return s
        def f(x):
            for i in range(cnt, len(cards)):
                y = cards[i]
                if x % 2 != y % 2:
                    return s - x + y
            return 0
        
        s0 = f(cards[cnt-1])
        s1 = 0
        for i in range(cnt-2,-1,-1):
            x = cards[i]
            if x % 2 != cards[cnt-1] % 2:
                s1 = f(x)
                break
        return max(s0,s1)

# @lc code=end



#
# @lcpr case=start
# [1,2,8,9]\n3`>\n
# @lcpr case=end

# @lcpr case=start
# [3,3,1]\n1`>\n
# @lcpr case=end

#

