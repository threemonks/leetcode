"""
1509. Minimum Difference Between Largest and Smallest Value in Three Moves
Medium

630

80

Add to List

Share
Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.



Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1].
The difference between the maximum and minimum is 1-0 = 1.
Example 3:

Input: nums = [6,6,0,1,1,4,6]
Output: 2
Example 4:

Input: nums = [1,5,6,14,15]
Output: 1


Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

"""
from typing import List

"""
Greedy

There are basically four possible moves after sort
1. remove 3 from left, 0 from right
2. remove 2 from left, 1 from right
3. remove 1 from left, 2 from right
4. remove 0 from left, 3 from right
we take min of the four cases

"""


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums = sorted(nums)

        ans = min(nums[-1] - nums[3],  # 3 from left, 0 from right
                  nums[-2] - nums[2],  # 2 from left, 1 from right
                  nums[-3] - nums[1],  # 1 from left, 2 from right
                  nums[-4] - nums[0]  # 0 from left, 3 from right
                  )

        return ans


def main():
    sol = Solution()
    assert sol.minDifference(nums = [5,3,2,4]) == 0, 'fails'

    assert sol.minDifference(nums = [1,5,0,10,14]) == 1, 'fails'

    assert sol.minDifference(nums = [6,6,0,1,1,4,6]) == 2, 'fails'

    assert sol.minDifference(nums = [1,5,6,14,15]) == 1, 'fails'

if __name__ == '__main__':
   main()