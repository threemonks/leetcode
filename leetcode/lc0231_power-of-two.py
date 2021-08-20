"""
231. Power of Two
Easy

1650

237

Add to List

Share
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.



Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
Example 4:

Input: n = 4
Output: true
Example 5:

Input: n = 5
Output: false


Constraints:

-2^31 <= n <= 2^31 - 1


Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfTwo0(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1


"""
Bit Manipulation

x & (-x) => changes x to keep only its right most "1" bit

(x & (-x)) == x => x is power of 2 (there's only one "1" bit in x's binary representation)

"""


class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n == (n & (-n))


"""
Bit Manipulation

x & (x - 1) is a way to set the rightmost 1-bit to zero.
x & (x-1) == 0 => x is power of 2 (it has only one 1-bit, which is now set to 0)
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return (n & (n - 1)) == 0


def main():
    sol = Solution()
    assert sol.isPowerOfTwo(n = 1) == True, 'fails'

    assert sol.isPowerOfTwo(n = 16) == True, 'fails'

    assert sol.isPowerOfTwo(n = 3) == False, 'fails'


if __name__ == '__main__':
   main()