"""
15. 3Sum
Medium

9487

974

Add to List

Share
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

"""
from typing import List

"""
Two Pointers

sort and use two pointers from both ends, and use binary search to find negative sum of the two pointer number values in array elements between the two pointers

Notes:
1. add early pruning if nums[i] > 0: break
2. skip duplicates

"""


class Solution0:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if not n:
            return []
        nums = sorted(nums)
        # print(nums)

        result = set()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            for j in range(n - 1, i, -1):
                # print('i=%s j=%s' % (i, j))
                s = (nums[i] + nums[j])
                if s + nums[i + 1] > 0:  # needs to decrease j
                    continue
                if s + nums[j - 1] < 0:  # needs to increase i
                    break
                left, right = i + 1, j
                while left < right:
                    # print('left=%s right=%s s=%s' % (left, right, s))
                    m = left + (right - left) // 2
                    if nums[m] == -s:
                        result.add((nums[i], nums[m], nums[j]))
                        break
                    elif nums[m] < -s:
                        left = m + 1
                    else:
                        right = m

        return [list(r) for r in result]


"""
use result of two sum with hashmap

sort and loop through nums, for each element nums[i], call twosum to find pairs within nums[i+1:] that sums to -nums[i]

we sort and check ajacent number to skip duplicates

"""


class Solution:
    def twosum(self, nums, target):
        """
        return list of index pairs of two elements that sum to target
        """
        compdict = {}
        for i, num in enumerate(nums):
            compdict[num] = i

        result = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicate
                continue
            if target - num in compdict and compdict[target - num] != i:
                result.append([num, target - num])

        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if not n:
            return []
        nums = sorted(nums)
        # print(nums)

        result = set()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:  # requirement sum to zero, we cannot reduce sum after this index
                continue
            target = -nums[i]
            pairs = self.twosum(nums[i + 1:], target)
            for pair in pairs:
                result.add(tuple(sorted([nums[i], pair[0], pair[1]])))

        return [list(r) for r in result]


def main():
    sol = Solution()

    assert sol.threeSum(nums = [-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]], 'fails'

    assert sol.threeSum(nums = []) == [], 'fails'

    assert sol.threeSum(nums = [0]) == [], 'fails'

if __name__ == '__main__':
   main()