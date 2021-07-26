"""
923. 3Sum With Multiplicity
Medium

Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.


Constraints:

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300

"""
import collections
from typing import List

"""
Counting with Case

let count[x] be number of times x occurs in A, for each x+y+z==target, we can count the correct contribution to the answer in the following different cases:

1. x!=y and y!=z and x!=z => count[x]*count[y]*count[z]
2. x==y and y != z => C(count[x], 2) * count[z], where C(n, k) is combination number, n picking k, C(n,k) = n!/k!*(n-k)!
3. x != y and y == z => count[x] * C(count[y], 2), where C(count[y], 2) = count[y]*(count[y]-1)/2
4. x == y == z => C(count[x], 3)= count[x]*(count[x]-1)*(count[x]-2)/(3!)

time O(N+W^2) N=len(A), W = max(A[i])
space O(W)
"""


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        count = collections.Counter(A)
        nums = count.keys()
        n = len(nums)

        ans = 0

        # case 1 all different
        for x in range(101):  # 0 <= arr[i] <= 100
            for y in range(x + 1, 101):
                z = target - x - y
                if y < z < 101:
                    ans += count[x] * count[y] * count[z]
                    ans %= MOD

        # case 2 x == y, y != z
        for x in range(101):
            z = target - 2 * x
            if x < z < 101:
                ans += (count[x] * (count[x] - 1) // 2) * count[z]
                ans %= MOD

        # case 3 x != y and y == z
        for x in range(101):
            if (target - x) % 2 == 0:
                z = (target - x) // 2
                if x < z < 101:
                    ans += count[x] * (count[z] * (count[z] - 1) // 2)
                    ans %= MOD

        # case 4 x == y == z
        if target % 3 == 0:
            x = target // 3
            ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6
            ans %= MOD

        return ans % MOD


def main():
    sol = Solution()
    assert sol.threeSumMulti(A = [1,1,2,2,3,3,4,4,5,5], target = 8) == 20, 'fails'

    assert sol.threeSumMulti(A = [1,1,2,2,2,2], target = 5) == 12, 'fails'


if __name__ == '__main__':
   main()