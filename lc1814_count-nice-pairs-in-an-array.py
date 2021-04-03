"""
1814. Count Nice Pairs in an Array
Medium

25

8

Add to List

Share
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.



Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
Example 2:

Input: nums = [13,10,35,24,76]
Output: 4


Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
"""
from functools import lru_cache

"""
Math

Observation:
number of nice divisors is equal to product of the count of each prime factor. So the problem is reduced to: given n, find a sequence of numbers whose sum equals n, and whose product is maximized.

It can be proved that the sequence numbers should be no larger than 4.

So we basically try to decompose number into as many 3 as possible, until remainder <=4.
"""


class Solution:
    def maxNiceDivisors(self, n: int) -> int:
        if n <= 3: return n
        MOD = 10 ** 9 + 7

        num_3 = n // 3
        remainder = n % 3

        # 3*a+1
        if remainder == 1:
            remainder = 4
            num_3 -= 1
        # 3*a+2
        elif remainder == 2:
            pass
        # 3*a+0
        elif remainder == 0:  # we will multiply by remainder, so change 0 to 1
            remainder = 1

        return (pow(3, num_3, MOD) * remainder) % MOD


"""
DP bottom up

dp[i] = max(dp[i], max(j, dp[j])*(i-j))

TLE <= input range 10^9 too large for DP
"""


class Solution1:
    def maxNiceDivisors(self, n: int) -> int:
        if n <= 3: return n
        MOD = 10 ** 9 + 7
        dp = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(i):
                dp[i] = (max(dp[i], (max(j, dp[j]) * (i - j))) % MOD)

        # print(dp[-1])
        return dp[-1] % MOD

def main():
    sol = Solution()
    assert sol.maxNiceDivisors(5) == 6, 'fails'

    assert sol.maxNiceDivisors(8) == 18, 'fails'


if __name__ == '__main__':
   main()