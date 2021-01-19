"""
42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105

"""
from typing import List

"""
amount of water that can be hold by any index is the minimum of the highest bar on two sides
use leftmax and rightmax to keep track of highest bar up to index i (excluding) from left, and up to index j (excluding) from right
"""


class Solution0:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        n = len(height)

        leftmax = [0] * n
        leftmax[0] = 0
        for i in range(1, n):
            leftmax[i] = max(leftmax[i - 1], height[i - 1])

        rightmax = [0] * n
        rightmax[n - 1] = 0
        for j in range(n - 2, -1, -1):
            rightmax[j] = max(rightmax[j + 1], height[j + 1])

        res = 0

        for i in range(1, n - 1):
            if min(leftmax[i], rightmax[i]) > height[i]:
                res += min(leftmax[i], rightmax[i]) - height[i]
                # print('i=%s leftmax[i]=%s rightmax[i]=%s res=%s' % (i, leftmax[i], rightmax[i], res))

        return res


"""
Using stack to keep track of bars that are bounded by higher bars, therefore may store water
 * use stack to store indices of bars
 * iterate the array:
   i) while stack is not empty and height[i] > height[stack[-1]]
      - It means that stack element can be popped, pop it as valley
      - then find the distance between current element and the element at top of stack, wihch is to be filled
         distance = i - stack[-1] -1
      - Find the bounded height bounded_height = min(height[i], height[stack[-1]])-height[valley]
      - Add resulting trapped water to answer ans += distance * bounded_height
    ii) push current index i to top of stack
    iii) increase current index i

"""


class Solution1:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        n = len(height)

        ans = 0
        stack = []

        i = 0
        while i < n:
            while stack and height[i] >= height[stack[-1]]:
                valley = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[valley]
                print('i=%s valley=%s stack[-1]=%s bounded_height=%s, water=%s stack=%s' % (
                i, valley, stack[-1], bounded_height, distance * bounded_height, str(stack)))
                ans += distance * bounded_height
            stack.append(i)
            i += 1

        return ans


"""
Two pointers - calculate leftmax and rightmax along the way from both left and right into middle
since water trapped on given index would depends on one side bar only
 - depends on left_max only if height[left] < height[right]
 - depends on right_max only if height[left] >= height[right]

so we can calculate left_max and right_max and only keep the latest value, and use it to calculate the water trapped by current index left or right when height[left] < left_max, or height[right] < right_max

"""


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        n = len(height)

        left = 0
        right = n - 1

        ans = 0
        left_max = 0
        right_max = 0

        while left < right:
            if height[left] < height[right]:  # if height[left] < height[right], water trapped depends on left_max only
                if height[left] >= left_max:  # if higher left bar found, update left_max
                    left_max = height[left]
                else:
                    ans += left_max - height[left]  # else calculate water trapped using known left_max
                left += 1
            else:  # height[left] >= height[right]
                if height[right] >= right_max:  # if higher right bar found, update right_max
                    right_max = height[right]
                else:
                    ans += right_max - height[right]  # else calculate water trapped using right_max
                right -= 1

        return ans


def main():
    sol = Solution()
    assert sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6, 'fails'

    assert sol.trap([4,2,0,3,2,5]) == 9, 'fails'

if __name__ == '__main__':
   main()