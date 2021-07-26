"""
46. Permutations
Medium

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

"""
from typing import List

"""
backtracking 1
in each recursive step, do this:
1. if the partial result is of desired length, add to global result sets
2. loop and take one number from remaining available numbers, append to partial result (path)

backtrack(nums[:i]+nums[i+1:], path+[nums[i]])

"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(nums, path):
            nonlocal res
            if len(path) == n:
                res.append(path)
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], path + [nums[i]])

        backtrack(nums, [])
        return res


"""
backtracking 1
in each recursive step, do this:
1. if the partial result is of desired length, add to global result sets
2. take first letter from remaining nums, insert into each possible position of running partial result

backtrack(nums[:i]+nums[i+1:], path+[nums[i]])

"""


class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(path, arr):
            nonlocal res
            if len(path) == n:
                res.append(path)
                return
            if not arr:
                return
            for i in range(len(path) + 1):
                backtrack(path[:i] + [arr[0]] + path[i:], arr[1:])

        backtrack([], nums)
        return res


"""
iterative - build from n-1 to n, for length n permutation, insert n-th element into every possible insertion position of the n-1 element result from previous run

Permutations of two elements are 1 2 and 2 1.
Permutations of three elements can be obtained by inserting 3 at different positions in all permutations of size 2.
Inserting 3 in different positions of 1 2 leads to 1 2 3, 1 3 2 and 3 1 2.
Inserting 3 in different positions of 2 1 leads to 2 1 3, 2 3 1 and 3 2 1.
"""


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        perms = [[]]
        for num in nums:
            prev_perms = list(perms)
            perms = []
            for p in prev_perms:
                if not p:
                    perms = [[nums[0]]]
                else:
                    for j in range(len(p) + 1):
                        perms.append(p[:j] + [num] + p[j:])

            for np in perms:
                if len(np) == n:
                    result.append(np)

        return result


"""
Iterative
取下一个可用元素，插入以有部分排列结果中每一个可能的位置，构成一个新的结果
"""
class Solution:
    def permute(self, nums):
        results = [[]]
        for num in nums:
            # newres = []
            # for r in results:
            #     for i in range(len(r)+1):
            #         newres.append(r[:i] + [num] + r[i:])   ###insert num
            # results = newres
            results = [r[:i] + [num] + r[i:] for r in results for i in range(len(r)+1)]
        return results

def main():
    sol = Solution()
    assert sorted(sol.permute([1,2,3])) == sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]), 'fails'

    assert sorted(sol.permute([0,1])) == sorted([[0,1],[1,0]]), 'fails'

    assert sorted(sol.permute([1])) == sorted([[1]]), 'fails'

if __name__ == '__main__':
   main()