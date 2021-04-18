"""
1830. Minimum Number of Operations to Make String Sorted
Hard

0

3

Add to List

Share
You are given a string s (0-indexed)​​​​​​. You are asked to perform the following operation on s​​​​​​ until you get a sorted string:

Find the largest index i such that 1 <= i < s.length and s[i] < s[i - 1].
Find the largest index j such that i <= j < s.length and s[k] < s[i - 1] for all the possible values of k in the range [i, j] inclusive.
Swap the two characters at indices i - 1​​​​ and j​​​​​.
Reverse the suffix starting at index i​​​​​​.
Return the number of operations needed to make the string sorted. Since the answer can be too large, return it modulo 109 + 7.



Example 1:

Input: s = "cba"
Output: 5
Explanation: The simulation goes as follows:
Operation 1: i=2, j=2. Swap s[1] and s[2] to get s="cab", then reverse the suffix starting at 2. Now, s="cab".
Operation 2: i=1, j=2. Swap s[0] and s[2] to get s="bac", then reverse the suffix starting at 1. Now, s="bca".
Operation 3: i=2, j=2. Swap s[1] and s[2] to get s="bac", then reverse the suffix starting at 2. Now, s="bac".
Operation 4: i=1, j=1. Swap s[0] and s[1] to get s="abc", then reverse the suffix starting at 1. Now, s="acb".
Operation 5: i=2, j=2. Swap s[1] and s[2] to get s="abc", then reverse the suffix starting at 2. Now, s="abc".
Example 2:

Input: s = "aabaa"
Output: 2
Explanation: The simulation goes as follows:
Operation 1: i=3, j=4. Swap s[2] and s[4] to get s="aaaab", then reverse the substring starting at 3. Now, s="aaaba".
Operation 2: i=4, j=4. Swap s[3] and s[4] to get s="aaaab", then reverse the substring starting at 4. Now, s="aaaab".
Example 3:

Input: s = "cdbea"
Output: 63
Example 4:

Input: s = "leetcodeleetcodeleetcode"
Output: 982157772


Constraints:

1 <= s.length <= 3000
s​​​​​​ consists only of lowercase English letters.
"""
import math

"""
The problem is given string understand what is the lexicographical order of this string

Sorted permutation rank with duplicates

关键1：操作实际是求当前排列的前一个排列，最终要求的答案其实是给定排列的字典序编号(lexicological rank)。比如，cba的答案是5，因为它在abc，acb，bac，bca，cab，cba的顺序编号是5.
关键2：需要注意有重复字母的情况：假设第i个字母的频率为n_i,n_1+n_2+...+n_26=N，则能组成的排列数是N!/(n_1!*n_2!*...*n_26!)。
    字符串长度N，总排列数是N!，去除每个重复字母内部排列数，得到N!/(n_1!*n_2!*...*n_26!)
关键3：关键2中的分母可能过大无法直接计算，那么从费马小定理a^(m01)=>1(mod m)推导出：一个数除以a等于这个数乘以a^(m-2)再对m取模。
关键4：用快速幂计算关键3中的a^(m-2)%m

cba
2!*2!
+ 1!*1!
"""


class Solution:
    def makeStringSorted(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)

        ans = 0
        cnt = [0] * 26  # total 26 chars
        for i in range(n - 1, -1, -1):  # iterate back, so we know the chars and counts after i-th position
            idx = ord(s[i]) - ord('a')
            cnt[idx] += 1
            smaller = sum(cnt[:idx])  # number of elements smaller than current one
            ans += smaller * math.factorial(n - i - 1) // math.prod([math.factorial(cnt[i]) for i in range(26)])
            ans %= MOD

        return ans


def main():
    sol = Solution()
    assert sol.makeStringSorted(s = "cba") == 5, 'fails'

    assert sol.makeStringSorted(s = "aabaa") == 2, 'fails'

    assert sol.makeStringSorted(s = "cdbea") == 63, 'fails'

    assert sol.makeStringSorted(s = "leetcodeleetcodeleetcode") == 982157772, 'fails'


if __name__ == '__main__':
   main()