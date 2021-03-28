"""
343. Integer Break
Medium

Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.



Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.


Constraints:

2 <= n <= 58
"""
"""
Math

lets assume we can break n into n/x x's, and the product is the (x)^(n/x). To maximize (x)^(n/x), we take derivative, gives n * x^(n/x-2) * (1 - ln(x)). To maximize (x)^(n/x), we need the derivative to be 0, which is zero when x = e.

But we can only break it into integer, so we have to choose integer. e is between 2 and 3, and in general, 3 is more preferred than 2.

We can see

6 = 3 + 3 => 3*3 = 9
    2 + 2 + 2 => 2*2*2 = 8 < 9

Since any number f > 4 can be broken into f-2 + 2, and (f-2)*2 = 2f-4 > f for f>4
its also better than split into f-1+1 as (f-2)*2 > (f-1)*1 for f > 4

So we should have only 3 and 2 left in the borken down integers, and we want as many as 3 as possible except for n=4

"""


class Solution:
    def integerBreak(self, n: int) -> int:
        MOD = 100000007
        if n == 2: return 1
        if n == 3: return 2
        num_3 = n // 3
        remainder = n % 3
        # n = 3*a+1
        if remainder == 0:  # we multiple remainder after this, so we change 0 to 1
            remainder = 1
        elif remainder == 1:  # we prefer 2*2 over 3*1 for 4
            remainder = 4
            num_3 -= 1
        elif remainder == 2:
            pass

        return pow(3, num_3) * remainder


def main():
    sol = Solution()
    assert sol.integerBreak(2) == 1, 'fails'

    assert sol.integerBreak(10) == 36, 'fails'


if __name__ == '__main__':
   main()