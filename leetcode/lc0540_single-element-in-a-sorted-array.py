"""
540. Single Element in a Sorted Array
Medium

2403

88

Add to List

Share
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.



Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10


Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
"""
from typing import List

"""
Binary Search

compare nums[m] with nums[m-1], nums[m+1], if they are all not equal, then return m
otherwise, if nums[m-1] == nums[m], then we know the length of 0...m-2, if that is even, means the single number is not in it
if 0...m-2 is odd, then the single element is in it
if nums[m] == nums[m+1], then we check 0 ... m-1

note this is guaranteed to work because we are given a sorted array, and all numbers appear twice except for one, which only appears once
 
time O(N)
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        l, r = 0, n-1
        while l < r:
            m = l+(r-l)//2
            # print('l=%s r=%s m=%s' % (l, r, m))
            if nums[m] == nums[m+1]: # then nums[m] == nums[m-1]
                # if m is odd, 0...m-1 is odd count, so single number is to left
                if m % 2 == 1:
                    r = m
                else:
                    l = m+2
            elif nums[m-1] == nums[m]:
                # if m-1 is odd, 0 ... m-2 is odd count, so single number is to left
                if (m-1) % 2 == 1:
                    r = m-1
                else:
                    l = m+1
            else: # nums[m-1] != nums[m] and m+1<n and nums[m] != nums[m+1]
                return nums[m]

        return nums[l]


def main():
    sol = Solution()
    assert sol.singleNonDuplicate(nums = [1,1,2,3,3,4,4,8,8]) == 2, 'fails'

    assert sol.singleNonDuplicate(nums = [3,3,7,7,10,11,11]) == 10, 'fails'

if __name__ == '__main__':
   main()