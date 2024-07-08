#
# @lc app=leetcode.cn id=2949 lang=python3
# @lcpr version=30204
#
# [2949] 统计美丽子字符串 II
#
# https://leetcode.cn/problems/count-beautiful-substrings-ii/description/
#
# algorithms
# Hard (33.55%)
# Likes:    19
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 7.4K
# Testcase Example:  '"baeyh"\n2'
#
# 给你一个字符串 s 和一个正整数 k 。
# 
# 用 vowels 和 consonants 分别表示字符串中元音字母和辅音字母的数量。
# 
# 如果某个字符串满足以下条件，则称其为 美丽字符串 ：
# 
# 
# vowels == consonants，即元音字母和辅音字母的数量相等。
# (vowels * consonants) % k == 0，即元音字母和辅音字母的数量的乘积能被 k 整除。
# 
# 
# 返回字符串 s 中 非空美丽子字符串 的数量。
# 
# 子字符串是字符串中的一个连续字符序列。
# 
# 英语中的 元音字母 为 'a'、'e'、'i'、'o' 和 'u' 。
# 
# 英语中的 辅音字母 为除了元音字母之外的所有字母。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "baeyh", k = 2
# 输出：2
# 解释：字符串 s 中有 2 个美丽子字符串。
# - 子字符串 "baeyh"，vowels = 2（["a","e"]），consonants = 2（["y","h"]）。
# 可以看出字符串 "aeyh" 是美丽字符串，因为 vowels == consonants 且 vowels * consonants % k == 0
# 。
# - 子字符串 "baeyh"，vowels = 2（["a","e"]），consonants = 2（["b","y"]）。
# 可以看出字符串 "baey" 是美丽字符串，因为 vowels == consonants 且 vowels * consonants % k == 0
# 。
# 可以证明字符串 s 中只有 2 个美丽子字符串。
# 
# 
# 示例 2：
# 
# 输入：s = "abba", k = 1
# 输出：3
# 解释：字符串 s 中有 3 个美丽子字符串。
# - 子字符串 "abba"，vowels = 1（["a"]），consonants = 1（["b"]）。
# - 子字符串 "abba"，vowels = 1（["a"]），consonants = 1（["b"]）。
# - 子字符串 "abba"，vowels = 2（["a","a"]），consonants = 2（["b","b"]）。
# 可以证明字符串 s 中只有 3 个美丽子字符串。
# 
# 
# 示例 3：
# 
# 输入：s = "bcdf", k = 1
# 输出：0
# 解释：字符串 s 中没有美丽子字符串。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 5 * 10^4
# 1 <= k <= 1000
# s 仅由小写英文字母组成。
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
    def beautifulSubstrings(self, s: str, k: int) -> int:
# @lc code=end



#
# @lcpr case=start
# "baeyh"\n2\n
# @lcpr case=end

# @lcpr case=start
# "abba"\n1\n
# @lcpr case=end

# @lcpr case=start
# "bcdf"\n1\n
# @lcpr case=end

#

