"""
785. Is Graph Bipartite?
Medium

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B, such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.



Example 1:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: We cannot find a way to divide the set of nodes into two independent subsets.



Constraints:

1 <= graph.length <= 100
0 <= graph[i].length < 100
0 <= graph[i][j] <= graph.length - 1
graph[i][j] != i
All the values of graph[i] are unique.
The graph is guaranteed to be undirected.

"""
import collections
from typing import List

"""
BFS
"""

class Solution0:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        group = dict()

        for i in range(n):  # This graph might be a disconnected graph. So check all nodes
            queue = collections.deque()
            if i not in group:
                group[i] = 0
            queue.append(i)  # add node

            while queue:
                # print('queue=%s group=%s' % (queue, group))
                cur = queue.popleft()
                # print('cur=%s' % cur)
                for nei in graph[cur]:
                    # print('nei=%s' % nei)
                    if nei not in group:
                        group[nei] = 1 - group[cur]
                        queue.append(nei)
                    elif group[nei] == group[cur]:
                        return False

        # print(group)
        return True


"""
DFS with recursion
"""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(i):
            nonlocal color
            for nei in graph[i]:
                if nei in color:
                    if color[i] == color[nei]:  # color conflict
                        return False
                else:
                    color[nei] = 1 - color[i]
                    if not dfs(nei):
                        return False
            return True

        n = len(graph)
        for i in range(n):  # This graph might be a disconnected graph. So check all nodes
            if i not in color:
                color[i] = 0
            if not dfs(i):
                return False
        # print(color)
        return True

def main():
    sol = Solution()
    assert sol.isBipartite(graph = [[1,3],[0,2],[1,3],[0,2]]) is True, 'fails'

    assert sol.isBipartite(graph = [[1,2,3],[0,2],[0,1,3],[0,2]]) is False, 'fails'

if __name__ == '__main__':
   main()