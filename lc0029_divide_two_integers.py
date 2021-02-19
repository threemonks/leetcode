"""
29. Divide Two Integers
Medium

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.


Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1


Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0

"""
"""
brutal force

improvement with exponential search, double divisor everytime, until it is bigger than dividend

Note:
1. requirement is function returns within [-2^31 ~ 2^31-1], but -2^31/(-1) would result is 2^31, which exceeds the range, and needs to return 2^31-1 instead
2. try to subtract one divisor from dividend a time is too slow, try to double the divisor by x power of 2 while divisor>>x < dividend, and subtract that from dividend to speed up the division, along with that add 1>>x to result, and reduce divisor by half until it is smaller than remainder from previous subtraction, when this finishes, it yields a quotient and a remainder that is less than divisor.

time O(log(N)) -- bit shift

"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        if dividend == -2147483648 and divisor == -1: # special case as 2147483648 is out of range [-2^31 ~ 2^31-1]
            return 2147483647
        else:
            a, b, ans = dividend, divisor, 0
            if a < 0:
                a = -a
            if b < 0:
                b = -b

            for x in range(32, -1, -1):
                if b<<x <= a:
                    ans += 1<<x
                    a -= (b<<x)

            return ans if (dividend > 0) == (divisor > 0) else -ans


def main():
    sol = Solution()
    assert sol.divide(dividend = 10, divisor = 3) == 3, 'fails'

    assert sol.divide(dividend = 7, divisor = -3) == -2, 'fails'

    assert sol.divide(dividend = 0, divisor = 1) == 0, 'fails'

    assert sol.divide(dividend = 1, divisor = 1) == 1, 'fails'


if __name__ == '__main__':
   main()