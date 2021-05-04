"""
493. Reverse Pairs
Hard

1371

145

Add to List

Share
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].



Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Example 2:

Input: nums = [2,4,3,5,1]
Output: 3


Constraints:

1 <= nums.length <= 5 * 10^4
2^31 <= nums[i] <= 2^31 - 1
"""
import bisect
from typing import List

"""
Sort and Binary Search

iterate array from right to left, for visited nums, insert into sorted new array and keep it ordered, before add, search its insertion location using binary search, the insertion location index is # of numbers smaller to right

reverse pair
0 <= i < j < nums.length and nums[i] > 2 * nums[j]

time O(Nlog(N))
"""
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        arr = []
        for i in range(n-1, -1, -1):
            num = nums[i]
            idx1 = bisect.bisect_left(arr, num/2)
            ans += idx1
            idx = bisect.bisect_left(arr, num)
            arr.insert(idx, num)

        return ans

"""
Fenwick Tree
[1, 3, 2, 3, 1]

from right to left, nums[i]>2*nums[j]
[0  1  0  1  0]

We basically add [2*num for num in nums] into nums, and for everytime we iterate a number, we update count of 2*num in fenwick tree, and query as normal

count 1   1
num   1 2 3
tree  1
query()
"""
class FenwickTree:
    def __init__(self, n):
        self.sums = [0]*(n+1)

    def update(self, i, delta):
        i += 1
        while i < len(self.sums):
            self.sums[i] += delta
            i += self._lowbit(i)

    def query(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.sums[i]
            i -= self._lowbit(i)
        return s

    def _lowbit(self, x):
        return x & (-x)

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # add 2*num into nums, so that for every num, we update the count of 2*num,
        # then query(rank[num]-1) would give count of nums[j] where 2*nums[j]<nums[i]
        all_nums = list(set(nums + [2*x for x in nums]))
        # compression - store all v:index so that fenwick tree just need to have size len(all_nums)
        rank = {v: i for i, v in enumerate(sorted(all_nums))}

        fw_tree = FenwickTree(len(all_nums))
        ans = 0
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            ans += fw_tree.query(rank[num]-1)
            fw_tree.update(rank[2*num], 1)

        return ans


def main():
    sol = Solution()
    assert sol.reversePairs(nums = [1,3,2,3,1]) == 2, 'fails'

    assert sol.reversePairs(nums = [2,4,3,5,1]) == 3, 'fails'

if __name__ == '__main__':
   main()