## Minimum spanning tree
https://www.geeksforgeeks.org/difference-between-prims-and-kruskals-algorithm-for-mst/

### Kruskal’s algorithm for MST

Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all the vertices together. A single graph can have many different spanning trees. A minimum spanning tree (MST) or minimum weight spanning tree for a weighted, connected and undirected graph is a spanning tree with weight less than or equal to the weight of every other spanning tree. The weight of a spanning tree is the sum of weights given to each edge of the spanning tree. 

Below are the steps for finding MST using Kruskal’s algorithm 

Sort all the edges in non-decreasing order of their weight. 
Pick the smallest edge. Check if it forms a cycle with the spanning-tree formed so far. If the cycle is not formed, include this edge. Else, discard it. 
Repeat step#2 until there are (V-1) edges in the spanning tree. 

### Prim’s algorithm for MST

Like Kruskal’s algorithm, Prim’s algorithm is also a Greedy algorithm. It starts with an empty spanning tree. The idea is to maintain two sets of vertices. The first set contains the vertices already included in the MST, the other set contains the vertices not yet included. At every step, it considers all the edges that connect the two sets and picks the minimum weight edge from these edges. After picking the edge, it moves the other endpoint of the edge to the set containing MST. 

Below are the steps for finding MST using Prim’s algorithm 

Create a set mstSet that keeps track of vertices already included in MST. 
Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE. Assign key value as 0 for the first vertex so that it is picked first. 
While mstSet doesn’t include all vertices 
Pick a vertex u which is not there in mstSet and has minimum key value. 
Include u to mstSet. 
Update the key value of all adjacent vertices of u. To update the key values, iterate through all adjacent vertices. For every adjacent vertex v, if the weight of edge u-v is less than the previous key value of v, update the key value as the weight of u-v 
Both Prim’s and Kruskal’s algorithm finds the Minimum Spanning Tree and follow the Greedy approach of problem-solving, but there are few major differences between them.  