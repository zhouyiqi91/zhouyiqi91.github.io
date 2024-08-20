/*
 * @lc app=leetcode.cn id=3137 lang=cpp
 * @lcpr version=30204
 *
 * [3137] K 周期字符串需要的最少操作次数
 *
 * https://leetcode.cn/problems/minimum-number-of-operations-to-make-word-k-periodic/description/
 *
 * algorithms
 * Medium (64.94%)
 * Likes:    9
 * Dislikes: 0
 * Total Accepted:    6.7K
 * Total Submissions: 9.5K
 * Testcase Example:  '"leetcodeleet"\n4'
 *
 * 给你一个长度为 n 的字符串 word 和一个整数 k ，其中 k 是 n 的因数。
 * 
 * 在一次操作中，你可以选择任意两个下标 i 和 j，其中 0 <= i, j < n ，且这两个下标都可以被 k 整除，然后用从 j 开始的长度为 k
 * 的子串替换从 i 开始的长度为 k 的子串。也就是说，将子串 word[i..i + k - 1] 替换为子串 word[j..j + k - 1]
 * 。
 * 
 * 返回使 word 成为 K 周期字符串 所需的 最少 操作次数。
 * 
 * 如果存在某个长度为 k 的字符串 s，使得 word 可以表示为任意次数连接 s ，则称字符串 word 是 K 周期字符串 。例如，如果 word
 * == "ababab"，那么 word 就是 s = "ab" 时的 2 周期字符串 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：word = "leetcodeleet", k = 4
 * 
 * 输出：1
 * 
 * 解释：可以选择 i = 4 和 j = 0 获得一个 4 周期字符串。这次操作后，word 变为 "leetleetleet" 。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：word = "leetcoleet", k = 2
 * 
 * 输出：3
 * 
 * 解释：可以执行以下操作获得一个 2 周期字符串。
 * 
 * 
 * 
 * 
 * i
 * j
 * word
 * 
 * 
 * 0
 * 2
 * etetcoleet
 * 
 * 
 * 4
 * 0
 * etetetleet
 * 
 * 
 * 6
 * 0
 * etetetetet
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n == word.length <= 10^5
 * 1 <= k <= word.length
 * k 能整除 word.length 。
 * word 仅由小写英文字母组成。
 * 
 * 
 */


// @lcpr-template-start
using namespace std;
#include <algorithm>
#include <array>
#include <bitset>
#include <climits>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <queue>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
// @lcpr-template-end
// @lc code=start

// c++ map
class Solution {
public:
    int minimumOperationsToMakeKPeriodic(string word, int k) {
        unordered_map<string, int> cnt;
        int mx = 0, n=word.size();
        for (int i=0; i < n; i+=k){
            mx = max(mx, ++cnt[word.substr(i, k)]);
        }
        return n/k-mx;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "leetcodeleet"\n4\n
// @lcpr case=end

// @lcpr case=start
// "leetcoleet"\n2\n
// @lcpr case=end

 */

