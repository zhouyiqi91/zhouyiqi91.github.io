# 定义

> 李煜东 进阶指南
与数字相关的统计问题。限定条件一般是[l,R]区间满足条件的数字有多少个，或者满足条件的第K小的数字是多少。

# 模版

[灵神模版2.0](https://leetcode.cn/problems/count-the-number-of-powerful-integers/solutions/2595149/shu-wei-dp-shang-xia-jie-mo-ban-fu-ti-da-h6ci/?source=vscode)

https://leetcode.cn/problems/numbers-with-repeated-digits/solutions/1748539/by-endlesscheng-c5vg/

limitLow：表示是否受到下界约束，若约束了，最小需要填start[i]，否则最小可以是0。

```py
        finish = num2
        n = len(finish)
        start = '0' * (n-len(num1)) + num1
        MOD = 10 ** 9 + 7

        @cache
        def dp(i: int, low_limit: bool, high_limit: bool) -> int:
            if i == n:
                return 1 if min_sum <= s else 0
            low = int(start[i]) if low_limit else 0 
            high = int(finish[i]) if high_limit else 9

            res = 0
            for x in range(low, high + 1):
                # 这里写可能有的限制
                res += dp(i + 1, low_limit and x==low, high_limit and x == high)
            return res % MOD

        return dp(0, True, True, 0)
```

什么时候需要考虑前导0？当前导0会影响后续选择数字
即使需要考虑前导0，isNum也可能不需要，因为可能有参数可以判断是否有前导0

# 题目

## [357\. 统计各位数字都不同的数字个数](https://leetcode.cn/problems/count-numbers-with-unique-digits/)
前导0不计入mask,用mask==0判断是否有前导0

## [2999.统计强大整数的数目](https://leetcode.cn/problems/count-the-number-of-powerful-integers/description/)
无需考虑前导0

## [902.最大为 N 的数字组合](https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/description/ "https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/description/")
需要考虑前导0 因为填入数字有限制在digits中， 需要isNum

## [统计范围内的步进数字数目](https://leetcode.cn/problems/count-stepping-numbers-in-range/description/ "https://leetcode.cn/problems/count-stepping-numbers-in-range/description/")
需要考虑前导0 因为限制了填入的数字,用pre判断isNum

## [统计整数数目](https://leetcode.cn/problems/count-of-integers/description/ "https://leetcode.cn/problems/count-of-integers/description/")
无需考虑前导0，因为前导0不会影响后续数字选择

## [1397\. 找到所有好字符串](https://leetcode.cn/problems/find-all-good-strings/)
数位DP + KMP