"""
1340. Jump Game V
Hard

358

14

Add to List

Share
Given an array of integers arr and an integer d. In one step you can jump from index i to index:

i + x where: i + x < arr.length and 0 < x <= d.
i - x where: i - x >= 0 and 0 < x <= d.
In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.



Example 1:


Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.
Example 2:

Input: arr = [3,3,3,3,3], d = 3
Output: 1
Explanation: You can start at any index. You always cannot jump to any index.
Example 3:

Input: arr = [7,6,5,4,3,2,1], d = 1
Output: 7
Explanation: Start at index 0. You can visit all the indicies.
Example 4:

Input: arr = [7,1,7,1,7,1], d = 2
Output: 2
Example 5:

Input: arr = [66], d = 1
Output: 1


Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 10^5
1 <= d <= arr.length
"""
from functools import lru_cache
from typing import List

"""
DP - bottom up

Since we can only jump to lower bars, cannot jump higher, or jump over higher bars, that means the higher bar's value would be derived based on lower bar's value, therefore we should sort the array and find jumps for lower bar's first.

dp[i] := max jumps starting at index i

base case
dp[*] = 1 can start from any index

sort arr in ascending order but keep its original index
iterate sorted arr
transition:
for j in range(i+1, i+d+1):
    if j<0 or j>=n or arr[j] > arr[i]: break
    dp[i] = max(dp[i], dp[j]+1)
same for j from i-1 to i-d

observation:
since we can only jump lower, if arr[j]>=arr[i], no need to check further j that satisfy i-d<=j<=i+d, since a higher bar would block from jumping to it, or over it

mistakes:
1. for j from i goes to i-d, if encounter higher bar, break, else update dp[i]=max(dp[i], 1+dp[j])
   then for j from i goes to i+d
"""
class Solution0:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1]*(n) # you can start from any index

        # can not jump to higher, or over higher bar, so we can sort arr as higher bar result only depends on lower ones
        for a, i in sorted((a, i) for i, a in enumerate(arr))[1:]:
            for di in [-1, 1]:
                for j in range(i+di, i+(d+1)*di, di):
                    # break out from searching j if higher bar encounter
                    if not (0 <= j < n and arr[j] < arr[i]):
                        break
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

"""
DP top down
"""
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def dfs(i):
            ans = 1
            for j in range(i-1, i-d-1, -1):
                if not (0<=j<n and arr[j] < arr[i]):
                    break
                ans = max(ans, 1 + dfs(j))
            for j in range(i+1, i+d+1):
                if not (0<=j<n and arr[j] < arr[i]):
                    break
                ans = max(ans, 1 + dfs(j))
            return ans

        return max(map(dfs, range(n)))


def main():
    sol = Solution()

    assert sol.maxJumps(arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2) == 4, 'fails'

    assert sol.maxJumps(arr = [3,3,3,3,3], d = 3) == 1, 'fails'

    assert sol.maxJumps(arr = [7,6,5,4,3,2,1], d = 1) == 7, 'fails'

    assert sol.maxJumps(arr = [7,1,7,1,7,1], d = 2) == 2, 'fails'

    assert sol.maxJumps(arr = [66], d = 1) == 1, 'fails'

if __name__ == '__main__':
   main()