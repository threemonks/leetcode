"""
934. Shortest Bridge
Medium

In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)


Example 1:

Input: A = [[0,1],[1,0]]
Output: 1
Example 2:

Input: A = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


Constraints:

2 <= A.length == A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1

"""
from itertools import product
import collections
from typing import List

"""
use DFS to find island1, for all its node, mark node as visited, add node to queue (for later BFS explore for island 2), also change node value to -1, so that later we will look for value 1 and know it is island 2

then use BFS to explore unvisited nodes (include 0 and 1s), and the first 1 node is island 2, and the cost to get to the first node with value 1 is the shortest bridge

Note it seems that BFS level by level should give the correct answer (shortest path), but that TLE, only BFS without level by level passes.

"""

class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited, queue = set(), collections.deque()

        def dfs(i, j):
            nonlocal A, visited, queue
            if (i, j) in visited: return
            visited.add((i, j))
            queue.append((i, j, 0))
            A[i][j] = -1  # turn island nodes value to -1, so later check 1 can be sure it is island 2
            for ni, nj in [(i + di, j + dj) for di, dj in dirs if 0 <= i + di < m and 0 <= j + dj < n]:
                if A[ni][nj] == 1 and (ni, nj) not in visited:
                    dfs(ni, nj)

        # find island 1, mark all its nodes as visited, and add thme to queue
        for i, j in product(range(m), range(n)):
            if A[i][j] == 1:
                dfs(i, j)
                break

        # start from all island'1 nodes on deque, BFS exploring unvisited neighbors to find island2
        # the first 1 we found that is island 2, because we have turned all nodes in island 1 to value -1
        # and the steps from node in island 1 is required to connect to island 2
        while queue:
            x, y, h = queue.popleft()
            if A[x][y] == 1:
                return h - 1
            for nx, ny in [(x + dx, y + dy) for dx, dy in dirs if 0 <= x + dx < m and 0 <= y + dy < n]:
                if (nx, ny) not in visited:  # we explore 0 (water) to find 1s in the second island
                    visited.add((nx, ny))
                    queue.append((nx, ny, h + 1))

        return -1


def main():
    sol = Solution()
    assert sol.shortestBridge([[0,1],[1,0]]) == 1, 'fails'

    assert sol.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]) == 1, 'fails'

    assert sol.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]) == 1, 'fails'

if __name__ == '__main__':
   main()