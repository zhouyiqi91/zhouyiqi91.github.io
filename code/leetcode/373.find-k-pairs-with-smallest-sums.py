#
# @lc app=leetcode.cn id=373 lang=python3
# @lcpr version=30204
#
# [373] 查找和最小的 K 对数字
#
# https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/description/
#
# algorithms
# Medium (41.11%)
# Likes:    610
# Dislikes: 0
# Total Accepted:    83.1K
# Total Submissions: 201.7K
# Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
#
# 给定两个以 非递减顺序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。
# 
# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。
# 
# 请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。
# 
# 
# 
# 示例 1:
# 
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
# ⁠    [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# 
# 
# 示例 2:
# 
# 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= nums1.length, nums2.length <= 10^5
# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1 和 nums2 均为 升序排列
# 1 <= k <= 10^4
# k <= nums1.length * nums2.length
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

# war story 4.4 War Story: Give me a Ticket on an Airplane
# x+1,y 和 x,y+1不会在x,y之前出队
# 优先队列 + hash避免重复添加
class Solution1:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m,n=len(nums1), len(nums2)
        hq = [(nums1[0]+nums2[0],0,0)]
        ans = []
        vis = set()
        for _ in range(k):
            _w,x,y = heappop(hq)
            ans.append([nums1[x],nums2[y]])
            if x+1 < m and (x+1,y) not in vis:
                heappush(hq, (nums1[x+1]+nums2[y], x+1,y))
                vis.add((x+1,y))
            if y+1 < n and (x,y+1) not in vis:
                heappush(hq, (nums1[x]+nums2[y+1],x,y+1))
                vis.add((x,y+1))
        return ans

# 可以只增加y，这样一开始要将所有(x,0)入队
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m,n=len(nums1), len(nums2)
        hq = [(nums1[i]+nums2[0],i,0) for i in range(min(m,k))]
        ans = []
        for _ in range(k):
            _w,x,y = heappop(hq)
            ans.append([nums1[x],nums2[y]])
            if y+1 < n:
                heappush(hq, (nums1[x]+nums2[y+1],x,y+1))
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,7,11]\n[2,4,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n[1,2,3]\n2\n
# @lcpr case=end

#

