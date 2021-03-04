"""
496. Next Greater Element I
Easy

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

"""
from typing import List

"""
brutal force
"""


class Solution1:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1_idx = dict([(val, idx) for idx, val in enumerate(nums1)])
        res = [-1 for _ in range(len(nums1))]
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i] and nums2[i] in nums1_idx:
                    res[nums1_idx[nums2[i]]] = nums2[j]
                    break

        return res

"""
Stack

use a dict with element val as key, its next greater element as value
use stack to hold elements of nums2 that have not found its next greater element
time O(len(nums2)+len(nums1))
space O(len(nums2)+len(nums1))
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge_dct = {}  # holding map of val to next greater element
        stack = []  # holds element in nums2 that have not found its next greater element
        for n in nums2:
            while stack and n > stack[-1]:
                nge_dct[stack.pop(-1)] = n
            stack.append(n)

        # store next greater element into array according to index in nums1
        res = []
        for n in nums1:
            res.append(nge_dct.get(n, -1))

        return res

def main():
    sol = Solution()
    assert sol.nextGreaterElement([4,1,2], [1,3,4,2]) == [-1,3,-1], 'fails'

    assert sol.nextGreaterElement([2,4], [1,2,3,4]) == [3,-1], 'fails'

if __name__ == '__main__':
   main()