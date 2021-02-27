"""
912. Sort an Array
Medium

https://leetcode.com/problems/sort-an-array/
"""
from typing import List

"""
quicksort

steps
1. pick a pivot, move all numbers smaller than pivot to left part, all number larger than pivot to right part.
2. repeat the above procedure for left part, and right part recursively
3. when done, the entire array is sorted

For pivot, can just pick right, but would result in worst case if it is already sorted, so we can do a shuffle before pick right as pivot, or pick pivot randomly

Note:
1. worst case could be O(N^2), it happens if the array is already sorted in descending order, and we pick right end element as pivot
2. this implementation is unstable, means elements of same value could change order after sorting

time O(Nlog(N))
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        self.quicksort(nums, 0, len(nums)-1)

        return nums

    def quicksort(self, nums, left, right):
        # one element, no need to sort
        if left >= right:
            return

        # pick a pivot, and partition nums into left and right two points
        # all nums in left part are smaller than pivot, and all in right part are larger than pivot
        pivot_idx = self.partition(nums, left, right)

        # now recursively call quicksort to sort left part, and right part
        # excluding the pivot point, which is already in its correct position
        self.quicksort(nums, left, pivot_idx-1)
        self.quicksort(nums, pivot_idx+1, right)

    def partition(self, nums, left, right):
        # pick right as pivot
        pivot_val = nums[right]

        # repeatedly move all nums smaller than pivot to left, and nums larger than pivot to right
        start, end = left, right-1 # leave pivot (nums[right]) outside of the loop, and only swap it to its position at last
        while start <= end:
            if nums[start] <= pivot_val:
                start += 1
            elif nums[end] > pivot_val:
                end -=1
            else:
                # swap nums pointed by start and end, if they are both on wrong side of pivot
                nums[start], nums[end] = nums[end], nums[start]
                # and advance the pointers
                start += 1
                end -= 1

        # now put pivot to its correct position
        nums[start], nums[right] = nums[right], nums[start]

        return start


def main():
    sol = Solution()
    assert sol.sortArray([5,2,3,1]) == [1,2,3,5], 'fails'

    assert sol.sortArray([5,1,1,2,0,0]) == [0,0,1,1,2,5], 'fails'


if __name__ == '__main__':
   main()