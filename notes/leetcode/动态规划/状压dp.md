
## [2741\. 特别的排列](https://leetcode.cn/problems/special-permutations/)

给你一个下标从 **0** 开始的整数数组 `nums` ，它包含 `n` 个 **互不相同** 的正整数。如果 `nums` 的一个排列满足以下条件，我们称它是一个特别的排列：

-   对于 `0 <= i < n - 1` 的下标 `i` ，要么 `nums[i] % nums[i+1] == 0` ，要么 `nums[i+1] % nums[i] == 0` 。

请你返回特别排列的总数目，由于答案可能很大，请将它对 `10^9 ^+ 7` **取余** 后返回。

思路：已经选择的数的下标构成集合s，上一个数添加的数是j，状态转移
dp(s,i) = sum(dp(s+j,j) for j in valid[i] if j not in s)

```py
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10 **9 +7
        n = len(nums)
        u = (1<<n)-1  # universe全集，括号必须
        valid = defaultdict(list)
        for i in range(n):
            for j in range(n):
                x,y=nums[i],nums[j]
                if i!=j and (x % y==0 or y % x==0):
                    valid[i].append(j)
        @cache
        def dp(s, i):
            if s==u: return 1
            return sum(dp(s|1<<j, j) for j in valid[i] if s&1<<j==0)

        return sum(dp(1<<i,i) for i in range(n)) % MOD
```

第二个参数直接使用数的值，而不是下标。这样不方便预处理valid
```py
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10 **9 +7
        n = len(nums)
        u = (1<<n)-1  # universe全集，括号必须
        @cache
        def dp(s, x):
            if s==u: return 1
            res = 0
            for i in range(n):
                if 1<<i & s == 0 and (nums[i] % x==0 or x % nums[i]==0):
                    res += dp(1<<i|s, nums[i])
            return res
        return dp(0,1) % MOD