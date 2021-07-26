"""
547. Number of Provinces
Medium

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3


Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]

"""
from typing import List

"""
disjoinset union find
"""

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp != yp:
            self.parent[yp] = xp


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
            if self.rank[xp] > self.rank[yp]:
                self.parent[yp] = xp
            elif self.rank[xp] < self.rank[yp]:
                self.parent[xp] = yp
            else:  # same rank, increase by 1
                self.parent[yp] = xp
                self.rank[xp] += 1


class Solution0:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DSUByRank(n)
        count = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    if dsu.find(i) != dsu.find(j):
                        dsu.union(i, j)
                        count -= 1

        return count


"""
DFS

input is adjacency matrix, we can view it as a graph
so we are looking for number of connected components
using DFS, we start from any unvisited node, recusrively visit all its connected neighbor nodes and mark them as visited, for each start of a unvisited node, we increase island count by 1

"""
from collections import defaultdict


class Solution:
    def dfs(self, M, visited, i):
        n = len(M)
        # start from node i, recursively visit all its connected neighbors
        for j in range(n):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(M, visited, j)

    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = [0 for _ in range(n)]  # nodes already visited

        ans = 0
        for i in range(n):
            if visited[i] == 0:  # not visited yet
                visited[i] = 1
                self.dfs(M, visited, i)
                ans += 1

        return ans

def main():
    sol = Solution()
    assert sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2, 'fails'

    assert sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3, 'fails'

if __name__ == '__main__':
   main()