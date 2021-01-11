"""
1462. Course Schedule IV
Medium

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have direct prerequisites, for example, to take course 0 you have first to take course 1, which is expressed as a pair: [1,0]

Given the total number of courses n, a list of direct prerequisite pairs and a list of queries pairs.

You should answer for each queries[i] whether the course queries[i][0] is a prerequisite of the course queries[i][1] or not.

Return a list of boolean, the answers to the given queries.

Please note that if course a is a prerequisite of course b and course b is a prerequisite of course c, then, course a is a prerequisite of course c.



Example 1:


Input: n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: course 0 is not a prerequisite of course 1 but the opposite is true.
Example 2:

Input: n = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites and each course is independent.
Example 3:


Input: n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]
Example 4:

Input: n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]
Output: [false,true]
Example 5:

Input: n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]]
Output: [true,false,true,false]


Constraints:

2 <= n <= 100
0 <= prerequisite.length <= (n * (n - 1) / 2)
0 <= prerequisite[i][0], prerequisite[i][1] < n
prerequisite[i][0] != prerequisite[i][1]
The prerequisites graph has no cycles.
The prerequisites graph has no repeated edges.
1 <= queries.length <= 10^4
queries[i][0] != queries[i][1]

"""
import collections
import math
from functools import lru_cache
from typing import List

"""
build graph of coures from prerequisite to the course
and traverse the graph by starting at any node i, and along the path of nodes visited, build a boolean array is_reachable[i][j]
then for each query, just check is_reachable[i][j]

"""

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = collections.defaultdict(list)
        children = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        for i in range(n):
            indegree[i] = 0

        for pair in prerequisites:
            s, t = pair
            adj_list[s].append(t)
            indegree[t] += 1

        is_reachable = [[False] * n for _ in range(n)]
        for i in range(n):
            sources = collections.deque([i])
            visited = set()
            while sources:
                c = sources.pop()
                visited.add(c)
                is_reachable[i][c] = True
                for child in adj_list[c]:
                    if child not in visited:
                        sources.append(child)

        return [is_reachable[query[0]][query[1]] for query in queries]


def main():
    sol = Solution()
    assert sol.checkIfPrerequisite(n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]) == [False, True], 'fails'

    assert sol.checkIfPrerequisite(n = 2, prerequisites = [], queries = [[1,0],[0,1]]) == [False, False], 'fails'

    assert sol.checkIfPrerequisite(n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]) == [True, True], 'fails'

    assert sol.checkIfPrerequisite(n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]) == [False, True], 'fails'

    assert sol.checkIfPrerequisite(n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]]) == [True, False, True, False], 'fails'


if __name__ == '__main__':
   main()