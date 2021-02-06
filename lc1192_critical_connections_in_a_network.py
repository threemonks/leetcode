"""
1192. Critical Connections in a Network
Hard

1967

108

Add to List

Share
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
use Tarjan's algorithm to find bridge
"""


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj_list = collections.defaultdict(list)

        for i, conn in enumerate(connections):
            adj_list[conn[0]].append(conn[1])
            adj_list[conn[1]].append(conn[0])

        visited = set()
        lowest = dict()
        res = []

        def dfs(parent, cur, curtime, visited):
            visited.add(cur)
            lowest[cur] = curtime
            for nei in adj_list[cur]:
                if nei == parent: continue  # dont go back to parent
                if nei not in visited:
                    dfs(cur, nei, curtime + 1, visited)
                lowest[cur] = min(lowest[cur], lowest[nei])
                if curtime < lowest[nei]:
                    res.append((cur, nei))

        dfs(-1, 0, 0, visited)

        return res


def main():
    sol = Solution()
    assert sol.criticalConnections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]) == [[1,3]], 'fails'


if __name__ == '__main__':
   main()