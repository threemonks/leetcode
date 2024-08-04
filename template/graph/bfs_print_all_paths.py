"""
Print all paths from a given source to a destination using BFS
https://www.geeksforgeeks.org/print-paths-given-source-destination-using-bfs/

create a queue which will store path(s) of type vector
initialise the queue with first path starting from src

Now run a loop till queue is not empty
   get the frontmost path from queue
   check if the lastnode of this path is destination
       if true then print the path
   run a loop for all the vertices connected to the
   current vertex i.e. lastnode extracted from path
      if the vertex is not visited in current path
         a) create a new path from earlier path and
             append this vertex
         b) insert this new path to queue

"""

# Python3 program to print all paths of
# source to destination in given graph
from typing import List
from collections import deque


# Utility function for printing
# the found path in graph
def printpath(path: List[int]) -> None:
    size = len(path)
    for i in range(size):
        print(path[i], end=" ")

    print()


# Utility function to check if current
# vertex is already present in path
def isNotVisited(x: int, path: List[int]) -> int:
    size = len(path)
    for i in range(size):
        if (path[i] == x):
            return 0

    return 1


# Utility function for finding paths in graph
# from source to destination
def findpaths(adj_list: dict[list], src: int,
              dst: int, v: int) -> None:
    # Create a queue which stores
    # the paths
    q = deque([src])
    seen = set()

    while q:
        path = q.popleft()
        last = path[len(path) - 1]

        # If last vertex is the desired destination
        # then print the path
        if (last == dst):
            printpath(path)

        # Traverse to all the nodes connected to
        # current vertex and push new path to queue
        for nei in adj_list[last]:
            if nei not in seen:
                q.append(path+[nei])
                seen.add(nei)


# Driver code
if __name__ == "__main__":
    # Number of vertices
    v = 4
    g = [[] for _ in range(4)]

    # Construct a graph
    g[0].append(3)
    g[0].append(1)
    g[0].append(2)
    g[1].append(3)
    g[2].append(0)
    g[2].append(1)

    src = 2
    dst = 3
    print("path from src {} to dst {} are".format(
        src, dst))

    # Function for finding the paths
    findpaths(g, src, dst, v)

# This code is contributed by sanjeev2552
