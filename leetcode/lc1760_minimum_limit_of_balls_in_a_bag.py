"""
https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

1760. Minimum Limit of Balls in a Bag
Medium

You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

You can perform the following operation at most maxOperations times:

Take any bag of balls and divide it into two new bags with a positive number of balls.
For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Return the minimum possible penalty after performing the operations.

Example 1:

Input: nums = [9], maxOperations = 2
Output: 3
Explanation:
- Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
- Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.
Example 2:

Input: nums = [2,4,8,2], maxOperations = 4
Output: 2
Explanation:
- Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
The bag with the most number of balls has 2 balls, so your penalty is 2 an you should return 2.
Example 3:

Input: nums = [7,17], maxOperations = 2
Output: 7

Constraints:

1 <= nums.length <= 105
1 <= maxOperations, nums[i] <= 109

"""
from typing import List

"""
Binary Search

observation
How do we come to binary search
*) minimize/maximize problems can also be solved with binary search as long as the predicate function is monotonic. When the problem is asking to maximize/minimize something, you may think of using binary search or dp. If the predicate function is monotonic, i.e., if we can split with penalty X, we can also split it with penalty X+1, X+2, then we can use binary search.
*) One would first try to directly calculate the answer (brutal force). Usually if it works, it is a dp. But the range here is 10^9, even with dp, time complexity would be number of recursive calls of 10^5, that results in TLE. So we try  binary search.
*) If the problem has a brutal force with pattern false,false....true,true...true or the contrary, i.e., all False until some value, then all True, or all True and then all False, (monotonic), then one can use binary search.

approach:

*) guess the maximum size we can get with certain maxOperations
*) then check the number of operations required for each of nums: nums[i] to be broken into less than guessed maxi size
*) and if the total number of operations for all nums is less than maxOperations, return False and guess a smaller max size and check again, 
       if the total number of ops for all nums is more than maxOperations, return True guess a larger max size and check again
*) repeat until low==high

Note: we can use max(nums) as initial up bound, but that is O(log(n)), so we can also just use 10^9 as that is the upper bound specified in the problem
"""
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(mid, nums, maxOperations):
            """
            check if we can break each element in nums so that largest number after operations is <= mid, and require total number of operations <= maxOperations
            """
            ops_count = 0
            for num in nums:
                if num % mid == 0:
                    ops_count += (num // mid) - 1  # num=8, mid=2, require 8//2-1 = 3 operations
                else:  # num % mid != 0
                    ops_count += num // mid  # num=8, mid=3, require 8//3 = 2 operations

            # print('mid=%s ops_count=%s %s' % (mid, ops_count, ops_count <= maxOperations))
            return ops_count <= maxOperations

        left, right = 1, max(nums)
        best = right
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid, nums, maxOperations):
                best = min(best, mid)
                right = mid - 1
            else:
                left = mid + 1

        return best

def main():
    sol = Solution()
    assert sol.minimumSize(nums = [9], maxOperations = 2) == 3, 'fails'

    assert sol.minimumSize(nums = [2,4,8,2], maxOperations = 4) == 2, 'fails'

    assert sol.minimumSize(nums = [7,17], maxOperations = 2) == 7, 'fails'


if __name__ == '__main__':
   main()