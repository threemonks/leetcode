"""
1780. Check if Number is a Sum of Powers of Three
Medium

Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.



Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false


Constraints:

1 <= n <= 107
"""
import collections

"""
Math
"""

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powers = collections.defaultdict(int)
        max_power = 20 # 3^20 > 10^7
        remainder = n
        for i in range(max_power, -1, -1):
            ipower = 3 ** i
            if remainder >= ipower:
                remainder = remainder - ipower

        return remainder == 0


def main():
    sol = Solution()
    assert sol.checkPowersOfThree(n = 12) is True, 'fails'

    assert sol.checkPowersOfThree(n = 91) is True, 'fails'

    assert sol.checkPowersOfThree(n = 21) is False, 'fails'


if __name__ == '__main__':
   main()