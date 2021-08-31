"""
338. Counting Bits
Easy

4680

233

Add to List

Share
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.



Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


Constraints:

0 <= n <= 105


Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

"""
from typing import List

"""
Bit Manipulation

time O(N(logN))
space O(1)
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for _ in range(n + 1)]

        for i in range(n + 1):
            v = i
            k = 0
            while 2 ** k <= v:
                k += 1

            while k >= 0:
                if v // (2 ** k) == 1:
                    ans[i] += 1
                    v %= (2 ** k)
                k -= 1

        return ans


def main():
    sol = Solution()
    assert sol.countBits(2) == [0,1,1], 'fails'

    assert sol.countBits(5) == [0,1,1,2,1,2], 'fails'


if __name__ == '__main__':
   main()