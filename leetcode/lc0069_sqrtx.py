"""
69. Sqrt(x)
Easy

5301

3692

Add to List

Share
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


Constraints:

0 <= x <= 2^31 - 1
"""
from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right = 2, x//2
        while left <= right:
            mid = left+(right-left)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                left = mid+1
            else: # mid*mid > x:
                right = mid-1

        # when while terminate, left > right
        # if x is perfect square, we would return mid already
        # if x is imperfect sqaure, right < sqrt(x) < left
        # to round down sqrt(x), then we return right
        return right


def main():
    sol = Solution()
    assert sol.mySqrt(4) == 2, 'fails'

    assert sol.mySqrt(8) == 2, 'fails'

if __name__ == '__main__':
   main()