"""
261. Graph Valid Tree
Medium

1401

42

Add to List

Share
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.



Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false


Constraints:

1 <= 2000 <= n
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.

"""
from typing import List

"""
BFS with dict tracking parent node along path

A graph G is a tree if and only if the following two conditions are met:

1. G is fully connected. in other words, for every pair of nodes in G, there is a path between them. Or, start from one node, we can traverse to every node
2. G contains no cycles.

cycle deteiction methods:
   i. BFS traverse only indegree=1 nodes, and reduce indegree for each of its neighbor nodes, and add to queue if its indegree is 1 after reduce, repeat until queue is empty, if all visited nodes counts is same as all number of vertices, then no cycle.
   ii. BFS or DFS traverse, keep track of parents of the current path, if a child node is in the parent (except for the immediate one, which means we just came from), then there is a cycle.
      Note we need to skip immediate parent as we represents undirected group with two directed edges.

time O(V+E)

mistakes:
1. just detect cycle is not enough, needs to make sure all nodes are connected
"""
from collections import defaultdict, deque


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = defaultdict(list)
        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])

        q = deque([0])
        # parent of nodes along current path
        parent = {0: -1}  # start node has no parent
        while q:
            cur = q.popleft()
            for nxt in adj_list[cur]:
                if nxt == parent[cur]:  # don't fail immediate parent, but don't explore it further either
                    continue
                if nxt in parent:  # otherwise, if a child node is found in parent, there's a cycle
                    return False
                parent[nxt] = cur
                q.append(nxt)

        return len(parent) == n  # when parent nodes equals all nodes, all nodes are connected


def main():
    sol = Solution()
    assert sol.validTree(n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]) is True, 'fails'

    assert sol.validTree(n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]) is False, 'fails'


if __name__ == '__main__':
   main()