### BFS vs DFS
- https://techdifferences.com/difference-between-bfs-and-dfs.html

|                                        | BFS                                                                                | DFS                                                                                              |
|:---------------------------------------|:-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| Basic                                  | Vertex-based algorithm                                                             | Edge-based algorithm                                                                             |
| Data structure used to store the nodes | Queue                                                                              | Stack                                                                                            |
| Memory consumption                     | Inefficient                                                                        | Efficient                                                                                        |
| Structure of the constructed tree      | Wide and short                                                                     | Narrow and long                                                                                  |
| Traversing fashion                     | Oldest unvisited vertices are explored at first.                                   | Vertices along the edge are explored in the beginning.                                           |
| Optimality                             | Optimal for finding the shortest distance, not in cost                             | Not optimal                                                                                      |
| Application                            | Examines bipartite graph, connected component and shortest path present in a graph | Examines two-edge connected graph, strongly connected graph, acyclic graph and topological order |
| Time complexity                        | O(V+E)                                                                             | O(V+E)                                                                                           |
