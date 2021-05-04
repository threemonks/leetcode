"""
55. Jump Game
Medium

6203

424

Add to List

Share
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i] <= 10^5
"""
from typing import List

"""
Greedy

Each element in the array represents your maximum jump length at that position.
=> at i-th position, we can jump at most to i+nums[i] position

So we just need to try jump the most at each location, and keep track of a global furthest position, whenever this global furthest position is at or beyond last index, return True

time O(n)
"""


class Solution0:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        farthest = 0
        for i in range(n):
            if farthest >= i:  # if we can get to i, then from i we can go to i+nums[i]
                farthest = max(farthest, i + nums[i])
            if farthest >= n - 1:  # if can get to n-1 in any steps, we reached end
                return True

        return False


"""
DP

dp[i] := can reach end from i

dp[i] = dp[0] == True and  (0+nums[0] > i) # can reach i from 0
 or     dp[1] == True and (1+nums[1]>=i) # can reach i from 1
 ...
        dp[i-1] == True and i-1+nums[i-1]>=i

try to jump some steps further to make it pass?

TLE

time O(N^2)
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        dp = [False] * (n)
        dp[0] = nums[0] >= 0
        i = 0
        while i < n:
            for j in range(i):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    i = j + nums[j] - 1  # cancel the +1 at bottom
                    break
            i += 1

        return dp[n - 1]


def main():
    sol = Solution()
    assert sol.canJump(nums = [2,3,1,1,4]) is True, 'fails'

    assert sol.canJump(nums = [3,2,1,0,4]) is False, 'fails'

if __name__ == '__main__':
   main()