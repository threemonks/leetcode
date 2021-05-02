"""
1697. Checking Existence of Edge Length Limited Paths
Hard

280

6

Add to List

Share
An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.



Example 1:


Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.
Example 2:


Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Exaplanation: The above figure shows the given graph.


Constraints:

2 <= n <= 105
1 <= edgeList.length, queries.length <= 10^5
edgeList[i].length == 3
queries[j].length == 3
0 <= ui, vi, pj, qj <= n - 1
ui != vi
pj != qj
1 <= disi, limitj <= 10^9
There may be multiple edges between two nodes.
"""
import collections
from typing import List
import collections

"""
DFS

Since the ask is each edge in path between pj and qj is strictly less than limitj, and n, len(edgeList), len(queries) <= 10^5
we can consider sort edgeList and queries in ascending order, and add edges as queries range increase, so the adj_list would only contain valid edges at the time of query?

Since the ask is boolean array answer that needs to align with queries, we keep the original index of each query

TLE

time O(q * (n+m)) q: # queries, m: # edges, this give 10^10, to TLE

mistakes:
1. DFS is way too slow, DFS is linear O(N), but we have n=10^5, also len(queries)=10^5, means using DFS the total would be 10^10, that will TLE, so we need some kind of algorithm to validate if we can go from node p to q in less than O(N) time
"""


class Solution0:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queries = sorted(enumerate(queries), key=lambda x: x[1][2])  # needs to keep original index of query
        edgeList = sorted(edgeList, key=lambda x: x[2])  # don't need to keep original index of edge

        ans = [None for _ in range(len(queries))]

        adj_set = collections.defaultdict(set)
        j = 0  # index to keep track which edges have been added
        for i, (p, q, limit) in queries:
            while j < len(edgeList) and edgeList[j][2] < limit:
                adj_set[edgeList[j][0]].add(edgeList[j][1])  # neighbor node, distance
                adj_set[edgeList[j][1]].add(edgeList[j][0])
                j += 1

            visited = set()
            dq = collections.deque([p])

            while dq:
                cur = dq.popleft()
                if cur == q:
                    ans[i] = True
                    break
                visited.add(cur)
                for nxt in adj_set[cur]:
                    if nxt not in visited:
                        dq.append(nxt)

        return ans


"""
Union-Find

still sort queries, and build union as queries range increases, thus adds longer edges into the graph 

"""


class DSU:
    def __init__(self, n):
        self.root = list(range(n))

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        self.root[rx] = self.root[ry] = min(rx, ry)

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queries = sorted(enumerate(queries), key=lambda x: x[1][2])  # needs to keep original index of query
        edgeList = sorted(edgeList, key=lambda x: x[2])  # don't need to keep original index of edge

        ans = [None for _ in range(len(queries))]

        dsu = DSU(n)

        j = 0  # index to keep track which edges have been added
        for i, (p, q, limit) in queries:
            while j < len(edgeList) and edgeList[j][2] < limit:
                v1, v2 = edgeList[j][0], edgeList[j][1]
                dsu.union(v1, v2)
                j += 1

            ans[i] = dsu.connected(p, q)

        return ans


def main():
    sol = Solution()
    assert sol.distanceLimitedPathsExist(n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]) == [False, True], 'fails'

    assert sol.distanceLimitedPathsExist(n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]) == [True, False], 'fails'



if __name__ == '__main__':
   main()