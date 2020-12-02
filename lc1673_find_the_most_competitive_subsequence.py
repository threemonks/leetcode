"""
1673. Find the Most Competitive Subsequence
Medium

Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.



Example 1:

Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
Example 2:

Input: nums = [2,4,3,3,5,4,9,6], k = 4
Output: [2,3,3,4]


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
1 <= k <= nums.length

"""
from typing import List

"""
observation
keep stack of size k stack[k], scan through nums[k:], if a number nums[i] is smaller than stack[-1], pop stack[-1] until stack[-1] >= nums[i] and there are enough remaining numbers to make k-size subsequence, then append nums[i] into stack
"""
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []

        for i in range(n):
            # new element is smaller, and have enough elements to push in after we pop this one
            while stack and stack[-1] > nums[i] and len(stack)-1+n-i >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(nums[i])
            # print(stack)

        return stack

def main():
    sol = Solution()
    assert sol.mostCompetitive([3,5,2,6], 2) == [2,6], 'fails'

    assert sol.mostCompetitive([2,4,3,3,5,4,9,6], 4) == [2,3,3,4], 'fails'

if __name__ == '__main__':
   main()