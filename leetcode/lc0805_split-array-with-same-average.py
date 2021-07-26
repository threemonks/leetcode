"""
805. Split Array With Same Average
Hard
"""
import collections
from functools import lru_cache
from typing import List

"""

DP with early pruning

Observation:

if avg(A) == avg(B), then avg(A) == avg(nums), to avoid division precision,

avg(A) = avg(nums) <=> sum(A) * len(nums) == sum(nums) * len(A)

So the problem is to find subset of nums, A, whose sum is sum(A), and count len(A), which satisfy

sum(A) * len(nums) == sum(nums) * len(A)

=>
sum(A) = sum(nums) * len(A) / len(nums)

since sum(A) is always integer, so we know we only need to check len(A) that would make sum(nums)*len(A)/len(nums) be integer
i.e., only len(A) satisfy this is valid:

sum(nums)*len(A)%len(nums) == 0

剪枝方法：
1. 如果对于一个数值，我们不选，那后面可能有这个数字重复，可以一起跳过

time O(2^N)

"""


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        n = len(nums)

        sums = sum(nums)

        @lru_cache(None)
        def find(len_a, sum_a, idx):
            """
            exploring nums up to index idx, can we creaet a subset array that have len_a elments, and sum to sum_a
            """
            # length of array A, total sum of array A, and current index in nums that we are exploring
            nonlocal nums
            # print('len_a=%s sum_a=%s idx=%s' % (len_a, sum_a, idx))
            if sum_a == 0 and len_a == 0:
                return True
            if sum_a == 0 or len_a == 0:
                return False
            if idx == n:
                return False
            if len_a + idx > n:
                return False

            # use idx:
            if find(len_a - 1, sum_a - nums[idx], idx + 1):
                return True

            # pruning, if we don't use nums[idx], and following nums element are same, we should skip them all
            i = idx
            while i < n and nums[i] == nums[idx]:
                i += 1

            # do not use nums[idx]
            if find(len_a, sum_a, i):
                return True

            # neither works, still False
            return False

        # search all possible length of subset array A, whose length is len_a, and sum sum_a
        # such that sum_a/len_a == sums/n <=> sum_a*n == sums*len_a
        for i in range(1, n // 2 + 1):  # this subset array length should 1<=len_a<=n//2+1
            if sums * i % n:  # len(A) is valid only if sums*len(A)%n==0
                continue
            if find(i, int(sums * i / n), 0):
                return True

        # no length of subset array A gives same sum as nums
        return False


def main():
    sol = Solution()
    assert sol.splitArraySameAverage([1,2,3,4,5,6,7,8]) is True, 'fails'

    assert sol.splitArraySameAverage([3,1]) is False, 'fails'

if __name__ == '__main__':
   main()