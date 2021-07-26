"""
50. Pow(x, n)
Medium

2710

4038

Add to List

Share
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
-10^4 <= x^n <= 10^4
"""
"""
Recurisve / Math

time O(log(N))
space O(logN) -> iterative can reduce space usage to O(1)

"""
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == 2:
            return x * x
        n2 = n//2
        return self.myPow(x, n2) * self.myPow(x, n-n2)


def main():
    sol = Solution()
    assert sol.myPow(x = 2.00000, n = 10) == 1024.00, 'fails'

    assert sol.myPow(x = 2.10000, n = 3) == 9.261000000000001, 'fails'

    assert sol.myPow(x = 2.00000, n = -2) == 0.25, 'fails'

if __name__ == '__main__':
   main()