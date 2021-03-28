"""
1808. Maximize Number of Nice Divisors
Hard

47

75

Add to List

Share
You are given a positive integer primeFactors. You are asked to construct a positive integer n that satisfies the following conditions:

The number of prime factors of n (not necessarily distinct) is at most primeFactors.
The number of nice divisors of n is maximized. Note that a divisor of n is nice if it is divisible by every prime factor of n. For example, if n = 12, then its prime factors are [2,2,3], then 6 and 12 are nice divisors, while 3 and 4 are not.
Return the number of nice divisors of n. Since that number can be too large, return it modulo 109 + 7.

Note that a prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. The prime factors of a number n is a list of prime numbers such that their product equals n.



Example 1:

Input: primeFactors = 5
Output: 6
Explanation: 200 is a valid value of n.
It has 5 prime factors: [2,2,2,5,5], and it has 6 nice divisors: [10,20,40,50,100,200].
There is not other value of n that has at most 5 prime factors and more nice divisors.
Example 2:

Input: primeFactors = 8
Output: 18


Constraints:

1 <= primeFactors <= 109
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