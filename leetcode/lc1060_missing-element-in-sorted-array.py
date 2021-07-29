"""
1060. Missing Element in Sorted Array
Medium

998

42

Add to List

Share
Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.



Example 1:

Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.
Example 2:

Input: nums = [4,7,9,10], k = 3
Output: 8
Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: nums = [1,2,4], k = 3
Output: 6
Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.


Constraints:

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^7
nums is sorted in ascending order, and all the elements are unique.
1 <= k <= 10^8


Follow up: Can you find a logarithmic time complexity (i.e., O(log(n))) solution?

"""
from typing import List

"""
One Pass

if nums[i] - nums[i-1] > 1, means there are nums[i]-nums[i-1] missing numbers in between, so we reduce the total missing count

time O(N)
"""


class Solution0:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)

        for i in range(1, n):
            if nums[i] - nums[i - 1] - 1 < k:
                k -= nums[i] - nums[i - 1] - 1
            else:  # missing within there
                return nums[i - 1] + k

        if k >= 0:
            return nums[n - 1] + k


"""
Array

Since input array is sorted, we can use binary search to fnd the left most element such that the number of missing numbers until this element is less than or equal to k.

if nums[i] - nums[i-1] > 1, means there are nums[i]-nums[i-1] missing numbers in between, so we reduce the total missing count

if nums[i] - nums[0] > i-0-k, that means k-th missing is to right of nums[i]
we look for nums[i]-nums[0] >= i-0+k and nums[i-1]-nums[0]<i-0+k

nums[n - 1] - nums[0] + 1: the total number from beginning to ending, e.g.[4,7,9,10], if filled with all numbers [4,5,6,7,8,9,10] totally 7
nums[n - 1] - nums[0] + 1 - n: this array missing how many numbers, e.g. should be 7 numbers but only 4, missing 3        

time O(log(N))
"""


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)

        l = nums[n - 1] - nums[0] + 1  # real value range from nums[0] to nums[n-1]
        missing = l - n  # missing counts
        if k > missing:  # if k-th missing is after end of nums[n-1]
            return nums[n - 1] + k - missing

        lo, hi = 0, n - 1
        while lo < hi:
            mi = lo + (hi - lo + 1) // 2
            missing = nums[mi] - nums[lo] - (mi - lo)  # missing from this range
            if missing < k:  # not enough missing, needs to move mid to right
                lo = mi
                k -= missing
            else:  # have more missing than needed, needs to move mid to left
                hi = mi - 1

        return nums[lo] + k

def main():
    sol = Solution()
    assert sol.missingElement(nums = [4,7,9,10], k = 1) == 5, 'fails'

    assert sol.missingElement(nums = [4,7,9,10], k = 3) == 8, 'fails'

    assert sol.missingElement(nums = [1,2,4], k = 3) == 6, 'fails'


if __name__ == '__main__':
   main()