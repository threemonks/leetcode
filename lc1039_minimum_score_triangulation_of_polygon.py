"""
1039. Minimum Score Triangulation of Polygon
Medium

531

63

Add to List

Share
Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1] in clockwise order.

Suppose you triangulate the polygon into N-2 triangles.  For each triangle, the value of that triangle is the product of the labels of the vertices, and the total score of the triangulation is the sum of these values over all N-2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.



Example 1:

Input: [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.
Example 2:



Input: [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.
Example 3:

Input: [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.


Note:

3 <= A.length <= 50
1 <= A[i] <= 100

"""
from typing import List


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        """

        dp[i][j] := minimum score after slicing using edge [i, j], a triangle would be with edge i,j plus any other vertice k (k!=i and k!=j)

        dp[i][j] = min([minScoreTriagulation(A[left side of triangle (i,j,k)]) + i*j*k + minScoreTriagulation(A[right side of triangle (i,j,k)]) for k from i+1, ... to j-1)

        """
        if len(A) <= 2:
            return 0
        l = len(A)

        @lru_cache(None)
        def dfs(i, j):
            nonlocal A
            if i + 1 < j:
                return min([A[i] * A[j] * A[k] + dfs(i, k) + dfs(k, j) for k in range(i + 1, j)])
            else:
                return 0

        return dfs(0, len(A) - 1)


def main():
    sol = Solution()
    assert sol.minScoreTriangulation([1,2,3]) == 6, 'fails'

    assert sol.minScoreTriangulation([3,7,4,5]) == 144, 'fails'

    assert sol.minScoreTriangulation([1,3,1,4,1,5]) == 13, 'fails'

if __name__ == '__main__':
   main()