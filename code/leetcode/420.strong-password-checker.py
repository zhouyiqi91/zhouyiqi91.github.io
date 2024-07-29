#
# @lc app=leetcode.cn id=420 lang=python3
# @lcpr version=30204
#
# [420] 强密码检验器
#
# https://leetcode.cn/problems/strong-password-checker/description/
#
# algorithms
# Hard (38.53%)
# Likes:    221
# Dislikes: 0
# Total Accepted:    19.2K
# Total Submissions: 49.8K
# Testcase Example:  '"a"'
#
# 满足以下条件的密码被认为是强密码：
# 
# 
# 由至少 6 个，至多 20 个字符组成。
# 包含至少 一个小写 字母，至少 一个大写 字母，和至少 一个数字 。
# 不包含连续三个重复字符 (比如 "Baaabb0" 是弱密码, 但是 "Baaba0" 是强密码)。
# 
# 
# 给你一个字符串 password ，返回 将 password 修改到满足强密码条件需要的最少修改步数。如果 password 已经是强密码，则返回 0
# 。
# 
# 在一步修改操作中，你可以：
# 
# 
# 插入一个字符到 password ，
# 从 password 中删除一个字符，或
# 用另一个字符来替换 password 中的某个字符。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：password = "a"
# 输出：5
# 
# 
# 示例 2：
# 
# 输入：password = "aA1"
# 输出：3
# 
# 
# 示例 3：
# 
# 输入：password = "1337C0d3"
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= password.length <= 50
# password 由字母、数字、点 '.' 或者感叹号 '!' 组成
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

# 思路：分组循环找到连续字符数目k，分情况讨论
# n<6时，只需要添加
# 6<=n<=20时，只需要替换
# n>20时，删除+替换，删除可以减少替换次数
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        i = 0
        ks = []
        c = [0,0,0]
        while i < n:
            x = password[i]
            if x.isdigit():
                c[0] = 1
            elif x.isalpha():
                if x.islower():
                    c[1] = 1
                else:
                    c[2] = 1
            k = 1
            while i<n-1 and password[i]==password[i+1]:
                k += 1
                i += 1
            if k >= 3: ks.append(k)
            i += 1
        if n<6: 
            return max(6-n, 3-sum(c))
        elif n <= 20:
            return max(sum(k//3 for k in ks), 3-sum(c))
        else:
            ans = 0
            hq = [(k % 3,k) for k in ks]
            heapify(hq)
            while n>20:
                n -= 1
                ans += 1
                if hq:
                    r, k = heappop(hq)
                    k -= 1
                    if k >= 3:
                        heappush(hq, (k%3, k))
            return ans + max(sum(k//3 for _, k in hq), 3-sum(c))



# @lc code=end



#
# @lcpr case=start
# "a"\n
# @lcpr case=end

# @lcpr case=start
# "aA1"\n
# @lcpr case=end

# @lcpr case=start
# "1337C0d3"\n
# @lcpr case=end

#

