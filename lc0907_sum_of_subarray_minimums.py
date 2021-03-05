"""
907. Sum of Subarray Minimums
Medium

Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.


Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000




Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444


Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
"""
from typing import List

"""
Stack

observation:
given array [3,1,2,4], we check the subarrays whose minimum is a given element arr[i]
subarray with minimum point 3 are [3], so to its left, there are 0 subarray with minimum at 3, and to its right, there are also 0 subarray with minimum at 3, so total number of subarray with 3 as minimum is (0+1)*(1+0), and the contribution from this to sum of min(B) is (0+1)*3*(1+0)
for element 1, there are [3,1], [3,1,2], [3,1,2,4],[1], [1,2], [1,2,4], so total number of subarrays with 1 as minimum is (1+1)*(1+2)
for element 2, there are [2], [2,4]
for element 4, there is only [4]

for arr[i], assume there are L consecutive numbers greater than arr[i] to the left of arr[i], i.e., in range arr[0]...arr[i-1], and R consecutive numbers greater than arr[i] to the right, in range arr[i+1]....arr[n-1], then arr[i] will be min of total of (L+1)*(R+1) subarrays.

note when the minimum numbers appear more than once, we need to use <= on one side to avoid double counting, i.e., for previous larger number we use less strict greater than (>=), and for next larger number we then use strict greater than (>).

"""


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = (10 ** 9 + 7)
        n = len(arr)

        stack = []
        prev_larger = [
                          1] * n  # number of consecutive elements larger than arr[i] on left, in range from arr[0] to arr[i-1], ending at arr[i-1]
        for i in range(0, n):
            while stack and stack[-1][0] >= arr[i]:
                prev_larger[i] += stack.pop()[1]
            stack.append((arr[i], prev_larger[i]))
            # print(stack)

        # print(prev_larger)

        stack = []
        next_larger = [
                          1] * n  # number of consecutive elements larger than arr[i] on right, in range from arr[i+1] to arr[n-1], starting at arr[i+1]
        for i in range(n - 1, -1, -1):
            while stack and stack[-1][0] > arr[i]:
                next_larger[i] += stack.pop()[1]
            stack.append((arr[i], next_larger[i]))
            # print(stack)

        # print(next_larger)

        return sum([(pl * nl * a) for (pl, nl, a) in zip(prev_larger, next_larger, arr)]) % MOD

def main():
    sol = Solution()
    assert sol.sumSubarrayMins([3,1,2,4]) == 17, 'fails'

    assert sol.sumSubarrayMins([11,81,94,43,3]) == 444, 'fails'

if __name__ == '__main__':
   main()