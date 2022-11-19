"""
886. Possible Bipartition
Medium

2825

65

Add to List

Share
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.



Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Constraints:

1 <= n <= 2000
0 <= dislikes.length <= 10^4
dislikes[i].length == 2
1 <= dislikes[i][j] <= n
ai < bi
All the pairs of dislikes are unique.
"""
from typing import List

"""
Union Find

1. build graph of dislikes using edges input
2. initialize union find of size n
3. iterate across all the vertices (1..n) and check if the vertex is connected with any of its neighbors
   a) if current vertex is connected with any of its neighbor, then the graph is NOT bipartite
   b) unionize all of a node's neighbors together because they belong to the same set

"""
from collections import defaultdict


class DSU:
    def __init__(self, n):
        # initiall all notes have itself as parent
        # but find will updat its parent as necessary
        self.p = list(range(n + 1))

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution0:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        adj_list = defaultdict(list)  # create dislike list (graph)

        for (u, v) in dislikes:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # print(f"{adj_list = }")

        dsu = DSU(n)

        for i in range(1, n + 1):  # iterate all vertices
            neighbors = adj_list[i]
            if len(neighbors) == 0:  # no neighbor to process
                continue
            first_neighbor = neighbors[0]
            if dsu.is_connected(i, first_neighbor):  # vertex is connected to its dislike neighbor
                return False
            for nei in neighbors[1:]:
                if dsu.is_connected(i, nei):  # vertex is connected to its dislike neighbor
                    return False
                dsu.union(first_neighbor, nei)  # unionize i's two neighbor, as they should belong to one set

        return True


"""
DFS traverse

for each traverse step, we assign next group an opposite group as the current node (since there should be only two groups)
before we add each neighbor node into queue, we check if it already has a group, and whether its known group is the same as the current node's group (which should be different from the neighbor node's group)

"""


class Solution:
    def dfs(self, i, group):
        pass

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        adj_list = defaultdict(list)  # create dislike list (graph)

        for (u, v) in dislikes:
            adj_list[u].append(v)
            adj_list[v].append(u)

        grouping = dict()  # with value 'A' or 'B'
        visited = set()

        # print(f"{adj_list = }")
        for i in range(1, n + 1):
            if i not in visited:
                if i not in grouping:
                    grouping[i] = True
                q = [i]
                while q:
                    node = q.pop()
                    visited.add(node)
                    group = grouping[node]
                    for nei in adj_list[node]:
                        # if nei has same group as node, then that is a conflict
                        if nei in grouping:
                            if ((group is True and grouping[nei] is True) or (
                                    group is False and grouping[nei] is False)):
                                # print(f"{i = } {node = } {group = } {nei = } {grouping = }")
                                return False
                        if nei not in visited:
                            grouping[nei] = not group
                            q.append((nei))

        return True


def main():
    sol = Solution()
    assert sol.possibleBipartition(n = 4, dislikes = [[1,2],[1,3],[2,4]]) is True, 'fails'

    assert sol.possibleBipartition(n = 3, dislikes = [[1,2],[1,3],[2,3]]) is False, 'fails'

    assert sol.possibleBipartition(n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]) is False, 'fails'

if __name__ == '__main__':
   main()