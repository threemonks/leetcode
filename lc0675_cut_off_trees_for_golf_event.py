"""
675. Cut Off Trees for Golf Event
Hard

You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

0 means the cell cannot be walked through.
1 represents an empty cell that can be walked through.
A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

You are guaranteed that no two trees have the same height, and there is at least one tree needs to be cut off.



Example 1:


Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
Output: 6
Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
Example 2:


Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
Output: -1
Explanation: The trees in the bottom row cannot be accessed as the middle row is blocked.
Example 3:

Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
Output: 6
Explanation: You can follow the same path as Example 1 to cut off all the trees.
Note that you can cut off the first tree at (0, 0) before making any steps.


Constraints:

m == forest.length
n == forest[i].length
1 <= m, n <= 50
0 <= forest[i][j] <= 109

"""
import heapq
from typing import List

"""

BFS

outer layer - we need to start at (0, 0), go to each tree in ascending height, avoid blocked cells, and minimizing total steps

from each step to next step, we use BFS/Dijkstra's algorithm  to explore all its neighbors, using steps as cost, to try to get to next height tree location with least number of steps


"""


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m = len(forest)
        n = len(forest[0])

        def distance(i, j, xx, yy):
            nonlocal forest
            q = [(0, i, j)]  # steps, x, y
            heapq.heapify(q)
            visited = set()
            visited.add((i, j))
            while q:
                steps, x, y = heapq.heappop(q)
                if x == xx and y == yy:
                    return steps
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or forest[nx][ny] == 0 or (nx, ny) in visited:
                        continue
                    else:
                        heapq.heappush(q, (steps + 1, nx, ny))
                        visited.add((nx, ny))

            return -1

        # all trees sorted by height, we will try to walk to each of them in order with least steps
        q = [(forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1]

        heapq.heapify(q)

        # start at cell (0, 0)
        i, j = 0, 0
        # print('i=%s j=%s' % (i, j))

        res = 0
        while q:
            # print('q=%s' % q)
            height, x, y = heapq.heappop(q)
            steps = distance(i, j, x, y)
            # print('i=%s j=%s x=%s y=%s steps=%s' % (i, j, x, y, steps))
            if steps == -1:
                return steps
            res += steps
            i, j = x, y  # move to next tree

        return res if res > 0 else -1


def main():
    sol = Solution()
    assert sol.cutOffTree([[1,2,3],[0,0,4],[7,6,5]]) == 6, 'fails'

    assert sol.cutOffTree([[1,2,3],[0,0,0],[7,6,5]]) == -1, 'fails'

    assert sol.cutOffTree([[2,3,4],[0,0,5],[8,7,6]]) == 6, 'fails'

if __name__ == '__main__':
   main()