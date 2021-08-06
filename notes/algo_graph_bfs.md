## BFS
use sea water flooding into inner land, or sea water go into inner as water rsies, has the following advantage vs BFS going from any node to sea
1. there's only m+n nodes as starting point of the sea shore, vs m*n if we use BFS start from any node
2. for sea water rising flooding inner land, we add neighbor node that is higher, and skip neighbor node when is lower (this will not miss any node that is lower then this but higher than other nodes that is now part of the sea)
   but if we start from any node traverse into sea, we don't have this early stopping/pruning opportunity
3. termination condition - for either BFS when queue is empty, for DFS, when no more unvisited neighbor

similar problem
  778 - https://leetcode.com/problems/swim-in-rising-water/
  407 - https://leetcode.com/problems/trapping-rain-water-ii/
  417 - https://leetcode.com/problems/pacific-atlantic-water-flow/

### BFS seen sets invariant - everything in queue is already marked as seen
https://cs.stackexchange.com/questions/123284/visited-vs-seen-positions-in-breadth-first-search
Keep the invariant that everything in the queue is already put in the seen queue.
```
seen = set()
while q:
    cur = q.pop()
    for nxt in g[cur]:
        if nxt not in seen:
            q.append(nxt)
            seen.add(nxt)
```
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
