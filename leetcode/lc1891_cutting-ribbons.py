"""
1891. Cutting Ribbons
Medium

48

4

Add to List

Share
You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon, and an integer k. You may cut any of the ribbons into any number of segments of positive integer lengths, or perform no cuts at all.

For example, if you have a ribbon of length 4, you can:
Keep the ribbon of length 4,
Cut it into one ribbon of length 3 and one ribbon of length 1,
Cut it into two ribbons of length 2,
Cut it into one ribbon of length 2 and two ribbons of length 1, or
Cut it into four ribbons of length 1.
Your goal is to obtain k ribbons of all the same positive integer length. You are allowed to throw away any excess ribbon as a result of cutting.

Return the maximum possible positive integer length that you can obtain k ribbons of, or 0 if you cannot obtain k ribbons of the same length.



Example 1:

Input: ribbons = [9,7,5], k = 3
Output: 5
Explanation:
- Cut the first ribbon to two ribbons, one of length 5 and one of length 4.
- Cut the second ribbon to two ribbons, one of length 5 and one of length 2.
- Keep the third ribbon as it is.
Now you have 3 ribbons of length 5.
Example 2:

Input: ribbons = [7,5,9], k = 4
Output: 4
Explanation:
- Cut the first ribbon to two ribbons, one of length 4 and one of length 3.
- Cut the second ribbon to two ribbons, one of length 4 and one of length 1.
- Cut the third ribbon to three ribbons, two of length 4 and one of length 1.
Now you have 4 ribbons of length 4.
Example 3:

Input: ribbons = [5,7,9], k = 22
Output: 0
Explanation: You cannot obtain k ribbons of the same positive integer length.


Constraints:

1 <= ribbons.length <= 10^5
1 <= ribbons[i] <= 10^5
1 <= k <= 10^9
"""
from typing import List

"""
Binary Search

for a given length x, can we get k copy of it from n ribbons
sort nums decreasing
we can get it from nums[0]//k, or nums[0:2]//(k/2), or nums[0:3]//(k//3), ... nums//k
"""
class Solution0:
    def maxLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums = sorted(nums, reverse=True)

        def can_cut(x):
            # can we get k copies of length x ribbons
            # greedily cut length x ribbons from longest one to shortest one, see if we can get k copies
            cuts = 0
            for num in nums:
                cuts += num//x
                if cuts >= k:
                    return True

            return cuts >= k


        left, right = 1, nums[0]+1 # left inclusive, right exclusive
        while left < right:
            mid = left + (right-left)//2
            if can_cut(mid):
                left = mid+1
            else: # cannot cut
                right = mid

        return left-1

"""
Binary Search

use both left, right bounardy inclusive
"""
class Solution:
    def maxLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums = sorted(nums, reverse=True)

        def can_cut(x):
            # can we get k copies of length x ribbons
            # greedily cut length x ribbons from longest one to shortest one, see if we can get k copies
            cuts = 0
            for num in nums:
                cuts += num//x
                if cuts >= k:
                    return True

            return cuts >= k

        left, right = 1, nums[0] # left and right both inclusive
        while left <= right:
            mid = left + (right-left+1)//2
            if can_cut(mid):
                left = mid+1 # needs to shrink search space when we can cut, otherwise it will be infinite loop when left=right=mid, we then return left-1 at end to take care of this extra shrink
            else: # cannot cut
                right = mid-1

        return left-1



def main():
    sol = Solution()
    assert sol.maxLength(nums = [9,7,5], k = 3) == 5, 'fails'

    assert sol.maxLength(nums = [7,5,9], k = 4) == 4, 'fails'

if __name__ == '__main__':
   main()