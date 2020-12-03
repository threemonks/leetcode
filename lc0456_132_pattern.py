"""
456. 132 Pattern
Medium

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].


Constraints:

n == nums.length
1 <= n <= 104
-109 <= nums[i] <= 109

"""
import math
from typing import List

"""
observation

to find pattern n1<n3<n2, we need to find the maximum n3 with n3<n2, and the smallest n1 to its left, scan through array and use decreasing stack to keep track of n3<n2 pattern
scan the array from right allow one pass finish as we just need to remember max n3, as the stack keep n3<n2

"""

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)

        n3 = -math.inf
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] < nums[i]:
                n3 = stack.pop()
                # print(stack)
            if nums[i] < n3:
                return True
            stack.append(nums[i])
            # print(stack)

        return False



class Solution1:
    """
    preprocess to keep left_min[i] refers to minimum number to left of nums[i], so that if left_min[i] < n3 < nums[i], then that is a 132 pattern found, but this does not seem to improve performance
    """

    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)

        left_min = [math.inf] * n
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], nums[i - 1])

        n3 = -math.inf
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] < nums[i]:
                n3 = stack.pop()
                # print(stack)
            if left_min[i] < n3:
                return True
            stack.append(nums[i])
            # print(stack)

        return False


def main():
    sol = Solution()
    assert sol.find132pattern([1,2,3,4]) is False, 'fails'

    assert sol.find132pattern([3,1,4,2]) is True, 'fails'

    assert sol.find132pattern([-1,3,2,0]) is True, 'fails'


if __name__ == '__main__':
   main()