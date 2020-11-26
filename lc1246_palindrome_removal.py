"""
1246. Palindrome Removal
Hard

Given an integer array arr, in one move you can select a palindromic subarray arr[i], arr[i+1], ..., arr[j] where i <= j, and remove that subarray from the given array. Note that after removing a subarray, the elements on the left and on the right of that subarray move to fill the gap left by the removal.

Return the minimum number of moves needed to remove all numbers from the array.



Example 1:

Input: arr = [1,2]
Output: 2
Example 2:

Input: arr = [1,3,4,1,5]
Output: 3
Explanation: Remove [4] then remove [1,3,1] then remove [5].


Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 20

"""
import math
from functools import lru_cache
from typing import List

"""
DP topdown with caching

idea: 区间型dp
dp[i][j] := minimum moves to remove subarray arr[i:j] (inclusive)
dp[i][j] = min(dp[i][k]+dp[k+1][j] for k from [i:j]

time O(N^3)
space O(N^2)

"""

class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        @lru_cache(None)
        def helper(i, j):
            nonlocal arr
            if i >= j:
                return 1
            else:
                if arr[i] == arr[j]:
                    res = helper(i+1,j-1)
                else:
                    res = helper(i, j-1) + 1
                for k in range(i, j):
                    res = min(res, helper(i, k)+helper(k+1, j))
            return res

        return helper(0, len(arr) - 1)

"""
bottom up 
dp[i][j] := minimum moves to remove subarray arr[i:j] (inclusive)
dp[i][j] = min(dp[i][k]+dp[k+1][j] for k from [i:j]

"""

class Solution1:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        # dp[i][j] = the min move for arr[i]...arr[j] (both included).
        # the max number of move is n.
        dp = [[n for _ in range(n)] for _ in range(n)] # default to max moves n

        # handle edge situation: subarray size == 1
        for i in range(n):
            dp[i][i] = 1

        # handle edge situation: subarray size == 2
        for i in range(n-1):
            dp[i][i+1] = 1 if arr[i] == arr[i+1] else 2

        # for subarray size >= 3
        for l in range(3,n+1):
            for i in range(n-l+1):
                j = i+l-1
                # if arr[i] == arr[j], then the two number: arr[i] and arr[j] can be
                # removed when the last move of subarray arr[i + 1:j - 1]
                if arr[i] == arr[j]:
                    dp[i][j] = dp[i+1][j-1]
                # or, if we cannot remove arr[left] and arr[right] in one move (the last move),
                # the subarray arr[left:right] must can be split into two subarrays
                # and remove them one by one.
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j])

        return dp[0][n-1]

def main():
    sol = Solution1()
    assert sol.minimumMoves([1,2]) == 2, 'fails'

    assert sol.minimumMoves([1,3,4,1,5]) == 3, 'fails'

    assert sol.minimumMoves([1,4,1,1,2,3,2,1]) == 2, 'fails'

if __name__ == '__main__':
   main()