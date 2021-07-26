"""
1608. Special Array With X Elements Greater Than or Equal X
Easy

276

51

Add to List

Share
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.



Example 1:

Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
Example 2:

Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.
Example 3:

Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.
Example 4:

Input: nums = [3,6,7,7,0]
Output: -1


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
from typing import List

"""
Sort
[5, 3]
5>1 3>2

time O(N*log(N))
mistakes:
1. single element, return 1 if nums[0]>=1 else -1
"""


class Solution0:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] >= 1:
                return 1
            else:
                return -1

        nums = sorted(nums, reverse=True)

        for i in range(1, n + 1):
            if nums[i - 1] >= i and (i >= n or nums[i] < i):
                return i

        return -1


"""
Counting Sort

"""


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        mx = max(nums)
        counts = [0 for _ in range(mx + 1)]

        # count frequences of each number
        for i in range(n):
            counts[nums[i]] += 1

        res = 0
        for i in range(len(counts) - 1, 0, -1):
            # from end of counts to left
            # accumulating count of numbers larger than i
            res += counts[i]
            if res == i:
                return i

        return -1


def main():
    sol = Solution()
    assert sol.specialArray([3,5]) == 2, 'fails'

    assert sol.specialArray([0,0]) == -1, 'fails'

    assert sol.specialArray([3,6,7,7,0]) == -1, 'fails'

if __name__ == '__main__':
   main()