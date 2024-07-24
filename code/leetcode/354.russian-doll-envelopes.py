#
# @lc app=leetcode.cn id=354 lang=python3
# @lcpr version=30204
#
# [354] 俄罗斯套娃信封问题
#
# https://leetcode.cn/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (35.69%)
# Likes:    1024
# Dislikes: 0
# Total Accepted:    116.8K
# Total Submissions: 327.9K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
# 
# 当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
# 
# 请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
# 
# 注意：不允许旋转信封。
# 
# 
# 示例 1：
# 
# 输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出：3
# 解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
# 
# 示例 2：
# 
# 输入：envelopes = [[1,1],[1,1],[1,1]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= envelopes.length <= 10^5
# envelopes[i].length == 2
# 1 <= wi, hi <= 10^5
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

# 固定一维，转化为最长递增子序列
# 第二维要逆序排序，保证第一维相同的信封不能互相包含。
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        tail = []
        for _,y in envelopes:
            if not tail or y > tail[-1]:
                tail.append(y)
            else:
                i = bisect_left(tail, y)
                tail[i] = min(tail[i], y)
        return len(tail)
# @lc code=end



#
# @lcpr case=start
# [[5,4],[6,4],[6,7],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,1],[1,1]]\n
# @lcpr case=end

#

