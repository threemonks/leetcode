"""
864. Shortest Path to Get All Keys
Hard

We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can't walk over a lock unless we have the corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.

Example 1:

Input: ["@.a.#","###.#","b.A.B"]
Output: 8
Example 2:

Input: ["@..aA","..B#.","....b"]
Output: 6


Note:

1 <= grid.length <= 30
1 <= grid[0].length <= 30
grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.
"""
import heapq
from typing import List

"""
BFS / Heap

find shorted path using modified BFS algorithm with number of steps as distance, but mark node along with keys on hand when visiting, so that we might revisit a node if we now have new keys

Note: usually, we should not visit a node again that has been visited. But in this problem, we have to go back and forth to get keys for the lock because we need to get keys before we can unlock locks and then go through the locked nodes.
So how do we relax the visited condition?
We should allow revisit a node when state changes (new key found), so we want to record visited node along with keys we visit that node with.

Time complexity: O(mn2^k) - keys_found dimension is 2^k 
k: number of keys
n: column length
m: row length
"""

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])

        seen = set()
        q, keys = [], ''
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    heapq.heappush(q, (0, i, j, ''))
                    seen.add((i, j, 0))  # location, and keys found along the path (always sort keys string in alphabetic order)
                elif grid[i][j] in 'abcdef':
                    keys += grid[i][j]

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            steps, x, y, keys_found = heapq.heappop(q)
            if grid[x][y] in 'abcdef' and grid[x][y] not in keys_found:
                keys_found += grid[x][y]
                keys_found = ''.join(sorted(keys_found))
            if len(keys_found) == len(keys):
                return steps
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny, keys_found) not in seen and grid[nx][ny] != '#' and \
                        (grid[nx][ny] not in 'ABCDEF' or (
                                grid[nx][ny] in 'ABCDEF' and grid[nx][ny].lower() in keys_found)):
                    heapq.heappush(q, (steps + 1, nx, ny, keys_found))
                    seen.add((nx, ny, keys_found))

        return -1

def main():
    sol = Solution()
    assert sol.shortestPathAllKeys(["@.a.#","###.#","b.A.B"]) == 8, 'fails'

    assert sol.shortestPathAllKeys(["@..aA","..B#.","....b"]) == 6, 'fails'

    assert sol.shortestPathAllKeys(["@...a",".###A","b.BCc"]) == 10, 'fails'


if __name__ == '__main__':
   main()