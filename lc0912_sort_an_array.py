"""
912. Sort an Array
Medium

738

351

Add to List

Share
Given an array of integers nums, sort the array in ascending order.



Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]


Constraints:

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000

"""
from typing import List

"""
Quicksort

steps
1. pick a pivot, move all numbers smaller than pivot to left part, all number larger than pivot to right part.
2. repeat the above procedure for left part, and right part recursively
3. when done, the entire array is sorted

For pivot, can just pick right, but would result in worst case if it is already sorted, so we can do a shuffle before pick right as pivot, or pick pivot randomly

Note:
1. worst case could be O(N^2), it happens if the array is already sorted in descending order, and we pick right end element as pivot
2. this implementation is unstable, means elements of same value could change order after sorting

mistakes:
1. in quick sort partition, when define start/end pointer, we leave pivot index/value outside of the pointer movement
2. if both left pointer value and right pointer value are on wrong side of pivot value, we swap them, then move both pointers towards middle

time O(Nlog(N))
"""


class Solution0:
    def sortArray(self, nums: List[int]) -> List[int]:

        self.quicksort(nums, 0, len(nums) - 1)

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
        self.quicksort(nums, left, pivot_idx - 1)
        self.quicksort(nums, pivot_idx + 1, right)

    def partition(self, nums, left, right):
        # pick right as pivot, have two pointers, start from left, and right-1 (as right is pivot index),
        # move towards middle if number pointed by left and right are in right part
        # (means in left part and smaller than pivot val, or in right part and larger than pivot val)
        # if both left and right pointer points at number that should be on the opposite part, then swap them
        pivot_val = nums[right]

        # repeatedly move all nums smaller than pivot to left, and nums larger than pivot to right
        start, end = left, right - 1  # leave pivot (nums[right]) outside of the loop, and only swap it to its position at last
        while start <= end:
            if nums[start] <= pivot_val:
                start += 1
            elif nums[end] > pivot_val:
                end -= 1
            else:
                # if both nums[start] and nums[end] are on wrong side of pivot_val, lets swap them
                nums[start], nums[end] = nums[end], nums[start]
                # and advance the pointers
                start += 1
                end -= 1
        # now put pivot to its correct position
        # when while loop finishes, start should be the first in  the right part of pivot, so it is safe to just swap pivot value with nums[start]
        nums[start], nums[right] = nums[right], nums[start]

        return start

    def partition2(self, nums, left, right):
        # pick right as pivot
        # pick left as wall, iterate wall from left to right-1, for any number that is smaller than wall value, swap it with wall value
        pivot_val, wall = nums[right], left

        for i in range(left, right):
            if nums[i] < pivot_val:
                nums[wall], nums[i] = nums[i], nums[wall]
                wall += 1

        # swap pivot value into its correct position at wall
        nums[wall], nums[right] = nums[right], nums[wall]

        return wall


"""
Merge Sort

1. repeatedly divide array into two parts, call merge sort on the two subarrays
2. base case for divide/merge sort process:
   if length == 1
3. merge back two sorted lists into one list in correct order, pick smaller one of two lists head, append to result, repeat until both lists are empty

time O(Nlog(N))

mistakes:
1. index++ within merge while loop
2. base case for divide left >= right (one element only)
"""


class Solution1:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums_left, nums_right):
            # merge two sorted lists
            result = []
            i, j = 0, 0
            while i < len(nums_left) and j < len(nums_right):
                if nums_left[i] <= nums_right[j]:
                    result.append(nums_left[i])
                    i += 1
                else:
                    result.append(nums_right[j])
                    j += 1
            # if there's remaining item in one of the lists
            while i < len(nums_left):
                result.append(nums_left[i])
                i += 1
            while j < len(nums_right):
                result.append(nums_right[j])
                j += 1

            return result

        def divide(nums, left, right):
            # divide nums[left:right+1] into two parts, recursively
            # and call merge to sort the two parts
            # base case: if single element, return
            if left >= right:
                return [nums[left]]
            mid = left + (right - left) // 2
            left_result = divide(nums, left, mid)
            right_result = divide(nums, mid + 1, right)
            return merge(left_result, right_result)

        return divide(nums, 0, len(nums) - 1)


"""
Heap Sort

1. for i in n//2 to 0, heapify subtree rooted at index i (this guarantees we make all subtree on left be proper heap first)
2. now entire tree is heapified, we then sort
3. each time, extract one element from heap, and add to result
4. repeat 3 until heap is empty

time O(Nlog(N))

"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def min_heapify(nums, n, i):
            # min heapify array nums of size n, at root i
            # this assume both left and right subtree of i is already properly heapified
            l = 2 * i + 1  # left children
            r = 2 * i + 2  # right children

            # find largest among i, l, and r
            largest = i
            # if left child is larger than root
            if l < n and nums[l] < nums[largest]:
                largest = l

            # if right child is larger than root
            if r < n and nums[r] < nums[largest]:
                largest = r

            if largest != i:
                # swap largest and i
                nums[largest], nums[i] = nums[i], nums[largest]
                # and recursively heapify the affected subtree
                min_heapify(nums, n, largest)

        def heap_sort(nums):
            # sort nums using min_heap
            n = len(nums)

            # build min heap first, only need to start build from n//2 to 0
            for i in range(n // 2, -1, -1):
                min_heapify(nums, n, i)

            # one by one extract element from heap
            for i in range(n - 1, 0, -1):
                # move current root to end, which will be sorted and excluded from further heapify and sort
                nums[i], nums[0] = nums[0], nums[i]
                # now heapify reduced heap of size i=n-1
                min_heapify(nums, i, 0)

            # min_heap sorts in descending order
            return nums[::-1]

        return heap_sort(nums)


def main():
    sol = Solution()
    assert sol.sortArray([5,2,3,1]) == [1,2,3,5], 'fails'

    assert sol.sortArray([5,1,1,2,0,0]) == [0,0,1,1,2,5], 'fails'


if __name__ == '__main__':
   main()