"""
847. Shortest Path Visiting All Nodes
Hard

An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.



Example 1:

Input: [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:

Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]


Note:

1 <= graph.length <= 12
0 <= graph[i].length < graph.length

"""
import collections
from typing import List

"""
BFS using deque to store nodes FIFO, so it effectively processes all nodes of one level before going to next level

to traverse the graph until all nodes are covered in the current path traversing, using bitmask to represent nodes along the path, return number of steps when all nodes are covered on the path

Since we want to find shortest path traversing all nodes, starting from any node, we init queue with all nodes in the graph

Note: 1. we can not just store node into visited, since we could visit same node multiple times in order to get all nodes
         so we store (node, mask) into visited, where 1 bits in mask represents nodes visited along this path.

      2. Using deque is faster then using a list to hold all nodes of one level, append neighbors into a new list, and reassign that list back for next batch

"""

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        adj_list = collections.defaultdict(list)

        fullmask = (1 << n) - 1

        for i in range(n):
            for v in graph[i]:
                if v != i:
                    adj_list[i].append(v)
        # print(adj_list)

        q = collections.deque()  # store node and its bitmask (represent what nodes have been visited along this path)
        visited = set()  # store node along with its bitmask representing nodes visited along the path (cannot just use node as we could revisit the same node)
        for i in range(n):
            q.append((i, (1 << i)))
            visited.add((i, (1 << i)))

        level = 0
        while q:
            l = len(q)
            while l:  # finish one level before we continue to next level (cost increased by 1 for each level)

                # print('q=%s' % q)
                cur, state = q.popleft()
                # print('cur=%s state=%s' % (cur, bin(state)))
                if state == fullmask:
                    return level

                for j in adj_list[cur]:
                    if (j, state | (1 << j)) not in visited:
                        q.append((j, state | (1 << j)))
                        visited.add((j, state | (1 << j)))

                l -= 1
            level += 1

        return level


"""
BFS as above, using one two lists instead of one deque

Note: this is slower than using one deque due to new list construct and assignment
"""

class Solution1:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        adj_list = collections.defaultdict(list)

        fullmask = (1 << n) - 1

        for i in range(n):
            for v in graph[i]:
                if v != i:
                    adj_list[i].append(v)
        # print(adj_list)

        q = []  # store node and its bitmask (represent what nodes have been visited along this path)
        visited = set()  # store node along with its bitmask representing nodes visited along the path (cannot just use node as we could revisit the same node)
        for i in range(n):
            q.append((i, (1 << i)))
            visited.add((i, (1 << i)))

        level = 0
        newq = []
        while q:  # finish one level before we continue to next level (cost increased by 1 for each level)
            # print('q=%s' % q)
            for cur, state in q:
                # print('cur=%s state=%s' % (cur, bin(state)))
                if state == fullmask:
                    return level

                for j in adj_list[cur]:
                    if (j, state | (1 << j)) not in visited:
                        newq.append((j, state | (1 << j)))
                        visited.add((j, state | (1 << j)))
            q = newq[:]
            level += 1

        return level


def main():
    sol = Solution()
    assert sol.shortestPathLength([[1,2,3],[0],[0],[0]]) == 4, 'fails'

    assert sol.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]) == 4, 'fails'

    assert sol.shortestPathLength([[2,6],[2,3],[0,1],[1,4,5,6,8],[3,9,7],[3],[3,0],[4],[3],[4]]) == 12, 'fails'


if __name__ == '__main__':
   main()