"""
962. Maximum Width Ramp
Medium

Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

Find the maximum width of a ramp in A.  If one doesn't exist, return 0.



Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation:
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation:
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.


Note:

2 <= A.length <= 50000
0 <= A[i] <= 50000

"""
from typing import List

"""
observation:
given array [3,1,2,4], we check the subarrays whose minimum is a given element arr[i]
subarray with minimum point 3 are [3], so to its left, there are 0 subarray with minimum at 3, and to its right, there are also 0 subarray with minimum at 3, so total number of subarray with 3 as minimum is (0+1)*(1+0), and the contribution from this to sum of min(B) is (0+1)*3*(1+0)
for element 1, there are [3,1], [3,1,2], [3,1,2,4],[1], [1,2], [1,2,4], so total number of subarrays with 1 as minimum is (1+1)*(1+2)
for element 2, there are [2], [2,4]
for element 4, there is only [4]

for arr[i], assume there are L consecutive numbers greater than arr[i] to the left of arr[i], i.e., in range arr[0]...arr[i-1], and R consecutive numbers greater than arr[i] to the right, in range arr[i+1]....arr[n-1], then arr[i] will be min of total of (L+1)*(R+1) subarrays.

note when the minimum numbers appear more than once, we need to use <= on one side to avoid double counting, i.e., for previous larger number we use less strict greater than (>=), and for next larger number we then use strict greater than (>).

"""
"""
observation
use stack to hold monotonic decreasing values and their indexes, as for any larger value appears later, the ramp from a later value to this one could be extended to an earlier smaller value, thus this value does not need to be added into the stack
"""


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)
        ramp = 0
        stack = []
        for i in range(n):
            if not stack or stack[-1][0] > A[i]:
                stack.append((A[i], i))
            if stack and stack[-1][0] <= A[i]:
                j = len(stack) - 1
                while j >= 0 and stack[j][0] <= A[i]:
                    j -= 1
                # now j points at -1 or a index with stack[j][0] > A[i]
                # print(j)
                if j == -1:
                    ramp = max(ramp, i)
                else:
                    ramp = max(ramp, i - (stack[j + 1][1]))
            # print(stack)

        return ramp


"""
use binary search to get maximum ramp width from the stack to current element we are checking
why is this even slower than the above brutal force search?
"""


class Solution2:
    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)
        ramp = 0
        stack = []
        for i in range(n):
            if not stack or stack[-1][0] > A[i]:
                stack.append((A[i], i))
            # print(stack)
            # binary search to find maximum ramp width with current element A[i] against stack elements
            l, r = 0, len(stack) - 1
            while l < r:
                mid = l + (r - l) // 2
                if stack[mid][0] > A[i]:
                    l = mid + 1
                else:  # stack[mid][0] < A[i]
                    r = mid
            ramp = max(ramp, i - stack[r][1])

        return ramp

def main():
    sol = Solution()
    assert sol.maxWidthRamp([6,0,8,2,1,5]) == 4, 'fails'

    assert sol.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]) == 7, 'fails'

if __name__ == '__main__':
   main()