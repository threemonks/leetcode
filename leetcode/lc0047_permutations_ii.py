"""
47. Permutations II
Medium

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

"""

from typing import List

"""
backtrack/DFS unsorted input

time complexity Sum(P(N, k) for k from 1 to N), O(N*N!)
space N! (for storing output)
"""


class Solution0:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        if not nums: return result

        n = len(nums)

        def backtrack(nums, path):
            """
            nums: remaining numbers to pick for permutation
            path: numbers selected so far for this permutation
            """
            if not nums and len(path) == n:
                result.append(path)
            for i in range(len(nums)):
                if nums[i] in nums[:i]:
                    continue
                backtrack(nums[:i] + nums[i + 1:], path + [nums[i]])

        backtrack(nums, [])

        return result


"""
backtrack/DFS

sort input first

time complexity Sum(P(N, k) for k from 1 to N), O(N*N!)
space N! (for storing output)
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        if not nums: return result
        nums = sorted(nums)

        n = len(nums)

        def backtrack(nums, path):
            """
            nums: remaining numbers to pick for permutation
            path: numbers selected so far for this permutation
            """
            if not nums and len(path) == n:
                result.append(path)
            for i in range(len(nums)):
                if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                    backtrack(nums[:i] + nums[i + 1:], path + [nums[i]])

        backtrack(nums, [])

        return result
"""
Iterative handles duplicate
取下一个可用元素，插入已经有的部分排列结果perm中每一个可能的位置，构成一个新的结果
重复处理：当要插入位置前面数字就是当前要插入的数字（重复），停止继续插入，转处理下一个结果perm
To handle duplication, just avoid inserting a number AFTER any of its duplicates.
"""
class Solution:
    def permuteUnique(self, nums):
        results = [[]]
        for num in nums:
            newres = []
            for r in results:
                for i in range(len(r)+1):
                    newres.append(r[:i]+[num]+r[i:])
                    if i<len(r) and r[i] == num:
                        break  #handles duplication
            results = newres
        return results

def main():
    sol = Solution()
    assert sol.permuteUnique([1,1,2]) == [[1,1,2], [1,2,1], [2,1,1]], 'fails'

    assert sol.permuteUnique([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], 'fails'

if __name__ == '__main__':
   main()