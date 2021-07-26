"""
1695. Maximum Erasure Value
Medium

251

7

Add to List

Share
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).



Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4

"""
from collections import defaultdict
from typing import List

"""
Sliding Window

keep a sliding window of uniq items, and max its score
use dict to keep number count, so that we can find valid window size
also use wsum to keep track of sum of window elements

time O(N)
"""


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        counts = defaultdict(int)  # count of elements in window
        wsum = 0

        ans = 0
        j = 0
        for i in range(n):
            counts[nums[i]] += 1
            wsum += nums[i]
            while counts and counts[nums[i]] > 1:
                counts[nums[j]] -= 1
                wsum -= nums[j]
                if counts[nums[j]] == 0:
                    del counts[nums[j]]
                j += 1
            # now all elements in window are uniq
            ans = max(ans, wsum)

        return ans

def main():
    sol = Solution()
    assert sol.maximumUniqueSubarray(nums = [4,2,4,5,6]) == 17, 'fails'

    assert sol.maximumUniqueSubarray(nums = [5,2,1,2,5,2,1,2,5]) == 8, 'fails'


if __name__ == '__main__':
   main()