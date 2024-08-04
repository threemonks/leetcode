"""
柱状图中最大的矩形

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。



https://www.1point3acres.com/bbs/thread-778019-1-1.html

https://leetcode.com/problems/largest-rectangle-in-histogram/

"""
"""
Monotonic Stack

"""
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        return False

def main():
    sol = Solution()
    assert sol.largestRectangleArea(heights = [2,1,5,6,2,3]) == 10, 'fails'

    assert sol.largestRectangleArea(heights = [2,4]) == 4, 'fails'


if __name__ == '__main__':
   main()