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
Greedy (monotonic increasing stack) + Binary Search

build longest increasing subsequence using this approach

[2, 6, 8, 3, 4, 5, 1]
[]
[2]
[2, 6] <= 6 > 2
[2, 6, 8] <= 8 > 6
[2, 6, 8] [2, 3] <= 3>2
[2, 6, 8] [2, 3, 4] <= 4 < 8 and 4 > 3
[2, 6, 8] [2, 3, 4, 5] <= 5 < 8 and 5 > 3
[2, 6, 8] [2, 3, 4, 5] [1] <= 1 < 8 and 1 < 5

observation: do we need to keep track of multiple subs? it turns out that we can just keep track of one subarray,
when new number x is not greater than last element of sub, we use binary search to find smallest element in sub that is >= x, and replace it with x

[2, 6, 8, 3, 4, 5, 1]
[]
[2]
[2, 6] <= 6>2
[2, 6, 8] <= 8>6
[2, 3, 8] <= with binary search smallest number >=3 is 6, so replace 6 with 3
[2, 3, 4] <= with binary search smallest number >=4 is 8, so replace 8 with 4
[2, 3, 4, 5] <= 5 > 4
[1, 3, 4, 5] <= with binary search smallest number >=1 is 2, so replace 2 with 1

time O(nlogn)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for num in nums:
            if not sub or num > sub[-1]:
                sub.append(num)
            elif num < sub[-1]:
                # binary search to find smallest number in sub that >= num
                left, right = 0, len(sub)
                while left < right:
                    mid = left + (right - left)//2
                    if sub[mid] < num:
                        left = mid + 1
                    elif sub[mid] >= num:
                        right = mid
                # when search is done, sub[left] is the target?
                sub[left] = num

        return len(sub)


def main():
    sol = Solution()

    assert sol.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]) == 4, 'fails'

    assert sol.lengthOfLIS(nums = [0,1,0,3,2,3]) == 4, 'fails'

    assert sol.lengthOfLIS(nums = [7, 7, 7, 7, 7, 7, 7]) == 1, 'fails'


if __name__ == '__main__':
   main()