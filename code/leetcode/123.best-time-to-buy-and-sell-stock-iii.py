#
# @lc app=leetcode.cn id=123 lang=python3
# @lcpr version=30204
#
# [123] 买卖股票的最佳时机 III
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (60.79%)
# Likes:    1722
# Dislikes: 0
# Total Accepted:    351.5K
# Total Submissions: 577.2K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 
# 
# 示例 1:
# 
# 输入：prices = [3,3,5,0,0,3,1,4]
# 输出：6
# 解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
# 随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
# 
# 示例 2：
# 
# 输入：prices = [1,2,3,4,5]
# 输出：4
# 解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4
# 。   
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 
# 
# 示例 3：
# 
# 输入：prices = [7,6,4,3,1] 
# 输出：0 
# 解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
# 
# 示例 4：
# 
# 输入：prices = [1]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^5
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

# 思路1：枚举分割点
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        right = [0] * (n+1)
        rmax = 0
        for i in range(n-1,-1,-1):
            right[i] = max(rmax-prices[i], right[i+1])
            rmax = max(rmax, prices[i])

        lmin = prices[0]
        ans = 0
        for i in range(n):
            left = prices[i] - lmin 
            cur =  left + right[i+1]
            ans = max(ans, cur)
            lmin = min(lmin, prices[i])
        
        return ans

# 思路2：dp

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dp(i, j, hold):
            if i==n: return 0
            res = dp(i+1,j,hold)
            if hold:
                res = max(res, dp(i+1,j,False) + prices[i])
            elif j>0:
                res = max(res, dp(i+1,j-1,True) - prices[i])
            return res
        ans = dp(0,2,False)
        dp.cache_clear()
        return ans
    

# dp递推写法

class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = defaultdict(int)
        dp[(1,True)] = dp[(0,True)] = -inf
        for x in prices:
            dp[(0,False)],dp[(0,True)],dp[(1,False)],dp[(1,True)] = (
                max(dp[(0,False)], dp[(0, True)] + x),
                max(dp[(0,True)], dp[(1,False)] - x),
                max(dp[(1,False)], dp[(1,True)] + x),
                max(dp[(1,True)], -x),
            )
        return max(dp.values())


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = -inf
        sell1 = sell2 = 0
        for x in prices:
            buy1 = max(buy1, -x)
            sell1 = max(sell1, buy1 + x)
            buy2 = max(buy2, sell1 - x)
            sell2 = max(sell2, buy2 + x)
        return sell2


# @lc code=end



#
# @lcpr case=start
# [3,3,5,0,0,3,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

