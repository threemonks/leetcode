"""
711. Number of Distinct Islands II
Hard

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if they have the same shape, or have the same shape after rotation (90, 180, or 270 degrees only) or reflection (left/right direction or up/down direction).

Example 1:
11000
10000
00001
00011
Given the above grid map, return 1.

Notice that:
11
1
and
 1
11
are considered same island shapes. Because if we make a 180 degrees clockwise rotation on the first island, then two islands will have the same shapes.
Example 2:
11100
10001
01001
01110
Given the above grid map, return 2.

Here are the two distinct islands:
111
1
and
1
1

Notice that:
111
1
and
1
111
are considered same island shapes. Because if we flip the first array in the up/down direction, then they have the same shapes.
Note: The length of each dimension in the given grid does not exceed 50.

"""

from itertools import product
from typing import List

"""
Algorithm (DFS)

1. Use regular DFS to find all the connected components for the grid.
2. For each component compute all the its symmetrical variants. This could be done by switching coordinate or rotating the grid.
3. Normalize all the components to the upper left corner. This step is necessary since otherwise equivalent components become difficult to identify as each component may live is a different coordinate chart.
4. after this, we should have for each component 8 equivalent representations in the same coordinate chart. We now pick the representative to be the smallest one in the natural(lexicographical) ordering.
5. Then we use a set to get the answer.

For each of 8 possible rotations and reflections of the shape, we will perform the transformation and then translate the shape so that the bottom-left-most coordinate is (0, 0). Afterwards, we will consider the canonical hash of the shape to be the maximum of these 8 intermediate hashes.

we use complex number to achieve rotation by 90 degrees by multipling by the imaginary unit 1j.

time O(R*C*log(R*C))
space O(R*C)

"""

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        print('m=%s n=%s' % (m, n))

        dirs = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        seen = set()

        def dfs(r, c):
            if (r, c) in seen:
                return
            seen.add((r, c))
            shape.add((r*n+c))
            print('r=%s c=%s' % (r, c))
            for nr, nc in [(r+dr, c+dc) for dr, dc in dirs if 0<=r+dr<m and 0<=c+dc<n]:
                if grid[nr][nc] == 1:
                    dfs(nr, nc)

        # input: a list of encoded coordinations of a original shape
        # transfer to the potential 8 same shapes
        # c = 0: original one, x -> x, y -> y
        # c = 1: upside down, x -> x, y -> -y
        # c = 2: left / right reflection, x -> -x, y -> y
        # c = 3: rotate 180°, x -> -x, y -> -y
        # c = 4: rotate 90°, x -> y, y -> x
        # c = 5: rotate 90° and upside down, x -> y, y -> -x
        # c = 6: rotate 90° and reflect right / left, x -> -y, y -> x
        # c = 7: rotate 270° , x -> -y, y -> -x
        def canonical(shape):
            print('len(shape)=%s' % len(shape))
            ans = ""
            lift = m + n
            out = [None] * len(shape)
            xs = [None] * len(shape)
            ys = [None] * len(shape)
            for dir in range(8):
                t = 0
                for idx, z in enumerate(shape):
                    x = int(z // n)
                    y = int(z % n)
                    if dir == 0:
                        xs[t], ys[t] = x, y
                    elif dir == 1:
                        xs[t], ys[t] = x, -y
                    elif dir == 2:
                        xs[t], ys[t] = -x, y
                    elif dir == 3:
                        xs[t], ys[t] = -x, -y
                    elif dir == 4:
                        xs[t], ys[t] = y, x
                    elif dir == 5:
                        xs[t], ys[t] = y, -x
                    elif dir == 6:
                        xs[t], ys[t] = -y, x
                    elif dir == 7:
                        xs[t], ys[t] = -y, -x
                    t += 1

                # we are on a 2D-plane, so it's necessary to identify same shape after translation
                # so we always put the top-left cell on (0, 0) to make a shape canonical
                # and we need to find it first, (mx, my) is the top-left cell

                mx, my = min(xs), min(ys)
                # canonical encode all the coordinations
                for j in range(len(shape)):
                    out[j] = (xs[j]-mx)*lift + (ys[j]-my)

                # always return the smallest shape in lexicological order
                # image you have two shapes: one and another upside-down one
                # this will guarantee canonical(one) == canonical(another)
                # it will help you decide whther shapes are exactly the same
                candidate = str(sorted(out))
                ans = max(ans, candidate)

            print('shape=%s canonical=%s' % (shape, ans))
            return ans

        shapes = set()
        for r in range(m):
            for c in range(n):
                shape = set()
                dfs(r, c)
                if shape:
                    print('r=%s c=%s shape=%s' % (r, c, shape))
                    shapes.add(canonical(shape))

        return len(shapes)


def main():
    sol = Solution()
    assert sol.numDistinctIslands2([[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]]) == 1, 'fails'

    # assert sol.numDistinctIslands2([[1,1,1,0,0], [1,0,0,0,1], [0,1,0,0,1], [0,1,1,1,0]]) == 2, 'fails'
    #
    # assert sol.numDistinctIslands2([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]) == 2, 'fails'


if __name__ == '__main__':
   main()