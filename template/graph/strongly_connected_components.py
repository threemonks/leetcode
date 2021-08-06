"""
undirected graph
DFS count number of connected components

dfs from each unvisited nodes, traverse to all nodes it can visit but not visited yet. For each such start, we find one connected component.
323. Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
"""
from collections import defaultdict, deque
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])

        cc = 0
        visited = set()

        nodes = list(range(n))  # all nodes

        for node in nodes:
            stack = []
            if node not in visited:
                stack.append(node)
                cc += 1
                visited.add(node)
                while stack:
                    cur = stack.pop()
                    for nxt in adj_list[cur]:
                        if nxt not in visited:
                            stack.append(nxt)
                            visited.add(nxt)

        return cc

"""
Tarjan algorithm to find bridge

Tarjan algorithm to find articulation point shares some idea but is slightly different 
1192. Critical Connections in a Network
https://leetcode.com/problems/critical-connections-in-a-network/
"""
"""
Tarjan algorithm

DFS traverse, for each node, keep track of its first visit timestamp curtime, as well as lowest timestamp it can reach (will be updated via its neighbor after DFS return)

if at any point, we found curtime < lowest[nei], means curtime of this node is smaller than lowest timestamp its neighbor can reach, that means from cur to neighbor is a bridge (since its neighbor cannot reach back to cur)

Note: Tarjan algorithm for bridge is defined for directed graph, but we can use it on undirected graph by considering each undirected edge as two direction edge.

"""


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)

        for c in connections:
            g[c[0]].append(c[1])
            g[c[1]].append(c[0])

        visited = set()
        lowest = dict()
        res = []

        def dfs(cur, parent, curtime):
            visited.add(cur)
            lowest[cur] = curtime
            for nxt in g[cur]:
                if nxt == parent: # don't go back to parent
                    continue
                if nxt not in visited: # explore unvisited neighbor
                    dfs(nxt, cur, curtime+1)
                lowest[cur] = min(lowest[cur], lowest[nxt]) # update cur's lowest timestamp with lowest timestamp from its nxt neighbor nodes
                if curtime < lowest[nxt]:# bridge found
                    res.append([cur, nxt])

        dfs(0, -1, 0)

        return res