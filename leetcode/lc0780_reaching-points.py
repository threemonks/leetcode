"""
780. Reaching Points
Hard

811

137

Add to List

Share
Given four integers sx, sy, tx, and ty, return true if it is possible to convert the point (sx, sy) to the point (tx, ty) through some operations, or false otherwise.

The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y).



Example 1:

Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: true
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)
Example 2:

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: false
Example 3:

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: true


Constraints:

1 <= sx, sy, tx, ty <= 10^9

"""
"""
Math

from sx,sy to tx,ty there are multiple paths, but from tx,ty to sx,sy there's only one path, we can validate if that is possible

              1,1
      1,2             2,1
  1,3       2,3     2,3     3,1
1,4 4,3   2,5 5,3 2,5 5,3 3,4 4,1

Also it is fast to do modulo tx%ty instead of tx-ty, assuming tx>ty

time O(log(N)) - N = max(tx, ty)
space O(1)
"""
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if tx > ty:
            return self.reachingPoints(sy, sx, ty, tx)
        if tx < sx or ty < sy:
            return False
        elif tx == sx:
            return (ty - sy) % sx == 0
        elif tx > sx:
            return self.reachingPoints(sy, sx, ty%tx, tx)


def main():
    sol = Solution()

    assert sol.reachingPoints(sx = 1, sy = 1, tx = 3, ty = 5) == True, 'fails'

    assert sol.reachingPoints(sx = 1, sy = 1, tx = 2, ty = 2) == False, 'fails'

    assert sol.reachingPoints(sx = 1, sy = 1, tx = 1, ty = 1) == True, 'fails'


if __name__ == '__main__':
   main()