"""
1686. Stone Game VI
Medium

245

15

Add to List

Share
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones in a pile. On each player's turn, they can remove a stone from the pile and receive points based on the stone's value. Alice and Bob may value the stones differently.

You are given two integer arrays of length n, aliceValues and bobValues. Each aliceValues[i] and bobValues[i] represents how Alice and Bob, respectively, value the ith stone.

The winner is the person with the most points after all the stones are chosen. If both players have the same amount of points, the game results in a draw. Both players will play optimally. Both players know the other's values.

Determine the result of the game, and:

If Alice wins, return 1.
If Bob wins, return -1.
If the game results in a draw, return 0.


Example 1:

Input: aliceValues = [1,3], bobValues = [2,1]
Output: 1
Explanation:
If Alice takes stone 1 (0-indexed) first, Alice will receive 3 points.
Bob can only choose stone 0, and will only receive 2 points.
Alice wins.
Example 2:

Input: aliceValues = [1,2], bobValues = [3,1]
Output: 0
Explanation:
If Alice takes stone 0, and Bob takes stone 1, they will both have 1 point.
Draw.
Example 3:

Input: aliceValues = [2,4,3], bobValues = [1,6,7]
Output: -1
Explanation:
Regardless of how Alice plays, Bob will be able to have more points than Alice.
For example, if Alice takes stone 1, Bob can take stone 2, and Alice takes stone 0, Alice will have 6 points to Bob's 7.
Bob wins.


Constraints:

n == aliceValues.length == bobValues.length
1 <= n <= 105
1 <= aliceValues[i], bobValues[i] <= 100
"""
from typing import List

"""
Greedy

key points:
1. when alice takes a[i], it also removes bob from taking b[i], so effectively her score gain is a[i]+b[i]

[1, 3]
[2, 1] a=3, b=2

[1, 2]
[3, 1] => a=1, b=1

[2, 4, 3]
[1, 6, 7] +1, -2, -4

a +1 -4
b -2

[2, 4, 3]
[1, 6, 7] 3, 10, 10

dp[i][0] := alice's score after taking i
dp[i][1] := bob's score after taking i

alice always take the index with max a[i]+b[i]

dp[i][0] = a[i] - max(dp[j][1] for j != i)
dp[i][1] = b[i] - max(dp[j][0] for j != i)

Use heap to store nums (a+b), and greedily always pick the best number at current step.

"""


class Solution0:
    def stoneGameVI(self, a: List[int], b: List[int]) -> int:
        n = len(a)
        nums = [a[i] + b[i] for i in range(n)]
        nums = [(-num, i) for i, num in enumerate(nums)]

        alice = 0
        bob = 0

        heapq.heapify(nums)
        turn = 1
        while nums:
            num, i = heapq.heappop(nums)
            if turn:
                alice += a[i]
            else:
                bob += b[i]
            turn = 1 - turn
            # print('i=%s alice=%s bob=%s' % (i, alice, bob))

        if alice > bob:
            return 1
        elif alice < bob:
            return -1
        else:
            return 0


"""
Greedy

sort a+b and take maximum always, compare final score

"""


class Solution:
    def stoneGameVI(self, a: List[int], b: List[int]) -> int:
        n = len(a)
        nums = [a[i] + b[i] for i in range(n)]
        nums = sorted([(num, i) for i, num in enumerate(nums)], reverse=True)

        alice = 0
        bob = 0

        for idx, numtuple in enumerate(nums):
            num, i = numtuple
            if idx % 2 == 0:
                alice += a[i]
            else:
                bob += b[i]

        if alice > bob:
            return 1
        elif alice < bob:
            return -1
        else:
            return 0


def main():
    sol = Solution()
    assert sol.stoneGameVI(a = [1,3], b = [2,1]) == 1, 'fails'

    assert sol.stoneGameVI(a=[1,2], b = [3,1]) == 0, 'fails'

    assert sol.stoneGameVI(a = [2,4,3], b = [1,6,7]) == -1, 'fails'

if __name__ == '__main__':
   main()