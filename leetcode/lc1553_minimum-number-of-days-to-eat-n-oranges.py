"""
1553. Minimum Number of Days to Eat N Oranges
Hard

481

37

Add to List

Share
There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

Eat one orange.
If the number of remaining oranges (n) is divisible by 2 then you can eat  n/2 oranges.
If the number of remaining oranges (n) is divisible by 3 then you can eat  2*(n/3) oranges.
You can only choose one of the actions per day.

Return the minimum number of days to eat n oranges.



Example 1:

Input: n = 10
Output: 4
Explanation: You have 10 oranges.
Day 1: Eat 1 orange,  10 - 1 = 9.
Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)
Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1.
Day 4: Eat the last orange  1 - 1  = 0.
You need at least 4 days to eat the 10 oranges.
Example 2:

Input: n = 6
Output: 3
Explanation: You have 6 oranges.
Day 1: Eat 3 oranges, 6 - 6/2 = 6 - 3 = 3. (Since 6 is divisible by 2).
Day 2: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. (Since 3 is divisible by 3)
Day 3: Eat the last orange  1 - 1  = 0.
You need at least 3 days to eat the 6 oranges.
Example 3:

Input: n = 1
Output: 1
Example 4:

Input: n = 56
Output: 6


Constraints:

1 <= n <= 2*10^9
"""
from functools import lru_cache

"""
DP

Observation:
1. if n/2 != 0, then (n - n%2) % 2 == 0. So it takes at most n%2 days till n%2==0. Same logic for n/3

The key idea is that we should never take more than 2 consecutive -1 operations.

time log(N)
"""


class Solution0:
    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if n <= 1:
            return 1
        return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3))


"""
BFS

at each node (remaining orange n), we have three branches (options) to explore,
if n%2==0, we eat n//2 in one day, and remains quantity n//2
if n%3==0, we eat (2*n)//3 in one day, and remains quantity n//3
and we can always eat just one in one day, remains quantity n-1

"""
from collections import deque


class Solution:
    def minDays(self, n: int) -> int:
        q = deque([(n, 0)])
        seen = set()
        while q:
            cur, days = q.popleft()
            if cur == 0:
                return days
            if cur not in seen:
                if cur % 2 == 0:
                    q.append((cur // 2, days + 1))
                if cur % 3 == 0:
                    q.append((cur // 3, days + 1))
                q.append((cur - 1, days + 1))
                seen.add(cur)

        return -1

def main():
    sol = Solution()
    assert sol.minDays(n = 10) == 4, 'fails'

    assert sol.minDays(n = 6) == 3, 'fails'

    assert sol.minDays(n = 1) == 1, 'fails'

    assert sol.minDays(n = 56) == 6, 'fails'


if __name__ == '__main__':
   main()