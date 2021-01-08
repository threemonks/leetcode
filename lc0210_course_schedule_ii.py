"""
210. Course Schedule II
Medium

There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""
import collections
from functools import lru_cache
from typing import List

"""
topological sort implemented via BFS using adjacency list and count indegrees of each node, use set to store visited nodes

time O(V+E)
space O(V+E)
"""


class Solution0:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adj_list and indegrees
        adj_list = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)

        for pair in prerequisites:
            c, prereq = pair
            adj_list[prereq].append(c)
            indegrees[c] += 1

        q = []

        for c in range(numCourses):
            if indegrees[c] == 0:
                q.append(c)

        L = []  # sorted list
        visited = set()

        while q:
            c = q.pop()
            visited.add(c)
            L.append(c)
            if c in adj_list:
                for dc in adj_list[c]:
                    indegrees[dc] -= 1
                    if indegrees[dc] == 0:
                        q.append(dc)

        if len(visited) == numCourses:
            return L
        else:
            return []


"""
PostOrder DFS traverse with path to detect cycle, along path traverse, mark node as visited, and store into sorted_list.
Final topological sort output is sorted_list in reverse order

time O(V+E)
space O(V+E)
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adj_list and indegrees
        adj_list = collections.defaultdict(list)

        for pair in prerequisites:
            c, prereq = pair
            adj_list[prereq].append(c)

        sorted_list = []
        visited = set()

        def postorder_dfs(curr, path):
            nonlocal sorted_list, visited, numCourses
            # print('curr=%s path=%s sorted_list=%s' % (curr, path, sorted_list))
            if curr in visited:
                return True
            else:  # not visited yet
                if curr in path:
                    return False
                else:
                    if curr in adj_list:
                        for dep in adj_list[curr]:
                            if postorder_dfs(dep, path + [curr]) is False:
                                return False
                    visited.add(curr)
                    sorted_list.append(curr)
                    return True

        for curr in range(numCourses):
            if postorder_dfs(curr, []) is False:
                break

        return sorted_list[::-1] if len(sorted_list) == numCourses else []

def main():
    sol = Solution()
    assert sol.findOrder(2, [[1,0]]) == [0, 1], 'fails'

    assert sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,2,1,3], 'fails'

    assert sol.findOrder(1, []) == [0], 'fails'

if __name__ == '__main__':
   main()