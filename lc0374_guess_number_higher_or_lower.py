"""
374. Guess Number Higher or Lower
Easy

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.



Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
Example 4:

Input: n = 2, pick = 2
Output: 2


Constraints:

1 <= n <= 231 - 1
1 <= pick <= n
"""
from functools import lru_cache
from typing import List

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

"""
binary search
"""

def guess(num):
    return num

class Solution:
    def guessNumber(self, n: int) -> int:

        lo = 1
        hi = n

        while lo < hi:
            mid = lo + (hi - lo) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                hi = mid
            else:  # res == 1:
                lo = mid + 1

        return lo

def main():
    sol = Solution()
    assert sol.guessNumber(10, 6) == 6, 'fails'

if __name__ == '__main__':
   main()