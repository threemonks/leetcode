"""
375. Guess Number Higher or Lower II
Medium

We are playing the Guessing Game. The game will work as follows:

I pick a number between 1 and n.
You guess a number.
If you guess the right number, you win the game.
If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.



Example 1:


Input: n = 10
Output: 16
Explanation: The winning strategy is as follows:
- The range is [1,10]. Guess 7.
    - If this is my number, your total is $0. Otherwise, you pay $7.
    - If my number is higher, the range is [8,10]. Guess 9.
        - If this is my number, your total is $7. Otherwise, you pay $9.
        - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
        - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
    - If my number is lower, the range is [1,6]. Guess 3.
        - If this is my number, your total is $7. Otherwise, you pay $3.
        - If my number is higher, the range is [4,6]. Guess 5.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
            - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
            - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
        - If my number is lower, the range is [1,2]. Guess 1.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
            - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.
Example 2:

Input: n = 1
Output: 0
Explanation: There is only one possible number, so you can guess 1 and not have to pay anything.
Example 3:

Input: n = 2
Output: 1
Explanation: There are two possible numbers, 1 and 2.
- Guess 1.
    - If this is my number, your total is $0. Otherwise, you pay $1.
    - If my number is higher, it must be 2. Guess 2. Your total is $1.
The worst case is that you pay $1.


Constraints:

1 <= n <= 200
"""
import math
from functools import lru_cache
from typing import List

"""
dp top down / recursive
   dfs(i, j) => min amount to guarantee win for target [i, j+1]
   dfs(i, j):
     for k in i to j:
       dfs(i, j) = max(dfs(i, k-1), dfs(k+1, j))
     take min dfs(i, j) for all k from i to j (including j)
"""
from functools import lru_cache


class Solution0:
    def getMoneyAmount(self, n: int) -> int:

        @lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0
            res = math.inf
            for k in range(i, j + 1):
                res = min(res, k + max(dfs(i, k - 1), dfs(k + 1, j)))

            # print('i=%s j=%s res=%s' % (i, j, res))
            return res

        return dfs(1, n)


"""
dp bottom up
dfs(i, j) => dp[i][j] since a and b are both int
dp[i][j]
    for k from i to j:
      dp[i][j] = min(dp[i][j], k+max(dp[i][k-1], dp[k+1][j]))
"""


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[None for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][i] = 0

        for l in range(2, n + 1):  # no need for length 1 range
            for i in range(1, n + 1 - l + 1):
                j = i + l - 1
                # print('i=%s j=%s' % (i, j))
                dp[i][j] = math.inf
                # print('i=%s j=%s l=%s dp[i][j]=%s' % (i, j, l, dp[i][j]))
                for k in range(i, j + 1):
                    dp[i][j] = min(dp[i][j],
                                   k + max(dp[i][k - 1] if k - 1 >= i else 0, dp[k + 1][j] if k + 1 <= j else 0))

        return dp[1][n]


"""
dp bottom up - another way to loop
WARNING: this fails because it does not guarantee that all dp[i][k-1] and dp[k+1][j] values are calculated before dp[i][j]
"""


class Solution2:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[None for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][i] = 0

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):  # no need for length 1 range
                # print('i=%s j=%s' % (i, j))
                dp[i][j] = math.inf
                # print('i=%s j=%s l=%s dp[i][j]=%s' % (i, j, j-i+1, dp[i][j]))
                for k in range(i, j + 1):
                    dp[i][j] = min(dp[i][j],
                                   k + max(dp[i][k - 1] if k - 1 >= i else 0, dp[k + 1][j] if k + 1 <= j else 0))

        return dp[1][n]

def main():
    sol = Solution()
    assert sol.getMoneyAmount(10) == 16, 'fails'

    assert sol.getMoneyAmount(6) == 8, 'fails'

    assert sol.getMoneyAmount(2) == 1, 'fails'

    assert sol.getMoneyAmount(1) == 0, 'fails'

if __name__ == '__main__':
   main()