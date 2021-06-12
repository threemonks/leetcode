"""
813. Largest Sum of Averages
Medium

1268

60

Add to List

Share
We partition a row of numbers nums into at most k adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in nums, and that scores are not necessarily integers.

Example:
Input:
nums = [9,1,2,3,9]
k = 3
Output: 20
Explanation:
The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.


Note:

1 <= nums.length <= 100.
1 <= nums[i] <= 10000.
1 <= k <= nums.length.
Answers within 10-6 of the correct answer will be accepted as correct.

"""
import math
from typing import List

"""
DP 区间I型

dp[i][j] := best score can be achieved by checking up to index i, and partition into j group

init to -math.inf

   idx
       0    1      2     3 # # of split groups
    0  
9   1  -    9      -     -
1   2  -    5     10
2   3       4     10.5   12   
3   4       3.75  11          11 = max((9+(1+2+3)/3),(9+1)/2+(2+3)/2,(9+1+2)/3+3)
9   5       4.8

dp[i][j] = max(dp[m][j-1]+avg(nums[m:i])) for m from 1...i
for m in range(j-1,i): # m cannot be less than j-1, as there would not be enough elements to split into j-1 groups
    dp[i][j] = max(dp[i][j], dp[m][j-1]+sum(nums[m:i])/(i-m))

time: O(k*n^2)
space: O(n*k) => can simplify to O(n)

optimization: use prefix sum so that sum(nums[m:i]) = presum[i]-presum[m-1]

mistakes:
1. make dp[n+1][k+1] to simplify edge case when j-1 < 0
2. with dp[n+1][k+1], the transition fomular has nums[i-1] corresponds to dp[i][j]
3. need to init dp[i][j] to -math.inf
"""


class Solution0:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)

        dp = [[-math.inf for _ in range(k + 1)] for _ in range(n + 1)]

        # base case
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for m in range(j - 1, i):
                    dp[i][j] = max(dp[i][j], dp[m][j - 1] + sum(nums[m:i]) / (i - m))

        return dp[n][k]


"""
DP 区间I型 + prefix sum

using prefix sum to optimize calculating average
"""


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)

        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        print(presum)

        dp = [[-math.inf for _ in range(k + 1)] for _ in range(n + 1)]

        # base case
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for m in range(j - 1, i):
                    dp[i][j] = max(dp[i][j], dp[m][j - 1] + (presum[i] - presum[m]) / (i - m))

        return dp[n][k]


def main():
    sol = Solution()
    assert sol.largestSumOfAverages(nums = [9,1,2,3,9], k = 3) == 20, 'fails'

    assert sol.largestSumOfAverages([1,2,3,4,5,6,7], k=4) == 20.5, 'fails'

if __name__ == '__main__':
   main()