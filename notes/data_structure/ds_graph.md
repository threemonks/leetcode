## BFS Breadth-first search
## DFS Depth-first search
## [Shortest path](../algorithm/algo_graph_shortest_path.md)
### Single Source Shortest Path
- Topological Sort
- Dijkstra Algorithm
  - non-negative weights
  - use PriorityQueue to keep nodes to be visited, as well as its cost at time of enque
  - use mincost dict (or array) to keep track of latest mininmum cost from source to each node
  - time complixity O(Elog(V))
- Bellman Ford
  - negative weights
  - can handle negative cycles
### All Pair Shortest Path Algorithm
- Floyd Wallshall Algorithm
  - ajacency matrix instead of adjacency list
## [Cycle detection](../algorithm/algo_graph_topological_sort_cycle_detection.md)
## [Minimum spanning tree](../algorithm/algo_graph_minimum_spanning_tree.md)
- Prim's Algo
  - start with any vertex, use priority queue to process smallest edge
  - use visited array or distance array
  - difference between Prim's and Dijkstra's: don't add current vertex distance to calculate neighbour distance.
    - dijkstra - dist[v] = dist[u] + graph[u][v]
    - Prim's   - dist[v] = graph[u][v]
- Kruskal Algo
  - sort all edges by their weights and use union find to avoid cycle
## [Strongly connected components](../algorithm/algo_graph_strongly_connected_components.md)
- DFS with visited array
- Tarjan
  - used to find scc, articulation point, bridge
- Kosaraju
## [Topological sorting](../algorithm/algo_graph_topological_sort_cycle_detection.md)
## Travelling Salesman Problem (TSP)
- it is a hamiltonian circuit. It is a hamiltonian path if returning to the start vertex is not needed
- implemented using dp with bit masking as dp[1<<N][N] where N is number of vertices.
- time complixity is O(N^2*2^N)
- [943. Find the Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring)
## Hamiltonian Path or TSP
- Path which traverses each vertex exactly once.
- Simple way: DFS + backtracking
## Euler Path
- Path which traverses each edge exactly once.
## Graph colouring
## Maximum flow
## Matching
## Verify if Graph is a tree
graph G is tree if and only if
- all nodes are connected - start one node, can visit all nodes (len(visited)==n)
- no cycles - BFS/DFS traverse, keep track of parent, if a neighbor node to be visited is already in parent, there is cycle
-           - BFS indegree==1 node add to queue, keep visit neighbors, reduce indegrees by 1, add to queue, and continue process, when done, len(visited)==n
