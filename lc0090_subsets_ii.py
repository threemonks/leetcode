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
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, res):
            """
            take first element from remaining nums, append to each element in partial subset (a path from tree root ([]) to current tree node) to get a new set of subsets, add this to result, and also use this as new partial subset into recursive call to next level, with nums[1:] as remaining nums to be explored (first element already processed)

            nums: remaining nums to explore/process
            path: partial subsets (partial path from tree root ([]) to current tree node) constructed so far after visiting leading parts of original array nums
            res: the result subsets created so far
            """
            res.append(path)
            for i in range(len(nums)):
                if i>=1 and nums[i] == nums[i-1]: # skip duplicate
                    continue
                dfs(nums[i+1:], path+[nums[i]], res)

        nums.sort()
        res = []
        dfs(nums, [], res)
        return res

def main():
    sol = Solution()
    assert sol.subsetsWithDup([1,2,2]) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]], 'fails'

if __name__ == '__main__':
   main()