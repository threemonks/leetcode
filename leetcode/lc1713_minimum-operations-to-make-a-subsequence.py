"""
1713. Minimum Operations to Make a Subsequence
Hard

You are given an array target that consists of distinct integers and another integer array arr that can have duplicates.

In one operation, you can insert any integer at any position in arr. For example, if arr = [1,4,1,2], you can add 3 in the middle and make it [1,4,3,1,2]. Note that you can insert the integer at the very beginning or end of the array.

Return the minimum number of operations needed to make target a subsequence of arr.

A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.



Example 1:

Input: target = [5,1,3], arr = [9,4,2,3,4]
Output: 2
Explanation: You can add 5 and 1 in such a way that makes arr = [5,9,4,1,2,3,4], then target will be a subsequence of arr.
Example 2:

Input: target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]
Output: 3


Constraints:

1 <= target.length, arr.length <= 105
1 <= target[i], arr[i] <= 109
target contains no duplicates.

"""
from typing import List

"""
DP / Greedy

The problem is to find longest subsequence of target that is in arr, if we construct an array nums of index of arr element in target, then we are looking for longest increasing subsequence of this new array nums

steps:
1. construct value to index map for arr
2. construct array nums, fill it with index of target[i] in arr
3. find longest increasing subsequence of nums

[6, 4, 8, 1, 3, 2]
 2     5  7 <= index of target element in arr in increasing order
[4, 7, 6, 2, 3, 8, 6, 1]

1, 2, 4, 6, 5, 8

TLE - 10^5 but LIS default implementation is O(N^2)
"""


class Solution0:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        n = len(arr)
        posmap = dict()
        nums = [-1 for _ in range(n)]

        for i, a in enumerate(target):
            posmap[a] = i

        for i in range(n):
            nums[i] = posmap.get(arr[i], -1)

        def len_lis(nums):
            """
            [6, 0, 5, 7, 4, 3]
             1  1  1  1  1  1
          dp    1  2  3  3  3

            """
            # find length of longest increasing subsequence of nums
            # ignoring -1
            if not nums: return 0
            n = len(nums)
            dp = [0 for _ in range(n + 1)]
            for i in range(n + 1):
                dp[i] = 1

            ans = 1
            for i in range(1, n + 1):
                if nums[i - 1] == -1:
                    continue  # don't count -1
                for j in range(1, i):
                    if nums[j - 1] == -1:
                        continue
                    if nums[i - 1] > nums[j - 1]:  # dp[i] corresponds to nums[i-1] since we have dummy dp[0] in front
                        dp[i] = max(dp[i], dp[j] + 1)
                        ans = max(ans, dp[i])  # best result might end anywhere
            return ans

        # print(nums)
        l = len_lis([n for n in nums if n != -1])
        # print(l)
        return len(target) - l


"""
DP / Greedy

use Nlog(N) LIS algo
"""


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        n = len(arr)
        posmap = dict()
        nums = [-1 for _ in range(n)]

        for i, a in enumerate(target):
            posmap[a] = i

        for i in range(n):
            nums[i] = posmap.get(arr[i], -1)

        def len_lis(nums):
            n = len(nums)
            tails = [0 for _ in range(n)]
            size = 0

            for x in nums:
                i, j = 0, size
                while i < j:
                    m = (i + j) // 2
                    if tails[m] < x:
                        i = m + 1
                    else:
                        j = m

                tails[i] = x
                size = max(size, i + 1)

            return size

        # print(nums)
        l = len_lis([n for n in nums if n != -1])
        # print(l)
        return len(target) - l

def main():
    sol = Solution()
    assert sol.minOperations(target = [5,1,3], arr = [9,4,2,3,4]) == 2, 'fails'

    assert sol.minOperations(target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]) == 3, 'fails'



if __name__ == '__main__':
   main()