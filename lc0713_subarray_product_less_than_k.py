"""
713. Subarray Product Less Than K
Medium

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

"""
import math
from typing import List

"""
take log of nums, so product of nums[i:j] become sum of nums[i:j], finding subarray of product < k, become finding longest subarray that sum nums[i:j] < k, then count how many subarray in this longest subarray
we can use prefix[i] means sum nums[0:i], then sum of subarray nums[i:j] = prefix[j] - prefix[i]
"""


class Solution1:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or k <= 0: return 0

        k = math.log(k)

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))

        ans = 0

        for i, x in enumerate(prefix):
            # find longest continuous subarray prefix[i:j] such that prefix[j]-prefix[i] < k, using binary search
            low = i + 1  # [low, high)
            high = len(prefix)
            while low < high:
                mid = low + (high - low) // 2
                if (prefix[mid] - prefix[i]) < k - 1e-9:
                    low = mid + 1
                else:
                    high = mid

            # done searching, to use low as the highest index such that (prefix[low] - prefix[i]) < k
            ans += low - i - 1

        return ans


"""
use a sliding window that is minimum length with prod (or sums on log of nums[i]) >= k
https://github.com/wisdompeak/LeetCode/tree/master/Two_Pointers/713.Subarray-Product-Less-Than-K

本题有很明显的滑窗的特征，所以基本思路是用双指针。保证一个乘积小于k的最大窗口，这个窗口内可以构成subarray的数目就是j-i+1;

本题需要注意的一点是，当nums[i]>k时，右指针动不了，而左指针依然会顺移，所以可能会出现j<i的情况，此时只需要重置这两个指针即可：

if (j<i)
{
    j = i;
    product = 1;
}

"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or k <= 0: return 0

        n = len(nums)
        prod = 1
        res = 0

        j = 0
        for i in range(n): # loop left index
            if j < i:  # in case j moved to left of i, reset it
                j = i
                prod = 1
            while j < n and prod * nums[j] < k:
                prod *= nums[j]
                j += 1
            res += j - i
            prod /= nums[i]

        return res

def main():
    sol = Solution1()
    assert sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8, 'fails'

if __name__ == '__main__':
   main()