"""
1753. Maximum Score From Removing Stones
Medium

You are playing a solitaire game with three piles of stones of sizes a​​​​​​, b,​​​​​​ and c​​​​​​ respectively. Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

Given three integers a​​​​​, b,​​​​​ and c​​​​​, return the maximum score you can get.

Example 1:

Input: a = 2, b = 4, c = 6
Output: 6
Explanation: The starting state is (2, 4, 6). One optimal set of moves is:
- Take from 1st and 3rd piles, state is now (1, 4, 5)
- Take from 1st and 3rd piles, state is now (0, 4, 4)
- Take from 2nd and 3rd piles, state is now (0, 3, 3)
- Take from 2nd and 3rd piles, state is now (0, 2, 2)
- Take from 2nd and 3rd piles, state is now (0, 1, 1)
- Take from 2nd and 3rd piles, state is now (0, 0, 0)
There are fewer than two non-empty piles, so the game ends. Total: 6 points.
Example 2:

Input: a = 4, b = 4, c = 6
Output: 7
Explanation: The starting state is (4, 4, 6). One optimal set of moves is:
- Take from 1st and 2nd piles, state is now (3, 3, 6)
- Take from 1st and 3rd piles, state is now (2, 3, 5)
- Take from 1st and 3rd piles, state is now (1, 3, 4)
- Take from 1st and 3rd piles, state is now (0, 3, 3)
- Take from 2nd and 3rd piles, state is now (0, 2, 2)
- Take from 2nd and 3rd piles, state is now (0, 1, 1)
- Take from 2nd and 3rd piles, state is now (0, 0, 0)
There are fewer than two non-empty piles, so the game ends. Total: 7 points.
Example 3:

Input: a = 1, b = 8, c = 8
Output: 8
Explanation: One optimal set of moves is to take from the 2nd and 3rd piles for 8 turns until they are empty.
After that, there are fewer than two non-empty piles, so the game ends.


Constraints:

1 <= a, b, c <= 105
"""
"""
Math
Let the pile with most be hi, the other two (lower) ones be lo1, lo2, there could be two situations
1. if lo1+lo2 <= hi, then we can at most take lo1+lo2 stones, with some (or 0) on hi left
2. if lo1+lo2 > hi, it can be proved that there will be two possible outcomes
  i) we can take all stones (if total sum is even)
  ii) we can take all but one stones (if total sum is odd)

proof is at 
https://leetcode.com/problems/maximum-score-from-removing-stones/discuss/1054216/Prove-the-math-O(1)

basic idea:
if lo1 + lo2 > hi, if we take hi-lo1 from lo2, and take hi-lo2 from lo1, and take (hi-lo1)+(hi-lo2) from hi, then all three are left with same amount lo1 + lo2 - hi => so whatever the pile numbers are, we can always reduce them to the same amount
on the other hand, if the piles all have more than 2 on each, we can always take 2 out of each (gaining 3 points), so that the remaining numbers are less than 2.
then this reduces to two possible situation, 
  i) all three piles have 1 stone => we can take 2, but let 1
  ii) all three piles have 0 stone => done

"""

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:

        nums = [a, b, c]
        nums = sorted(nums)
        if nums[0] + nums[1] <= nums[2]:  # if lo1+lo2 < hi, we can get at most lo1+lo2
            return nums[0] + nums[1]
        else:  # else, we can get at most (a+b+c)//2
            return sum(nums) // 2


def main():
    sol = Solution()
    assert sol.maximumScore(a = 2, b = 4, c = 6) == 6, 'fails'

    assert sol.maximumScore(a = 4, b = 4, c = 6) == 7, 'fails'

    assert sol.maximumScore(a = 1, b = 8, c = 8) == 8, 'fails'



if __name__ == '__main__':
   main()