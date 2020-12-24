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


class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, path):  # backtrack
            nonlocal nums
            ans = [path]
            for i in range(start, len(nums)):
                ans += dfs(i + 1, path + [nums[i]])

            # print('ans=%s' % ans)
            return ans

        return dfs(0, [])

"""
backtrack/dfs
pass remaining part of nums to be explored/processed into recusrive call, use third argument to return result 
"""
class Solution2:
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
                dfs(nums[i+1:], path + [nums[i]], res)

        res = []
        dfs(nums, [], res)
        return res


"""
binary sorted / bitmask
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        for i in range(1 << n):
            # if j-th bit of i is set, append nums[j] (index starts at 0)
            # for bit test for i, its index starts at 1
            output.append([nums[j] for j in range(n) if (i & (1 << ((j + 1) - 1)))])

        # print(output)
        return output


def main():
    sol = Solution()
    #assert sol.subsets([1,2,3]) == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]], 'fails'
    assert sol.subsets([1,2,3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]], 'fails'

    assert sol.subsets([0]) == [[],[0]], 'fails'

if __name__ == '__main__':
   main()