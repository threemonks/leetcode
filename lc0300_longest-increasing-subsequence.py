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
-104 <= nums[i] <= 104

"""
from typing import List

"""
DP Sequence 序列型

dp[i] := length of longest strictly increasing subsequence ending at i

base case:
dp[i] = 1 # any single element is a increasing subseq

transition:
dp[i] = max(dp[j]+1|nums[i]>nums[j] for j 0...i-1)

ans is max(dp)

time O(N^2)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0 for _ in range(n+1)]

        #base case
        for i in range(1, n+1):
            dp[i] = 1 # one element is valid increasing subsequence

        for i in range(1, n+1):
            for j in range(1, i):
                if nums[i-1] > nums[j-1]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp) # longest increasng subseq may not end at last char


def main():
    sol = Solution()

    assert sol.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]) == 4, 'fails'

    assert sol.lengthOfLIS(nums = [0,1,0,3,2,3]) == 4, 'fails'

    assert sol.lengthOfLIS(nums = [7, 7, 7, 7, 7, 7, 7]) == 1, 'fails'


if __name__ == '__main__':
   main()