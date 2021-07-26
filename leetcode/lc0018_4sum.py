"""
18. 4Sum
Medium

https://leetcode.com/problems/4sum/

"""
import collections
from typing import List

"""
Hashmap 

basic idea is to sort nums, and wrap external loop to reduce the problem to 2sum, then one can choose one of the two sum's method
    i) two pointers
    ii) hashmap

loop and calculate sum of three different elements of nums, construct a hashmap of nums[i], and lookup target-sum in hashmap

For arbituary k-sum, we can use recursive call to reduce until it is 2-sum

notes:
1. sort so we can easily skip duplicate and early prune if smallest four sum to larger than target, or largest four sum to less than target
2. build hashmap for O(1) lookup time for 4th number

time O(N^3) - three loops and O(1) for hashmap lookup
space O(N)

"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        nums = sorted(nums)

        # if all four largest sum to less than target, or all four smallest sum to larger than target, there's no answer
        if sum(nums[:4]) > target or sum(nums[n - 4:]) < target:
            return []

        # print(nums)
        numdict = collections.defaultdict(list)

        for i in range(n):
            numdict[nums[i]].append(i)

        result = set()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, n):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    sumijk = nums[i] + nums[j] + nums[k]
                    # print('i=%s j=%s k=%s sumijk=%s' % (i, j, k, sumijk))
                    if target - sumijk in numdict and len(
                            [l for l in numdict[target - sumijk] if l != i and l != j and l != k]) > 0:
                        # print('i=%s j=%s k=%s target-sumijk=%s numdict[target-sumijk]=%s' % (i, j, k, target-sumijk, numdict[target-sumijk]))
                        result.add(tuple(sorted([nums[i], nums[j], nums[k], target - sumijk])))

        return [list(r) for r in result]


def main():
    sol = Solution()
    assert sol.fourSum(nums = [1,0,-1,0,-2,2], target = 0) == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]], 'fails'

    assert sol.fourSum(nums = [], target = 0) == [], 'fails'

if __name__ == '__main__':
   main()