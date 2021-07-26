"""
1872. Stone Game VIII
Hard

69

4

Add to List

Share
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, while the number of stones is more than one, they will do the following:

Choose an integer x > 1, and remove the leftmost x stones from the row.
Add the sum of the removed stones' values to the player's score.
Place a new stone, whose value is equal to that sum, on the left side of the row.
The game stops when only one stone is left in the row.

The score difference between Alice and Bob is (Alice's score - Bob's score). Alice's goal is to maximize the score difference, and Bob's goal is the minimize the score difference.

Given an integer array stones of length n where stones[i] represents the value of the ith stone from the left, return the score difference between Alice and Bob if they both play optimally.



Example 1:

Input: stones = [-1,2,-3,4,-5]
Output: 5
Explanation:
- Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her score, and places a stone of
  value 2 on the left. stones = [2,-5].
- Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places a stone of value -3 on
  the left. stones = [-3].
The difference between their scores is 2 - (-3) = 5.
Example 2:

Input: stones = [7,-6,5,10,5,-2,-6]
Output: 13
Explanation:
- Alice removes all stones, adds 7 + (-6) + 5 + 10 + 5 + (-2) + (-6) = 13 to her score, and places a
  stone of value 13 on the left. stones = [13].
The difference between their scores is 13 - 0 = 13.
Example 3:

Input: stones = [-10,-12]
Output: -22
Explanation:
- Alice can only make one move, which is to remove both stones. She adds (-10) + (-12) = -22 to her
  score and places a stone of value -22 on the left. stones = [-22].
The difference between their scores is (-22) - 0 = -22.


Constraints:

n == stones.length
2 <= n <= 10^5
-10^4 <= stones[i] <= 10^4
"""
from typing import List

"""
Greedy

-1, 2, -3, 4, -5
-1, 1, -2, 2, -3 presum
-6 -4  -7  5  -3 gain

last row is diff A-B if alice first pick update to that index

1. if Alice first pick up all stones, her score is -3, she puts back -3, bob cannot take (since there's only 1 stone left), so Alice's gain is A-B = -3 - 0 = -3, we store -3 at index 4 on row 3
2. if Alice first pick up to index 3, her score is 2, and she put back 2, then bob's score is 2+-5=-3, so her advantage is A-B=2-(-3)=5, we write 5 as the gain at index 3 on row 3. We also notice that 5 = presum[3] - max(gain[4:]), i.e., 
gain[3] = presum[3] - max(gain[4:])
3. if Alice first pick up to index 2, her score is presum[2]=-2, then Bob has -2, 4, -5 to pick, his best move is to pick (-2, 4), which gives him score as presum[3]=2, then Alice has to pick (2, -5) with score -3, so Alice's total gain advantage is -2+-3-2=-7, which is just -2 - 5, i.e.,
gain[2] = presum[2] - max(gain[3:])
4. if Alice first pick up to index 1, her score is presum[1]=1, then Bob has 1,-3,4,5 to pick from, his best move is still pick up to index 3, with score presum[3]=2, then Alice has to pick 2, -5 with score presum[4]=-3, and Alice's gain is 1-2+-3=-4, which is just 1 - 5 = -4
gain[1] = presum[1] - max(gain[2:])
5. if Alice first pickup just index 0, then her score is presum[0] = -1, Bob's best move is again pick up to index 3 with score 2, then Alice has to pick two remaining with score presum[4]=-3, so Alice's gain is -1-2+-3=-6, which is -6=-1-5
gain[0] = presum[0] - max(gain[1:])

So if we calculate row 3 gain from right to next, and keep the max of gain up to current index, this can be solved in O(N)

Eventually, Alice's best move would result in max gain at max(gain)

"""


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return 0  # no move possible
        elif n == 2:
            return sum(stones)  # only Alice can move once

        presum = [0] * n
        presum[0] = stones[0]

        for i in range(1, n):
            presum[i] = presum[i - 1] + stones[i]

        gain = [0] * n
        gain[n - 1] = presum[n - 1]
        max_gain = gain[n - 1]

        for i in range(n - 2, -1, -1):
            gain[i] = presum[i] - max_gain
            max_gain = max(max_gain, gain[i])

        return max_gain


"""
DP

"""

def main():
    sol = Solution()
    assert sol.stoneGameVIII(stones = [-1,2,-3,4,-5]) == 5, 'fails'

    assert sol.stoneGameVIII(stones = [7,-6,5,10,5,-2,-6]) == 13, 'fails'

    assert sol.stoneGameVIII(stones = [-10,-12]) == -22, 'fails'

if __name__ == '__main__':
   main()