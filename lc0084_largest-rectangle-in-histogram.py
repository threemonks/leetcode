"""
84. Largest Rectangle in Histogram
Hard

"""
from math import inf
from typing import List

"""
Brutal Force
iterate all pairs of height, calculate area between the pairs (width * min height of all bars in between)
for min height between pairs, we iterate through all heights in between the pairs to find it

time O(N^3)
TLE
"""


class Solution0:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            for j in range(i, n):
                min_height = inf
                for k in range(i, j + 1):
                    min_height = min(min_height, heights[k])
                max_area = max(max_area, min_height * (j - i + 1))

        return max_area


"""
Brutal Force with some improvement
iterate all pairs of height, calculate area between the pairs (width * min height of all bars in between)
we keep min height for pairs[i...j], then for min height pairs[i...j+1], it would be
min_height[i][j+1] = min(min_height[i][j], heights[j])

time O(N^2)
TLE
"""


class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            prev_min_height = heights[i]
            for j in range(i, n):
                min_height = min(prev_min_height, heights[j])
                max_area = max(max_area, min_height * (j - i + 1))
                prev_min_height = min_height

        return max_area


"""
Divide and Conquer

observation: rectangle with maximum area will be maximum of the three cases:
1. widest possible rectangle with height equal to height of shortest bar
2. largest rectangle confined to the left of the shortest bars (subproblem)
3. largest rectangle confined to the right of the shortest bars (subproblem)

therefore we use divide and conquer to calculate result from the subproblem

time O(Nlog(N)) - average
     O(N^2) - worst case - if numbers are already sorted

TLE
"""
from functools import lru_cache


class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        @lru_cache(None)
        def cal_area(start, end):
            nonlocal heights
            if start > end:
                return 0
            minidx = start
            for i in range(start, end + 1):
                if heights[i] < heights[minidx]:
                    minidx = i

            return max(heights[minidx] * (end - start + 1), cal_area(start, minidx - 1), cal_area(minidx + 1, end))

        return cal_area(0, len(heights) - 1)


"""
Stack -- index of monotonic increasing bar height

Use a stack to record index of monotonic increasing bars, if a new bar height is higher than stack top index bar height, push it in, 
if the new bar is lower, we pop out the stack top, and the just popped out bar height would be highest bar inside the rectangle we want to consider max area for, and the new bar would be the right boundary of the rectangle, the stack top (after pop) would be the left boundary of the rectangle, update max area with this one if this one is larger. We keep pop out stack top until the stack top index's bar height is less than the new bar, then we push the new bar index into stack

Note:
    the rectangle in consideration has width i-stack[-1]-1
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights
        stack = []
        max_area = 0
        for i in range(len(heights)):
            # print('i=%s stack=%s' % (i, stack))
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack[-1]]
                w = i - (stack[-2] if len(stack) >= 2 else -1) - 1
                max_area = max(max_area,
                               w * h)  # new rectangle with height h, right boundary i (exclusive) and left boundary stack[-1] (exclusive)
                # print('h=%s w=%s w*h=%s stack=%s' % (h, w, w*h, stack))
                stack.pop()

            # now heights[i] > heights[stack[-1]]
            stack.append(i)

        # print(stack)
        # remaining index on stack, these bars have no shorter bar to right
        while stack:
            h = heights[stack.pop()]
            w = len(heights) - (stack[-1] if stack else -1) - 1
            max_area = max(max_area,
                           w * h)  # new rectangle with height h, right boundary i (exclusive) and left boundary stack[-1] (exclusive)

        # print(stack)
        return max_area


"""
Stack -- index of monotonic increasing bar height

Same as above, but use sentinel element (dummy heights head) to handle boundary condition
Note:
    the rectangle in consideration has width i-stack[-1]-1
"""


class Solution4:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            # print('i=%s stack=%s' % (i, stack))
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area,
                               w * h)  # new rectangle with height h, right boundary i (exclusive) and left boundary stack[-1] (exclusive)
                # print('h=%s w=%s w*h=%s stack=%s' % (h, w, w*h, stack))

            # now heights[i] > heights[stack[-1]]
            stack.append(i)

        # because we add dummy index [-1] (corresponding height 0) as sentinel element in front of stack, we don't need to process any remaining itesm

        # print(stack)
        return max_area


def main():
    sol = Solution()
    assert sol.largestRectangleArea(heights = [2,1,5,6,2,3]) == 10, 'fails'

    assert sol.largestRectangleArea([2,4]) == 4, 'fails'


if __name__ == '__main__':
   main()