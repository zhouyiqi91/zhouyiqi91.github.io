#
# @lc app=leetcode.cn id=488 lang=python3
# @lcpr version=30204
#
# [488] 祖玛游戏
#
# https://leetcode.cn/problems/zuma-game/description/
#
# algorithms
# Hard (46.70%)
# Likes:    295
# Dislikes: 0
# Total Accepted:    21.3K
# Total Submissions: 45.7K
# Testcase Example:  '"WRRBBW"\n"RB"'
#
# 你正在参与祖玛游戏的一个变种。
# 
# 在这个祖玛游戏变体中，桌面上有 一排 彩球，每个球的颜色可能是：红色 'R'、黄色 'Y'、蓝色 'B'、绿色 'G' 或白色 'W'
# 。你的手中也有一些彩球。
# 
# 你的目标是 清空 桌面上所有的球。每一回合：
# 
# 
# 从你手上的彩球中选出 任意一颗 ，然后将其插入桌面上那一排球中：两球之间或这一排球的任一端。
# 接着，如果有出现 三个或者三个以上 且 颜色相同 的球相连的话，就把它们移除掉。
# 
# 如果这种移除操作同样导致出现三个或者三个以上且颜色相同的球相连，则可以继续移除这些球，直到不再满足移除条件。
# 
# 
# 如果桌面上所有球都被移除，则认为你赢得本场游戏。
# 重复这个过程，直到你赢了游戏或者手中没有更多的球。
# 
# 
# 给你一个字符串 board ，表示桌面上最开始的那排球。另给你一个字符串 hand ，表示手里的彩球。请你按上述操作步骤移除掉桌上所有球，计算并返回所需的
# 最少 球数。如果不能移除桌上所有的球，返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 输入：board = "WRRBBW", hand = "RB"
# 输出：-1
# 解释：无法移除桌面上的所有球。可以得到的最好局面是：
# - 插入一个 'R' ，使桌面变为 WRRRBBW 。WRRRBBW -> WBBW
# - 插入一个 'B' ，使桌面变为 WBBBW 。WBBBW -> WW
# 桌面上还剩着球，没有其他球可以插入。
# 
# 示例 2：
# 
# 输入：board = "WWRRBBWW", hand = "WRBRW"
# 输出：2
# 解释：要想清空桌面上的球，可以按下述步骤：
# - 插入一个 'R' ，使桌面变为 WWRRRBBWW 。WWRRRBBWW -> WWBBWW
# - 插入一个 'B' ，使桌面变为 WWBBBWW 。WWBBBWW -> WWWW -> empty
# 只需从手中出 2 个球就可以清空桌面。
# 
# 
# 示例 3：
# 
# 输入：board = "G", hand = "GGGGG"
# 输出：2
# 解释：要想清空桌面上的球，可以按下述步骤：
# - 插入一个 'G' ，使桌面变为 GG 。
# - 插入一个 'G' ，使桌面变为 GGG 。GGG -> empty
# 只需从手中出 2 个球就可以清空桌面。
# 
# 
# 示例 4：
# 
# 输入：board = "RBYYBBRRB", hand = "YRBGB"
# 输出：3
# 解释：要想清空桌面上的球，可以按下述步骤：
# - 插入一个 'Y' ，使桌面变为 RBYYYBBRRB 。RBYYYBBRRB -> RBBBRRB -> RRRB -> B
# - 插入一个 'B' ，使桌面变为 BB 。
# - 插入一个 'B' ，使桌面变为 BBB 。BBB -> empty
# 只需从手中出 3 个球就可以清空桌面。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= board.length <= 16
# 1 <= hand.length <= 5
# board 和 hand 由字符 'R'、'Y'、'B'、'G' 和 'W' 组成
# 桌面上一开始的球中，不会有三个及三个以上颜色相同且连着的球
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

# 卡在"RRWWRRBBRR" "WB" 
# RRWWRRBBRR -> RRWWRRBBRWR -> RRWWRRBBBRWR -> RRWWRRRWR -> RRWWWR -> RRR -> ”“
class Solution1:
    def findMinStep(self, board: str, hand: str) -> int:
        hand = str(sorted(list(hand)))

        def clean(s):
            n = 1
            while n:
                s, n = subn(r'(.)\1{2,}', '', s)
            return s

        def dp(board, hand):
            if (not hand) and board: return inf
            if not board: return 0
            i = 0
            n = len(board)
            res = inf
            cnt = Counter(hand)
            while i<n:
                x = board[i]
                start = i
                i += 1
                if x not in cnt: continue
                if i<n and board[i] == x:
                    i += 1
                if i==start+1:
                    if cnt[x] < 2:
                        continue
                    else:
                        h = hand.replace(x, "", 2)
                        add = 2
                else:
                    h = hand.replace(x, "", 1)
                    add = 1
                b = clean(board[:start] + board[i:])
                res = min(res, dp(b,h) + add)
            return res
        
        ans = dp(board,hand)
        return ans if ans != inf else -1 
    

# 剪枝条件：难想
# regex 正则 反复替换连续的3个相同字符
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand = "".join(sorted(list(hand))) # 犯错 不能写成str(1个list)

        def clean(s):
            n = 1
            while n:
                s, n = subn(r'(.)\1{2,}', '', s)
            return s

        @cache
        def dp(board, hand):
            if (not hand) and board: return inf
            if not board: return 0
            i = 0
            n = len(board)
            res = inf
            se = set(hand)
            for i in range(n):
                for x in se:
                    if i>0 and x==board[i-1]: continue
                    choose = False
                    #  - 第 1 种情况 : 当前球颜色与后面的球的颜色相同
                    if i < n and board[i] == x:
                        choose = True
                    #  - 第 2 种情况 : 当前后颜色相同且与当前颜色不同时候放置球
                    if 0 < i < n and board[i - 1] == board[i] and board[i] != x:
                        choose = True
                    if choose:
                        b = board[:i] + x + board[i:]
                        b = clean(b)
                        h = hand.replace(x, "", 1)
                        res = min(res, dp(b,h) + 1)
            return res
        
        ans = dp(board,hand)
        dp.cache_clear()
        return ans if ans != inf else -1
# @lc code=end



#
# @lcpr case=start
# "WRRBBW"\n"RB"\n
# @lcpr case=end

# @lcpr case=start
# "WWRRBBWW"\n"WRBRW"\n
# @lcpr case=end

# @lcpr case=start
# "G"\n"GGGGG"\n
# @lcpr case=end

# @lcpr case=start
# "RBYYBBRRB"\n"YRBGB"\n
# @lcpr case=end

#

