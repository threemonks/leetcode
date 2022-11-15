"""
826. Most Profit Assigning Work
Medium

1168

115

Add to List

Share
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.



Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
Example 2:

Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0


Constraints:

n == difficulty.length
n == profit.length
m == worker.length
1 <= n, m <= 10^4
1 <= difficulty[i], profit[i], worker[i] <= 10^5
"""
from typing import List

"""
Sorting / Two Pointers


sort difficulty with job id
sort worker with job id
then we can iterate these two using two pointers

find all valid job ids for given worker, find max profit this work can achieve
sum all the max profit for each worker

"""


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        m = len(worker)

        difficulties = [(d, idx) for idx, d in enumerate(difficulty)]
        difficulties = sorted(difficulties)

        workers = [(w, idx) for idx, w in enumerate(worker)]
        workers = sorted(workers)

        ans = 0
        max_p = 0

        j = 0  # index for difficulties

        for w, i in workers:
            # print(f"{i = } {j = } {difficulties[j] = } {workers[i] = }")
            while j < n and difficulties[j][0] <= w:
                d_idx = difficulties[j][1]
                max_p = max(max_p, profit[d_idx])
                j += 1
            # now j-1 was the last one that this worker can handle
            # max_p was the large profit this worker can make
            # print(f"{i = } {j = } {max_p = }")
            ans += max_p
            # print(f"{ans = }")

        return ans


def main():
    sol = Solution()
    assert sol.maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]) == 100, 'fails'

    assert sol.maxProfitAssignment(difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]) == 0, 'fails'

if __name__ == '__main__':
   main()