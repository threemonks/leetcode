"""
1567. Maximum Length of Subarray With Positive Product
Medium

419

7

Add to List

Share
Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.



Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
Example 4:

Input: nums = [-1,2]
Output: 1
Example 5:

Input: nums = [1,2,3,5,-6,4,0,10]
Output: 4


Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
from typing import List

"""
Greedy

steps:
1. split whole array by zero
2. if subarray has even number of negative numbers, the whole subarray has positive product
3. if the subarray has odd number of negative numbers, we need to either remove the prefix until the first negative element in this subarray, or remove the suffix starting from the last negative element in this subarray

time O(N)
space O(N) # can further simplify by storing first index, last index and count of negative elements within subarray
"""


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        negative = []  # negative element index within this subarray
        start = 0  # start of subarray
        ans = 0
        for i in range(n):
            if nums[i] < 0:
                negative.append(i)
            elif nums[i] == 0:  # start a new one
                end = i - 1
                # process subarray
                if len(negative) % 2 == 0:
                    ans = max(ans, end - start + 1)
                else:
                    ans = max(ans, max(end - negative[0], negative[-1] - start))
                # reset
                start = i + 1
                negative = []

        # calculate last section
        end = n - 1
        if len(negative) % 2 == 0:
            ans = max(ans, end - start + 1)
        else:
            ans = max(ans, max(end - negative[0], negative[-1] - start))

        return ans


def main():
    sol = Solution()
    assert sol.getMaxLen(nums = [1,-2,-3,4]) == 4, 'fails'

    assert sol.getMaxLen(nums = [0,1,-2,-3,-4]) == 3, 'fails'

    assert sol.getMaxLen(nums = [-1,-2,-3,0,1]) == 2, 'fails'

    assert sol.getMaxLen(nums = [-1,2]) == 1, 'fails'

if __name__ == '__main__':
   main()