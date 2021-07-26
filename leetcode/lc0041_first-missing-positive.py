"""
41. First Missing Positive
Hard

6235

1050

Add to List

Share
Given an unsorted integer array nums, find the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1


Constraints:

1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""
from typing import List

"""
Array

from 1 to n, check each of i if it is in set(nums)
"""


class Solution0:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)
        for i in range(1, n + 1):
            if i not in nums:
                return i

        return i + 1  # if all numbers in [1, n+1] presents, missing n+1


"""
Array

from 1 to n, check each of i if it is in set(nums)
"""
class Solution0:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)
        for i in range(1, n+1):
            if i not in nums:
                return i

        return i + 1 # if all numbers in [1, n+1] presents, missing n+1

"""
Try to optimize using O(1) space (allowing modifying input array)

observation, if there's no missing in first n numbers, then nums[i] must be 1, 2, 3, 4, ..., n at index 0, 1, 2, ..., n-1.

Put each number in its right place.

For example:

When we find 5, then swap it with A[4].

At last, the first place where its number is not right, return the place + 1.    

[3, 4, 2, 1, 5]
 2, 4, 3, 1, 5 <= after first swap (nums[nums[0]-1]=2 != nums[0]=3)
 4, 2, 3, 1, 5 <= second swap nums[nums[0]-1] = 4 != nums[0] = 2
 1, 2, 3, 4, 5 <= second swap nums[nums[0]-1] = 1 != nums[0] = 4
 
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            # exclude <0, or > n, then check if nums[i] are in right position,
            while nums[i] > 0 and nums[i] <= n and nums[nums[i]-1] != nums[i]:
                # if not,
                # swap nums[nums[i]-1] and nums[i]
                t = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = t

        for i in range(n):
            if nums[i] != i+1:
                return i+1

        # all nums <=n presents
        return n+1

def main():
    sol = Solution()
    assert sol.firstMissingPositive(nums = [1,1]) == 2, 'fails'

    # assert sol.firstMissingPositive(nums = [1,2,0]) == 3, 'fails'
    #
    # assert sol.firstMissingPositive(nums = [3,4,-1,1]) == 2, 'fails'
    #
    # assert sol.firstMissingPositive(nums = [7,8,9,11,12]) == 1, 'fails'


if __name__ == '__main__':
   main()