"""
1498. Number of Subsequences That Satisfy the Given Sum Condition
Medium

Given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.



Example 1:

Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
Example 2:

Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
Example 3:

Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them don't satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).
Example 4:

Input: nums = [5,2,4,1,7,6,8], target = 16
Output: 127
Explanation: All non-empty subset satisfy the condition (2^7 - 1) = 127


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= target <= 106

"""
from typing import List

"""
Sliding Window

Since we only want the count of subsequence, we don't care about the order of item, so we can sort the array

Since each subsequence is valid only depending on its min and max, after sorting, that is the first and last element of the subsequence.

Use a sliding window A[l]~A[r], with A[l]+A[r] <= target, with A[l] (smallest) included, each of A[l+1] ... A[r] can be picked or not picked, so that is a total of 2^(r-l) number of valid subsequence.

So at each step, if A[l]+A[r]<=target, there will be 2^(r-l) of valid new subsequence (all including A[l])

How do you know whether to sort or not?

Normally subsequences mean that their order does matter. The fact that min/max element location is not fixed in the subsequences makes them subsets.
After sorting, we decrement r, because that's the only way to bring A[l] + A[r] > target down.


key points:
1. a valid subsequence in the sliding window must include l, since the sum(A[l]+A[r]) < target will stay valid with r shrinks, and it might becomes invalid only if l increases. However, increasing l will generate a new set of subsequences, because each subsequence must include l (for A[l]+A[r]<=target)
2. We need to iterate r, because after sorting, only reducing r would make change condition from A[l]+A[r]>target to valid again A[l]+A[r]<=target
3. we update result for each different l because 

time O(N)
space O(1)
"""

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7
        nums.sort()

        ans = 0
        l, r = 0, n - 1
        for r in range(n - 1, -1, -1):
            while l <= r and nums[l] + nums[r] <= target:
                ans += pow(2, r - l, MOD)
                l += 1

        return ans % MOD

def main():
    sol = Solution()
    assert sol.numSubseq(nums = [3,5,6,7], target = 9) == 4, 'fails'

    assert sol.numSubseq(nums = [3,3,6,8], target = 10) == 6, 'fails'

    assert sol.numSubseq(nums = [2,3,3,4,6,7], target = 12) == 61, 'fails'

    assert sol.numSubseq(nums = [5,2,4,1,7,6,8], target = 16) == 127, 'fails'

if __name__ == '__main__':
   main()