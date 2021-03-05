"""
1494. Parallel Courses II
Hard

Given the integer n representing the number of courses at some university labeled from 1 to n, and the array dependencies where dependencies[i] = [xi, yi]  represents a prerequisite relationship, that is, the course xi must be taken before the course yi.  Also, you are given the integer k.

In one semester you can take at most k courses as long as you have taken all the prerequisites for the courses you are taking.

Return the minimum number of semesters to take all courses. It is guaranteed that you can take all courses in some way.



Example 1:



Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
Output: 3
Explanation: The figure above represents the given graph. In this case we can take courses 2 and 3 in the first semester, then take course 1 in the second semester and finally take course 4 in the third semester.
Example 2:



Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
Output: 4
Explanation: The figure above represents the given graph. In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester and take course 4 in the second semester, then take course 1 in the third semester and finally take course 5 in the fourth semester.
Example 3:

Input: n = 11, dependencies = [], k = 2
Output: 6


Constraints:

1 <= n <= 15
1 <= k <= n
0 <= dependencies.length <= n * (n-1) / 2
dependencies[i].length == 2
1 <= xi, yi <= n
xi != yi
All prerequisite relationships are distinct, that is, dependencies[i] != dependencies[j].
The given graph is a directed acyclic graph.

"""
import collections
import itertools
import math
from functools import lru_cache
from typing import List

"""
BFS
observation:

we need to keep track whether a given courses' prerequisite has all been met or not
state is bitmask representing which coures have been taken, bit i is 1 means coure i has been taken
dp[state] := minimum steps (semester) required to take coures represented in state

transition
dp[state] = min(dp[state], dp[prev_state]+1)

prev_state and state must satisfy this:
1. all coures taken in prev_state must also be in state (cannot lose course), i..e, prev_state is subset of state
2. count_bits(state) - count_bits(prev_state) <= k 
3. all prerequisite of all coures in state must have been taken in prev_state

time O(2^N*2^N)
space O(N) N=(1<<n)
"""
class Solution:
    """
    lets try BFS / bitmask since DP/bitmask always TLE

    """
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        N = (1 << n)
        course_deps = [0 for _ in range(n)]
        for dep in dependencies:
            course_deps[dep[1]-1] |= (1 << (dep[0]-1)) # courses are 1-index, array are 0-indexed

        # print([(idx, bin(d)) for idx, d in enumerate(course_deps)])

        queue = collections.deque()
        queue.append((0, 0))  # state (bitmask represents all classes using bit 1's, and step to get to this state (# of semesters)
        visited = set()
        visited.add(0)

        while queue:
            state, step = queue.popleft()
            # print('bin(state)=%s step=%s' % (bin(state), step))
            if state >= N - 1:  # done study all courses
                return step
            # with current state courses fulfill dependencies, what is the next_state we can take courses to get to
            next_state = state
            for i in range(n):
                if (state & course_deps[i]) == course_deps[i]:
                    next_state |= (1 << i)  # add this course to next state
            # print('bin(next_state)=%s' % (bin(next_state)))
            diff = next_state ^ state # new courses with dependencies ready (included in state) that we can take
            # print('bin(diff)=%s' % (bin(diff)))
            if bin(diff).count("1") <= k and state+diff not in visited:  # less than k new courses, study them all in one step
                visited.add(state+diff)
                # print('study next_state=%s step=%s' % (bin(next_state), step))
                queue.append((next_state, step+1))
            else:
                # if diff has more than k, select k to complete, loop through all possible such combinations with k courses
                diffk = diff
                while diffk:
                    # print('diffk=%s' % bin(diffk))
                    if bin(diffk).count('1') <= k and state+diffk not in visited:
                        visited.add(state+diffk)
                        queue.append((state+diffk, step+1))
                    diffk = (diffk-1) & (diff)

