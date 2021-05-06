"""

Medium

1229

36

Add to List

Share
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.



Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1


Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.

"""
from typing import List

"""
DFS

dfs from each unvisited nodes, traverse to all nodes it can visit but not visited yet. For each such start, we find one connected component.

"""
from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])

        cc = 0
        stack = []

        visited = set()

        nodes = list(range(n))  # all nodes

        for node in nodes:
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

def main():
    sol = Solution()
    assert sol.countComponents(n = 5, edges = [[0,1],[1,2],[3,4]]) == 2, 'fails'

    assert sol.countComponents(n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]) == 1, 'fails'

if __name__ == '__main__':
   main()