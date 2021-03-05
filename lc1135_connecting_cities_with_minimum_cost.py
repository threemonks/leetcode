"""
1135. Connecting Cities With Minimum Cost
Medium

There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.



Example 1:



Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation:
Choosing any 2 edges will connect all cities so we choose the minimum 2.
Example 2:



Input: N = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation:
There is no way to connect all cities even if all edges are used.


Note:

1 <= N <= 10000
1 <= connections.length <= 10000
1 <= connections[i][0], connections[i][1] <= N
0 <= connections[i][2] <= 10^5
connections[i][0] != connections[i][1]

"""
import collections
import heapq
from typing import List

"""
MST minimum Spanning Tree - Prim with minheap

start from any city, mark it as visited, add all its neighboring edges into minheap queue, 
popping from queue the next node with least edge cost, if not visited, add its cost to total cost, mark visited, then explore its neighboring edges and costs, add them into the minheap queue

stop processing when queue is empty or visited set is size N (all nodes are visited)

time O(Elog(V))

"""


class Solution0:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        adj_list = collections.defaultdict(list)
        for conn in connections:
            adj_list[conn[0]].append((conn[1], conn[2]))  # edge cost, next city
            adj_list[conn[1]].append((conn[0], conn[2]))  # edge cost, next city

        q = [(0, 1)]  # (cost, next city) start with any node
        heapq.heapify(q)
        visited = set()
        costs = 0
        while q and len(visited) < N:
            cost, city = heapq.heappop(q)
            if city not in visited:
                costs += cost
                visited.add(city)
                for nxt, cost in adj_list[city]:
                    heapq.heappush(q, (cost, nxt))

        return costs if len(visited) == N else -1


"""
MST minimum Spanning Tree - Kruskal's algorithm

sorty all edges and process each edge starting with least cost

if the two ends of the edge are not in same group (union find), then add this cost to total cost, and merge these two vertices

terminate if no more edges to process

Minimum cost if we did extactly N-1 union operations (means total of N nodes found and merged into one set), otherwise not found

time O(Vlog(E))

"""


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        try:
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        except Exception:
            print(x)

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp != yp:
            self.parent[yp] = xp


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        print('N=%s' % N)
        if not connections:
            return -1

        dsu = DSU(N)
        edges = []
        costs = 0
        for conn in connections:
            edges.append((conn[2], conn[0], conn[1]))  # cost, start, end vertex

        for edge in sorted(edges):
            cost, s, e = edge[0], edge[1], edge[2]
            if dsu.find(s - 1) != dsu.find(e - 1):
                costs += cost
                dsu.union(s - 1, e - 1)
                N -= 1

        return costs if N == 1 else -1


def main():
    sol = Solution()
    assert sol.minimumCost(N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]) == 6, 'fails'

    assert sol.minimumCost(N = 4, connections = [[1,2,3],[3,4,4]]) == -1, 'fails'

if __name__ == '__main__':
   main()