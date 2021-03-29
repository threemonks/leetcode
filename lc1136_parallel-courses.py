"""
1136. Parallel Courses
Medium

You are given an integer n which indicates that we have n courses, labeled from 1 to n. You are also given an array relations where relations[i] = [a, b], representing a prerequisite relationship between course a and course b: course a has to be studied before course b.

In one semester, you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

Return the minimum number of semesters needed to study all courses. If there is no way to study all the courses, return -1.



Example 1:


Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.
Example 2:


Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they depend on each other.


Constraints:

1 <= n <= 5000
1 <= relations.length <= 5000
1 <= a, b <= n
a != b
All the pairs [a, b] are unique.

"""
import collections
from typing import List

"""
BFS traverse and calclculate max depth

detect cycle using len(visited) == len(vertices)

mistakes:
1. after visiting node i, reduce indegrees of its adj target node
    for d in adj_list[i]:
        indegrees[d]-=1
2. when do we update indegrees[d]-=1?
    should be after node i is visited (popped out from queue), not after discovered
"""


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        vertices = set()

        for rel in relations:
            # [a, b] a before b
            adj_list[rel[0]].append(rel[1])
            indegrees[rel[1]] += 1
            vertices.add(rel[0])
            vertices.add(rel[1])

        # print('adj_list=%s' % adj_list)
        # print('vertices=%s' % vertices)
        # print('indegrees=%s' % indegrees)
        sources = [k for k in vertices if (k not in indegrees or indegrees.get(k) == 0)]
        # print('sources=%s' % sources)

        q = collections.deque([(s, 1) for s in sources])
        visited = set(sources)
        lvl = 0

        while q:
            # print('q=%s' % q)
            cur, depth = q.popleft()
            visited.add(cur)
            for d in adj_list[cur]:
                indegrees[d] -= 1
            lvl = max(lvl, depth)
            for n in adj_list[cur]:
                if n not in visited and indegrees[n] == 0:
                    q.append((n, depth + 1))

        # print('visited=%s' % visited)
        if len(visited) != len(vertices):
            return -1

        return lvl


def main():
    sol = Solution()
    assert sol.minimumSemesters(n = 3, relations = [[1,3],[2,3]]) == 2, 'fails'

    assert sol.minimumSemesters(n = 3, relations = [[1,2],[2,3],[3,1]]) == -1, 'fails'

    assert sol.minimumSemesters(25, [[5,10],[11,14],[21,22],[16,19],[21,25],[6,18],[1,9],[4,7],[10,23],[5,14],[9,18],[18,21],[11,22],[1,15],[1,2],[5,18],[7,20],[2,23],[12,13],[9,14],[10,16],[11,21],[5,12],[2,24],[8,17],[15,17],[10,13],[11,16],[20,22],[7,11],[9,15],[16,22],[18,20],[19,22],[10,18],[3,20],[16,25],[10,15],[1,23],[13,16],[23,25],[1,8],[4,10],[19,24],[11,20],[3,18],[6,25],[11,13],[13,15],[22,24],[6,24],[17,20],[2,25],[15,24],[8,21],[14,16],[5,16],[19,23],[1,5],[4,22],[19,20],[12,15],[16,18],[9,13],[13,22],[14,22],[2,8],[3,13],[9,23],[14,15],[14,17],[8,20],[9,17],[3,19],[8,25],[2,12],[7,24],[19,25],[1,13],[6,11],[14,21],[7,15],[3,14],[15,23],[10,17],[4,20],[6,14],[10,21],[2,13],[3,21],[8,11],[5,21],[6,23],[17,25],[16,21],[12,22],[1,16],[6,19],[7,25],[3,23],[11,25],[3,10],[6,7],[2,3],[5,25],[1,6],[4,17],[2,16],[13,17],[17,22],[6,13],[5,6],[4,11],[4,23],[4,8],[12,23],[7,21],[5,20],[3,24],[2,10],[13,14],[11,24],[1,3],[2,7],[7,23],[6,17],[5,17],[16,17],[8,15],[8,23],[7,17],[14,18],[16,23],[23,24],[4,12],[17,19],[5,9],[10,11],[5,23],[2,9],[1,19],[2,19],[12,20],[2,14],[11,12],[1,12],[13,23],[4,9],[7,13],[15,20],[21,24],[8,18],[9,11],[8,19],[6,22],[16,20],[22,25],[20,21],[6,16],[3,17],[1,22],[9,22],[20,24],[2,6],[9,16],[2,4],[2,20],[20,25],[9,10],[3,11],[15,18],[1,20],[3,6],[8,14],[10,22],[12,21],[7,8],[8,16],[9,20],[3,8],[15,21],[17,21],[11,18],[13,24],[17,24],[6,20],[4,15],[6,15],[3,22],[13,21],[2,22],[13,25],[9,12],[4,19],[1,24],[12,19],[5,8],[1,7],[3,16],[3,5],[12,24],[3,12],[2,17],[18,22],[4,25],[8,24],[15,19],[18,23],[1,4],[1,21],[10,24],[20,23],[4,14],[16,24],[10,20],[18,24],[1,14],[12,14],[10,12],[4,16],[5,19],[4,5],[19,21],[15,25],[1,18],[2,21],[4,24],[7,14],[4,6],[15,16],[3,7],[21,23],[1,17],[12,16],[13,18],[5,7],[9,19],[2,15],[22,23],[7,19],[17,23],[8,22],[11,17],[7,16],[8,9],[6,21],[4,21],[4,13],[14,24],[3,4],[7,18],[11,15],[5,11],[12,17],[6,9],[1,25],[12,18],[6,12],[8,10],[6,8],[11,23],[7,10],[14,25],[14,23],[12,25],[5,24],[10,19],[3,25],[7,9],[8,12],[5,22],[24,25],[13,19],[3,15],[5,15],[15,22],[10,14],[3,9],[13,20],[1,10],[9,21],[10,25],[9,24],[14,20],[9,25],[8,13],[7,12],[5,13],[6,10],[2,5],[2,18],[14,19],[1,11],[7,22],[18,25],[11,19],[18,19],[4,18],[17,18],[2,11]]) == 25, 'fails'


if __name__ == '__main__':
   main()