"""
2065. Maximum Path Quality of a Graph
Hard

4

1

Add to List

Share
There is an undirected graph with n nodes numbered from 0 to n - 1 (inclusive). You are given a 0-indexed integer array values where values[i] is the value of the ith node. You are also given a 0-indexed 2D integer array edges, where each edges[j] = [uj, vj, timej] indicates that there is an undirected edge between the nodes uj and vj, and it takes timej seconds to travel between the two nodes. Finally, you are given an integer maxTime.

A valid path in the graph is any path that starts at node 0, ends at node 0, and takes at most maxTime seconds to complete. You may visit the same node multiple times. The quality of a valid path is the sum of the values of the unique nodes visited in the path (each node's value is added at most once to the sum).

Return the maximum quality of a valid path.

Note: There are at most four edges connected to each node.



Example 1:


Input: values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49
Output: 75
Explanation:
One possible path is 0 -> 1 -> 0 -> 3 -> 0. The total time taken is 10 + 10 + 10 + 10 = 40 <= 49.
The nodes visited are 0, 1, and 3, giving a maximal path quality of 0 + 32 + 43 = 75.
Example 2:


Input: values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30
Output: 25
Explanation:
One possible path is 0 -> 3 -> 0. The total time taken is 10 + 10 = 20 <= 30.
The nodes visited are 0 and 3, giving a maximal path quality of 5 + 20 = 25.
Example 3:


Input: values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50
Output: 7
Explanation:
One possible path is 0 -> 1 -> 3 -> 1 -> 0. The total time taken is 10 + 13 + 13 + 10 = 46 <= 50.
The nodes visited are 0, 1, and 3, giving a maximal path quality of 1 + 2 + 4 = 7.
Example 4:



Input: values = [0,1,2], edges = [[1,2,10]], maxTime = 10
Output: 0
Explanation:
The only path is 0. The total time taken is 0.
The only node visited is 0, giving a maximal path quality of 0.


Constraints:

n == values.length
1 <= n <= 1000
0 <= values[i] <= 108
0 <= edges.length <= 2000
edges[j].length == 3
0 <= uj < vj <= n - 1
10 <= timej, maxTime <= 100
All the pairs [uj, vj] are unique.
There are at most four edges connected to each node.
The graph may not be connected.
"""
from typing import List

"""
DFS

1. early prune: exclude invalid node time > maxTime
2. we can revisit same node, but don't increase quality

"""
from collections import defaultdict
import heapq

"""
BFS

1. early prune: exclude invalid node time > maxTime
2. we can revisit same node, but don't add its value to quality again

mistakes:
1. undirected graph means each edge adds two entries into adj_list
2. priorityqueue/heap (dijsktra) TLE , but regular BFS passes (without visited set)

"""
from collections import defaultdict, deque
import heapq


class Solution0:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:

        adj_list = defaultdict(dict)

        for u, v, t in edges:
            if t < maxTime:  # only include valid edges
                adj_list[u][v] = t
                adj_list[v][u] = t

        # print(adj_list)

        start = 0
        q = [(0, start, values[0], set([start]))]
        # q = deque([(0, start, values[0], set([start]))]) # start point, time to it, quality along the path, nodeset visited along the path
        # keep track of nodes along the path to avoid adding same node into quality again

        ans = 0
        while q:
            time, node, quality, nodeset = heapq.heappop(q)
            # time, node, quality, nodeset = q.popleft()
            # print('node=%s time=%s quality=%s nodes=%s q=%s' % (node, time, quality, nodeset, q))
            if node == start and time <= maxTime:
                ans = max(ans, quality)

            if time > maxTime:
                continue

            for nxt, cost in adj_list[node].items():
                if nxt not in nodeset:  # node not visited yet, add to quality
                    heapq.heappush(q, (time + cost, nxt, quality + values[nxt], nodeset | set([nxt])))
                    # q.append((time + cost, nxt, quality+values[nxt], nodeset | set([nxt])))
                else:
                    heapq.heappush(q, (time + cost, nxt, quality, nodeset))
                    # q.append((time + cost, nxt, quality, nodeset))

        return ans


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:

        adj_list = defaultdict(dict)

        for u, v, t in edges:
            if t < maxTime:  # only include valid edges
                adj_list[u][v] = t
                adj_list[v][u] = t

        # print(adj_list)

        start = 0
        val = values[start]
        q = deque([(start, 0, val,
                    1)])  # start point, time to it, val along the path, nodes visited along the path (1 bit for each node)
        # keep track of nodes along the path to avoid adding same node into val again

        # visited = set((0, 1)) # node #, nodemask

        ans = 0
        while q:
            time, node, val, nodemask = q.popleft()
            # print('node=%s time=%s val=%s nodes=%s q=%s' % (node, time, val, nodes, q))
            if node == start and time <= maxTime:
                ans = max(ans, val)

            if time > maxTime:
                continue

            for nxt, cost in adj_list[node].items():
                # if ((nxt, nodemask)) not in visited:
                #     visited.add((nxt, nodemask))
                if nodemask | (1 << nxt) != nodemask:  # not added
                    q.append((time + cost, nxt, val + values[nxt], nodemask | (1 << nxt)))
                else:  # already added value, can revisit, but don't add to val
                    q.append((time + cost, nxt, val, nodemask))

        return ans


class Solution2(object):
    def maximalPathQuality(self, values, edges, maxTime):
        graph = defaultdict(list)

        for u, v, cost in edges:
            graph[u].append((v, cost))
            graph[v].append((u, cost))

        start = 0
        visited = set()
        val = values[start]
        nodemask = (1 << start)
        visited.add((start, nodemask))

        queue = deque()
        queue.append((start, 0, val, nodemask))

        ans = 0
        while queue:
            node, time, val, nodemask = queue.popleft()

            if node == 0 and time <= maxTime:
                ans = max(ans, val)

            if time > maxTime:
                continue

            for child, cost in graph[node]:
                if (child, nodemask) not in visited:
                    visited.add((child, nodemask))
                    if nodemask | (1 << child) != nodemask:
                        # val not added yet
                        queue.append((child, time + cost, val + values[child], nodemask | (1 << child)))
                    else:
                        queue.append((child, time + cost, val, nodemask))

        return ans

def main():
    sol = Solution()
    assert sol.maximalPathQuality(values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49) == 75, 'fails'

    assert sol.maximalPathQuality(values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30) == 25, 'fails'

    assert sol.maximalPathQuality(values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50) == 7, 'fails'

    assert sol.maximalPathQuality(values = [0,1,2], edges = [[1,2,10]], maxTime = 10) == 0, 'fails'

if __name__ == '__main__':
   main()