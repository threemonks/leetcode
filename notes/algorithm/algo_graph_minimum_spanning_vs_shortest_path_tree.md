## Minimum spanning vs shortest path tree
https://www.baeldung.com/cs/minimum-spanning-vs-shortest-path-trees

### Prim’s algorithm for Minimum Spanning Tree (MST)
Data: A graph G with weighted edges
Result: A minimum spanning tree of G
Initialize a node set S1 with an arbitrary node u from G;
Put all other nodes in G into a node set S2;
Initialize an empty edge set T to store minimum spanning tree edges;
Initialize an edge set E to store edges that have one end node in S1 and another end node in S2;
Add all edges {u,v|v in S2} into E;
while S2 is not empty do
  Select an edge {u, v| u in S1, v in S2} from E that has the minimum weight;
  Add {u,v} to T;
  Remove {u,v} from E;
  Remove v from S2 and add it to S1;
  Add all edges {v,w| w in S2} into E;
end
return T;

### Dijkstra's algorith for Shortest Path Tree (SPT)
Data: A graph G with weighted edges, a source node s
Result: A shortest path tree of G rooted at s
Initialize a node set S1 with s;
Assign a distance value 0 to node s: Dist(s) = 0;
Put all the other nodes in G into a node set S2;
Initialize an empty edge set T to store shortest path tree edges;
Initialize an edge set E to store edges that have one end node in S1 and another end node in S2;
Add all edges {u,v|v in S2} into E;
while S2 is not empty do
  Select an edge {u,v| u in S1, v in S2} from E that has the minimum Dist(u)+weight(u,v);
  Add {u,v} to T;
  Remove {u,v} from E;
  Remove v from S2 and add it to S1;
  Dist(v) = Dist(u) + weight(u,v);
  Add all edges {v,w| w in S2} into E;
end
return T;

### Prim's vs Dijkstra's
In Prim's algorithm, we select the node that has the smallest weight. However, in Dijkstra's algorithm, we select the node that has the shortest path weight from the source node.