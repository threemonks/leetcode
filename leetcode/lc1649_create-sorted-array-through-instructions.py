"""
1649. Create Sorted Array through Instructions
Hard

354

50

Add to List

Share
Given an integer array instructions, you are asked to create a sorted array from the elements in instructions. You start with an empty container nums. For each element from left to right in instructions, insert it into nums. The cost of each insertion is the minimum of the following:

The number of elements currently in nums that are strictly less than instructions[i].
The number of elements currently in nums that are strictly greater than instructions[i].
For example, if inserting element 3 into nums = [1,2,3,5], the cost of insertion is min(2, 1) (elements 1 and 2 are less than 3, element 5 is greater than 3) and nums will become [1,2,3,3,5].

Return the total cost to insert all elements from instructions into nums. Since the answer may be large, return it modulo 109 + 7



Example 1:

Input: instructions = [1,5,6,2]
Output: 1
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 5 with cost min(1, 0) = 0, now nums = [1,5].
Insert 6 with cost min(2, 0) = 0, now nums = [1,5,6].
Insert 2 with cost min(1, 2) = 1, now nums = [1,2,5,6].
The total cost is 0 + 0 + 0 + 1 = 1.
Example 2:

Input: instructions = [1,2,3,6,5,4]
Output: 3
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 2 with cost min(1, 0) = 0, now nums = [1,2].
Insert 3 with cost min(2, 0) = 0, now nums = [1,2,3].
Insert 6 with cost min(3, 0) = 0, now nums = [1,2,3,6].
Insert 5 with cost min(3, 1) = 1, now nums = [1,2,3,5,6].
Insert 4 with cost min(3, 2) = 2, now nums = [1,2,3,4,5,6].
The total cost is 0 + 0 + 0 + 0 + 1 + 2 = 3.
Example 3:

Input: instructions = [1,3,3,3,2,4,2,1,2]
Output: 4
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3,3].
Insert 2 with cost min(1, 3) = 1, now nums = [1,2,3,3,3].
Insert 4 with cost min(5, 0) = 0, now nums = [1,2,3,3,3,4].
​​​​​​​Insert 2 with cost min(1, 4) = 1, now nums = [1,2,2,3,3,3,4].
​​​​​​​Insert 1 with cost min(0, 6) = 0, now nums = [1,1,2,2,3,3,3,4].
​​​​​​​Insert 2 with cost min(2, 4) = 2, now nums = [1,1,2,2,2,3,3,3,4].
The total cost is 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4.


Constraints:

1 <= instructions.length <= 10^5
1 <= instructions[i] <= 10^5
"""
import bisect
from typing import List

"""
Can also use these methods:
1. merge sort + count inversions
2. SortedList + bisect.bisect_left and bisect.bisect_right
"""

"""
Sort + Binary Search

for each insert, find left most and right most insertion location, and take the min of these two values

time O(N^2)
TLE

mistakes:
1. MOD 10**9+7
"""


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n, MOD = len(instructions), 10 ** 9 + 7
        ans = 0
        nums = []
        for i in range(n):
            x = instructions[i]
            left = bisect.bisect_left(nums, x)
            right = bisect.bisect_right(nums, x)
            # print('i=%s x=%s left=%s right=%s' % (i, x, left, right))
            ans = (ans + min(left, len(nums) - right)) % MOD
            # nums.insert(left, x)
            bisect.insort(nums, x)
            # print('i=%s x=%s ans=%s' % (i, x, ans))

        return ans


"""
Fenwick Tree

to count number of occurances of numbers, take min at each step from occurances of smaller number, and i - (total count of occurances of smaller number or same)
"""


class FenwickTree:
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, delta):
        i += 1
        while i < len(self.sums):
            self.sums[i] += delta
            i += self._lowbit(i)

    def query(self, i):  # prefix sum[1,...,i]
        i += 1
        s = 0
        while i > 0:
            s += self.sums[i]
            i -= self._lowbit(i)
        return s

    def _lowbit(self, x):
        return x & (-x)


class Solution1:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10 ** 9 + 7

        fw_tree = FenwickTree(
            max(instructions) + 1)  # could compress index using distinct nums from instructions, but not necessary here

        ans = 0
        for i, num in enumerate(instructions):
            left = fw_tree.query(num - 1)
            right = i - fw_tree.query(num)
            ans = (ans + min(left, right)) % MOD
            fw_tree.update(num, 1)

        return ans


def main():
    sol = Solution()
    assert sol.createSortedArray(instructions = [1,5,6,2]) == 1, 'fails'

    assert sol.createSortedArray(instructions = [1,2,3,6,5,4]) == 3, 'fails'

    assert sol.createSortedArray(instructions = [1,3,3,3,2,4,2,1,2]) == 4, 'fails'

if __name__ == '__main__':
   main()