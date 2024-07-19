#
# @lc app=leetcode.cn id=273 lang=python3
# @lcpr version=30204
#
# [273] 整数转换英文表示
#
# https://leetcode.cn/problems/integer-to-english-words/description/
#
# algorithms
# Hard (36.59%)
# Likes:    336
# Dislikes: 0
# Total Accepted:    40.9K
# Total Submissions: 111.9K
# Testcase Example:  '123'
#
# 将非负整数 num 转换为其对应的英文表示。
# 
# 
# 
# 示例 1：
# 
# 输入：num = 123
# 输出："One Hundred Twenty Three"
# 
# 
# 示例 2：
# 
# 输入：num = 12345
# 输出："Twelve Thousand Three Hundred Forty Five"
# 
# 
# 示例 3：
# 
# 输入：num = 1234567
# 输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= num <= 2^31 - 1
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
# 考察编码能力，边界情况： 空格，r是否为0

singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]

class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        
        def f(x):
            s = ""
            if x == 0:
                return ""
            if x < 20: 
                return (singles+teens)[x] + " "
            elif x < 100:
                return tens[x//10] + " " + f(x % 10)
            elif x < 1000:
                return f(x//100) + "Hundred " + f(x % 100)
            
        i = 0
        ans = ""
        while num:
            r = num % 1000
            if r:
                ans = f(r) + thousands[i] + " " + ans
            i += 1
            num //= 1000
        return ans.strip()

            



# @lc code=end



#
# @lcpr case=start
# 123\n
# @lcpr case=end

# @lcpr case=start
# 12345\n
# @lcpr case=end

# @lcpr case=start
# 1234567\n
# @lcpr case=end

#

