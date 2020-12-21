"""
1658. Minimum Operations to Reduce X to Zero
Medium

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.



Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109

"""
import collections
from functools import lru_cache
from typing import List

"""
observation:
let total=sum(nums), min operation to reduce X to zero, is equivalent to find longest subarray with sum equal to K=total-X

use two pointers, iterate (fix) right pointer, explore left pointer to keep a window of size equal to K

"""

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        K = total - x  # find minOperations to reduce x to zero, is equivalent to finding longest subarray with sum K
        # print('K=%s' % K)
        n = len(nums)

        i = 0
        sums = 0
        res = -1
        for j in range(n):
            sums += nums[j]
            while i <= j and sums > K:
                sums -= nums[i]
                # print('while i=%s j=%s sums=%s' % (i, j, sums))
                i += 1
            if sums == K:
                res = max(res, j - i + 1)
            # print('i=%s j=%s sums=%s res=%s' % (i, j, sums, res))

        # print('res=%s' % res)
        return n - res if res >= 0 else res

def main():
    sol = Solution()
    assert sol.minOperations([1,1,4,2,3], 5) == 2, 'fails'

    assert sol.minOperations([5,6,7,8,9], 4) == -1, 'fails'

    assert sol.minOperations([3,2,20,1,1,3], 10) == 5, 'fails'

if __name__ == '__main__':
   main()