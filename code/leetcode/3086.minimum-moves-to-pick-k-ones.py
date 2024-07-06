#
# @lc app=leetcode.cn id=3086 lang=python3
# @lcpr version=30204
#
# [3086] 拾起 K 个 1 需要的最少行动次数
#
# https://leetcode.cn/problems/minimum-moves-to-pick-k-ones/description/
#
# algorithms
# Hard (26.44%)
# Likes:    19
# Dislikes: 0
# Total Accepted:    2.8K
# Total Submissions: 7.8K
# Testcase Example:  '[1,1,0,0,0,1,1,0,0,1]\n3\n1'
#
# 给你一个下标从 0 开始的二进制数组 nums，其长度为 n ；另给你一个 正整数 k 以及一个 非负整数 maxChanges 。
# 
# Alice 在玩一个游戏，游戏的目标是让 Alice 使用 最少 数量的 行动 次数从 nums 中拾起 k 个 1 。游戏开始时，Alice
# 可以选择数组 [0, n - 1] 范围内的任何索引 aliceIndex 站立。如果 nums[aliceIndex] == 1 ，Alice
# 会拾起一个 1 ，并且 nums[aliceIndex] 变成0（这 不算 作一次行动）。之后，Alice 可以执行 任意数量 的
# 行动（包括零次），在每次行动中 Alice 必须 恰好 执行以下动作之一：
# 
# 
# 选择任意一个下标 j != aliceIndex 且满足 nums[j] == 0 ，然后将 nums[j] 设置为 1 。这个动作最多可以执行
# maxChanges 次。
# 选择任意两个相邻的下标 x 和 y（|x - y| == 1）且满足 nums[x] == 1, nums[y] == 0 ，然后交换它们的值（将
# nums[y] = 1 和 nums[x] = 0）。如果 y == aliceIndex，在这次行动后 Alice 拾起一个 1 ，并且 nums[y]
# 变成 0 。
# 
# 
# 返回 Alice 拾起 恰好 k 个 1 所需的 最少 行动次数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1
# 
# 输出：3
# 
# 解释：如果游戏开始时 Alice 在 aliceIndex == 1 的位置上，按照以下步骤执行每个动作，他可以利用 3 次行动拾取 3 个 1
# ：
# 
# 
# 游戏开始时 Alice 拾取了一个 1 ，nums[1] 变成了 0。此时 nums 变为 [1,1,1,0,0,1,1,0,0,1] 。
# 选择 j == 2 并执行第一种类型的动作。nums 变为 [1,0,1,0,0,1,1,0,0,1]
# 选择 x == 2 和 y == 1 ，并执行第二种类型的动作。nums 变为 [1,1,0,0,0,1,1,0,0,1] 。由于 y ==
# aliceIndex，Alice 拾取了一个 1 ，nums 变为  [1,0,0,0,0,1,1,0,0,1] 。
# 选择 x == 0 和 y == 1 ，并执行第二种类型的动作。nums 变为 [0,1,0,0,0,1,1,0,0,1] 。由于 y ==
# aliceIndex，Alice 拾取了一个 1 ，nums 变为  [0,0,0,0,0,1,1,0,0,1] 。
# 
# 
# 请注意，Alice 也可能执行其他的 3 次行动序列达成拾取 3 个 1 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0,0,0,0], k = 2, maxChanges = 3
# 
# 输出：4
# 
# 解释：如果游戏开始时 Alice 在 aliceIndex == 0 的位置上，按照以下步骤执行每个动作，他可以利用 4 次行动拾取 2 个 1
# ：
# 
# 
# 选择 j == 1 并执行第一种类型的动作。nums 变为 [0,1,0,0] 。
# 选择 x == 1 和 y == 0 ，并执行第二种类型的动作。nums 变为 [1,0,0,0] 。由于 y == aliceIndex，Alice
# 拾起了一个 1 ，nums 变为 [0,0,0,0] 。
# 再次选择 j == 1 并执行第一种类型的动作。nums 变为 [0,1,0,0] 。
# 再次选择 x == 1 和 y == 0 ，并执行第二种类型的动作。nums 变为 [1,0,0,0] 。由于y == aliceIndex，Alice
# 拾起了一个 1 ，nums 变为 [0,0,0,0] 。
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= n <= 10^5
# 0 <= nums[i] <= 1
# 1 <= k <= 10^5
# 0 <= maxChanges <= 10^5
# maxChanges + sum(nums) >= k
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
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        c = 0
        a = []
        for i,x in enumerate(nums):
            if x==1:
                a.append(i)
                cur = 1
                if i>0 and nums[i-1]==1:
                    cur += 1
                    if i>1 and nums[i-2]==1:
                        cur += 1
                c = max(c, cur)

        if c >= k:
            return k - 1
        if c + maxChanges >= k:
            return max(c-1, 0) + (k-c) * 2
        
        s = list(accumulate(a,initial=0))
        def cnt(l,r):
            mid = l+r>>1
            x = a[mid]
            left = x * (mid-l) - (s[mid] - s[l])
            right = s[r+1] - s[mid+1] - x * (r-mid) # 写错
            return left + right
        
        nk = k - maxChanges
        l = 0
        res = inf
        for r,rx in enumerate(a):
            if r-l+1 < nk:
                continue
            if r-l+1 > nk:
                l += 1
            res = min(res, cnt(l,r))
        return res + 2 * maxChanges


# @lc code=end



#
# @lcpr case=start
# [1,1,0,0,0,1,1,0,0,1]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,0]\n2\n3\n
# @lcpr case=end

#

