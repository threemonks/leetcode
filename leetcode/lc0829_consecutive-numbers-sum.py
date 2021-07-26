"""
829. Consecutive Numbers Sum
Hard

623

784

Add to List

Share
Given a positive integer n, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: n = 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: n = 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: n = 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= n <= 10 ^ 9.
"""
import math

"""
Math

if n is sum of consecutive positive integers, it would be sum of 1, 2, 3, ..., k consecutive positive integers

let's assume n is sum of k consecutive positive integers, starts at x, then we have
n = x+1 + x+2 + ... + x+k = x*k + k*(k-1)/2
since we know x >= 0, then we have k*(k-1)/2 <= n, or k*(k-1)<=2*n,
or we know k's range is k < sqrt(2*n)

so we can brutally try all k from 2 to sqrt(2*n), if (n-k*(k-1)/2)/k is an integer, then we find a valid answer of k integer sum
"""


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        sqrt = int(math.sqrt(2 * n))

        ans = 1
        for k in range(2, sqrt + 1):
            if (n - k * (k - 1) // 2) % k == 0:
                # print('k=%s x=%s' % (k, (n - k*(k-1)//2) % k))
                ans += 1

        return ans

def main():
    sol = Solution()
    assert sol.consecutiveNumbersSum(n = 5) == 2, 'fails'

    assert sol.consecutiveNumbersSum(n = 9) == 3, 'fails'

    assert sol.consecutiveNumbersSum(n = 15) == 4, 'fails'

if __name__ == '__main__':
   main()