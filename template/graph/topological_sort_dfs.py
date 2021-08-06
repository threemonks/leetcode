import collections

class Solution:
    def topological_sort_dfs(self, n, prerequisites):
        # DFS time O(V+E), space (V^2)

        WHITE = 0
        GREY = 1
        BLACK = 2

        # Step 1: build graph and init visited (3 states)
        graph = [[] for _ in range(n)]
        visited = [WHITE] * n

        for x, y in prerequisites:
            graph[x].append(y) # trick: reversed the edge direction so final output is topo sort result, else the final output needs to be reversed

        # Step 2: run DFS recursively
        ans = []
        for i in range(n):
            if not self.dfs(graph, visited, i, ans):
                return []

        return ans

        def dfs(self, graph, visited, i, ans):
            # if i-th node is marked as being visited, then a cycle is found
            if visited[i] == GREY:
                return False
            # if it is done visited, then do not visit again
            if visited[i] == BLACK:
                return True
            # mark as being visited
            visited[i] = GREY
            # visit all neighbors
            for j in graph[i]:
                if not self.dfs(graph, visited, j, ans):
                    return False
            # after visit all neighbors, mark it as done visited
            visited[i] = BLACK
            ans.append(i)
            return True