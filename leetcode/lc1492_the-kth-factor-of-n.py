"""
1492. The kth Factor of n
Medium

381

149

Add to List

Share
Given two positive integers n and k.

A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.



Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
Example 2:

Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.
Example 3:

Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
Example 4:

Input: n = 1, k = 1
Output: 1
Explanation: Factors list is [1], the 1st factor is 1.
Example 5:

Input: n = 1000, k = 3
Output: 4
Explanation: Factors list is [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000].


Constraints:

1 <= k <= n <= 1000
"""
import math

"""
Brutal force

time O(N)
"""


class Solution0:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, n + 1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i

        return -1


"""
Heap

i iterate from 1 ... sqrt(n), if n%i ==0, push i and n%i into heap, when heap reaches size k, return heap top

note:
1. note i and n//i could be equal, thus need to ensure push once only

time O(sqrt(N)*logk)
"""
import heapq


class Solution1:
    def kthFactor(self, n: int, k: int) -> int:
        q = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                heapq.heappush(q, -i)
                if i != n // i:
                    heapq.heappush(q, -(n // i))
                while len(q) > k:
                    heapq.heappop(q)

        if len(q) == k:
            return -q[0]
        else:
            return -1


"""
Math

d iterate from 1 ... sqrt(n), k-=1, if n%d ==0,  and k == 0, return d
d iterate from sqrt(n) to 1, k-=1, if n%d ==0, and k==0, then return n//d (n//d increases as d decreases)

note:
1. note d and n//d could be equal, thus need to ensure push once only

time O(sqrt(N))
"""


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f1, f2 = [], []  # list of factors, and corresponding factor pair
        d = 1
        for d in range(1, int(math.sqrt(n)) + 1):
            if n % d == 0:
                f1.append(d)
                f2.append(n // d)

        # remove duplicate if perfect square
        if f1[-1] == f2[-1]:
            f2.pop()

        f = f1 + f2[::-1]  # combine two lists of factors
        if len(f) >= k:
            return f[k - 1]
        else:
            return -1


def main():
    sol = Solution()
    assert sol.kthFactor(n = 12, k = 3) == 3, 'fails'

    assert sol.kthFactor(n = 7, k = 2) == 7, 'fails'

    assert sol.kthFactor(n = 4, k = 4) == -1, 'fails'

    assert sol.kthFactor(n = 1, k = 1) == 1, 'fails'

    assert sol.kthFactor(n = 1000, k = 3) == 4, 'fails'

if __name__ == '__main__':
   main()