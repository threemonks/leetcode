"""
1761. Minimum Degree of a Connected Trio in a Graph
Hard

You are given an undirected graph. You are given an integer n which is the number of nodes in the graph and an array edges, where each edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi.

A connected trio is a set of three nodes where there is an edge between every pair of them.

The degree of a connected trio is the number of edges where one endpoint is in the trio, and the other is not.

Return the minimum degree of a connected trio in the graph, or -1 if the graph has no connected trios.



Example 1:


Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
Output: 3
Explanation: There is exactly one trio, which is [1,2,3]. The edges that form its degree are bolded in the figure above.
Example 2:


Input: n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
Output: 0
Explanation: There are exactly three trios:
1) [1,4,3] with degree 0.
2) [2,5,6] with degree 2.
3) [5,6,7] with degree 2.


Constraints:

2 <= n <= 400
edges[i].length == 2
1 <= edges.length <= n * (n-1) / 2
1 <= ui, vi <= n
ui != vi
There are no repeated edges.
"""
from typing import List

"""
Graph BFS
brutal force - build adjacency list, calculate degrees of each nodes (node value from edges, not n)

using example/ base case, we know that degree of a trio (u, v, w) is degree[u] + degree[v] + degree [w] - 6, where 6 counts for the edges (undirected means two edges between each node pair) between three nodes of the trio

then we iterate through all nodes, than for each of (iterate through) its neighbor nodes, then iterate through the intersect of the neighbor nodes of these two nodes, this will get all trios, and calculate the degrees of each trio along with this loops, and keep the minimum value of the degrees.

Note: need to calculate degrees first because
    1. to avoid TLE, we need to prune edges (node from adj_list of another node) once that edge /trio is considered
    2. as soon as we prune some edges, len(adj_list[i]) will change, so we need to calculate degrees before hand
    3. for performance we want to calculate degrees first and once only for each node

mistakes:
1. return -1 instead of inf if no trios
2. check if node is in adj_list of another node before removing
3. n is # of nodes, not the node values, node values come from edges

"""
import math
from collections import defaultdict


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(set)

        for e in edges:
            adj_list[e[0]].add(e[1])
            adj_list[e[1]].add(e[0])

        degrees = defaultdict(int)
        for i in adj_list:
            degrees[i] = len(adj_list[i])

        # print('degrees=%s' % degrees)

        min_degree = math.inf
        for v, neighbors in adj_list.items():
            for nei1 in neighbors:
                for nei2 in neighbors:
                    if nei1 != nei2 and nei2 in adj_list[nei1]:
                        degree = degrees[v] + degrees[nei1] + degrees[nei2] - 6
                        # print('v=%s nei1=%s nei2=%s degree=%s' % (v, nei1, nei2, degree))
                        min_degree = min(min_degree, degree)
                        if v in adj_list[nei2]:
                            adj_list[nei2].remove(v)
                if v in adj_list[nei1]:
                    adj_list[nei1].remove(v)

        return min_degree if min_degree != math.inf else -1


def main():
    sol = Solution()
    assert sol.minTrioDegree(n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]) == 3, 'fails'

    assert sol.minTrioDegree(n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]) == 0, 'fails'



if __name__ == '__main__':
   main()