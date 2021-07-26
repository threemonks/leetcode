"""
11. Container With Most Water
Medium

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2


Constraints:

n == height.length
2 <= n <= 3 * 104
0 <= height[i] <= 3 * 104

"""
from typing import List

"""
two pointers (brutal force)

TLE

time O(N^2)
"""


class Solution0:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        water = -float('inf')
        for i in range(n):
            for j in range(n - 1, i, -1):
                water = max(water, (j - i) * min(height[i], height[j]))

        return water


"""
two pointers

since if we move pointers towards the middle, the width of area will reduce, but we want to find maximum water hold, so it is always better to move the shorter height of the two pointer, as that might find a higher height that might hold more water (the height of water hold is bounded by the shorter of the two end pointer height)

time O(N)
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        water = -float('inf')
        cur_height = 0
        i, j = 0, n - 1
        while i < j:
            if height[i] < height[j]:
                water = max(water, (j - i) * height[i])
                i += 1
            else:
                water = max(water, (j - i) * height[j])
                j -= 1

        return water

def main():
    sol = Solution()
    assert sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49, 'fails'

    assert sol.maxArea([1,1]) == 1, 'fails'

    assert sol.maxArea([4,3,2,1,4]) == 16, 'fails'

    assert sol.maxArea([1,2,1]) == 2, 'fails'

if __name__ == '__main__':
   main()