"""
python 1-d bottom up dp with bitmask 
seems always TLE when submit in leetcode, though locally runs fine though slow.
"""
class Solution1:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        course_deps = [0 for _ in range(n)]
        for dep in dependencies:
            course_deps[dep[1]-1] |= (1<<(dep[0]-1)) # courses are 1-index

        # print([(idx, bin(d)) for idx, d in enumerate(course_deps)])

        prereq = [0 for _ in range((1<<n))] # all prerequisites of all courses in state i
        for state in range((1<<n)):
            # loop all courses represented by i
            for j in range(n):
                if (state & (1<<j)):
                    prereq[state] |= course_deps[j]

        # print([(idx, bin(pr)) for idx, pr in enumerate(prereq)])

        dp = [math.inf/2 for _ in range((1<<n))] # minimum semesters required for completing all coures in state i
        dp[0] = 0

        for state in range(0, (1<<n)):
            # loop all its prev_state, how do we get that? either brutal force loop all prev_state
            # or just get all state's subset state since prev_state is required to be a subset of state
            # print('state=%s' % bin(state))
            prev_state = state
            while prev_state >=0:
                prev_state = (prev_state-1)&state # prev_state is loop through all sub-state of state
                # print('prev_state=%s' % bin(prev_state))
                if ((bin(state).count("1") - bin(prev_state).count("1") <= k) and ((prev_state & prereq[state]) == prereq[state])):
                    dp[state] = min(dp[state], dp[prev_state]+1)
                    # print('dp_prev_state=%s dp_state=%s' % (dp[prev_state], dp[state]))
                if prev_state == 0:
                    break

        return dp[(1<<n)-1]

def main():
    sol = Solution()
    assert sol.minNumberOfSemesters(4, [[2,1],[3,1],[1,4]], 2) == 3, 'fails'

    assert sol.minNumberOfSemesters(5, [[2,1],[3,1],[4,1],[1,5]], 2) == 4, 'fails'

    assert sol.minNumberOfSemesters(11, [], 2) == 6, 'fails'

    assert sol.minNumberOfSemesters(15, [[2, 1]], 4) == 4, 'fails'

    assert sol.minNumberOfSemesters(15, [[10, 2], [15, 3], [9, 14], [13, 1], [5, 14], [5, 6], [12, 11], [9, 13], [13, 3], [9, 8], [12, 3], [5, 9], [15, 10],
     [10, 6], [7, 1], [9, 7], [15, 4], [3, 14], [5, 1], [13, 10], [5, 13], [15, 7], [5, 11], [13, 2], [10, 8], [15, 2],
     [14, 11], [15, 13], [12, 1], [15, 6], [12, 5], [5, 2], [12, 13], [13, 14], [8, 6], [10, 4], [1, 11], [4, 1],
     [6, 11], [9, 3], [2, 6], [4, 2]], 4) == 9, 'fails'

    import time
    start = time.time()
    assert sol.minNumberOfSemesters(15, [[2,5],[2,1],[10,13],[8,1],[6,5],[9,5],[2,12],[2,9],[3,9],[8,11],[8,4],[5,1],[15,10],[10,1],[3,1],[2,7],[3,2],[15,13],[8,12],[11,13],[2,6],[11,1],[14,7],[12,5],[9,4],[12,9],[6,10],[8,9],[10,5],[8,13],[12,10],[9,7],[3,15],[12,13],[14,13],[2,10],[14,10],[3,12],[4,1],[14,11],[2,14],[3,7],[2,15],[2,11],[11,4],[15,11],[12,7],[11,5],[10,4],[14,1],[3,13],[15,1],[14,5],[7,13],[9,10],[14,4],[15,7],[6,1],[2,13],[6,4],[8,7],[3,5],[10,11],[12,1],[6,11],[9,1],[15,9],[7,5],[9,11],[8,10],[3,10],[15,4],[12,14],[14,6],[6,13],[8,6],[14,9],[5,13],[8,14],[4,5],[9,13]], 8) == 10, 'fails'
    end = time.time()
    print(f"Elapsed Time: {end - start}")

if __name__ == '__main__':
   main()