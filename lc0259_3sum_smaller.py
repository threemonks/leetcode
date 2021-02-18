"""
259. 3Sum Smaller
Medium

Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Follow up: Could you solve it in O(n2) runtime?



Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
Example 2:

Input: nums = [], target = 0
Output: 0
Example 3:

Input: nums = [0], target = 0
Output: 0


Constraints:

n == nums.length
0 <= n <= 300
-100 <= nums[i] <= 100
-100 <= target <= 100
"""
from typing import List

"""
brutal force

Note:
    0<=i<j<k<n just means don't reuse number, as there's no requirement on the order of i, j, k, since the satisfying condition is nums[i]+nums[j]+nums[k] < target, => we can sort and use two pointers or do binary search

"""


class Solution0:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        remains = [target - i for i in nums]

        result = []

        for i in range(n):
            for j in range(i + 1, n):
                t = nums[i] + nums[j]
                for k in range(j + 1, n):
                    if t < remains[k]:
                        result.append([nums[i], nums[j], nums[k]])

        # print(result)
        return len(result)


"""
brutal force

Note:
    0<=i<j<k<n just means don't reuse number, as there's no requirement on the order of i, j, k, since the satisfying condition is nums[i]+nums[j]+nums[k] < target, => we can sort and use two pointers or do binary search

time O(N^3)
"""


class Solution0:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)

        result = []

        for i in range(n):
            for j in range(i + 1, n):
                t = nums[i] + nums[j]
                for k in range(j + 1, n):
                    if t + nums[k] < target:
                        result.append([nums[i], nums[j], nums[k]])

        # print(result)
        return len(result)


"""
binary search
"""


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        print(nums)

        count = 0
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    # adding all valid triplets (i, j, l) for l from j+1 to k
                    count += k - j
                    j += 1
                else:
                    k -= 1

        return count


def main():
    sol = Solution()
    assert sol.threeSumSmaller(nums = [-2,0,1,3], target = 2) == 2, 'fails'

    assert sol.threeSumSmaller(nums = [], target = 0) == 0, 'fails'

    assert sol.threeSumSmaller(nums = [0], target = 0) == 0, 'fails'

if __name__ == '__main__':
   main()