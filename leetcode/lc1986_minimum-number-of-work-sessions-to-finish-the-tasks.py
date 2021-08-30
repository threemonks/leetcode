"""
1986. Minimum Number of Work Sessions to Finish the Tasks
Medium

7

2

Add to List

Share
There are n tasks assigned to you. The task times are represented as an integer array tasks of length n, where the ith task takes tasks[i] hours to finish. A work session is when you work for at most sessionTime consecutive hours and then take a break.

You should finish the given tasks in a way that satisfies the following conditions:

If you start a task in a work session, you must complete it in the same work session.
You can start a new task immediately after finishing the previous one.
You may complete the tasks in any order.
Given tasks and sessionTime, return the minimum number of work sessions needed to finish all the tasks following the conditions above.

The tests are generated such that sessionTime is greater than or equal to the maximum element in tasks[i].



Example 1:

Input: tasks = [1,2,3], sessionTime = 3
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish the first and the second tasks in 1 + 2 = 3 hours.
- Second work session: finish the third task in 3 hours.
Example 2:

Input: tasks = [3,1,3,1,1], sessionTime = 8
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish all the tasks except the last one in 3 + 1 + 3 + 1 = 8 hours.
- Second work session: finish the last task in 1 hour.
Example 3:

Input: tasks = [1,2,3,4,5], sessionTime = 15
Output: 1
Explanation: You can finish all the tasks in one work session.


Constraints:

n == tasks.length
1 <= n <= 14
1 <= tasks[i] <= 10
max(tasks[i]) <= sessionTime <= 15
"""
"""
Bin Pack problem
"""
"""
Recursion + Memoization

use array sessions to record the number of hours we accumulated for each session sessions[i]

for each task, we can
1. add it to a new session
2. add it to one of the existing session, if it can be added withou this session exceeding sessionTime

TLE

time (2^n*n) - mask 2^n, each mask do work O(n)
space (2^n)
"""


class Solution0:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        sessions = []

        def solve(i):
            # index of tasks being evaluated
            nonlocal sessions
            if i >= n:
                return 0

            # add tasks[i] to a new session
            sessions.append(tasks[i])
            # explore further with task i added to new session
            ans = 1 + solve(i + 1)
            sessions.pop()  # remove it for backtracking

            # try to add task i into any of the existing session instead
            for j in range(len(sessions)):
                if sessions[j] + tasks[i] <= sessionTime:
                    sessions[j] += tasks[i]
                    ans = min(ans, solve(i + 1))
                    sessions[j] -= tasks[i]

            return ans

        return solve(0)


"""
Recursion + Memoization

time (2^n*n) - mask 2^n, each mask do work O(n)
space (2^n)
"""
from functools import lru_cache


class Solution1:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)

        @lru_cache(None)
        def solve(i, sessions):
            # index of tasks being evaluated
            if i >= n:
                return 0

            # add tasks[i] to a new session
            # explore further with task i added to new session
            ans = 1 + solve(i + 1, tuple(list(sessions) + [tasks[i]]))

            # try to add task i into any of the existing session instead
            for j in range(len(sessions)):
                if sessions[j] + tasks[i] <= sessionTime:
                    sessions_lst = list(sessions)
                    sessions_lst[j] += tasks[i]
                    ans = min(ans, solve(i + 1, tuple(sessions_lst)))

            return ans

        sessions = tuple()
        return solve(0, sessions)


"""
Recursion + Bitmask

using bitmask to represent whether we have used given task or not
also carry along the remaining time of current session

time (2^n*n) - mask 2^n, each mask do work O(n)
space (2^n)
"""
from functools import lru_cache


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        fullmask = (1 << n) - 1

        @lru_cache(None)
        def solve(mask, remain):
            # mask showing which tasks has been used,
            # remain showing remaining time of current session
            if mask == 0:  # no more task to process
                return 0

            ans = math.inf
            # explore each task
            for i, x in enumerate(tasks):
                if mask & (1 << i):  # task i not used yet
                    if x <= remain:
                        # use it in current session
                        ans = min(ans, solve(mask ^ (1 << i), remain - x))
                    # use it but start new one
                    else:
                        ans = min(ans, 1 + solve(mask ^ (1 << i), sessionTime - x))

            return ans

        return solve(fullmask, 0)



def main():
    sol = Solution()
    assert sol.minSessions(tasks = [1,2,3], sessionTime = 3) == 2, 'fails'

    assert sol.minSessions(tasks = [3,1,3,1,1], sessionTime = 8) == 2, 'fails'

    assert sol.minSessions(tasks = [1,2,3,4,5], sessionTime = 15) == 1, 'fails'

if __name__ == '__main__':
   main()