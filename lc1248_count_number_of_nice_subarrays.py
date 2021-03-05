"""
1248. Count Number of Nice Subarrays
Medium

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16


Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length

"""
from typing import List

"""
Two Pointers
replace even with 0, odd with 1, so we are counting number of subarrays with exactly k ones.

we first solve for less than k ones,
iterate (fix) left pointer, explore right pointer, to keep a windows with k ones in it, or to find last 0 or 1 that has just k ones, or find first 1 that causes k+1 ones

then exact_k_ones(k) = less_than(k+1) - less_than(k)
"""
class Solution0:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [(1 if n%2 else 0) for n in nums]
        n = len(nums)

        def less_than_k(K):
            nonlocal nums
            # print('K=%s' % K)
            j = 0
            sums = 0 # number of ones within window
            res = 0
            for i in range(n):
                if j < i:
                    j = i
                    sums = 0
                while j < n and sums+nums[j]< K:
                    sums += nums[j]
                    j += 1
                res += j-i
                # print('i=%s j=%s sums=%s res=%s' % (i, j-1, sums, res))
                sums -= nums[i]

            # print('res=%s' % res)
            return res

        return less_than_k(k+1) - less_than_k(k)

"""
双指针
固定（遍历）左指针，探索右指针，同时保持window内1的和补超过K
exact_count(k) = at_most(k) - at_most(k-1)
"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [(1 if n%2 else 0) for n in nums]
        n = len(nums)

        def at_most(K):
            nonlocal nums
            # print('K=%s' % K)
            j = 0
            sums = 0 # number of ones within window
            res = 0
            for i in range(n):
                while j < n and sums+nums[j]<= K:
                    sums += nums[j]
                    j += 1
                # sums > K （j-1 is last index for sums <=k between nums[i:j] (including i and j))
                res += j-i
                # print('i=%s j=%s sums=%s res=%s' % (i, j-1, sums, res))
                sums -= nums[i]

            # print('res=%s' % res)
            return res

        return at_most(k) - at_most(k-1)

def main():
    sol = Solution()
    assert sol.numberOfSubarrays([1,1,2,1,1], 3) == 2, 'fails'

    assert sol.numberOfSubarrays([2,4,6], 1) == 0, 'fails'

    assert sol.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2) == 16, 'fails'

if __name__ == '__main__':
   main()