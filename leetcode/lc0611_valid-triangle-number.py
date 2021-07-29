"""
611. Valid Triangle Number
Medium

1948

132

Add to List

Share
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.



Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000

"""
from typing import List

"""
Two Pointers

iterate sorted array for edge nums[k], then for all edges shorter than nums[k], use two pointers i, j to iterate from 0 and k-1 to middle, while checking if nums[i]+nums[j]>nums[k], would add i-j valid triplets, if still valid, we can try to move j to left and try again, if invalid, move i to right to increase nums[i], until i meets j

time O(N*logN)

brutal force O(N^3)
loop + binary search  O(N^2*log(N))


"""


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)

        ans = 0
        for k in range(2, n):
            i, j = 0, k - 1  # search all numbers i, j such that nums[i]+nums[j] < nums[k]
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ans += j - i
                    j -= 1
                else:
                    i += 1

        return ans


def main():
    sol = Solution()
    assert sol.triangleNumber(nums = [2,2,3,4]) == 3, 'fails'

    assert sol.triangleNumber(nums = [4,2,3,4]) == 4, 'fails'


if __name__ == '__main__':
   main()