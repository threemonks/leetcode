"""
360. Sort Transformed Array
Medium

435

126

Add to List

Share
Given a sorted integer array nums and three integers a, b and c, apply a quadratic function of the form f(x) = ax2 + bx + c to each element nums[i] in the array, and return the array in a sorted order.



Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]


Constraints:

1 <= nums.length <= 200
-100 <= nums[i], a, b, c <= 100
nums is sorted in ascending order.


Follow up: Could you solve it in O(n) time?
"""
from typing import List

"""
Array

use map and lambda and sort
time O(N*log(N))
"""


class Solution0:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        return sorted(map(lambda x: a * x * x + b * x + c, nums))


"""
Array

since nums is already sorted, a*x^2+b*x+c is a parabola
if a>0 it is concave, means two ends are larger
if a<0 it is convex, means two ends are smaller
so we need to calculate two sides separately and do merge sort O(N)

nums = [-4,-2,2,4], a = 1, b = 3, c = 5

time O(N)
"""


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        n = len(nums)
        ans = []
        i, j = 0, n - 1
        while i <= j:
            xi = a * nums[i] * nums[i] + b * nums[i] + c
            xj = a * nums[j] * nums[j] + b * nums[j] + c
            if a > 0:  # concave, add big ones (from ends) first, reverse at output
                if xi <= xj:
                    ans.append(xj)
                    j -= 1
                else:
                    ans.append(xi)
                    i += 1
            else:  # a<0 # convex, add smaller ones (from ends) first
                if xi <= xj:
                    ans.append(xi)
                    i += 1
                else:
                    ans.append(xj)
                    j -= 1

        return ans[::-1] if a > 0 else ans

def main():
    sol = Solution()
    assert sol.sortTransformedArray(nums = [-4,-2,2,4], a = 1, b = 3, c = 5) == [3,9,15,33], 'fails'

    assert sol.sortTransformedArray(nums = [-4,-2,2,4], a = -1, b = 3, c = 5) == [-23,-5,1,7], 'fails'


if __name__ == '__main__':
   main()