## Traverse

|                 | BFS                                                              | DFS                                                |
|:----------------|:-----------------------------------------------------------------|:---------------------------------------------------|
| data structure  | deque                                                            | stack                                              |
| application     | single source shortest path in unweighted graph                  | decision tree, game or puzzle                      |
| do not use for  | not suitable for decision making trees used in games or puzzles. | shortest path                                      |
| time complexity | O(V+E) with adj_list, O(V^2) with adjacency matrix               | O(V+E) with adj_list, O(V^2) with adjacency matrix |


## Shortest path

- Dijkstra's Shortest path from one node to all nodes
- modified BFS for shortest path from single source to single dest in unweighted graph
- Bellman-Ford Shortest path from one node to all nodes, negative edges
  allowed, negative cycles allowed
- Floyd-Warshall Shortest path between all pairs of vertices, negative
  edges allowed

## Minimum spanning tree (最小生成树)

- Prim Native implementation O(V2) Dense graph

- Prim PQ implementation (ElogV) Sparse graph

- Kruskal Union-Find implementation (ElogV) Larger Sparse graph

## SCC Strongly Connected Component

- [DFS (undirected graph)](strongly_connected_components.py)
- Tarjan’s Algorithm

## Topological sort

BFS Kahn

DFS

## Reachability: <==> (iff) belongs to same connected components

1. One or few queries, BFS or DFS
2. Many queries - use preprocessing Floyd-Warshall Algorithm ->
   transitive closure

