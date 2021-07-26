"""
1510. Stone Game IV
Hard

342

24

Add to List

Share
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile.  On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n. Return True if and only if Alice wins the game otherwise return False, assuming both players play optimally.



Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
Example 4:

Input: n = 7
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
If Alice starts removing 4 stones, Bob will remove 1 stone then Alice should remove only 1 stone and finally Bob removes the last one (7 -> 3 -> 2 -> 1 -> 0).
If Alice starts removing 1 stone, Bob will remove 4 stones then Alice only can remove 1 stone and finally Bob removes the last one (7 -> 6 -> 2 -> 1 -> 0).
Example 5:

Input: n = 17
Output: false
Explanation: Alice can't win the game if Bob plays optimally.


Constraints:

1 <= n <= 10^5

"""
import math
from functools import lru_cache
from typing import List
"""
DP top down / recursive

observation

dp[i] : result (boolean must win or lose) of the current player when there's i stone left 
dp[i] = true if we can force component to false state
    for j from 1 to i/2
        if j*j = i:
        return True

"""

import math
class Solution1:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def solve(i): # i - remaining stones
            if i == 0 :
                return False
            r = int(math.sqrt(i))
            for j in range(1, r+1):
                if not solve(i-j*j): # if this move force opponent into lose, then we win
                    return True

            return False

        return solve(n)


"""
DP bottom up
dp[i] : given i stone remains, the current play must win or must lose?

since one can only remove square numbers
dp[i] depends on dp[i-1], dp[i-4], dp[i-9], ....
time O(n*sqrt(n))
space O(n)
"""


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        dp[0] = False  # no stone to remove, must lose

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                if dp[i - j * j] is False:
                    dp[i] = True
                    break
                j += 1

        return dp[n]


def main():
    sol = Solution()
    assert sol.winnerSquareGame(1) is True, 'fails'

    assert sol.winnerSquareGame(2) is False, 'fails'

    assert sol.winnerSquareGame(4) is True, 'fails'

    assert sol.winnerSquareGame(7) is False, 'fails'

    assert sol.winnerSquareGame(17) is False, 'fails'

if __name__ == '__main__':
   main()