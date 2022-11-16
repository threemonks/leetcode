"""
858. Mirror Reflection
Medium

1028

2439

Add to List

Share
There is a special square room with mirrors on each of the four walls. Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Given the two integers p and q, return the number of the receptor that the ray meets first.

The test cases are guaranteed so that the ray will meet a receptor eventually.



Example 1:


Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
Example 2:

Input: p = 3, q = 1
Output: 1


Constraints:

1 <= q <= p <= 1000
"""
"""
Geometry

See explanation with drawings here https://leetcode.com/problems/mirror-reflection/discuss/146336/Java-solution-with-an-easy-to-understand-explanation

imagine we extend this square room infinitely to above, and for reflection from top, we just consider it going through (which will hit the side wall after going through top wall)
the problem then becomes to look for some integer m, and n, such that m*p = n*q

m = the number of room extension + 1.
n = the number of light reflection + 1.

If the number of light reflection is odd (which means n is even), it means the corner is on the left-hand side. The possible corner is 2.
Otherwise, the corner is on the right-hand side. The possible corners are 0 and 1.
Given the corner is on the right-hand side.
If the number of room extension is even (which means m is odd), it means the corner is 1. Otherwise, the corner is 0.
So, we can conclude:

m is even & n is odd => return 0.
m is odd & n is odd => return 1.
m is odd & n is even => return 2.

"""
import math


class Solution:

    def mirrorReflection(self, p: int, q: int) -> int:
        m, n = 1, 1
        while (m * p != n * q):
            n += 1
            m = n * q // p

        # after the light meets a corner, find out which corner it is
        if m % 2 == 0 and n % 2 == 1:
            return 0
        elif m % 2 == 1 and n % 2 == 1:
            return 1
        elif m % 2 == 1 and n % 2 == 0:
            return 2
        else:  # impossible for both m and n been even, because then we divide both m and n by 2, which means we should already meet a corner before these m, n values
            return -1


def main():
    sol = Solution()
    assert sol.mirrorReflection(p = 2, q = 1) == 2, 'fails'

    assert sol.mirrorReflection(p = 3, q = 1) == 1, 'fails'

if __name__ == '__main__':
   main()