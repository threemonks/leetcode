"""
581. Shortest Unsorted Continuous Subarray
Medium

3891

177

Add to List

Share
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.



Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0


Constraints:

1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5

"""
from typing import List

"""
Sort

sort with index, then iterate the sorted with original index, and find which original index does not match with index in sorted output. Those don't match are the unsorted subarray.

[2,6,4,8,10,9,15]
max to left of 9 is 10, which is > 9, so 9 needs to be in subarray to be sorted
(2, 0), (4, 2), (6, 1), (8, 3), (9, 5), (10, 4), (15, 6)

time O(Nlog(N))
space O(1)

"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        numsidx = sorted([(num, i) for i, num in enumerate(nums)])

        left, right = -1, len(nums) - 1
        for i, (num, idx) in enumerate(numsidx):
            if i != idx:  # not sorted
                if left == -1:  # first unsorted
                    left = i
                right = i

        if left == -1:  # already sorted
            return 0
        return right - left + 1


"""
Array Two passes

Iterate array from left to right, keep maxval, if a value is less than maxval seen so far, then it is not in right place, so it is the (up to now) right boundary of the unsorted subarray. Keep iterating until end, we got the final right boundary.

Iterate from right to left, keep min found so far, any number greater than min seen so far would be the current left boundary of unsorted subarray.

time O(N)
"""


class Solution1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        maxval = -math.inf
        right = 0
        for i in range(n):
            maxval = max(maxval, nums[i])
            if nums[i] < maxval:
                right = i
        minval = math.inf
        left = 0
        for i in range(n - 1, -1, -1):
            minval = min(minval, nums[i])
            if nums[i] > minval:
                left = i
        return right - left + 1 if right > left else 0


"""
Stack

one stack store from left to right numbers that are in correct ascending order, i.e., if nums[j] < stack[-1], then we pop stack. When we finish entire array, the stack top would be the highest number from left side in proper ascending order

use another stack to traverse from right to left to find lowest number of right side in proper ascending order

Note we store index instead of value so we can use the index to calculate target unsorted subarray.

time O(N)
"""


class Solution2:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        st = []
        left = n
        for i in range(n):
            while st and nums[st[-1]] > nums[i]:
                left = min(left, st.pop())
            st.append(i)
        right = 0
        st = []
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] < nums[i]:
                right = max(right, st.pop())
            st.append(i)

            # if right < left, entire array is already sorted
        return right - left + 1 if right > left else 0


def main():
    sol = Solution()

    assert sol.findUnsortedSubarray(nums = [2,6,4,8,10,9,15]) == 5, 'fails'

    assert sol.findUnsortedSubarray(nums = [1,2,3,4]) == 0, 'fails'

    assert sol.findUnsortedSubarray(nums=[1]) == 0, 'fails'

if __name__ == '__main__':
   main()