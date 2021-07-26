"""
733. Flood Fill
Easy

2207

263

Add to List

Share
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.



Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]


Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n

"""
from typing import List

"""
DFS
"""
from collections import deque


class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])

        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        oldColor = image[sr][sc]
        q = deque([[sr, sc]])
        image[sr][sc] = newColor
        seen = set([(sr, sc)])
        while q:
            cur = q.popleft()
            # print('cur=%s q=%s' % (cur, q))
            for ni, nj in [[cur[0] + di, cur[1] + dj] for di, dj in dirs]:
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if (ni, nj) not in seen and image[ni][nj] == oldColor:
                    q.append([ni, nj])
                    image[ni][nj] = newColor
                    seen.add((ni, nj))

        return image

def main():

    sol = Solution()

    assert sol.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2) == [[2,2,2],[2,2,0],[2,0,1]], 'fails'

    assert sol.floodFill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2) == [[2,2,2],[2,2,2]], 'fails'

if __name__ == '__main__':
   main()