"""
1027. Longest Arithmetic Subsequence
Medium

1561

83

Add to List

Share
Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Recall that a subsequence of an array nums is a list nums[i1], nums[i2], ..., nums[ik] with 0 <= i1 < i2 < ... < ik <= nums.length - 1, and that a sequence seq is arithmetic if seq[i+1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).



Example 1:

Input: nums = [3,6,9,12]
Output: 4
Explanation:
The whole array is an arithmetic sequence with steps of length = 3.
Example 2:

Input: nums = [9,4,7,2,10]
Output: 3
Explanation:
The longest arithmetic subsequence is [4,7,10].
Example 3:

Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:
The longest arithmetic subsequence is [20,15,10,5].


Constraints:

2 <= nums.length <= 1000
0 <= nums[i] <= 500

"""
from typing import List

"""
Hash Map

[6,9,4,7,2,10]

for each index i, check all index j to its left, j=0,1,...,i-1, update dp[i][diff] with dp[j][diff]+1 if nums[i]-nums[j] == diff

note:
1. since we are checking arithematic subsequence,  a subsequence of diff up to earlier index j-x, would be replaced by a sequence of diff up to a later index j, so updating dp[(i, diff)] for outer loop index i can be just updated with dp[(j, diff)], without having to consider earlier dp[(j-x, diff)]
"""


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}  # key would be (index, diff) where index is the ending range of subseuqnce (not necessarily ended on this one), diff is the seq diff
        for i in range(n):
            for j in range(i):
                dp[(i, nums[i] - nums[j])] = dp.get((j, nums[i] - nums[j]), 1) + 1

        return max(dp.values())


def main():
    sol = Solution()

    assert sol.longestArithSeqLength(nums = [3,6,9,12]) == 4, 'fails'

    assert sol.longestArithSeqLength(nums = [9,4,7,2,10]) == 3, 'fails'

    assert sol.longestArithSeqLength(nums = [20,1,15,3,10,5,8]) == 4, 'fails'


if __name__ == '__main__':
   main()