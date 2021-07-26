"""
1192. Critical Connections in a Network
Hard

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.



Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.


Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.

"""
import collections
from typing import List

"""
Tarjan algorithm

DFS traverse, for each node, keep track of its first visit timestamp curtime, as well as lowest timestamp it can reach (will be updated via its neighbor after DFS return)

if at any point, we found curtime < lowest[nei], means curtime of this node is smaller than lowest timestamp its neighbor can reach, that means from cur to neighbor is a bridge (since its neighbor cannot reach back to cur)

Note: Tarjan algorithm for bridge is defined for directed graph, but we can use it on undirected graph by considering each undirected edge as two direction edge.

"""
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = collections.defaultdict(list)

        for c in connections:
            g[c[0]].append(c[1])
            g[c[1]].append(c[0])

        visited = set()
        lowest = dict()
        res = []

        def dfs(cur, parent, curtime):
            nonlocal res, visited
            visited.add(cur)
            lowest[cur] = curtime
            for nei in g[cur]:
                if nei == parent: # don't go back to parent
                    continue
                if nei not in visited:
                    dfs(nei, cur, curtime+1)
                lowest[cur] = min(lowest[cur], lowest[nei])
                if curtime < lowest[nei]:
                    res.append([cur, nei])

        dfs(0, -1, 0)

        return res


def main():
    sol = Solution()
    assert sol.criticalConnections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]) == [[1,3]], 'fails'


if __name__ == '__main__':
   main()