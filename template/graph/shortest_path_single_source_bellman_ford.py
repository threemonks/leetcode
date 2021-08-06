"""
Bellman–Ford algorithm

1) This step initializes distances from the source to all vertices as infinite and distance to the source itself as 0. Create an array dist[] of size |V| with all values as infinite except dist[src] where src is source vertex.

2) This step calculates shortest distances. Do following |V|-1 times where |V| is the number of vertices in given graph.
…..a) Do following for each edge u-v
………………If dist[v] > dist[u] + weight of edge uv, then update dist[v]
………………….dist[v] = dist[u] + weight of edge uv



3) This step reports if there is a negative weight cycle in graph. Do following for each edge u-v
……If dist[v] > dist[u] + weight of edge uv, then “Graph contains negative weight cycle”

"""
import math
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dist = [math.inf] * n
        dist[src] = 0
        for _ in range(K + 1):
            dist2 = dist[:]
            for u, v, w in flights:
                if dist2[v] > dist[u] + w:
                    dist2[v] = dist[u] + w
            dist = dist2[:]
        if dist[dst] < math.inf:
            return dist[dst]
        else:
            return -1