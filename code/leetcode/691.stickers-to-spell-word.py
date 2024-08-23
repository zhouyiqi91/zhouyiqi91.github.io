#
# @lc app=leetcode.cn id=691 lang=python3
# @lcpr version=30204
#
# [691] 贴纸拼词
#
# https://leetcode.cn/problems/stickers-to-spell-word/description/
#
# algorithms
# Hard (57.79%)
# Likes:    300
# Dislikes: 0
# Total Accepted:    27.6K
# Total Submissions: 47.8K
# Testcase Example:  '["with","example","science"]\n"thehat"'
#
# 我们有 n 种不同的贴纸。每个贴纸上都有一个小写的英文单词。
# 
# 您想要拼写出给定的字符串 target ，方法是从收集的贴纸中切割单个字母并重新排列它们。如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。
# 
# 返回你需要拼出 target 的最小贴纸数量。如果任务不可能，则返回 -1 。
# 
# 注意：在所有的测试用例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选择的，并且 target 被选择为两个随机单词的连接。
# 
# 
# 
# 示例 1：
# 
# 输入： stickers = ["with","example","science"], target = "thehat"
# 输出：3
# 解释：
# 我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
# 把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
# 此外，这是形成目标字符串所需的最小贴纸数量。
# 
# 
# 示例 2:
# 
# 输入：stickers = ["notice","possible"], target = "basicbasic"
# 输出：-1
# 解释：我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。
# 
# 
# 
# 提示:
# 
# 
# n == stickers.length
# 1 <= n <= 50
# 1 <= stickers[i].length <= 10
# 1 <= target.length <= 15
# stickers[i] 和 target 由小写英文单词组成
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
    def minStickers(self, stickers: List[str], target: str) -> int:
        all_ch = reduce(lambda x,y: x.union(y), (set(s) for s in stickers))
        if not set(target).issubset(all_ch):
            return -1

        ts = set(target)
        stickers = [Counter(s) for s in stickers if ts.intersection(s)]

        n = len(target)
        @cache
        def dp(mask):
            if mask == 0: return 0
            res = n+1
            for s in stickers:
                cur = mask
                s = s.copy()
                for i,c in enumerate(target):
                    if cur & (1<<i) and s[c]:
                        cur ^= 1<<i
                        s[c] -= 1
                if cur != mask:
                    res = min(res, dp(cur)+1)
            return res

        return dp((1<<n)-1)



# @lc code=end



#
# @lcpr case=start
# ["with","example","science"]\n"thehat"\n
# @lcpr case=end

# @lcpr case=start
# ["notice","possible"]\n"basicbasic"\n
# @lcpr case=end

#

