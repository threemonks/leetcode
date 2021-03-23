"""
1574. Shortest Subarray to be Removed to Make Array Sorted
Medium

Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

A subarray is a contiguous subsequence of the array.

Return the length of the shortest subarray to remove.



Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
Example 4:

Input: arr = [1]
Output: 0


Constraints:

1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9
"""
from typing import List

"""
Binary Search

Observation:
1. since we can only remove subarray, so the result would be either (1) prefix subarray, or (2) suffix subarray, or (3) a merge from prefix and suffix subarray

steps:
1. find non-decreasing prefix subarray
2. find non-decreasing suffix subarray
3. try to merge these two by removing elements from middle that violates the non-decreasing requirement, and find the shortest subarray that we would move from middle

time O(N)
space O(1)
"""


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        n = len(arr)

        l = 0
        while l < n - 1 and arr[l] <= arr[l + 1]:
            l += 1
        if l == n - 1:  # sorted ascending
            return 0

        r = n - 1
        while r > 0 and arr[r] >= arr[r - 1]:
            r -= 1
        if r == 0:  # sorted descending
            return 0

        # now l is last element of non-decreasing subarray starting at 1
        # r is first element of non-decreasing suffix array ending at n-1

        res = min(r, n - l - 1)  # min # of nodes to remove
        # i.e., keep either only all non-decreasing prefix, or keep only all non-increasing suffix
        # binary search to find 0<=i<=l and r<=j<=n-1 make sure arr[i] <= arr[j]
        # and minimize j-i+1
        i, j = 0, r
        while i <= l and j <= n - 1:
            if arr[i] <= arr[j]:  # need to remove more
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1

        # print('i=%s j=%s' % (i, j))
        return res

from lc_tools import deserialize
def main():
    sol = Solution()
    assert sol.findLengthOfShortestSubarray(arr = [1,2,3,10,4,2,3,5]) == 3, 'fails'

    assert sol.findLengthOfShortestSubarray(arr = [5,4,3,2,1]) == 4, 'fails'

    assert sol.findLengthOfShortestSubarray(arr = [1,2,3]) == 0, 'fails'

    assert sol.findLengthOfShortestSubarray(arr = [1]) == 0, 'fails'



if __name__ == '__main__':
   main()