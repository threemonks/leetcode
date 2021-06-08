"""
1335. Minimum Difficulty of a Job Schedule
Hard

730

88

Add to List

Share
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.



Example 1:


Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7
Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.
Example 4:

Input: jobDifficulty = [7,1,7,1,7,1], d = 3
Output: 15
Example 5:

Input: jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
Output: 843


Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10
"""
import math
from typing import List

"""
DP 区间I

dp[i][k] := min difficulty to schedule first i jobs (1-based) in k days

init:
    dp[*][*] = inf
    dp[0][0] = 0

transition:
    # try all different possible job scheduling before today, 
    # plus max difficulty on today (max difficult of all remaining jobs after prevous schedules)
    # take the min of all these possible scheduling result difficulty
    dp[i][k] = min{dp[j][k-1] + max(jobs[j+1~i])} for k-1<=j<i

answer:
    dp[n][k]

improve: can optimize max(jobs[j+1~i]) by iterating j from i to k-1, and keep updating max(jobs[j+1~i])

time: O(n^2*k)

"""


class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        n = len(jobs)

        dp = [[math.inf for _ in range(d + 1)] for _ in
              range(n + 1)]  # add padding index 0 to simplify boundary condition

        dp[0][0] = 0  # jobs is 0-based

        for i in range(1, n + 1):
            for k in range(1, d + 1):
                md = 0
                for j in range(i - 1, k - 2, -1):
                    md = max(md, jobs[j])
                    dp[i][k] = min(dp[i][k], dp[j][k - 1] + md)

        return dp[n][d] if dp[n][d] < math.inf else -1

def main():
    sol = Solution()
    assert sol.minDifficulty(jobs = [6,5,4,3,2,1], d = 2) == 7, 'fails'

    assert sol.minDifficulty(jobs = [9,9,9], d = 4) == -1, 'fails'

    assert sol.minDifficulty(jobs = [1,1,1], d = 3) == 3, 'fails'

    assert sol.minDifficulty(jobs = [7,1,7,1,7,1], d = 3) == 15, 'fails'

    assert sol.minDifficulty(jobs = [11,111,22,222,33,333,44,444], d = 6) == 843, 'fails'

if __name__ == '__main__':
   main()