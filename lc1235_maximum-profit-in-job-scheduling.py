"""
1235. Maximum Profit in Job Scheduling
Hard

1381

14

Add to List

Share
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.



Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:



Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6


Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
"""
import bisect
from functools import lru_cache
from typing import List

"""
DP + Binary Search

Approach:
Step 1: Sort start, end and profit according to the start time (some test cases are not sorted - the examples are misleading in this respect)
Step 2: If you choose to take job i skip all jobs that start before job i ends. jump is used to find the index of the first job that starts after job i ends.
Step 3: Take a dynamic programming approach to determine the optimal profit. At each step you can choose:

    i. to take the job for profit[i] + helper(jump[i])
	ii. or to skip the job for helper(i+1)

if all profit=1, that is Greedy, count number of jobs we can finish without overlapping

Greedy always pick the one finish sooner, if same finish time, pick larger profit but we cannot use greedy since we have profit/weight

Note: similarly, we can sort jobs by end time, and calculate max profit we can get after checking job i (do it or not). With this thought, the idea is we should do binary search to get maximum compatable profit from previous time (<= current job's start time).

time O(Nlog(N))
"""


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted([(st, endTime[i], profit[i], i) for i, st in enumerate(startTime)])

        @lru_cache(None)
        def dp(i):
            # maximum profit after checking job i (whether do it or not)

            if i == n:
                return 0

            # find next job that can start after job i finishes
            # cannot compare tuple with int, so we make current job end time (also the start time of next job we can pick), jobs[i][1],
            # which is a int, a tuple by appending some dummy value
            nxt = bisect.bisect_right(jobs, (jobs[i][1], 1, 1, 1))

            return max(dp(i + 1),  # don't run job i, then we can always do job i+1
                       dp(nxt) + jobs[i][2]
                       # run job i, get profit, and try all future compatable jobs (that starts after i finish time)
                       )

        return dp(0)

def main():
    sol = Solution()
    assert sol.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]) == 120, 'fails'

    assert sol.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]) == 150, 'fails'

    assert sol.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]) == 6, 'fails'


if __name__ == '__main__':
   main()