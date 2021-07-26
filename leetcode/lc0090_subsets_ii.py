"""
90. Subsets II
Medium

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""
import math
from functools import lru_cache
from typing import List
class Solution0:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, res):
            """
            take first element from remaining nums, append to each element in partial subset (a path from tree root ([]) to current tree node) to get a new set of subsets, add this to result, and also use this as new partial subset into recursive call to next level, with nums[1:] as remaining nums to be explored (first element already processed)

            nums: remaining nums to explore/process
            path: partial subsets (partial path from tree root ([]) to current tree node) constructed so far after visiting leading parts of original array nums
            res: the result subsets created so far
            """
            print('nums=%s path=%s res=%s' % (nums, path, res))
            res.append(path)
            for i in range(len(nums)):
                if i>=1 and nums[i] == nums[i-1]: # skip duplicate
                    continue
                dfs(nums[i+1:], path+[nums[i]], res)

        nums.sort()
        res = []
        dfs(nums, [], res)
        return res


"""
subsets via backtracking / dfs

1. take first element from remaining nums, append to each element in partial subset (a path from tree root ([]) to current tree node) to get a new set of subsets
2. add this new set of subsets to result
3. also use this as new partial subset into recursive call to next level, with nums[1:] as remaining nums to be explored (first element already processed)
visualization:
https://medium.com/@CalvinChankf/a-general-approach-for-subsets-combinations-and-permutations-5c8fe3aff0ae

"""

class Solution0:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, path):
        self.res.append(path)
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1]:  # skip duplicate
                continue
            self.dfs(nums[i + 1:], path + [nums[i]])


"""
sort nums first to check duplicates
If we want to insert an element which is a dup, we can only insert it after the newly inserted elements from last step.
So we use k = size to keep track starting position of newly added subsets within result from prevous run, and only append new numbers to those subsets from previous result

"""


class Solution1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        size = 0  # index of starting position of newly added subsets
        ans = [[]]

        for i in range(len(nums)):
            k = size if i >= 1 and nums[i] == nums[i - 1] else 0
            size = len(ans)
            ans += [ans[j] + [nums[i]] for j in range(k, size)]

        return ans


"""
Iteratively

当有 n 个重复数字出现，其实就是在出现重复数字之前的所有解中，分别加 1 个重复数字， 2 个重复数字，3 个重复数字

"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = [[]]

        i = 0
        while i < n:
            dupcount = 0
            while i + 1 < n and nums[i] == nums[i + 1]:
                dupcount += 1
                i += 1
            if dupcount:
                newres = []
                # for each result before duplicates, add 1,2,...dupcount copies of dup nums
                res += [r + [nums[i]] * j for r in res for j in range(1, dupcount + 2)]
                # for r in res:
                #     for j in range(1, dupcount+2):
                #         newres.append(r+[nums[i]]*j)
                # res += newres
            else:
                # add new element to each element of existing result to form new set of results
                res += [r + [nums[i]] for r in res]
            i += 1

        return res


def main():
    sol = Solution()
    assert sol.subsetsWithDup([1,2,2]) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]], 'fails'

    # assert sol.subsetsWithDup([0]) == [[], [0]], 'fails'

if __name__ == '__main__':
   main()