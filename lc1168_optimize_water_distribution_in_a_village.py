"""
1168. Optimize Water Distribution in a Village
Hard

There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes, where each pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe. Connections are bidirectional.

Return the minimum total cost to supply water to all houses.

Example 1:

Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation:
The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.

Constraints:

1 <= n <= 104
wells.length == n
0 <= wells[i] <= 105
1 <= pipes.length <= 104
pipes[j].length == 3
1 <= house1j, house2j <= n
0 <= costj <= 105
house1j != house2j

"""
import heapq
import collections
from typing import List

"""
adding a virtual house, 0, so that from any house i to this house's pipe cost is wells[i-1]

Then this is to find minmum spanning tree for all n+1 houses/vertices

Kruskal's algorithm

time O(E*log(V))
"""


class DSUByRank:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1 for _ in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp != yp:
            if self.rank[xp] < self.rank[yp]:
                self.parent[xp] = yp
            elif self.rank[xp] > self.rank[yp]:
                self.parent[yp] = xp
            else:  # same rank
                self.parent[yp] = xp
                self.rank[xp] += 1


class Solution0:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        dsu = DSUByRank(
            n + 1)  # added one virtual house, the wells[i] cost of each house 1 thourgh n, represents pipe cost between house 0 and 1~n

        q = []

        for i in range(n):
            q.append((wells[i], 0, i + 1))
            q.append((wells[i], i + 1, 0))

        for p in pipes:
            house1, house2, cost = p
            q.append((cost, house1, house2))
            q.append((cost, house2, house1))

        q = sorted(q)

        count = 0
        costs = 0
        for cost, src, dest in q:
            if dsu.find(src) != dsu.find(dest):
                dsu.union(src, dest)
                costs += cost
                count += 1

        return costs if count == n else -1


"""
adding a virtual house, 0, so that from any house i to this house's pipe cost is wells[i-1]

Then this is to find minmum spanning tree for all n+1 houses/vertices

Prim's

time O(E*log(V))
"""


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        adj_list = collections.defaultdict(list)

        for i in range(n):
            adj_list[0].append((wells[i], i + 1))
            adj_list[i + 1].append((wells[i], 0))

        for p in pipes:
            house1, house2, cost = p
            adj_list[house1].append((cost, house2))
            adj_list[house2].append((cost, house1))

        q = [(0, 0)]  # start with virtual house 0, whose cost to itself is 0
        heapq.heapify(q)

        visited = set()
        costs = 0
        while q:
            cost, node = heapq.heappop(q)
            if node not in visited:
                costs += cost
                visited.add(node)
                for cost, nxt in adj_list[node]:
                    heapq.heappush(q, (cost, nxt))

        return costs if len(visited) == n + 1 else -1


def main():
    sol = Solution()
    assert sol.minCostToSupplyWater(n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]) == 3, 'fails'


if __name__ == '__main__':
   main()