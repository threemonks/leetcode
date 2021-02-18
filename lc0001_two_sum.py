"""
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""
import collections
from typing import List

"""

build hashmap of num to index, check if target-num exists in hashmap

time O(n)
space O(n)

mistakes:
1. need to check target-num != num

"""


class Solution0:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = collections.defaultdict(list)

        for i, num in enumerate(nums):
            index[num].append(i)

        for i, num in enumerate(nums):
            if (target - num != num and target - num in index):
                return [i, index[target - num][0]]
            elif target - num == num and len(index[target - num]) == 2:
                return index[target - num]  # only one valid answer, we could omit len(index[target-num]) == 2 check


"""
Two pass hash table

build hashmap of num to index, check if target-num exists in hashmap

this uses the fact that if a number is target/2, then it would appear at most twice (because it is known there's only one valid answer)
so we can just use dict(int) to keep num to index map (for duplicate number, it will keep the second index only, and later we will be at the first index i for nums[i], to look for the target-num's index which is the second index of nums[i])

"""


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # build index map
        index_map = dict()
        for i in range(len(nums)):
            index_map[nums[
                i]] = i  # always keep the latest index for duplicate number (only second as we know exactly one solution)

        # build and use complements map
        for i in range(len(nums)):
            comp_num = target - nums[i]
            if comp_num in index_map and index_map[comp_num] != i:
                return [i, index_map[comp_num]]


"""
One pass hash table

check if target-num exists in hashmap, and build hashmap along the check

mistakes:
1. need to check first, then add number index to hashmap

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # build index map
        index_map = dict()

        # build and use complements map
        for i in range(len(nums)):
            comp_num = target - nums[i]
            if comp_num in index_map and index_map[
                comp_num] != i:  # only one valid solution, so if duplicate number that is target/2, it would appear only twice
                return [i, index_map[comp_num]]
            index_map[nums[i]] = i


def main():
    sol = Solution()
    assert sorted(sol.twoSum(nums = [2,7,11,15], target = 9)) == sorted([1, 0]), 'fails'

    assert sorted(sol.twoSum(nums = [3,2,4], target = 6)) == sorted([1,2]), 'fails'

    assert sorted(sol.twoSum(nums = [3,3], target = 6)) == sorted([0,1]), 'fails'

if __name__ == '__main__':
   main()