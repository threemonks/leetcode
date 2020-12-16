"""
209. Minimum Size Subarray Sum
Medium

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

"""
import math
from functools import lru_cache
from typing import List

"""
use two pointers i, j
keep a sum of nums[i:j], 
if sum > s, record min length, then increase left pointer i, which will reduces sum, until it casues sum < s
  sum -= nums[i]
  i += 1
if sum < s, increase right pointer j, which increases sum
  sum += nums[j]
  j += 1

time O(N)
space O(1)

"""


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        sumij = 0
        l = math.inf

        for j in range(n):
            sumij += nums[j]
            if sumij < s:
                continue
            else:
                while sumij >= s:
                    l = min(l, j - i + 1)
                    sumij -= nums[i]
                    i += 1

        if l == math.inf:
            l = 0

        return l


def main():
    sol = Solution()
    assert sol.minSubArrayLen(7, [2,3,1,2,4,3]) == 2, 'fails'

if __name__ == '__main__':
   main()