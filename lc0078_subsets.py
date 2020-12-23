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
cascading / bitmasking
iterate through nums, for each element, append it to each set in result, to form new sets, the old sets also stay as is (for not adding this new element)
"""


class Solution0:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            ans += [cur + [num] for cur in ans]
            # print('num=%s ans=%s' % (num, ans))

        return ans


"""
backtrack / dfs
Recursively call a dfs search that removes first element from remaining nums to explore, append it to end of resulting path
since path+[nums[i]] is creating new object (list) to pass into recursive call, we don't need to pop (backtrack)
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(start, path):  # backtrack
            nonlocal nums
            ans = [path]
            for i in range(start, len(nums)):
                ans += helper(i + 1, path + [nums[i]])

            # print('ans=%s' % ans)
            return ans

        return helper(0, [])

def main():
    sol = Solution()
    #assert sol.subsets([1,2,3]) == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]], 'fails'
    assert sol.subsets([1,2,3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]], 'fails'

    assert sol.subsets([0]) == [[],[0]], 'fails'

if __name__ == '__main__':
   main()