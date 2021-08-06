"""
BFS cycle detection - undirected graph

1. start with node indegrees == 0
2. explore all its neighbors, and reduces their indegrees by 1
3. if any of the newly found neighbors now have indegrees == 0, add them to queue
4. when done, all nodes visited should equal to total # of nodes
   otherwise there's cycle

"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        indegrees = defaultdict(int)
        adj_list = defaultdict(list)
        for e in edges:
            adj_list[e[0]].append(e[1])
            indegrees[e[0]] += 1
            adj_list[e[1]].append(e[0])
            indegrees[e[1]] += 1

        # BFS start from all nodes with indegress==1
        q = deque()
        for v, d in indegrees.items():
            if d == 1:
                q.append(v)

        visited = set() # actually visited, this is different from discovered
        while q:
            cur = q.popleft()
            visited.add(cur)
            for nxt in adj_list[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 1:
                    q.append(nxt)

        if len(visited) == n: # no cycle
            return True
        else:
            return False  # cycle