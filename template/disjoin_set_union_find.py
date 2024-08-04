"""
Union Find only stores number

"""
from typing import List


class DSU:
    def __init__(self, n):
        # initially all notes have itself as parent
        # but find will update its parent if necessary
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

# improve by size (weighted)
# attach small tree as child for big tree
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # improve by size (weighted)
    # attach small tree as child to big tree
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty: return False
        if self.size[rootx] <= self.size[rooty]:
            self.parent[rootx] = rooty
            self.size[rooty] += self.size[rootx]
        elif self.size[rootx] > self.size[rooty]:
            self.parent[rooty] = rootx
            self.size[rootx] += self.size[rooty]

# improve by ranked
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # improve by size (weighted)
    # attach small tree as child of big tree
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty: return
        if self.rank[rootx] <= self.rank[rooty]:
            self.parent[rootx] = rooty
        elif self.size[rootx] > self.size[rooty]:
            self.parent[rooty] = rootx
        else: # 只有rank相等时才需要更新rank
            self.parent[rootx] = rooty
            self.rank[rooty] += 1

## DSU for 2D matrix
        def numIslands(self, grid: List[List[str]]) -> int:
            m = len(grid)
            n = len(grid[0])

            count = 0

            dsu = DSU(m * n)

            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == '0':
                        continue
                    count += 1
                    for ni, nj in [(i + di, j + dj) for di, dj in dirs if 0 <= i + di < m and 0 <= j + dj < n]:
                        if grid[ni][nj] == "1":
                            p1, p2 = i * n + j, ni * n + nj  # convert 2-d index to 1-d index for DSU
                            island1 = dsu.find(p1)
                            island2 = dsu.find(p2)
                            if island1 != island2:
                                dsu.union(p1, p2)
                                count -= 1

            return count


