"""
2150. Find All Lonely Numbers in the Array
Medium

13

2

Add to List

Share
You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.

Return all lonely numbers in nums. You may return the answer in any order.



Example 1:

Input: nums = [10,6,5,8]
Output: [10,8]
Explanation:
- 10 is a lonely number since it appears exactly once and 9 and 11 does not appear in nums.
- 8 is a lonely number since it appears exactly once and 7 and 9 does not appear in nums.
- 5 is not a lonely number since 6 appears in nums and vice versa.
Hence, the lonely numbers in nums are [10, 8].
Note that [8, 10] may also be returned.
Example 2:

Input: nums = [1,3,5,3]
Output: [1,5]
Explanation:
- 1 is a lonely number since it appears exactly once and 0 and 2 does not appear in nums.
- 5 is a lonely number since it appears exactly once and 4 and 6 does not appear in nums.
- 3 is not a lonely number since it appears twice.
Hence, the lonely numbers in nums are [1, 5].
Note that [5, 1] may also be returned.


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 106
"""
from typing import List

"""
Sort

time: nlog(n) - sort
"""


class Solution0:
    def findLonely(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        nums = sorted(nums)

        ans = []

        if nums[0] + 1 < nums[1]:
            ans.append(nums[0])

        if nums[n - 2] + 1 < nums[n - 1]:
            ans.append(nums[n - 1])

        for i in range(1, n - 1):
            if nums[i - 1] + 1 < nums[i] and nums[i] + 1 < nums[i + 1]:
                ans.append(nums[i])

        return ans


"""
Use HashMap

time: n 
"""
from collections import Counter


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)

        ans = []

        for n in nums:
            if counter.get(n, 0) == 1 and counter.get(n - 1, 0) == 0 and counter.get(n + 1, 0) == 0:
                ans.append(n)

        return ans


def main():
    sol = Solution()
    assert sol.findLonely(nums = [10,6,5,8]) == [10,8], 'fails'

    assert sol.findLonely(nums = [1,3,5,3]) == [1,5], 'fails'

if __name__ == '__main__':
   main()