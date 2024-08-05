#
# @lc app=leetcode.cn id=1702 lang=python3
# @lcpr version=30204
#
# [1702] 修改后的最大二进制字符串
#
# https://leetcode.cn/problems/maximum-binary-string-after-change/description/
#
# algorithms
# Medium (53.43%)
# Likes:    86
# Dislikes: 0
# Total Accepted:    24.3K
# Total Submissions: 45.5K
# Testcase Example:  '"000110"'
#
# 给你一个二进制字符串 binary ，它仅有 0 或者 1 组成。你可以使用下面的操作任意次对它进行修改：
# 
# 
# 操作 1 ：如果二进制串包含子字符串 "00" ，你可以用 "10" 将其替换。
# 
# 
# 比方说， "00010" -> "10010"
# 
# 
# 操作 2 ：如果二进制串包含子字符串 "10" ，你可以用 "01" 将其替换。
# 
# 比方说， "00010" -> "00001"
# 
# 
# 
# 
# 请你返回执行上述操作任意次以后能得到的 最大二进制字符串 。如果二进制字符串 x 对应的十进制数字大于二进制字符串 y
# 对应的十进制数字，那么我们称二进制字符串 x 大于二进制字符串 y 。
# 
# 
# 
# 示例 1：
# 
# 输入：binary = "000110"
# 输出："111011"
# 解释：一个可行的转换为：
# "000110" -> "000101" 
# "000101" -> "100101" 
# "100101" -> "110101" 
# "110101" -> "110011" 
# "110011" -> "111011"
# 
# 
# 示例 2：
# 
# 输入：binary = "01"
# 输出："01"
# 解释："01" 没办法进行任何转换。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= binary.length <= 10^5
# binary 仅包含 '0' 和 '1' 。
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

# 直接构造：开头的1不用移动，剩余所有0可以全部移动到第一个0的后面，然后变成11..110
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        c0 = binary.count('0')
        if c0 <= 1: return binary
        i = binary.index('0')
        return (i+c0-1)*'1' + '0' + (n-i-c0) * '1'
# @lc code=end



#
# @lcpr case=start
# "000110"\n
# @lcpr case=end

# @lcpr case=start
# "01"\n
# @lcpr case=end

#

