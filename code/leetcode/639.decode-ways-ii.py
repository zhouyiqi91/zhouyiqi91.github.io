#
# @lc app=leetcode.cn id=639 lang=python3
# @lcpr version=30204
#
# [639] 解码方法 II
#
# https://leetcode.cn/problems/decode-ways-ii/description/
#
# algorithms
# Hard (36.79%)
# Likes:    237
# Dislikes: 0
# Total Accepted:    27K
# Total Submissions: 73.5K
# Testcase Example:  '"*"'
#
# 一条包含字母 A-Z 的消息通过以下的方式进行了 编码 ：
# 
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# 
# 要 解码 一条已编码的消息，所有的数字都必须分组，然后按原来的编码方案反向映射回字母（可能存在多种方式）。例如，"11106" 可以映射为：
# 
# 
# "AAJF" 对应分组 (1 1 10 6)
# "KJF" 对应分组 (11 10 6)
# 
# 
# 注意，像 (1 11 06) 这样的分组是无效的，因为 "06" 不可以映射为 'F' ，因为 "6" 与 "06" 不同。
# 
# 除了 上面描述的数字字母映射方案，编码消息中可能包含 '*' 字符，可以表示从 '1' 到 '9' 的任一数字（不包括 '0'）。例如，编码字符串
# "1*" 可以表示 "11"、"12"、"13"、"14"、"15"、"16"、"17"、"18" 或 "19" 中的任意一条消息。对 "1*"
# 进行解码，相当于解码该字符串可以表示的任何编码消息。
# 
# 给你一个字符串 s ，由数字和 '*' 字符组成，返回 解码 该字符串的方法 数目 。
# 
# 由于答案数目可能非常大，返回 10^9 + 7 的 模 。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "*"
# 输出：9
# 解释：这一条编码消息可以表示 "1"、"2"、"3"、"4"、"5"、"6"、"7"、"8" 或 "9" 中的任意一条。
# 可以分别解码成字符串 "A"、"B"、"C"、"D"、"E"、"F"、"G"、"H" 和 "I" 。
# 因此，"*" 总共有 9 种解码方法。
# 
# 
# 示例 2：
# 
# 输入：s = "1*"
# 输出：18
# 解释：这一条编码消息可以表示 "11"、"12"、"13"、"14"、"15"、"16"、"17"、"18" 或 "19" 中的任意一条。
# 每种消息都可以由 2 种方法解码（例如，"11" 可以解码成 "AA" 或 "K"）。
# 因此，"1*" 共有 9 * 2 = 18 种解码方法。
# 
# 
# 示例 3：
# 
# 输入：s = "2*"
# 输出：15
# 解释：这一条编码消息可以表示 "21"、"22"、"23"、"24"、"25"、"26"、"27"、"28" 或 "29" 中的任意一条。
# "21"、"22"、"23"、"24"、"25" 和 "26" 由 2 种解码方法，但 "27"、"28" 和 "29" 仅有 1 种解码方法。
# 因此，"2*" 共有 (6 * 2) + (3 * 1) = 12 + 3 = 15 种解码方法。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s[i] 是 0 - 9 中的一位数字或字符 '*'
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
    def numDecodings(self, s: str) -> int:
        mod = 10**9+7
        n = len(s)
        @cache
        def dp(i, pre):
            if i==n:
                return pre == 0
            x = s[i]
            if x=='*':
                if pre == 0:
                    res = 9 * dp(i+1, 0) + dp(i+1,1) + dp(i+1,2)
                elif pre == 1:
                    res = 9 * dp(i+1, 0)
                elif pre == 2:
                    res = 6 * dp(i+1, 0)
            else:
                x = int(x)
                if x in (1,2):
                    res = dp(i+1, 0) + dp(i+1, x)
                else:
                    res = dp(i+1, 0)
            return res % mod
        
        return dp(0, 0)




# @lc code=end



#
# @lcpr case=start
# "*"\n
# @lcpr case=end

# @lcpr case=start
# "1*"\n
# @lcpr case=end

# @lcpr case=start
# "2*"\n
# @lcpr case=end

#

