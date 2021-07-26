"""
300. Longest Increasing Subsequence
Medium

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4

"""
from typing import List

"""
DP Sequence 序列型

dp[i] := length of longest strictly increasing subsequence ending at i

base case:
dp[i] = 1 # any single element is a increasing subseq

transition:
dp[i] = max(dp[j]+1|nums[i]>nums[j] for j 0...i-1)

ans is max(dp) because longest lis might end anywhere

sample run
    [6, 0, 5, 7, 4, 3]
     1  1  1  1  1  1
  dp    1  2  3  3  3

time O(N^2)
"""


class Solution0:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0 for _ in range(n + 1)]

        # base case
        for i in range(1, n + 1):
            dp[i] = 1  # one element is valid increasing subsequence

        for i in range(1, n + 1):
            for j in range(1, i):
                if nums[i - 1] > nums[j - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)  # longest increasng subseq may not end at last char


"""
DP with Binary Search + Monotonic decreasing array

tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i].
For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
len = 3   :      [4, 5, 6]            => tails[2] = 6

We can easily prove that tails is a increasing array. Therefore it is possible to do a binary search in tails array to find the one needs update.

Each time we only do one of the two:

(1) if x is larger than all tail element, append it at end, increase size by 1
(2) if tails[i-1] < x <= tails[i], update tails[i]

this will maintain tails invariant, and the final answer is size


time O(Nlog(N))
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        tails = [0 for _ in range(n)]
        size = 0

        for x in nums:
            # binary search and update tails[i]
            i, j = 0, size
            while i < j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            # now i points at right boundary of arrays <x
            tails[i] = x
            size = max(i + 1, size)  # update size to i+1 if that is larger

        return size

def main():
    sol = Solution()

    assert sol.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]) == 4, 'fails'

    assert sol.lengthOfLIS(nums = [0,1,0,3,2,3]) == 4, 'fails'

    assert sol.lengthOfLIS(nums = [7, 7, 7, 7, 7, 7, 7]) == 1, 'fails'


if __name__ == '__main__':
   main()