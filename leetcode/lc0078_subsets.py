"""
78. Subsets
Medium

Given an integer array nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

"""
import math
from functools import lru_cache
from typing import List

"""
Subset Backtrack
"""


class Solution0:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        # Python3 program to find all subsets by backtracking.
        # In the array nums at every step we have two choices for each element
        # either we can ignore the element
        # or we can include the element in our subset
        def dfs(idx, subset):
            nonlocal nums
            res.append(subset[:])
            for i in range(idx, n):
                # include the nums[i] in subset.

                # move onto explore next element.
                dfs(i + 1, subset + [nums[i]])

                # exclude the nums[i] from subset and
                # triggers backtracking.
            return

        # keeps track of current element in vector nums
        dfs(0, [])

        return res


"""
Backtrack
"""


class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, res):  # backtrack
            """
            take first element from remaining nums, append to each element in partial subset (a path from tree root ([]) to current tree node) to get a new set of subsets, add this to result, and also use this as new partial subset into recursive call to next level, with nums[1:] as remaining nums to be explored (first element already processed)

            nums: remaining nums to explore/process
            path: partial subsets (partial path from tree root ([]) to current tree node) constructed so far after visiting leading parts of original array nums
            res: the result subsets created so far
            """
            res.append(path)
            for i in range(len(nums)):
                dfs(nums[i + 1:], path + [nums[i]], res)

        res = []
        dfs(nums, [], res)
        return res


"""
Generate subset via iterative
每次考虑一个新的元素，在考虑k-1个元素的所有结果里加上这个新的元素nums[k]

"""


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[]]  # init to empty subset
        for i in range(n):
            newres = []
            # for each element is existing result
            for r in res:
                newres.append(r + [nums[i]])  # create a new result by appending new item nums[i]
            res += newres

        return res


"""
Cascading / Bitmasking / Iterative
iterate through nums, for each element, append it to each set in current result, to form new sets, the old sets also stay as is (for not adding this new element)
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            ans += [cur + [num] for cur in ans]

        return ans


def main():
    sol = Solution()
    assert sol.subsets([1,2,3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]], 'fails'

    assert sol.subsets([0]) == [[],[0]], 'fails'

if __name__ == '__main__':
   main()